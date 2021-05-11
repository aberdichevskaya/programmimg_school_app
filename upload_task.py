# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'upload_task.ui'
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
        self.choose_topic = QtWidgets.QComboBox(self.centralwidget)
        self.choose_topic.setMinimumSize(QtCore.QSize(0, 40))
        self.choose_topic.setObjectName("choose_topic")
        self.verticalLayout.addWidget(self.choose_topic)
        self.upload_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.upload_button.setFont(font)
        self.upload_button.setObjectName("upload_button")
        self.verticalLayout.addWidget(self.upload_button)
        self.task_name = QtWidgets.QLineEdit(self.centralwidget)
        self.task_name.setCursorPosition(0)
        self.task_name.setAlignment(QtCore.Qt.AlignCenter)
        self.task_name.setObjectName("task_name")
        self.verticalLayout.addWidget(self.task_name)
        self.add_task = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.add_task.setFont(font)
        self.add_task.setObjectName("add_task")
        self.verticalLayout.addWidget(self.add_task)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
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
        self.upload_button.setText(_translate("MainWindow", "ЗАГРУЗИТЬ ЗАДАЧУ"))
        self.task_name.setPlaceholderText(_translate("MainWindow", "НАЗВАНИЕ ЗАДАЧИ"))
        self.add_task.setText(_translate("MainWindow", "ДОБАВИТЬ ЗАДАЧУ В ТЕМУ"))

