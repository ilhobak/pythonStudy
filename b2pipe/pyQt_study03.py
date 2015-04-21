# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyQt_study03.ui'
#
# Created: Thu Apr 16 20:24:52 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(823, 762)
        # scrollArea
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 320, 691))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 318, 689))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))


        # verticalLayout
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        # buttonA
        self.pushButton_A = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_A.setObjectName(_fromUtf8("pushButton_A"))
        self.verticalLayout.addWidget(self.pushButton_A)
        #formLayout
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        # buttonB
        self.pushButton_B = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_B.setEnabled(True)
        self.pushButton_B.setMinimumSize(QtCore.QSize(40, 150))
        self.pushButton_B.setMaximumSize(QtCore.QSize(40, 100000))
        self.pushButton_B.setBaseSize(QtCore.QSize(25, 100))
        self.pushButton_B.setObjectName(_fromUtf8("pushButton_B"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.pushButton_B)
        # textEdit
        self.textEdit = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setEnabled(True)
        self.textEdit.setMinimumSize(QtCore.QSize(200, 150))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        #add layout
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.textEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 500, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_A.setText(_translate("Form", "▼r001", None))
        self.pushButton_B.setText(_translate("Form", "r001", None))

