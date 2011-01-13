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
from random import choice

from lib.utils import sha512sum

class LTCConfigParser(object):
	"""LTCConfigParser class to manipulate XML configuration file
	to Librix Thin Client Administration Interface"""

	def __init__(self):
		"""Instantiate LTCConfigParser

		@param	self		A LTCConfigParser instance
		"""
		self.st_mtime = 0
		self.hash = 0
		self._parser = ET.XMLParser(encoding="utf-8", remove_blank_text=True)

	def _makeTestConfigs(self, file):
		"""Make test configs

		Write some random configurations to tests librix TCAI
		@param	self		A LTCConfigParser instance
		"""
		self._config = ET.Element("librix_tcd_config")

		self._profileFalse = ET.SubElement(self._config, "profileFalse",
			attrib={"name": "profileFalse"})

		for c in ["hardware", "software"]:
				category = ET.SubElement(self._profileFalse, "category",
					attrib={"name": c})
				for o in range(1, 5):
					o = "{0} option {1}".format(c, o)
					option = ET.SubElement(category, "option",
						attrib={"name": o, "on": "false"})

		self._profiles = ET.SubElement(self._config, "profiles")

		for p in ["Profile 1", "Profile 2", "Profile 3"]:
			profile = deepcopy(self._profileFalse)
			profile.tag = "profile"
			profile.attrib["name"] = p
			self._profiles.append(profile)
			for c in profile:
				if c.tag == 'category':
					for o in c:
						if o.tag == 'option':
							o.attrib["on"] = str(choice([False, True])).lower()

		self._users = ET.SubElement(self._config, "users")
		for u in ['andre', 'ivan', 'roberto', 'guilherme',
			'david', 'carvalho']:
				user = ET.SubElement(self._users, "user",
					attrib={"name": u, "profile": choice(self.getProfilesList())})

		self.backupfile = file
		self.syncConfigs()
		del self.backupfile

	def readConfigFile(self, file=''):
		"""Parse a configfile

		@param	self		A LTCConfigParser instance
		@param	file		A filepath string. Default is self.configfile
		"""
		if not file: file = self.configfile
		self.configfile = file
		self.backupfile = file + '~'

		# Register mtime and sha512sum
		self.st_mtime = os.stat(file).st_mtime
		self.hash = sha512sum(file)

		self._config = ET.parse(file, parser=self._parser).getroot()

		self._profiles = self._config.find("profiles")
		self._profileFalse = self._config.find("profileFalse")
		self._users = self._config.find("users")

	def writeConfigFile(self, file=''):
		"""Write configurations from self.backupfile to file

		@param	self		A LTCConfigParser instance
		@param	file		A filepath string. Default is self.configfile
		"""
		if not file: file = self.configfile
		if not os.path.isfile(self.backupfile): return

		with open(file, 'w') as destfile, open(self.backupfile, 'r') as backup:
			destfile.write(backup.read())

		os.remove(self.backupfile)
		self.readConfigFile(file)

	def _syncConfigs(self):
		"""Sync self.xml with self.backupfile

		@param	self		A LTCConfigParser instance
		"""
		self._config.getroottree().write(self.backupfile, pretty_print=True)

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
		@param	profile	Optional. A profile name string.
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

		profile = deepcopy(self._findProfile(oldprofile))
		profile.set("name", newprofile)
		self._profiles.append(profile)

		# Remove oldprofile
		if not copy:
			for u in self.getProfileUsersList(oldprofile):
				self.setUserProfile(u, newprofile)
			self._deleteProfile(oldprofile)

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

	def getCategoriesList(self):
		"""Return a list of categories in profile

		@param	self		A LTCConfigParser() instance
		@return				A list of strings with the
							categories names
		"""

		_c = [c.get("name") for c in self._profileFalse.findall("category")]
		_c.sort()
		return(_c)

	def getOptionsList(self, category=''):
		"""Return a list of options in category of profile

		If category not given, all options are listed
		@param	self		A LTCConfigParser() instance
		@param	profile		A profile name string.
		@param	category	A category name string.
		@return				A list of strings with the options names
								in category
		"""
		if category and not category in self.getCategoriesList():
			raise IndexError("\"{0}\" not in \
				category list".format(category))

		if category:
			_o = [o.get("name") for o in self._profileFalse.findall(
				"category[@name='{0}']/option".format(category))]
		else:
			_o = [o.get("name") for o in self._profileFalse.findall(
				"category/option".format(category))]
		_o.sort()
		return(_o)

	def getActiveOptions(self, profile):
		"""Return a list of options in category of profile

		If category not given, all options are listed
		@param	self		A LTCConfigParser() instance
		@param	profile		A profile name string.
		@param	category	A category name string.
		@return				A list of strings with the options names
								in category
		"""


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

		o = self._profiles.find(("profile[@name='{0}']/category/"+
			"option[@name='{2}']").format(profile, option))
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

		o = self._profiles.find(("profile[@name='{0}']/category/"+
			"option[@name='{2}']").format(profile, option))
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
			self._profiles.find(("profile[@name='{0}']/category/"+
			"option[@name='{2}']").format(profile, option))))

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

		O = self._profiles.find(("profile[@name='{0}']/category/"+
			"option[@name='{2}']").format(profile, option))
		att = deepcopy(O.attrib)
		O.getparent().replace(O, config)

		self._profiles.find(("profile[@name='{0}']/category/"+
		"option[@name='{2}']").format(profile, option)).attrib = att

		self._syncConfigs()
		del att
		del O

if __name__ == '__main__':
	from sys import argv
	configparser = LTCConfigParser()
	configparser._makeTestConfigs(argv[1])
