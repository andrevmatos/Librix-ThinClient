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
from copy import deepcopy

class LibrixTCD(object):
	def __init__(self):
		"""Instantiate a LibrixTCD iobject

		@param	self	a LibrixTCD() instance
		"""
		self.options = {
			'hardware': dict([(o, False) for o in ['option 1','option 2','option 3','option 4']]),
			'software': dict([(o, False) for o in ['option 5','option 6','option 7','option 8']]),
		}

		self.profiles = dict([(p,  deepcopy(self.options)) for p in ['Profile 1', 'Profile 2', 'Profile 3']])

		for p in self.profiles:
			for c in self.profiles[p]:
				for o in self.profiles[p][c]:
					self.profiles[p][c][o] = choice([False, True])

		self.users = dict([(u, choice(self.getProfilesList())) for u in ['andre', 'ivan', 'roberto', 'guilherme','david', 'carvalho']])

	def getUsersList(self):
		"""Return the users list

		@param	self		A LibrixTCD() instance
		@return			A list of existing users
		"""
		_u = list(self.users.keys())
		_u.sort()
		return(_u)

	def getProfilesList(self):
		"""Return the profiles list

		@param	self		A LibrixTCD() instance
		@return			A list of existing profiles
		"""
		_p = list(self.profiles.keys())
		_p.sort()
		return(_p)

	def getUserProfile(self, user):
		"""Return the profile of a given user

		@param	self		A LibrixTCD() instance
		@param	user		A user name string
		@return			A string containing the profile of user
		"""
		if not user in self.users:
			raise IndexError("\"{0}\" not in users list".format(user))
		return(self.users[user])

	def setUserProfile(self, user, profile=''):
		"""Set the profile of a given user to profile

		@param	self		A LibrixTCD() instance
		@param	user		A user name string
		@param	profile	Optional. A profile name string. Clear the user profile if profile not given
		"""
		if not user in self.users:
			raise IndexError("\"{0}\" not in users list".format(user))
		if profile and not profile in self.profiles:
			raise IndexError("\"{0}\" not in profiles list".format(profile))
		self.users[user] = profile

	def getProfileUsersList(self, profile):
		"""Return the users list in a profile

		@param	self		A LibrixTCD() instance
		@param	profile	A profile name string
		@return			A list of users in profile
		"""
		if not profile in self.profiles:
			raise IndexError("\"{0}\" not in profiles list".format(profile))
		_u = [u for u in self.users if self.users[u] == profile]
		_u.sort()
		return(_u)

	def moveProfile(self, oldname, newname='', copy=False):
		"""Move the 'oldname' profile to 'newname' profile

		@param	self		A LibrixTCD() instance
		@param	oldname	A user name string
		@param	newname	Optional. A profile name string. Del oldname profile if newname not given
		@param	copy		Optional. Bool default False. If true, preserve the original profile, making a copy
		"""

		if not oldname in self.profiles:
			raise IndexError("\"{0}\" not in profiles list".format(oldname))
		if newname in self.profiles:
			del self.profiles[newname]


		if not newname:
			for u in self.getProfileUsersList(oldname):
				self.setUserProfile(u)
			del self.profiles[oldname]
			return
		self.profiles[newname] = deepcopy(self.profiles[oldname])
		if not copy:
			for u in self.getProfileUsersList(oldname):
				self.setUserProfile(u, newname)
			del self.profiles[oldname]

	def getProfileCategoriesList(self, profile):
		"""Return a list of categories in profile

		@param	self		A LibrixTCD() instance
		@param	profile	A profile name string.
		@return			A list of strings with the categories names in profile
		"""
		if not profile in self.profiles:
			raise IndexError("\"{0}\" not in profiles list".format(profile))

		_c = [c for c in self.profiles[profile]]
		_c.sort()
		return(_c)

	def getOptionsList(self, profile, category):
		"""Return a list of options in category of profile

		@param	self		A LibrixTCD() instance
		@param	profile	A profile name string.
		@param	category	A category name string.
		@return			A list of strings with the options names in category in profile
		"""
		if not profile in self.profiles:
			raise IndexError("\"{0}\" not in profiles list".format(profile))
		if not category in self.profiles[profile]:
			raise IndexError("\"{0}\" not in \"{1}\" category list".format(category, profile))

		_o = [o for o in self.profiles[profile][category]]
		_o.sort()
		return(_o)

	def getOption(self, profile, category, option):
		"""Return the value of option in category in profile

		@param	self		A LibrixTCD() instance
		@param	profile	A profile name string.
		@param	category	A category name string.
		@param	option	A option name string.
		@return			The value of option
		"""
		if not profile in self.profiles:
			raise IndexError("\"{0}\" not in profiles list".format(profile))
		if not category in self.profiles[profile]:
			raise IndexError("\"{0}\" not in \"{1}\" profile category list".format(category, profile))
		if not option in self.profiles[profile][category]:
			raise IndexError("\"{0}\" not in \"{1}\"category of {2} profile options list".format(option, category, profile))

		return(self.profiles[profile][category][option])


	def setOption(self, profile, category, option, value):
		"""Set the option in category in profile to value

		@param	self		A LibrixTCD() instance
		@param	profile	A profile name string.
		@param	category	A category name string.
		@param	option	A option name string.
		@param	value	A new value bool.
		"""
		if not profile in self.profiles:
			raise IndexError("\"{0}\" not in profiles list".format(profile))
		if not category in self.profiles[profile]:
			raise IndexError("\"{0}\" not in \"{1}\" profile category list".format(category, profile))
		if not option in self.profiles[profile][category]:
			raise IndexError("\"{0}\" not in \"{1}\"category of {2} profile options list".format(option, category, profile))

		self.profiles[profile][category][option] = value

	def newProfile(self, profile):
		"""Set the option in category in profile to value

		@param	self		A LibrixTCD() instance
		@param	profile	A profile name string.
		"""
		self.profiles[profile] = deepcopy(self.options)

if __name__ == '__main__':
	LibrixTCD()
