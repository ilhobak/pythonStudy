# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore, uic
import util
import os.path

class mainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(mainWindow, self).__init__()
        # get UI
        self.ui = uic.loadUi('pyQt_study02.ui', self)

        # user name
        user = util.get_user_name()
        self.ui.lineEdit_user.setText(user)

        # project List
        projectList = util.get_folder_list("P:/")
        # print projectList
        self.ui.comboBox_project.addItems(projectList)

        # signals
        self.ui.comboBox_project.activated[str].connect(self.changeProject)
        self.ui.listView_assetType.clicked.connect(self.addAssetList)
        self.ui.listView_asset.clicked.connect(self.addAssetComponent)
        self.ui.listView_assetComponent.clicked.connect(self.showAssetHistory)

        # add default preview image.
        # 'N:/b1Env/maya/2014/icons/noPreview.jpg'
        dataEmpty = QtCore.QStringList()
        self.modelEmpty = QtGui.QStringListModel(dataEmpty)

    def changeProject(self, curProject):

        self.resetUI(0)

        # setProjectPath
        projectRoot = "P:/"
        self.lineEdit_projectPath.setText(projectRoot + curProject)

        # load asset Types
        assetDir = (projectRoot + curProject + '/4.Asset/')
        if os.path.isdir(assetDir):
            assetTypeList = util.get_folder_list(str(assetDir))
            # print assetTypeList
            model = QtGui.QStringListModel()
            model.setStringList(assetTypeList)
            self.ui.listView_assetType.setModel(model)
        else:
            self.ui.statusBar().showMessage('Warning:' + curProject + 'has no 4.Asset folder.')

    def addAssetList(self, index):

        self.resetUI(1)

        # print index
        # sender = self.sender()
        projectPath = self.lineEdit_projectPath.text()
        # print projectPath
        curAssetType = index.data().toString()
        # print curAssetType
        assetTypeDir = (projectPath + '/4.Asset/' + curAssetType + '/' )
        # print assetTypeDir

        if os.path.isdir(assetTypeDir):
            assetList = util.get_folder_list(str(assetTypeDir))
            # print assetList
            model = QtGui.QStringListModel()
            model.setStringList(assetList)
            self.ui.listView_asset.setModel(model)
        else:
            self.ui.statusBar().showMessage('Warning:' + assetTypeDir + 'is not exist.')

    def addAssetComponent(self, index):

        self.resetUI(2)

        projectPath = self.lineEdit_projectPath.text()
        assetIndex = self.ui.listView_assetType.selectedIndexes()
        # print assetIndex[0]
        curAssetType = assetIndex[0].data().toString()
        # print curAssetType
        curAsset = index.data().toString()
        assetDir = (projectPath + '/4.Asset/' + curAssetType + '/' + curAsset + '/')
        # print assetDir

        if os.path.isdir(assetDir):
            assetCompoList = util.get_folder_list(str(assetDir))
            # print assetCompoList
            model = QtGui.QStringListModel()
            model.setStringList(assetCompoList)
            self.ui.listView_assetComponent.setModel(model)
        else:
            self.ui.statusBar().showMessage('Warning:' + assetDir + 'is not exist.')

    def showAssetHistory(self, index):

        self.resetUI(3)

        projectPath = self.lineEdit_projectPath.text()
        assetTypeIndex = self.ui.listView_assetType.selectedIndexes()
        curAssetType = assetTypeIndex[0].data().toString()
        # print curAssetType
        assetIndex = self.ui.listView_asset.selectedIndexes()
        curAsset = assetIndex[0].data().toString()
        curComp = index.data().toString()
        compDir = (projectPath + '/4.Asset/' + curAssetType + '/' + curAsset + '/' + curComp + '/_info/')
        infoFileName = (curAssetType + '_' + curAsset + '_' + curComp + '_History.xml')
        # print (compDir + infoFileName)

        if os.path.isfile((compDir + infoFileName)):
            # get history info.
            history = util.b2HistoryParsing((compDir + infoFileName), 'all')



            # develop color palette set
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)

            # make history TextEdits
            for i in range(len(history)):
                # verticalLayout
                self.verticalLayout = QtGui.QVBoxLayout()
                self.verticalLayout.setSpacing(0)
                self.verticalLayout.setObjectName("verticalLayout_history_00" + str(i))
                self.verticalLayout_historySub.addLayout(self.verticalLayout)

                # buttonA
                self.pushButton_A = QtGui.QPushButton(self.verticalLayout_historyAdd)
                self.pushButton_A.setObjectName("pushButton_A" + str(i))
                self.verticalLayout.addWidget(self.pushButton_A)

                #formLayout
                self.formLayout = QtGui.QFormLayout()
                self.formLayout.setHorizontalSpacing(0)
                self.formLayout.setObjectName("formLayout" + str(i))
                self.verticalLayout.addLayout(self.formLayout)

                # buttonB
                self.pushButton_B = QtGui.QPushButton(self.verticalLayout_historyAdd)
                self.pushButton_B.setEnabled(True)
                self.pushButton_B.setMinimumSize(QtCore.QSize(40, 150))
                self.pushButton_B.setMaximumSize(QtCore.QSize(40, 100000))
                self.pushButton_B.setBaseSize(QtCore.QSize(25, 100))
                self.pushButton_B.setObjectName("pushButton_B" + str(i))
                self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.pushButton_B)

                # make history TextEdits
                self.textEdit = QtGui.QTextEdit(self.verticalLayout_historyAdd)
                self.textEdit.setMinimumSize(QtCore.QSize(0, 150))
                self.textEdit.setMaximumSize(QtCore.QSize(16777215, 150))
                self.textEdit.setObjectName("history" + str(i))
                self.textEdit.setReadOnly(True)
                self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.textEdit)

                # add button label
                self.pushButton_A.setText(u"▼" + history[i][3][0] + history[i][4])
                self.pushButton_B.setText(history[i][3][0] + history[i][4])

                # add text
                text = util.b2HistoryAdd(history[i])
                self.textEdit.append(unicode(text))

                # develop condition
                if history[i][3] == 'develop':
                    self.textEdit.setPalette(palette)

            spacerItem = QtGui.QSpacerItem(20, 400, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
            self.verticalLayout_historySub.addItem(spacerItem)

            # print self.verticalLayout_historySub.count()

    def resetUI(self, num):

        if num > 2 :
            print 3
            # delete exist histories
            for cnt in reversed(range(self.verticalLayout_historySub.count())):
                print cnt
                widget = self.verticalLayout_historySub.takeAt(cnt).widget()
                if widget is not None:
                    print ('delete ' + widget)
                    widget.deleteLater()

        elif num > 1:
            print 2
            model = QtGui.QStringListModel()
            self.ui.listView_assetComponent.setModel(self.modelEmpty)
        elif num > 0:
            print 1
            model = QtGui.QStringListModel()
            self.ui.listView_asset.setModel(self.modelEmpty)
        else:
            print 0
            model = QtGui.QStringListModel()
            self.ui.listView_assetType.setModel(self.modelEmpty)



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())




