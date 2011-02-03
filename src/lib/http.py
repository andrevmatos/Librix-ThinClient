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

from http.server import HTTPServer,BaseHTTPRequestHandler
from PyQt4.QtCore import QThread

class VersionHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		"""Answer get request with configname string

		@param	self		A VersionHandler instance
		"""
		self.send_response(200)
		self.send_header('Content-Type', 'text/plain')
		#self.send_header('Transfer-Encoding', 'chunked')
		self.end_headers()

		self.wfile.write(self.server.configparser.getName().encode('utf-8'))

class ThreadedServer(QThread):
	def __init__(self, configparser, port):
		"""Instantiate a threaded HTTP Server

		providing configparser version name
		@param	self		A ThreadedServer instance
		@param	configparser	A LTCConfigParser instance
		@param	port		Int Port Number to listen
		"""
		QThread.__init__(self)

		self.configparser = configparser
		self.port = port

		self.server = HTTPServer(('', port), VersionHandler)
		self.server.configparser = configparser

	def run(self):
		"""Start server listening

		@param	self		A ThreadedServer instance
		"""
		print("HTTP Serving on port {0}".format(self.port))
		self.server.serve_forever()

