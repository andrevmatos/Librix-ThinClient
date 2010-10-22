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
#
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with librix-thinclient.  If not, see <http://www.gnu.org/licenses/>.

from random import choice
from xml.dom import minidom
from os.path import join, dirname,abspath

class LibrixTCD(object):
	def makeTestConfigs(self):
		"""Make test configs

		Effect: creates self.xml, self.config, self.profiles and self.users
			DOM objects, with default test configs
		@param	self		A LibrixTCD instance
		"""
		self.xml = minidom.getDOMImplementation().createDocument(None,
				"librix_tcd_config", None)

		self.config = self.xml.getElementsByTagName("librix_tcd_config")[0]

		self.profileFalse = self.xml.createElement("profileFalse")
		self.profileFalse.attributes["name"] = "profileFalse"
		self.config.appendChild(self.profileFalse)

		for c in ["hardware", "software"]:
				category = self.xml.createElement("category")
				category.attributes["name"] = c
				self.profileFalse.appendChild(category)
				for o in range(1, 5):
					o = "{0} option {1}".format(c, o)
					option = self.xml.createElement("option")
					option.attributes["name"] = o
					option.attributes["type"] = "bool"
					option.appendChild(self.xml.createTextNode(\
						str(False).lower()))
					category.appendChild(option)

		self.profiles = self.xml.createElement("profiles")
		self.config.appendChild(self.profiles)

		for p in ["Profile 1", "Profile 2", "Profile 3"]:
			profile = self.profileFalse.cloneNode(deep=True)
			profile.attributes["name"] = p
			profile.nodeName = profile.tagName = "profile"

			self.profiles.appendChild(profile)

			for c in [C for C in profile.childNodes if C.nodeName == 'category']:
				for o in [O for O in c.childNodes if O.nodeName == 'option']:
					o.firstChild.data = str(choice([False, True])).lower()

		self.users = self.xml.createElement("users")
		self.config.appendChild(self.users)
		for u in ['andre', 'ivan', 'roberto', 'guilherme',
			'david', 'carvalho']:
				user = self.xml.createElement("user")
				user.attributes["name"] = u
				user.attributes["profile"] = choice(self.getProfilesList())
				self.users.appendChild(user)

		self.syncConfigs()

	def __init__(self):
		"""Instantiate LibrixTCD

		@param	self		A LibrixTCD instance
		"""
		self.configfile = "configs.xml"
		self.configfile = join(dirname(abspath(__file__)), self.configfile)

		try:
			self.xml = minidom.parse(self.configfile)
			self.config = self.xml.getElementsByTagName("librix_tcd_config")[0]
			self.profiles = self.config.getElementsByTagName("profiles")[0]
			self.profileFalse = self.config.getElementsByTagName(\
				"profileFalse")[0]
			self.users = self.config.getElementsByTagName("users")[0]
			self.norm(self.xml)
			self.syncConfigs()
		except:
			self.makeTestConfigs()

	def norm(self, xml):
		for i in xml.childNodes:
			if type(i) == minidom.Text:
				i.data = i.data.strip()
			else:
				self.norm(i)

	def syncConfigs(self):
		"""Sync self.xml with self.configfile

		@param	self		A LibrixTCD instance
		"""
		file = open(self.configfile, 'w')
		file.write(self.xml.toprettyxml(encoding="UTF-8").decode("utf-8"))
		file.close()

	def getUsersList(self):
		"""Return the users list

		@param	self		A LibrixTCD() instance
		@return				A list of existing users
		"""
		_u = [u.attributes["name"].value for u in self.users.childNodes\
			if u.nodeName == 'user']
		_u.sort()
		return(_u)

	def getProfilesList(self):
		"""Return the profiles list

		@param	self		A LibrixTCD() instance
		@return				A list of existing profiles
		"""
		_p = [p.attributes["name"].value for p in self.profiles.childNodes \
			if p.nodeName == 'profile']
		_p.sort()
		return(_p)

	def getUserProfile(self, user):
		"""Return the profile of a given user

		@param	self		A LibrixTCD() instance
		@param	user		A user name string
		@return				A string containing the profile of user
		"""
		if not user in self.getUsersList():
			raise IndexError("\"{0}\" not in users list".format(user))

		for U in self.users.childNodes:
			if U.nodeName == 'user' and U.attributes["name"].value == user:
				return(U.attributes["profile"].value)

	def setUserProfile(self, user, profile=''):
		"""Set the profile of a given user to profile

		@param	self		A LibrixTCD() instance
		@param	user		A user name string
		@param	profile	Optional. A profile name string.
									Clear the user profile if profile not given
		"""
		if not user in self.getUsersList():
			raise IndexError("\"{0}\" not in users list".format(user))
		if profile and not profile in self.getProfilesList():
			raise IndexError("\"{0}\" not in profiles list".format(profile))

		for u in self.users.childNodes:
			if u.nodeName == 'user' and u.attributes["name"].value == user:
				u.attributes["profile"] = profile
				self.syncConfigs()
				return

	def getProfileUsersList(self, profile):
		"""Return the users list in a profile

		@param	self		A LibrixTCD() instance
		@param	profile	A profile name string
		@return				A list of users in profile
		"""
		if not profile in self.getProfilesList():
			raise IndexError("\"{0}\" not in profiles list".format(profile))

		_u = [u for u in self.getUsersList() \
			if self.getUserProfile(u) == profile]
		_u.sort()
		return(_u)

	def _findProfile(self, profile):
		"""Take the Element object of profile

		@param	self			A LibrixTCD() instance
		@param	profile		A 'from' profile name string
		@return					A Element DOM object of profile
		"""
		if not profile in self.getProfilesList():
			raise IndexError("\"{0}\" not in profiles list".format(profile))

		for p in self.profiles.childNodes:
			if p.nodeName == 'profile' and \
				p.attributes["name"].value == profile:
				return(p)

	def _deleteProfile(self, profile):
		"""Delete and return profile from profiles list

		@param	self			A LibrixTCD() instance
		@param	profile		A profile name string to remove
		@return					A Element object of profile
		"""
		if not profile in self.getProfilesList():
			raise IndexError("\"{0}\" not in profiles list".format(profile))

		p = self._findProfile(profile)
		for u in self.getProfileUsersList(profile):
			self.setUserProfile(u)
		P = self.profiles.removeChild(p)
		self.syncConfigs()
		return(P)

	def moveProfile(self, oldprofile, newprofile='', copy=False):
		"""Move the 'oldprofile' to 'newprofile'

		If newprofile not given, delete oldprofile
		If newprofile already exists, overwrite it

		@param	self			A LibrixTCD() instance
		@param	oldprofile	A 'from' profile name string
		@param	newprofile	A 'to' profile name string.
		@param	copy	If False (default), delete oldprofile after copy it to
									newprofile and move all users from
									oldprofile to newprofile
		"""

		if not oldprofile in self.getProfilesList():
			raise IndexError("\"{0}\" not in profiles list".format(oldprofile))

		if not newprofile:
			self._deleteProfile(oldprofile)
			self.syncConfigs()
			return
		elif newprofile in self.getProfilesList():
			self._deleteProfile(newprofile)

		profile = self._findProfile(oldprofile).cloneNode(deep=True)
		profile.attributes["name"] = newprofile
		self.profiles.appendChild(profile)

		if not copy:
			for u in self.getProfileUsersList(oldprofile):
				self.setUserProfile(u, newprofile)
			self._deleteProfile(oldprofile)

		self.syncConfigs()

	def getProfileCategoriesList(self, profile):
		"""Return a list of categories in profile

		@param	self		A LibrixTCD() instance
		@param	profile	A profile name string.
		@return				A list of strings with the
									categories names in profile
		"""
		if not profile in self.getProfilesList():
			raise IndexError("\"{0}\" not in profiles list".format(profile))

		_c = [c.attributes["name"].value for c in \
			self._findProfile(profile).childNodes if c.nodeName == 'category']
		_c.sort()
		return(_c)

	def getOptionsList(self, profile, category):
		"""Return a list of options in category of profile

		@param	self		A LibrixTCD() instance
		@param	profile	A profile name string.
		@param	category	A category name string.
		@return			A list of strings with the options names
								in category in profile
		"""
		if not profile in self.getProfilesList():
			raise IndexError("\"{0}\" not in profiles list".format(profile))
		if not category in self.getProfileCategoriesList(profile):
			raise IndexError("\"{0}\" not in \"{1}\
				\" category list".format(category, profile))

		for c in [c for c in self._findProfile(profile).childNodes \
			if c.nodeName == 'category']:
			if c.attributes["name"].value == category:
				_o = [o.attributes["name"].value for o in c.childNodes \
					if o.nodeName == 'option']

		_o.sort()
		return(_o)

	def getOption(self, profile, category, option):
		"""Return the value of option in category in profile

		@param	self			A LibrixTCD() instance
		@param	profile		A profile name string.
		@param	category	A category name string.
		@param	option		A option name string.
		@return					The bool value of option
		"""
		if not profile in self.getProfilesList():
			raise IndexError("\"{0}\" not in profiles list".format(profile))
		if not category in self.getProfileCategoriesList(profile):
			raise IndexError("\"{0}\" not in \"{1}\
				\" profile category list".format(category, profile))
		if not option in self.getOptionsList(profile, category):
			raise IndexError("\"{0}\" not in \"{1}\" category of \
				{2} profile options list".format(option, category, profile))

		for C in self._findProfile(profile).childNodes:
			if C.nodeName == 'category' and \
				C.attributes["name"].value == category:
				for O in C.childNodes:
					if O.nodeName == 'option' and \
						O.attributes["name"].value == option:
						o = O

		if "bool" in o.attributes["type"].value.lower():
			if "false" in o.firstChild.data.strip().lower():
				return(False)
			else:
				return(True)
		elif "int" in o.attributes["type"].value.lower():
			return(int(o.firstChild.data.strip()))
		else:
			return(o.firstChild.data.strip())

	def setOption(self, profile, category, option, value):
		"""Set the option in category in profile to value

		@param	self		A LibrixTCD() instance
		@param	profile	A profile name string.
		@param	category	A category name string.
		@param	option	A option name string.
		@param	value	A new value bool.
		"""
		if not profile in self.getProfilesList():
			raise IndexError("\"{0}\" not in profiles list".format(profile))
		if not category in self.getProfileCategoriesList(profile):
			raise IndexError("\"{0}\" not in \"{1}\
				\" profile category list".format(category, profile))
		if not option in self.getOptionsList(profile, category):
			raise IndexError("\"{0}\" not in \"{1}\" category of \
				{2} profile options list".format(option, category, profile))

		for C in self._findProfile(profile).childNodes:
			if C.nodeName == 'category' and \
				C.attributes["name"].value == category:
				for O in C.childNodes:
					if O.nodeName == 'option' and \
						O.attributes["name"].value == option:
						o = O

		o.attributes["type"] = str(type(value)).lower()
		o.firstChild.data = str(value).strip()
		self.syncConfigs()

	def newProfile(self, profile):
		"""Set the option in category in profile to value

		@param	self		A LibrixTCD() instance
		@param	profile	A profile name string.
		"""
		if not profile:
			return

		if profile in self.getProfilesList():
			self.profiles.removeChild(self._findProfile(profile))

		p = self.profileFalse.cloneNode(deep=True)
		p.attributes["name"] = profile
		p.nodeName = p.tagName = "profile"
		self.profiles.appendChild(p)
		self.syncConfigs()

if __name__ == '__main__':
	LibrixTCD()
