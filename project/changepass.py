# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changepass.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(362, 355)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: 18pt \"MS UI Gothic\";")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("2.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("font: 18pt \"MS UI Gothic\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 2, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 2, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 4, 1, 1, 2, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 5, 0, 1, 2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 2, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">CHANGE PASSWORD</p><p align=\"center\"><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "OLD PASSWORD"))
        self.label.setText(_translate("MainWindow", "NEW PASSWORD"))
        self.pushButton_2.setText(_translate("MainWindow", "BACK TO PREVIOUS MENU"))
        self.pushButton.setText(_translate("MainWindow", "CHANGE PASSWORD"))
