# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 801, 51))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.toolButton = QtWidgets.QToolButton(self.groupBox)
        self.toolButton.setGeometry(QtCore.QRect(0, 10, 71, 41))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_2.setGeometry(QtCore.QRect(70, 10, 71, 41))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_3.setGeometry(QtCore.QRect(140, 10, 71, 41))
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_4.setGeometry(QtCore.QRect(210, 10, 71, 41))
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_5 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_5.setGeometry(QtCore.QRect(280, 10, 71, 41))
        self.toolButton_5.setObjectName("toolButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menu_3)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        self.menu_6 = QtWidgets.QMenu(self.menubar)
        self.menu_6.setObjectName("menu_6")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtWidgets.QAction(MainWindow)
        self.action_9.setObjectName("action_9")
        self.action_10 = QtWidgets.QAction(MainWindow)
        self.action_10.setObjectName("action_10")
        self.action_11 = QtWidgets.QAction(MainWindow)
        self.action_11.setObjectName("action_11")
        self.action_12 = QtWidgets.QAction(MainWindow)
        self.action_12.setObjectName("action_12")
        self.action_13 = QtWidgets.QAction(MainWindow)
        self.action_13.setObjectName("action_13")
        self.action_15 = QtWidgets.QAction(MainWindow)
        self.action_15.setObjectName("action_15")
        self.action_16 = QtWidgets.QAction(MainWindow)
        self.action_16.setObjectName("action_16")
        self.action_17 = QtWidgets.QAction(MainWindow)
        self.action_17.setObjectName("action_17")
        self.action_18 = QtWidgets.QAction(MainWindow)
        self.action_18.setObjectName("action_18")
        self.action_19 = QtWidgets.QAction(MainWindow)
        self.action_19.setObjectName("action_19")
        self.action_20 = QtWidgets.QAction(MainWindow)
        self.action_20.setObjectName("action_20")
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action_5)
        self.menu.addAction(self.action_6)
        self.menu.addAction(self.action_7)
        self.menu.addAction(self.action_8)
        self.menu.addAction(self.action_9)
        self.menu.addAction(self.action_10)
        self.menu_2.addAction(self.action_11)
        self.menu_2.addAction(self.action_12)
        self.menu_2.addAction(self.action_13)
        self.menu_4.addAction(self.action_15)
        self.menu_4.addAction(self.action_16)
        self.menu_4.addAction(self.action_17)
        self.menu_4.addAction(self.action_18)
        self.menu_3.addAction(self.menu_4.menuAction())
        self.menu_5.addAction(self.action_20)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.toolButton.clicked.connect(self.sign_or_encode)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton.setText(_translate("MainWindow", "签名/加密"))
        self.toolButton_2.setText(_translate("MainWindow", "解密/校验"))
        self.toolButton_3.setText(_translate("MainWindow", "导入"))
        self.toolButton_4.setText(_translate("MainWindow", "导出"))
        self.toolButton_5.setText(_translate("MainWindow", "记事本"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "查看"))
        self.menu_3.setTitle(_translate("MainWindow", "工具"))
        self.menu_4.setTitle(_translate("MainWindow", "剪切板"))
        self.menu_5.setTitle(_translate("MainWindow", "设置"))
        self.menu_6.setTitle(_translate("MainWindow", "帮助"))
        self.action_2.setText(_translate("MainWindow", "新建密钥对"))
        self.action.setText(_translate("MainWindow", "导入"))
        self.action_3.setText(_translate("MainWindow", "导出"))
        self.action_4.setText(_translate("MainWindow", "解密/校验"))
        self.action_5.setText(_translate("MainWindow", "签名/加密"))
        self.action_6.setText(_translate("MainWindow", "签名/加密文件夹"))
        self.action_7.setText(_translate("MainWindow", "创建校验和文件"))
        self.action_8.setText(_translate("MainWindow", "验证校验和文件"))
        self.action_9.setText(_translate("MainWindow", "关闭"))
        self.action_10.setText(_translate("MainWindow", "退出"))
        self.action_11.setText(_translate("MainWindow", "重新显示"))
        self.action_12.setText(_translate("MainWindow", "停止操作"))
        self.action_13.setText(_translate("MainWindow", "记事本"))
        self.action_15.setText(_translate("MainWindow", "证书导入"))
        self.action_16.setText(_translate("MainWindow", "加密"))
        self.action_17.setText(_translate("MainWindow", "签名"))
        self.action_18.setText(_translate("MainWindow", "解密/校验"))
        self.action_19.setText(_translate("MainWindow", "执行自检"))
        self.action_20.setText(_translate("MainWindow", "显示工具栏"))

    def sign_or_encode(self):
        self.statusbar.showMessage("sign_or_encode was pressed")
