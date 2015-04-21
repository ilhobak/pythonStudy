# -*- coding: utf-8 -*-

from PyQt4 import QtGui, uic

uicFile = file('pyQt_study03.ui')
pyFile = file('pyQt_study03.py', 'w')

uic.compileUi(uicFile, pyFile)

uicFile.close()
pyFile.close()