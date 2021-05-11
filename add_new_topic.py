# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_new_topic.ui'
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
        self.choose_group = QtWidgets.QComboBox(self.centralwidget)
        self.choose_group.setMinimumSize(QtCore.QSize(0, 40))
        self.choose_group.setObjectName("choose_group")
        self.verticalLayout.addWidget(self.choose_group)
        self.topic_name = QtWidgets.QLineEdit(self.centralwidget)
        self.topic_name.setAlignment(QtCore.Qt.AlignCenter)
        self.topic_name.setObjectName("topic_name")
        self.verticalLayout.addWidget(self.topic_name)
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
        self.topic_name.setPlaceholderText(_translate("MainWindow", "НАЗВАНИЕ НОВОЙ ТЕМЫ"))

