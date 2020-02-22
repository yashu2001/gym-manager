# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginpage.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(466, 394)
        MainWindow.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color: rgb(0,0,0);\n"
"")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("color: rgb(0,0,0);\n"
"")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: 18pt \"MS UI Gothic\";")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("2.jpg"))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(194, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(240, 240, 240);")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.pushButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "USERNAME"))
        self.label_2.setText(_translate("MainWindow", "PASSWORD"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))
