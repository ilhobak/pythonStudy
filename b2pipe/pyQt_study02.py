# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyQt_study02.ui'
#
# Created: Wed Apr 15 17:25:27 2015
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(878, 844)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_projectInfo = QtGui.QHBoxLayout()
        self.horizontalLayout_projectInfo.setSpacing(20)
        self.horizontalLayout_projectInfo.setObjectName(_fromUtf8("horizontalLayout_projectInfo"))
        self.formLayout_project = QtGui.QFormLayout()
        self.formLayout_project.setHorizontalSpacing(1)
        self.formLayout_project.setObjectName(_fromUtf8("formLayout_project"))
        self.label_project = QtGui.QLabel(self.centralwidget)
        self.label_project.setObjectName(_fromUtf8("label_project"))
        self.formLayout_project.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_project)
        self.comboBox_project = QtGui.QComboBox(self.centralwidget)
        self.comboBox_project.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox_project.setObjectName(_fromUtf8("comboBox_project"))
        self.formLayout_project.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_project)
        self.horizontalLayout_projectInfo.addLayout(self.formLayout_project)
        self.formLayout_projectPath = QtGui.QFormLayout()
        self.formLayout_projectPath.setHorizontalSpacing(1)
        self.formLayout_projectPath.setObjectName(_fromUtf8("formLayout_projectPath"))
        self.label_projectPath = QtGui.QLabel(self.centralwidget)
        self.label_projectPath.setObjectName(_fromUtf8("label_projectPath"))
        self.formLayout_projectPath.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_projectPath)
        self.lineEdit_projectPath = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_projectPath.setEnabled(True)
        self.lineEdit_projectPath.setMinimumSize(QtCore.QSize(350, 0))
        self.lineEdit_projectPath.setObjectName(_fromUtf8("lineEdit_projectPath"))
        self.formLayout_projectPath.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_projectPath)
        self.horizontalLayout_projectInfo.addLayout(self.formLayout_projectPath)
        self.formLayout_user = QtGui.QFormLayout()
        self.formLayout_user.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_user.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_user.setHorizontalSpacing(1)
        self.formLayout_user.setObjectName(_fromUtf8("formLayout_user"))
        self.lineEdit_user = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_user.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_user.setObjectName(_fromUtf8("lineEdit_user"))
        self.formLayout_user.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_user)
        self.label_user = QtGui.QLabel(self.centralwidget)
        self.label_user.setObjectName(_fromUtf8("label_user"))
        self.formLayout_user.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_user)
        self.horizontalLayout_projectInfo.addLayout(self.formLayout_user)
        self.verticalLayout_2.addLayout(self.horizontalLayout_projectInfo)
        self.horizontalLayout_main = QtGui.QHBoxLayout()
        self.horizontalLayout_main.setObjectName(_fromUtf8("horizontalLayout_main"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(500, 700))
        self.tabWidget.setMaximumSize(QtCore.QSize(500, 700000))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_assetBroswer = QtGui.QWidget()
        self.tab_assetBroswer.setObjectName(_fromUtf8("tab_assetBroswer"))
        self.frame_assetDir = QtGui.QFrame(self.tab_assetBroswer)
        self.frame_assetDir.setGeometry(QtCore.QRect(10, 10, 481, 351))
        self.frame_assetDir.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_assetDir.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_assetDir.setObjectName(_fromUtf8("frame_assetDir"))
        self.label_assetType = QtGui.QLabel(self.frame_assetDir)
        self.label_assetType.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label_assetType.setObjectName(_fromUtf8("label_assetType"))
        self.pushButton_assetTypeDelete = QtGui.QPushButton(self.frame_assetDir)
        self.pushButton_assetTypeDelete.setGeometry(QtCore.QRect(70, 290, 51, 23))
        self.pushButton_assetTypeDelete.setObjectName(_fromUtf8("pushButton_assetTypeDelete"))
        self.pushButton_assetTypeNew = QtGui.QPushButton(self.frame_assetDir)
        self.pushButton_assetTypeNew.setGeometry(QtCore.QRect(10, 290, 61, 23))
        self.pushButton_assetTypeNew.setObjectName(_fromUtf8("pushButton_assetTypeNew"))
        self.listView_assetType = QtGui.QListView(self.frame_assetDir)
        self.listView_assetType.setGeometry(QtCore.QRect(10, 30, 111, 261))
        self.listView_assetType.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listView_assetType.setObjectName(_fromUtf8("listView_assetType"))
        self.pushButton_assetCompDelete = QtGui.QPushButton(self.frame_assetDir)
        self.pushButton_assetCompDelete.setGeometry(QtCore.QRect(420, 290, 51, 23))
        self.pushButton_assetCompDelete.setObjectName(_fromUtf8("pushButton_assetCompDelete"))
        self.label_assetComponent = QtGui.QLabel(self.frame_assetDir)
        self.label_assetComponent.setGeometry(QtCore.QRect(370, 10, 91, 16))
        self.label_assetComponent.setObjectName(_fromUtf8("label_assetComponent"))
        self.pushButton_assetNew = QtGui.QPushButton(self.frame_assetDir)
        self.pushButton_assetNew.setGeometry(QtCore.QRect(130, 290, 171, 23))
        self.pushButton_assetNew.setObjectName(_fromUtf8("pushButton_assetNew"))
        self.listView_assetComponent = QtGui.QListView(self.frame_assetDir)
        self.listView_assetComponent.setGeometry(QtCore.QRect(370, 30, 101, 261))
        self.listView_assetComponent.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listView_assetComponent.setObjectName(_fromUtf8("listView_assetComponent"))
        self.pushButton_assetCompNew = QtGui.QPushButton(self.frame_assetDir)
        self.pushButton_assetCompNew.setGeometry(QtCore.QRect(370, 290, 51, 23))
        self.pushButton_assetCompNew.setObjectName(_fromUtf8("pushButton_assetCompNew"))
        self.listView_asset = QtGui.QListView(self.frame_assetDir)
        self.listView_asset.setGeometry(QtCore.QRect(130, 30, 231, 261))
        self.listView_asset.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listView_asset.setObjectName(_fromUtf8("listView_asset"))
        self.label_asset = QtGui.QLabel(self.frame_assetDir)
        self.label_asset.setGeometry(QtCore.QRect(130, 10, 56, 12))
        self.label_asset.setObjectName(_fromUtf8("label_asset"))
        self.pushButton_assetDelete = QtGui.QPushButton(self.frame_assetDir)
        self.pushButton_assetDelete.setGeometry(QtCore.QRect(300, 290, 61, 23))
        self.pushButton_assetDelete.setObjectName(_fromUtf8("pushButton_assetDelete"))
        self.frame_assetPreview = QtGui.QFrame(self.tab_assetBroswer)
        self.frame_assetPreview.setGeometry(QtCore.QRect(10, 370, 481, 311))
        self.frame_assetPreview.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_assetPreview.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_assetPreview.setObjectName(_fromUtf8("frame_assetPreview"))
        self.label_assetPreviewImage = QtGui.QLabel(self.frame_assetPreview)
        self.label_assetPreviewImage.setGeometry(QtCore.QRect(10, 10, 320, 240))
        self.label_assetPreviewImage.setText(_fromUtf8(""))
        self.label_assetPreviewImage.setPixmap(QtGui.QPixmap(_fromUtf8("N:/b1Env/maya/2014/icons/noPreview.png")))
        self.label_assetPreviewImage.setObjectName(_fromUtf8("label_assetPreviewImage"))
        self.tabWidget.addTab(self.tab_assetBroswer, _fromUtf8(""))
        self.tab_shotBrowser = QtGui.QWidget()
        self.tab_shotBrowser.setObjectName(_fromUtf8("tab_shotBrowser"))
        self.frame_3 = QtGui.QFrame(self.tab_shotBrowser)
        self.frame_3.setGeometry(QtCore.QRect(10, 370, 481, 311))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.label_shotPreviewImage = QtGui.QLabel(self.frame_3)
        self.label_shotPreviewImage.setGeometry(QtCore.QRect(10, 10, 320, 240))
        self.label_shotPreviewImage.setText(_fromUtf8(""))
        self.label_shotPreviewImage.setPixmap(QtGui.QPixmap(_fromUtf8("N:/b1Env/maya/2014/icons/noPreview.png")))
        self.label_shotPreviewImage.setObjectName(_fromUtf8("label_shotPreviewImage"))
        self.frame_4 = QtGui.QFrame(self.tab_shotBrowser)
        self.frame_4.setGeometry(QtCore.QRect(10, 10, 481, 351))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.label_14 = QtGui.QLabel(self.frame_4)
        self.label_14.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.pushButton_14 = QtGui.QPushButton(self.frame_4)
        self.pushButton_14.setGeometry(QtCore.QRect(60, 290, 51, 23))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.pushButton_15 = QtGui.QPushButton(self.frame_4)
        self.pushButton_15.setGeometry(QtCore.QRect(10, 290, 51, 23))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.listView_7 = QtGui.QListView(self.frame_4)
        self.listView_7.setGeometry(QtCore.QRect(10, 30, 101, 261))
        self.listView_7.setObjectName(_fromUtf8("listView_7"))
        self.pushButton_16 = QtGui.QPushButton(self.frame_4)
        self.pushButton_16.setGeometry(QtCore.QRect(310, 290, 51, 23))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.label_15 = QtGui.QLabel(self.frame_4)
        self.label_15.setGeometry(QtCore.QRect(260, 10, 91, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.pushButton_17 = QtGui.QPushButton(self.frame_4)
        self.pushButton_17.setGeometry(QtCore.QRect(120, 290, 81, 23))
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.listView_8 = QtGui.QListView(self.frame_4)
        self.listView_8.setGeometry(QtCore.QRect(260, 30, 101, 261))
        self.listView_8.setObjectName(_fromUtf8("listView_8"))
        self.pushButton_18 = QtGui.QPushButton(self.frame_4)
        self.pushButton_18.setGeometry(QtCore.QRect(260, 290, 51, 23))
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.listView_9 = QtGui.QListView(self.frame_4)
        self.listView_9.setGeometry(QtCore.QRect(120, 30, 131, 261))
        self.listView_9.setObjectName(_fromUtf8("listView_9"))
        self.label_16 = QtGui.QLabel(self.frame_4)
        self.label_16.setGeometry(QtCore.QRect(120, 10, 56, 12))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.pushButton_19 = QtGui.QPushButton(self.frame_4)
        self.pushButton_19.setGeometry(QtCore.QRect(200, 290, 51, 23))
        self.pushButton_19.setObjectName(_fromUtf8("pushButton_19"))
        self.pushButton_20 = QtGui.QPushButton(self.frame_4)
        self.pushButton_20.setGeometry(QtCore.QRect(420, 290, 51, 23))
        self.pushButton_20.setObjectName(_fromUtf8("pushButton_20"))
        self.listView_10 = QtGui.QListView(self.frame_4)
        self.listView_10.setGeometry(QtCore.QRect(370, 30, 101, 261))
        self.listView_10.setObjectName(_fromUtf8("listView_10"))
        self.pushButton_21 = QtGui.QPushButton(self.frame_4)
        self.pushButton_21.setGeometry(QtCore.QRect(370, 290, 51, 23))
        self.pushButton_21.setObjectName(_fromUtf8("pushButton_21"))
        self.label_17 = QtGui.QLabel(self.frame_4)
        self.label_17.setGeometry(QtCore.QRect(370, 10, 91, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.tabWidget.addTab(self.tab_shotBrowser, _fromUtf8(""))
        self.horizontalLayout_main.addWidget(self.tabWidget)
        self.verticalLayout_history = QtGui.QVBoxLayout()
        self.verticalLayout_history.setObjectName(_fromUtf8("verticalLayout_history"))
        self.label_history = QtGui.QLabel(self.centralwidget)
        self.label_history.setObjectName(_fromUtf8("label_history"))
        self.verticalLayout_history.addWidget(self.label_history)
        self.scrollArea_AssetHistoty = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea_AssetHistoty.setMinimumSize(QtCore.QSize(350, 690))
        self.scrollArea_AssetHistoty.setWidgetResizable(True)
        self.scrollArea_AssetHistoty.setObjectName(_fromUtf8("scrollArea_AssetHistoty"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 331, 1110))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textEdit = QtGui.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 150))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 150))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.textEdit_2 = QtGui.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_2.setMinimumSize(QtCore.QSize(0, 150))
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 150))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.verticalLayout.addWidget(self.textEdit_2)
        self.textEdit_3 = QtGui.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_3.setMinimumSize(QtCore.QSize(0, 150))
        self.textEdit_3.setMaximumSize(QtCore.QSize(16777215, 150))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.verticalLayout.addWidget(self.textEdit_3)
        self.textEdit_4 = QtGui.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_4.setMinimumSize(QtCore.QSize(0, 150))
        self.textEdit_4.setMaximumSize(QtCore.QSize(16777215, 150))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.verticalLayout.addWidget(self.textEdit_4)
        self.textEdit_6 = QtGui.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_6.setMinimumSize(QtCore.QSize(0, 150))
        self.textEdit_6.setMaximumSize(QtCore.QSize(16777215, 150))
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.verticalLayout.addWidget(self.textEdit_6)
        self.textEdit_7 = QtGui.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_7.setMinimumSize(QtCore.QSize(0, 150))
        self.textEdit_7.setMaximumSize(QtCore.QSize(16777215, 150))
        self.textEdit_7.setObjectName(_fromUtf8("textEdit_7"))
        self.verticalLayout.addWidget(self.textEdit_7)
        self.textEdit_5 = QtGui.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_5.setMinimumSize(QtCore.QSize(0, 150))
        self.textEdit_5.setMaximumSize(QtCore.QSize(16777215, 150))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.verticalLayout.addWidget(self.textEdit_5)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea_AssetHistoty.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_history.addWidget(self.scrollArea_AssetHistoty)
        self.horizontalLayout_main.addLayout(self.verticalLayout_history)
        self.verticalLayout_2.addLayout(self.horizontalLayout_main)
        self.horizontalLayout_fileLocation = QtGui.QHBoxLayout()
        self.horizontalLayout_fileLocation.setObjectName(_fromUtf8("horizontalLayout_fileLocation"))
        self.label_fileLocation = QtGui.QLabel(self.centralwidget)
        self.label_fileLocation.setObjectName(_fromUtf8("label_fileLocation"))
        self.horizontalLayout_fileLocation.addWidget(self.label_fileLocation)
        self.lineEdit_fileLocation = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_fileLocation.setObjectName(_fromUtf8("lineEdit_fileLocation"))
        self.horizontalLayout_fileLocation.addWidget(self.lineEdit_fileLocation)
        self.pushButton_fileLocation = QtGui.QPushButton(self.centralwidget)
        self.pushButton_fileLocation.setObjectName(_fromUtf8("pushButton_fileLocation"))
        self.horizontalLayout_fileLocation.addWidget(self.pushButton_fileLocation)
        self.verticalLayout_2.addLayout(self.horizontalLayout_fileLocation)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 878, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSetup = QtGui.QMenu(self.menubar)
        self.menuSetup.setObjectName(_fromUtf8("menuSetup"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuSetup.addAction(self.actionExit)
        self.menubar.addAction(self.menuSetup.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "b2 PipeLine", None))
        self.label_project.setText(_translate("MainWindow", "Project:", None))
        self.label_projectPath.setText(_translate("MainWindow", "Project Path:", None))
        self.label_user.setText(_translate("MainWindow", "User:", None))
        self.label_assetType.setText(_translate("MainWindow", "Asset Type", None))
        self.pushButton_assetTypeDelete.setText(_translate("MainWindow", "Delete", None))
        self.pushButton_assetTypeNew.setText(_translate("MainWindow", "New..", None))
        self.pushButton_assetCompDelete.setText(_translate("MainWindow", "Delete", None))
        self.label_assetComponent.setText(_translate("MainWindow", "Component", None))
        self.pushButton_assetNew.setText(_translate("MainWindow", "New..", None))
        self.pushButton_assetCompNew.setText(_translate("MainWindow", "New..", None))
        self.label_asset.setText(_translate("MainWindow", "Asset", None))
        self.pushButton_assetDelete.setText(_translate("MainWindow", "Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_assetBroswer), _translate("MainWindow", "Asset Browser", None))
        self.label_14.setText(_translate("MainWindow", "Sequence", None))
        self.pushButton_14.setText(_translate("MainWindow", "Delete", None))
        self.pushButton_15.setText(_translate("MainWindow", "New..", None))
        self.pushButton_16.setText(_translate("MainWindow", "Delete", None))
        self.label_15.setText(_translate("MainWindow", "Component", None))
        self.pushButton_17.setText(_translate("MainWindow", "New..", None))
        self.pushButton_18.setText(_translate("MainWindow", "New..", None))
        self.label_16.setText(_translate("MainWindow", "Shot", None))
        self.pushButton_19.setText(_translate("MainWindow", "Delete", None))
        self.pushButton_20.setText(_translate("MainWindow", "Delete", None))
        self.pushButton_21.setText(_translate("MainWindow", "New..", None))
        self.label_17.setText(_translate("MainWindow", "Layer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_shotBrowser), _translate("MainWindow", "Shot Browser", None))
        self.label_history.setText(_translate("MainWindow", "History", None))
        self.label_fileLocation.setText(_translate("MainWindow", "File Location", None))
        self.pushButton_fileLocation.setText(_translate("MainWindow", "PushButton", None))
        self.menuSetup.setTitle(_translate("MainWindow", "&Setup", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionExit.setText(_translate("MainWindow", "&Exit", None))

