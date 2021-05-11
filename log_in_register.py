# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log_in_register.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(443, 191)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.log_in = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.log_in.setFont(font)
        self.log_in.setObjectName("log_in")
        self.horizontalLayout_2.addWidget(self.log_in)
        self.registrate = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.registrate.setFont(font)
        self.registrate.setObjectName("registrate")
        self.horizontalLayout_2.addWidget(self.registrate)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setText("")
        self.login.setCursorPosition(0)
        self.login.setAlignment(QtCore.Qt.AlignCenter)
        self.login.setObjectName("login")
        self.verticalLayout_4.addWidget(self.login)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setText("")
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.verticalLayout_4.addWidget(self.password)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
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
        self.log_in.setText(_translate("MainWindow", "ВОЙТИ"))
        self.registrate.setText(_translate("MainWindow", "ЗАРЕГИСТРИРОВАТЬСЯ"))
        self.login.setPlaceholderText(_translate("MainWindow", "ЛОГИН"))
        self.password.setPlaceholderText(_translate("MainWindow", "ПАРОЛЬ"))

