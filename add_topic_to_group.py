# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_topic_to_group.ui'
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
        self.choose_topic = QtWidgets.QComboBox(self.centralwidget)
        self.choose_topic.setMinimumSize(QtCore.QSize(0, 40))
        self.choose_topic.setBaseSize(QtCore.QSize(0, 40))
        self.choose_topic.setObjectName("choose_topic")
        self.verticalLayout.addWidget(self.choose_topic)
        self.topic_to_group = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.topic_to_group.setFont(font)
        self.topic_to_group.setObjectName("topic_to_group")
        self.verticalLayout.addWidget(self.topic_to_group)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
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
        self.topic_to_group.setText(_translate("MainWindow", "ДОБАВИТЬ ТЕМУ В ГРУППУ"))

