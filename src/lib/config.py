#!/usr/bin/env python3
#
#  Copyright (C) 2010 - Librix Dev Team
#
# This file is part of librix-thinclient.
#
# librix-thinclient is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# librix-thinclient is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with librix-thinclient.  If not, see <http://www.gnu.org/licenses/>.

import os
from lxml import etree as ET
from copy import deepcopy
from tempfile import mkstemp
from crypt import crypt

from lib.utils import sha512sum, passwdGen
from lib.modules import LTCModuleParser

class LTCConfigParser(object):
	"""LTCConfigParser class to manipulate XML configuration file
	to Librix Thin Client Administration Interface"""

	def __init__(self, moduleparser=LTCModuleParser()):
		"""Instantiate LTCConfigParser

		@param	self		A LTCConfigParser instance
		@param	moduleparser	A LTCModuleParser instance
		"""
		self.moduleparser = moduleparser
		self.st_mtime = 0
		self.hash = 0
		self.configfile = ''
		self._parser = ET.XMLParser(encoding="utf-8", remove_blank_text=True)

	def readConfigFile(self, file=''):
		"""Parse a configfile

		@param	self		A LTCConfigParser instance
		@param	file		A filepath string. Default is self.configfile
		"""
		print("__readConfigFile:", file)
		if not file and self.configfile:
			file = self.configfile
		elif not file and not self.configfile:
			return
		self.configfile = file
		self.backupfile = file + '~'

		# Register mtime and sha512sum
		self.st_mtime = os.stat(file).st_mtime
		self.hash = sha512sum(file)

		self._config = ET.parse(file, parser=self._parser).getroot()

		self._name = self._config.find("name")
		self._profiles = self._config.find("profiles")
		self._profileFalse = self._config.find("profileFalse")
		self._users = self._config.find("users")
		self._keys = self._config.find("keys")

	def writeConfigFile(self, file=''):
		"""Write configurations from self.backupfile to file

		Then load file as configfile
		@param	self		A LTCConfigParser instance
		@param	file		A filepath string. Default is self.configfile
		"""
		if not file:
			file = self.configfile
			backupfile = self.backupfile
			if not self.modified(): return
		else:
			if os.path.isfile(self.configfile): backupfile = self.configfile
			elif os.path.isfile(self.backupfile): backupfile = self.backupfile

		if file == backupfile: return

		with open(file, 'w') as destfile, open(backupfile, 'r') as backup:
			destfile.write(backup.read())

		if self.modified():
			os.remove(self.backupfile)
		self.readConfigFile(file)

	def newConfigFile(self):
		"""Creates a new config file in /tmp

		@param	self		A LTCConfigParser instance
		"""
		self.configfile = mkstemp(suffix='.conf', prefix='.tmp')[1]
		if os.path.isfile(self.configfile): os.remove(self.configfile)
		self.backupfile = self.configfile + '~'

#		self.st_mtime = os.stat(config).st_mtime
#		self.hash = sha512sum(file)

		self._config = ET.Element("librix_tcd_config")
		self._name = ET.SubElement(self._config, "name")

		self._profileFalse = ET.SubElement(self._config, "profileFalse",
			attrib={"name": "profileFalse"})
		self._profiles = ET.SubElement(self._config, "profiles")
		self._users = ET.SubElement(self._config, "users")
		self._keys = ET.SubElement(self._config, "keys")

		for m in self.moduleparser.getModulesList():
			ET.SubElement(self._profileFalse, "option",
				attrib={"name": m, "on": str(False).lower()})

	def updateConfigFile(self):
		"""Update current config file with modules list of moduleparser

		adding present modules, if absent in configfile. This don't touch
		present config if module isn't present (to future configs).
		@param	self		A LTCConfigParser instance
		"""
		for m in self.moduleparser.getModulesList():
			if m not in self.getOptionsList():
				ET.SubElement(self._profileFalse, "option",
					attrib={'name':m, 'on':'false'})
				for p in self._profiles:
					ET.SubElement(p, "option", attrib={'name':m, 'on':'false'})
		self._syncConfigs()

	def _syncConfigs(self):
		"""Sync self.xml with self.backupfile

		@param	self		A LTCConfigParser instance
		"""
		self._config.getroottree().write(self.backupfile, pretty_print=True)

	def modified(self, file=''):
		"""Tell if file is modified

		Return true if all changes in file are saved (there's no backupfile)
		and False otherwise
		@param	self		A LTCConfigParser instance
		@param	file		Optional argument. If not given, use self.backupfile
		@return				Int value. 0 if not modified, 1 if yes and 2 if new
		"""
		if not file:
			configfile = self.configfile
			backupfile = self.backupfile
		else:
			configfile = file
			backupfile = file + '~'

		#return(not os.path.isfile(file)|)
		configfile + backupfile
		if os.path.isfile(configfile) and os.path.isfile(backupfile):
			return(1)
		elif os.path.isfile(backupfile):
			return(2)
		else:
			return(0)

	def getName(self):
		"""Return config file name

		@param	self		A LTCConfigParser instance
		@return				A string containing config file name
		"""
		return(self._name.text)

	def setName(self, name):
		"""Set config file name

		@param	self		A LTCConfigParser instance
		@param	name		A string containing config file name
		"""
		if name != self.getName():
			self._name.text = name
			self._syncConfigs()

	def getUsersList(self):
		"""Return the users list

		@param	self		A LTCConfigParser() instance
		@return				A list of existing users
		"""

		_u = [u.get("name") for u in self._users.findall("user")]
		_u.sort()
		return(_u)

	def getProfilesList(self):
		"""Return the profiles list

		@param	self		A LTCConfigParser() instance
		@return				A list of existing profiles
		"""
		_p = [p.get("name") for p in self._profiles.findall("profile")]
		_p.sort()
		return(_p)

	def getUserProfile(self, user):
		"""Return the profile of a given user

		@param	self		A LTCConfigParser() instance
		@param	user		A user name string
		@return				A string containing the profile of user
		"""
		if not user in self.getUsersList():
			raise IndexError("\"{0}\" not in users list".format(user))

		return(self._users.find("user[@name='{0}']".format(user)).get("profile"))

	def setUserProfile(self, user, profile=''):
		"""Set the profile of a given user to profile

		@param	self		A LTCConfigParser() instance
		@param	user		A user name string
		@param	profile		Optional. A profile name string.
								Clear the user profile if profile not given
		"""
		if not user in self.getUsersList():
			raise IndexError("\"{0}\" not in users list".format(user))
		if profile and not profile in self.getProfilesList():
			raise IndexError("\"{0}\" not in profiles list".format(profile))

		self._users.find("user[@name='{0}']".format(user)).set("profile", profile)
		self._syncConfigs()

	def getProfileUsersList(self, profile):
		"""Return the users list in a profile

		@param	self		A LTCConfigParser() instance
		@param	profile	A profile name string
		@return				A list of users in profile
		"""
		if not profile in self.getProfilesList():
			raise IndexError("\"{0}\" not in profiles list".format(profile))

		_u = [u.get("name") for u in self._users.findall(
			"user[@profile='{0}']".format(profile))]
		_u.sort()

		return(_u)

	def _findProfile(self, profile):
		"""Take the Element object of profile

		@param	self			A LTCConfigParser() instance
		@param	profile			A 'from' profile name string
		@return					A Element object of profile
		"""
		if not profile in self.getProfilesList():
			raise IndexError("\"{0}\" not in profiles list".format(profile))

		return(self._profiles.find("profile[@name='{0}']".format(profile)))

	def _deleteProfile(self, profile):
		"""Delete and return profile from profiles list

		@param	self			A LTCConfigParser() instance
		@param	profile			A profile name string to remove
		"""
		if not profile in self.getProfilesList():
			raise IndexError("\"{0}\" not in profiles list".format(profile))

		self._profiles.remove(
			self._profiles.find("profile[@name='{0}']".format(profile)))

	def moveProfile(self, oldprofile, newprofile='', copy=False):
		"""Move the 'oldprofile' to 'newprofile'

		If newprofile not given, delete oldprofile
		If newprofile already exists, overwrite it

		@param	self			A LTCConfigParser() instance
		@param	oldprofile	A 'from' profile name string
		@param	newprofile	A 'to' profile name string.
		@param	copy	If True, make a copy and keep users on oldprofile,
							instead a move.
		"""

		if not oldprofile in self.getProfilesList():
			raise IndexError("\"{0}\" not in profiles list".format(oldprofile))

		if not newprofile:
			self._deleteProfile(oldprofile)
			self._syncConfigs()
			return
		elif newprofile in self.getProfilesList():
			self._deleteProfile(newprofile)

		if copy:
			profile = deepcopy(self._findProfile(oldprofile))
			self._profiles.append(profile)
		else:
			profile = self._findProfile(oldprofile)
			for u in self.getProfileUsersList(oldprofile):
				self.setUserProfile(u, newprofile)

		profile.set("name", newprofile)

		self._syncConfigs()

	def newProfile(self, profile):
		"""Creates a new profile based on profileFalse

		@param	self		A LTCConfigParser() instance
		@param	profile		A profile name string.
		"""
		if not profile:
			return

		if profile in self.getProfilesList():
			self._deleteProfile(self._findProfile(profile))

		p = deepcopy(self._profileFalse)
		p.tag = "profile"
		p.set("name", profile)
		self._profiles.append(p)
		self._syncConfigs()

	def getOptionsList(self):
		"""Return a list of options in category of profile

		If category not given, all options are listed
		@param	self		A LTCConfigParser() instance
		@param	profile		A profile name string.
		@return				A list of strings with the options names
								in category
		"""
		_o = [o.get("name") for o in self._profileFalse.findall("option")]
		_o.sort()
		return(_o)

	def getActiveOptions(self, profile):
		"""Return a list of options activated on profile

		@param	self		A LTCConfigParser() instance
		@param	profile		A profile name string.
		@return				A list of strings with the options names
							in category
		"""
		if not profile in self.getProfilesList():
			raise IndexError("\"{0}\" not in profiles list".format(profile))

		_o = [o.get('name') for o in self._profiles.find(("profile[@name='{0}']/"+
			"option[@on='true']").format(profile))]
		_o.sort()
		return(_o)

	def getOption(self, profile, option):
		"""Return the value of option in profile

		@param	self		A LTCConfigParser() instance
		@param	profile		A profile name string.
		@param	option		A option name string.
		@return				The bool value of option
		"""
		if not profile in self.getProfilesList():
			raise IndexError("\"{0}\" not in profiles list".format(profile))
		if not option in self.getOptionsList():
			raise IndexError("\"{0}\" not in options list".format(option))

		o = self._profiles.find(("profile[@name='{0}']/option[@name='{1}']")\
			.format(profile, option))
		# Using string to match partial names, like F and no, to false
		if o.get("on").lower() in "false off not 0":
			return(False)
		else:
			return(True)

	def setOption(self, profile, option, value):
		"""Set the option in profile to value

		@param	self		A LTCConfigParser() instance
		@param	profile	A profile name string.
		@param	option	A option name string.
		@param	value	A new bool value.
		"""
		if not profile in self.getProfilesList():
			raise IndexError("\"{0}\" not in profiles list".format(profile))
		if not option in self.getOptionsList():
			raise IndexError("\"{0}\" not in options list".format(option))

		o = self._profiles.find(("profile[@name='{0}']/option[@name='{1}']")\
			.format(profile, option))
		o.set("on", str(value).lower())
		self._syncConfigs()

	def getConfig(self, profile, option):
		"""Get XML object based config information of an option

		@param	self		A LTCConfigParser() instance
		@param	profile		A profile name string.
		@param	option		A option name string.
		@return				A lxml.etree.Element object
		"""
		if not profile in self.getProfilesList():
			raise IndexError("\"{0}\" not in profiles list".format(profile))
		if not option in self.getOptionsList():
			raise IndexError("\"{0}\" not in options list".format(option))

		return(deepcopy(
			self._profiles.find(("profile[@name='{0}']/option[@name='{1}']")\
				.format(profile, option))))

	def setConfig(self, profile, option, config):
		"""Get XML object based config information of an option

		@param	self		A LTCConfigParser() instance
		@param	profile		A profile name string.
		@param	option		A option name string.
		@param	config		A lxml.etree.Element object to be stored
		"""
		if not profile in self.getProfilesList():
			raise IndexError("\"{0}\" not in profiles list".format(profile))
		if not option in self.getOptionsList():
			raise IndexError("\"{0}\" not in options list".format(option))

		P = self._profiles.find("profile[@name='{0}']".format(profile))
		O = P.find(("option[@name='{0}']").format(option))
		config.tag = O.tag
		#config.attrib = O.attrib
		config.attrib.clear()
		for i in O.attrib:
			config.attrib[i] = O.attrib[i]


		P.remove(O)
		P.append(config)

		self._syncConfigs()
		del O

	def addUser(self, username):
		"""Add a user to configfile

		@param	self		A LTCConfigParser instance
		@param	username	A string containing user's username
		"""
		if username in self.getUsersList():
			return
		ET.SubElement(self._users, "user", attrib={"name": username,
			"profile": "", "sync": "false"})
		self._syncConfigs()

	def delUser(self, username):
		"""Remove user of configfile

		@param	self		A LTCConfigParser instance
		@param	username	A string containining user's username
		"""
		if not username in self.getUsersList():
			raise IndexError("\"{0}\" not in users list".format(username))
		self._users.remove(self._users.find("user[@name='{0}']".format(username)))
		self._syncConfigs()
	
	def getUserS(self, user):
		"""Return true if user will be synced
		
		@param	self		A LTCConfigParser instance
		@param	user		A valid existing user string name
		@return			Bool	
		"""
		if not user in self.getUsersList():
			raise IndexError("\"{0}\" not in users list".format(user))
			
		U = self._users.find("user[@name='{0}']".format(user))
		if U.get("sync").lower() in "false no off 0":
			return(False)
		else:
			return(True)
	
	def setUserSync(self, user, passwd, uid, initGroup, groups, home, shell):
		"""Set sync options for user
		
		@param	self		A LTCConfigParser instance
		@param	user		A valid existing username
		@param	passwd		Plaintext password, will be encrypted
		@param	uid			Int value for UID. If already in use, skip user sync
		@param	initGroup	Initial group. It'll be created if doesn't exist
		@param	groups		String list. Other groups. Skip non-existing ones
		@param	home		Home directory
		@param	shell		Shell
		"""
		if not user in self.getUsersList():
			raise IndexError("\"{0}\" not in users list".format(user))
			
		U = self._users.find("user[@name='{0}']".format(user))
		U.set("sync", "true")
		
		p = U.find("shadow_pw")
		if not p: p = ET.SubElement(U, "shadow_pw")
		hash = crypt(passwd, '$1$'+passwdGen(8))
		p.text = hash
		
		u = U.find("uid")
		if not u: u = ET.SubElement(U, "uid")
		u.text = str(uid)
		
		i = U.find("init_group")
		if not i: i = ET.SubElement(U, "init_group")
		i.text = initGroup
		
		g = U.find("groups")
		if not g: g = ET.SubElement(U, "groups")
		g.text = ','.join(groups)
		
		h = U.find("home")
		if not h: h = ET.SubElement(U, "home")
		h.text = home
		
		s = U.find("shell")
		if not s: s = ET.SubElement(U, "shell")
		s.text = shell
		
		self._syncConfigs()
	
	def getUserSync(self, user):
		"""Get sync options for user
		
		@param	self		A LTCConfigParser instance
		@param	user		A valid existing username
		@return			A dict containing user's options
		"""
		if not user in self.getUsersList():
			raise IndexError("\"{0}\" not in users list".format(user))
		
		U = self._users.find("user[@name='{0}']".format(user))
		if U.get("sync").lower() in "false no off 0":
			return({i: None for i in 
				["hash", "uid", "init_group", "groups", "home", "shell"]})
		
		p = U.find("shadow_pw")
		if p is not None: p = p.text
		u = U.find("uid")
		if u is not None: u = int(u.text)
		i = U.find("init_group")
		if i is not None: i = i.text
		g = U.find("groups")
		if g is not None: g = g.text.split(',')
		h = U.find("home")
		if h is not None: h = h.text
		s = U.find("shell")
		if s is not None: s = s.text
		
		D = {
			"hash": p, 
			"uid": u, 
			"init_group": i, 
			"groups": g, 
			"home": h, 
			"shell": s
		}
		
		return(D)

	def getKeys(self):
		"""Return config file SSH public keys list

		@param	self		A LTCConfigParser instance
		@return				A list of strings containing pubkeys
		"""
		return([k.text for k in self._keys.findall("key")])

	def addKey(self, key):
		"""Add a given key to configfile

		@param	self		A LTCConfigParser instance
		@param	key			A string containing a valid pubkey
		"""
		if key.strip() in self.getKeys():
			return

		ET.SubElement(self._keys, "key").text = key.strip()
		self._syncConfigs()

	def delKey(self, key):
		"""Remove a given key from configfile

		@param	self		A LTCConfigParser instance
		@param	key			A string containing a valid pubkey
		"""
		k = key.strip().split()
		if len(k) != 3 or k[0] not in ['ssh-dss', 'ssh-rsa']:
			raise ValueError("Invalid SSH PubKey")
		if key.strip() not in self.getKeys():
			raise IndexError("PubKey not in Keys list")

		for k in self._keys:
			if k.text.strip() == key.strip():
				self._keys.remove(k)

		self._syncConfigs()

if __name__ == '__main__':
	from sys import argv
	configparser = LTCConfigParser()
	configparser._makeTestConfigs(argv[1])
