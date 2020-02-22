# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add-client.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(724, 726)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("2.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 7, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 3, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(171, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 6, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 2, 1, 2, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 3, 4, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 2, 1, 2, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 4, 4, 1, 2, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 2, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 5, 1, 2, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout.addWidget(self.calendarWidget, 6, 1, 1, 2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.gridLayout.addWidget(self.calendarWidget_2, 6, 4, 1, 3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 7, 1, 1, 2, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 7, 6, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 6, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">NAME</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">CONTACT NUMBER</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">CHOOSE PLAN</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">AMOUNT PAID</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">VALID FROM</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">VALID TO</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "BACK TO PREVIOUS MENU"))
        self.pushButton.setText(_translate("MainWindow", "ADD CLIENT"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">ADD CLIENT</span></p><p align=\"center\"><br/></p></body></html>"))
