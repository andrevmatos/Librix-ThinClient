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

import sys
import signal
from os.path import isfile
from optparse import OptionParser

if __name__ == "__main__":
	# Accept C^c and SIGTERMs to exit (skip passing this keys to Qt)
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	
	usage = "Usage: %prog [-c|-v] [configfile]"
	
	parser = OptionParser(usage=usage)
	parser.add_option("-c", "--client", dest="mode", default=False,
		action="store_true", help="Executes LTMT GUI Client")
	parser.add_option("-d", "--daemon", dest="mode", default=False,
		action="store_false", help="Executes LTMT Daemon")
		
	parser.add_option("-v", "--verbose", default=False, dest="verbose",
		action="store_true", help="Print debug messages to standard output")
	parser.add_option("-q", "--quiet", default=False, dest="verbose",
		action="store_false", help="Don't print debug messages to standard output")
	
	(options, args) = parser.parse_args()
	
	if not options.verbose:
		sys.stdout = open("/dev/null", "w")
		sys.stderr = open("/dev/null", "w")
		#sys.stderr.close()
		#sys.stdout.close()
	
	configfile = None
	for o in args:
		if isfile(o):
			configfile = o
			break
	
	if options.mode:
		from ui.main import main
		main(configfile)
	else:
		from daemon.tcd import main
		main(configfile)
