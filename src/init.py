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

if __name__ == "__main__":
	# Accept C^c and SIGTERMs to exit (skip passing this keys to Qt)
	signal.signal(signal.SIGINT, signal.SIG_DFL)

	# TODO: basic argument parser, make it better
	if "-c" in sys.argv:
		from ui.main import main
		main()
	elif "-d" in sys.argv:
		from daemon.tcd import run
		run()
	else:
		sys.stderr.write("Invalid option!\n")
