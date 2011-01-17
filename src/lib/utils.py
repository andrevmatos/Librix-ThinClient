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

import string
from random import choice
from hashlib import sha512

def passwdGen(size=8):
	"""Generates a password (random letters and digits string) of size lenght

	@param	size		The string lenght
	"""
	return(''.join([choice(string.ascii_letters + string.digits)\
		for i in range(size)]))

def sha512sum(filepath):
	"""Generates a sha512 hex digest of filepath

	@param	filepath	A filepath string
	"""
	with open(filepath, 'r') as f:
		return(sha512(f.read().encode('utf-8')).hexdigest())

def subnetwork(ip, netmask):
	"""Returns a tuple with 2 strings containing first and last IPs in subnet

	@param	ip		A string containing a valid IPv4 address
	@param	netmask	A string containing a valid IPv4 subnetwork mask
	@return			A 2 strings tuple
	"""
	# I = IP in binary notation
	I = ''
	for i in ip.split('.'):
		I += bin(int(i)).replace('0b', '', 1).rjust(8, '0')
	# N = netmask in binary notation
	N = ''
	for n in netmask.split('.'):
		N += bin(int(n)).replace('0b', '', 1).rjust(8, '0')
	#print("@@", '\n', I, '\n', N)
	# net = network address in binary notation
	net = ''.join([I[i] for i in range(32) if int(N[i], 2)]).ljust(32, '0')
	# first = first ip (net+1) in binary notation
	first = bin(int(net, 2)+1).replace('0b', '', 1).rjust(32, '0')
	# last = last ip (net+n-broadcast-1) in binary notation,
	# where n is number of hosts on subnetwork
	last = bin(int(net, 2)+(2**N.count('0'))-2)\
		.replace('0b', '', 1).rjust(32, '0')

	# convert first and last IPs from binary to decimal notation
	r = ('.'.join([str(int(first[i*8:(i+1)*8], 2)) for i in range(4)]),
		'.'.join([str(int(last[i*8:(i+1)*8], 2)) for i in range(4)]))
	return(r)
