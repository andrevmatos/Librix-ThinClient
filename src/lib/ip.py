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

def Bin2Int(addr):
	"""Convert addr from binary to integer notation

	@param	addr		Address in binary notation: (0|1)*32 string
	@return				Int containing addr in int format
	"""
	return(int(addr, 2))

def Int2Bin(addr):
	"""Convert addr from integer to binary notation

	@param	addr		IP address in integer notation
	@return				String containing binary notation of addr
	"""
	return(bin(int(addr)).replace('0b', '', 1).rjust(32, '0'))

def Dec2Bin(addr):
	"""Convert addr from decimal to binary notation

	@param	addr		Address in decimal notation
	@return				String containing addr in binary notation
	"""
	_I = ''
	for i in addr.split('.'):
		_I += bin(int(i)).replace('0b', '', 1).rjust(8, '0')
	return(_I)

def Bin2Dec(addr):
	"""Convert addr from binary to decimal notation

	@param	addr		Address in binary notation: (0|1)*32 string
	@return				String containing addr in decimal notation
	"""
	return('.'.join([str(int(addr[i*8:(i+1)*8], 2)) for i in range(4)]))

class IPRange(object):
	"""Iterates over a ip range, from start to end, including"""
	def __init__(self, start, end):
		"""Init method

		@param	self		A IPRange instance
		@param	start		A range start address
		@param	end			A range end address, including
		"""
		self._start = Bin2Int(Dec2Bin(start))
		self._end = Bin2Int(Dec2Bin(end))

	def __contains__(self, ip):
		"""Tell if IP is within range

		@param	self		A IPRange instance
		@param	ip			A IP address in decimal notation
		@return				Bool. True if IP is into range
		"""
		i = Bin2Int(Dec2Bin(ip))
		if i >= self._start and i <= self._end:
			return True
		else:
			return False

	def __iter__(self):
		self._current = self._start
		return self

	def __next__(self):
		p = self._current
		if p > self._end:
			raise StopIteration
		self._current += 1
		return(Bin2Dec(Int2Bin(p)))

class Subnetwork(object):
	"""Iterator class for subnetwork addresses"""
	def __init__(self, ip, netmask):
		"""Returns a tuple with 2 strings containing first and last IPs in subnet

		@param	ip		A string containing address in decimal notation
		@param	netmask	A string containing subnet in decimal notation
		@return			Iterator for all address in subnetwork
		"""
		# self._I is ip in integer notation
		self._I = Bin2Int(Dec2Bin(ip))

		# self._N is netmask in integer notation
		try:
			# If netmask given in CIDR notation
			self._N = Bin2Int(('1'*int(netmask)).ljust(32, '0'))
		except ValueError:
			# Else
			self._N = Bin2Int(Dec2Bin(netmask))

		self._net = Bin2Int(''.join([Int2Bin(self._I)[i] for i in range(32) \
			if int(Int2Bin(self._N)[i], 2)]).ljust(32, '0'))

		self._end =  self._net+(2**Int2Bin(self._N).count('0'))-3

	def __iter__(self):
		"""Iterator return"""

		self._current = self._net

		return self

	def __contains__(self, ip):
		"""Tell if ip is into subnetwork

		@param	self		A Subnetwork instance
		@param	ip			A IP address in decimal notation
		@return				Bool. True if ip is into network
		"""
		i = Bin2Int(Dec2Bin(ip))
		if i > self._net and i <= self._end:
			return True
		else:
			return False

	def __next__(self):
		if self._current > self._end:
			raise StopIteration
		# current += 1
		self._current += 1
		return(Bin2Dec(Int2Bin(self._current)))
