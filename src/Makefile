# Makefile
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

# Makefile

SHELL=/bin/bash

.PHONY: compile

compile:
	for i in $$( find -iname *.ui ); do \
		echo "Compiling UI: $${i}" ; \
		pyuic4 --from-imports -x -i 0 "$${i}" -o "$$( dirname $${i} )/Ui_$$( basename $${i} | sed 's/.ui$$/.py/g' )" ; \
	done ;
	for i in $$( find -iname *.qrc ); do \
		echo "Compiling Resource: $${i}" ; \
		pyrcc4 -py3 "$${i}" -o "$$( dirname $${i} )/../$$( basename $${i} | sed 's/.qrc$$/_rc.py/g' )" ; \
	done

clean:
	find ./ -iname \*.pyc -delete ; \
	find ./ -iname \*Ui_\*py -delete ; \
	find ./ -iname \*_rc.py -delete
