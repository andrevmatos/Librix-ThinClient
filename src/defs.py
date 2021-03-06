#!/usr/bin/env python3
#
#
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

pidfile = "/var/run/thinclient.pid"

configfile = "/etc/thinclient.conf"

logfile = "/var/log/thinclient.log"

rsyncdirs = ["/mnt/cdrom/librix"]
rsyncexclude = []	# e.g.: ['/mnt/cdrom/librix/etc/passwd']

http_port = 8088

version = "0.0.99"

__all__ = ["pidfile", "configfile", "logfile", "http_port", "version"]
