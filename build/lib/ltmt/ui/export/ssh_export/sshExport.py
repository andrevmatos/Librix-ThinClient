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

import os
from PyQt4 import QtGui

from ltmt.ui.export.ssh_export.Ui_sshExport import Ui_SSHExport
from ltmt.ui.export.ssh_export.threadedExport import ThreadedExport

n_threads = 4

class SSHExport(QtGui.QDialog):
	"""Show a progress dialog of export operations through SSH"""
	def __init__(self, files, privkey, targets, parent=None):
		"""Init method

		@param	self	A SSHExport instance
		@param	files	A list of files to send to
		@param	privkey	A filepath to a readable private key file
		@param	targets	A list of hosts to do scp with files
		@param	parent	Parent QtGui.QWidget
		"""
		print("__sshExport initiated")
		self.files = files
		self.privkey = privkey
		self.targets = targets
		self.parent = parent

		for i in files:
			if not os.access(i, os.R_OK):
				raise IOError("\"{0}\" file could not be read!".format(i))
		if not os.access(privkey, os.R_OK):
			raise IOError("\"{0}\" privkey file could not be read!")

		QtGui.QDialog.__init__(self, parent)

		self.ui = Ui_SSHExport()
		self.ui.setupUi(self)

		self.showDetails(False)

		self.threads = []
		self.tree = {}
		self.done = []
	
	def showDetails(self, value):
		"""Show or hide details widget

		@param	self		A SSHExport instance
		@param	value		Bool. If True, show widget, else, hide
		"""
		self.ui.detailsWidget.setVisible(value)
		self.ui.detailsButton.setIcon(
			[QtGui.QIcon(":/ssh_export/arrow-down-double.png"),
			QtGui.QIcon(":/ssh_export/arrow-up-double.png")][value])

	def execThreads(self):
		targets = []	# a list of n_threads list or less, containing targets
		# distribute self.targets in n_threads number of lists into targets
		for i in range(len(self.targets)):
			t = i % n_threads
			if len(targets) <= t:
				targets.append([])
			targets[t].append(self.targets[i])

		# for each list of targets, start a thread
		for i in targets:
			T = ThreadedExport(self.files, self.privkey, i)
			self.threads.append(T)
			T.startedSCP.connect(self.targetRun)
			T.finishedSCP.connect(self.targetDone)
			T.errorSCP.connect(self.targetError)
			T.requestPasswd.connect(self.passwdRequest)
			T.finished.connect(self.threadFinished)

		# for each thread
		for i in range(len(self.threads)):
			T = QtGui.QTreeWidgetItem(self.ui.detailsTree,
				["Thread {0}".format(i)])
			for t in self.threads[i].targets:
				self.tree[t] = QtGui.QTreeWidgetItem(T, ["Send Files",
					t, "Queued"])

		# finally, start threads
		for i in self.threads:
			i.start()

	def targetDone(self, target):
		"""For a given target, set done status in details tree

		@param	self		A ThreadedExport instance
		@param	target		String containing target's address
		"""
		self.tree[target].setText(2, "Done")
		self.done.append(target)
		self.ui.progressBar.setValue(
			int(100.0*float(len(self.done))/float(len(self.targets))))

	def targetError(self, target):
		"""For a given target, set error status in details tree

		@param	self		A ThreadedExport instance
		@param	target		String containing target's address
		"""
		self.tree[target].setText(2, "Error")
		self.done.append(target)
		self.ui.progressBar.setValue(len(self.done)/len(self.targets))

	def targetRun(self, target):
		"""For a given target, set running status in details tree

		@param	self		A ThreadedExport instance
		@param	target		String containing target's address
		"""
		self.tree[target].setText(2, "Running")
		self.ui.progressLabel.setText(self.tr("Operation {0} of {1}: "+
		"Send files to {2}").format(len(self.done)+1, len(self.targets), target))

	def passwdRequest(self, target):
		"""Request a passwd from admin and set it on threads

		@param	self		A ThreadedExport instance
		@param	target		String containing target's address
		"""
		# pause threads on next item
		for i in self.threads:
			i.pause = True
		# request passwd
		p = QtGui.QInputDialog.getText(self, self.tr("Root Password"),
			self.tr("The host {0} require a password!").format(target),
			QtGui.QLineEdit.Password)[0]
		if p:
			for i in self.threads:
				i.password = p	# set passwd
				i.start()	# restart thread
		else:
			self.reject()

	def threadFinished(self):
		"""Executed when a thread is finished

		Verifies if all threads are completed, and accept dialog
		@param	self		A ThreadedExport instance
		"""
		if not any([bool(i.targets) for i in self.threads]):
			#self.accept()
			pass

	def reject(self):
		"""Reimplement QtGui.QDialog.reject method

		@param	self		A ThreadedExport instance
		"""
		print("__rejected")
		#for i in self.threads:
		#	try: i.stop()
		QtGui.QDialog.reject(self)
