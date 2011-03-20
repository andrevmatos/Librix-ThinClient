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

import os
from PyQt4 import QtGui

import subprocess

from ltmt.ui.keygen.Ui_keyGen import Ui_KeyGen
from ltmt.ui.keygen.OpenKey import OpenKey
from ltmt.lib.utils import passwdGen

class KeyGen(QtGui.QDialog):
	"""Show a SSH key generation dialog"""
	def __init__(self, parent=None):
		"""Init method
		
		@param	self			A KeyGen instance
		"""
		self.parent = parent
		
		QtGui.QDialog.__init__(self)
		self.ui = Ui_KeyGen()
		self.ui.setupUi(self)
		self.ui.logText.setFontFamily('monospace')
		
		self.privkeyfile, self.pubkeyfile, output = self.keygen()
		
		self.ui.logText.setPlainText(output)
		
	def keygen(self, tmpdir=os.path.expanduser('~/.ssh')):
		"""Generates SSH key pair on tmpdir
		
		Returns a tuple containint public and private keys paths 
		and output of keygen command
		@param	self			A KeyGen instance
		@param	tmpdir		A dirpath string
		@return				(privkeypath, pubkeypath, output)
		"""
		privkeyfile = os.path.join(tmpdir, '~id_rsa_'+passwdGen(4))
		pubkeyfile = privkeyfile+'.pub'
		
		if os.path.isfile(privkeyfile): os.remove(privkeyfile)
		if os.path.isfile(pubkeyfile): os.remove(pubkeyfile)
			
		p = subprocess.Popen("ssh-keygen -t rsa -N '' -f '{0}'".format(
			privkeyfile), shell=True, stdin=subprocess.PIPE, 
			stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		
		r = p.wait()
		if r:
			raise(Exception, "An error ocurred on ssh-keygen")
		
		return(privkeyfile, pubkeyfile, p.stdout.read().decode().strip())
	
	def reject(self):
		"""Reimplement QtGui.QDialog.reject method
		
		Clear temporary files before return
		"""
		if os.path.isfile(self.privkeyfile): os.remove(self.privkeyfile)
		if os.path.isfile(self.pubkeyfile): os.remove(self.pubkeyfile)
		
		QtGui.QDialog.reject(self)

	def savePrivKey(self):
		"""Ask for a place to save private key file
		
		@param	self			A KeyGen instance
		"""
		file = QtGui.QFileDialog.getSaveFileName(self, self.tr("Save SSH "+
			"Private Key"), os.path.expanduser("~/.ssh/id_rsa"))
		if file:
			with open(file, 'w') as NEW, open(self.privkeyfile, 'r') as PKF:
				NEW.write(PKF.read())
	
	def savePubKey(self):
		"""Ask for a place to save public key file
		
		@param	self			A KeyGen instance
		"""
		file = QtGui.QFileDialog.getSaveFileName(self, self.tr("Save SSH "+
			"Public Key"), os.path.expanduser("~/.ssh/id_rsa.pub"))
		if file:
			with open(file, 'w') as NEW, open(self.pubkeyfile, 'r') as PKF:
				NEW.write(PKF.read())
	
	def openPrivKey(self):
		"""Show private key to user"""
		with open(self.privkeyfile, 'r') as PKF:
			OpenKey(PKF.read(), self.tr("SSH Private Key"), self).exec_()
	
	def openPubKey(self):
		"""Show private key to user"""
		with open(self.pubkeyfile, 'r') as PKF:
			OpenKey(PKF.read(), self.tr("SSH Public Key"), self).exec_()
