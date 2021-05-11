# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacher_menu.ui'
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.see_group_requests = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.see_group_requests.setFont(font)
        self.see_group_requests.setObjectName("see_group_requests")
        self.verticalLayout.addWidget(self.see_group_requests)
        self.add_group = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.add_group.setFont(font)
        self.add_group.setObjectName("add_group")
        self.verticalLayout.addWidget(self.add_group)
        self.add_topic = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.add_topic.setFont(font)
        self.add_topic.setObjectName("add_topic")
        self.verticalLayout.addWidget(self.add_topic)
        self.add_task = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.add_task.setFont(font)
        self.add_task.setObjectName("add_task")
        self.verticalLayout.addWidget(self.add_task)
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
        self.label.setText(_translate("MainWindow", "МЕНЮ"))
        self.see_group_requests.setText(_translate("MainWindow", "ЗАПРОСЫ НА ДОБАВЛЕНИЕ В ГРУППУ"))
        self.add_group.setText(_translate("MainWindow", "ДОБАВИТЬ ГРУППУ"))
        self.add_topic.setText(_translate("MainWindow", "ОТКРЫТЬ ТЕМУ ДЛЯ ГРУППЫ"))
        self.add_task.setText(_translate("MainWindow", "ДОБАВИТЬ ЗАДАЧУ"))

