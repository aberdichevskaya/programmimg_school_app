# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sending_task.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(443, 388)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.compilators = QtWidgets.QComboBox(self.centralwidget)
        self.compilators.setMinimumSize(QtCore.QSize(0, 40))
        self.compilators.setObjectName("compilators")
        self.verticalLayout.addWidget(self.compilators)
        self.sourse_code = QtWidgets.QTextEdit(self.centralwidget)
        self.sourse_code.setObjectName("sourse_code")
        self.verticalLayout.addWidget(self.sourse_code)
        self.send_task = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.send_task.setFont(font)
        self.send_task.setObjectName("send_task")
        self.verticalLayout.addWidget(self.send_task)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 443, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.send_task.setText(_translate("MainWindow", "ОТПРАВИТЬ"))

