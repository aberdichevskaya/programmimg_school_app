# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task.ui'
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
        self.task_name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.task_name.setFont(font)
        self.task_name.setAlignment(QtCore.Qt.AlignCenter)
        self.task_name.setObjectName("task_name")
        self.verticalLayout.addWidget(self.task_name)
        self.ml = QtWidgets.QLabel(self.centralwidget)
        self.ml.setAlignment(QtCore.Qt.AlignCenter)
        self.ml.setObjectName("ml")
        self.verticalLayout.addWidget(self.ml)
        self.tl = QtWidgets.QLabel(self.centralwidget)
        self.tl.setAlignment(QtCore.Qt.AlignCenter)
        self.tl.setObjectName("tl")
        self.verticalLayout.addWidget(self.tl)
        self.task_text = QtWidgets.QTextEdit(self.centralwidget)
        self.task_text.setObjectName("task_text")
        self.verticalLayout.addWidget(self.task_text)
        self.send_task = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.send_task.setFont(font)
        self.send_task.setObjectName("send_task")
        self.verticalLayout.addWidget(self.send_task)
        self.see_packages = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.see_packages.setFont(font)
        self.see_packages.setObjectName("see_packages")
        self.verticalLayout.addWidget(self.see_packages)
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
        self.task_name.setText(_translate("MainWindow", "TextLabel"))
        self.ml.setText(_translate("MainWindow", "TextLabel"))
        self.tl.setText(_translate("MainWindow", "TextLabel"))
        self.send_task.setText(_translate("MainWindow", "ОТОСЛАТЬ ЗАДАЧУ"))
        self.see_packages.setText(_translate("MainWindow", "ПОСМОТРЕТЬ СВОИ ПОСЫЛКИ"))

