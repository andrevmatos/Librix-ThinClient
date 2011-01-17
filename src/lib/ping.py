﻿#!/usr/bin/env python3
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

import os, sys, socket, struct, select, time

#####################################
# Python Ping implementation
# credits to Matthew Dixon Cowles
# http://www.g-loaded.eu/2009/10/30/python-ping/
# distributed under GNU GPL v2
#####################################

ICMP_ECHO_REQUEST = 8 # Seems to be the same on Solaris.

def checksum(source_string):
	"""
	I'm not too confident that this is right but testing seems
	to suggest that it gives the same answers as in_cksum in ping.c
	"""
	sum = 0
	countTo = (len(source_string)/2)*2
	count = 0
	while count<countTo:
		thisVal = ord(source_string[count + 1])*256 + ord(source_string[count])
		sum = sum + thisVal
		sum = sum & 0xffffffff # Necessary?
		count = count + 2

	if countTo<len(source_string):
		sum = sum + ord(source_string[len(source_string) - 1])
		sum = sum & 0xffffffff # Necessary?

	sum = (sum >> 16)  +  (sum & 0xffff)
	sum = sum + (sum >> 16)
	answer = ~sum
	answer = answer & 0xffff

	# Swap bytes. Bugger me if I know why.
	answer = answer >> 8 | (answer << 8 & 0xff00)

	return answer


def receive_one_ping(my_socket, ID, timeout):
	"""
	receive the ping from the socket.
	"""
	timeLeft = timeout
	while True:
		startedSelect = time.time()
		whatReady = select.select([my_socket], [], [], timeLeft)
		howLongInSelect = (time.time() - startedSelect)
		if whatReady[0] == []: # Timeout
			return

		timeReceived = time.time()
		recPacket, addr = my_socket.recvfrom(1024)
		icmpHeader = recPacket[20:28]
		type, code, checksum, packetID, sequence = struct.unpack(
			"bbHHh", icmpHeader
		)
		if packetID == ID:
			bytesInDouble = struct.calcsize("d")
			timeSent = struct.unpack("d", recPacket[28:28 + bytesInDouble])[0]
			return timeReceived - timeSent

		timeLeft = timeLeft - howLongInSelect
		if timeLeft <= 0:
			return


def send_one_ping(my_socket, dest_addr, ID):
	"""
	Send one ping to the given >dest_addr<.
	"""
	dest_addr  =  socket.gethostbyname(dest_addr)

	# Header is type (8), code (8), checksum (16), id (16), sequence (16)
	my_checksum = 0

	# Make a dummy heder with a 0 checksum.
	header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, my_checksum, ID, 1)
	bytesInDouble = struct.calcsize("d")
	data = (192 - bytesInDouble) * "Q"
	data = str(struct.pack("d", time.time())) + data

	# Calculate the checksum on the data and the dummy header.
	my_checksum = checksum(str(header) + data)

	# Now that we have the right checksum, we put that in. It's just easier
	# to make up a new header than to stuff it into the dummy.
	header = struct.pack(
		"bbHHh", ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), ID, 1
	)
	packet = str(header) + data
	my_socket.sendto(packet, (dest_addr, 1)) # Don't know about the 1


def ping(dest_addr, timeout=5):
	"""
	Returns either the delay (in seconds) or none on timeout.
	"""
	icmp = socket.getprotobyname("icmp")
	try:
		my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
	except socket.error as errors_tuple:
		(errno, msg) = errors_tuple
		if errno == 1:
			# Operation not permitted
			msg = msg + (
				" - Note that ICMP messages can only be sent from processes"
				" running as root."
			)
			raise socket.error(msg)
		raise # raise the original error

	my_ID = os.getpid() & 0xFFFF

	send_one_ping(my_socket, dest_addr, my_ID)
	delay = receive_one_ping(my_socket, my_ID, timeout)

	my_socket.close()
	return delay
