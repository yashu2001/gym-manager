'''
developed by yash narang
gym management system 
'''
'''importing code for ui files'''
from project.admin import Ui_MainWindow as admin
from project.adattd import Ui_MainWindow as adattd_ui
from project.add_client import Ui_MainWindow as add_client
from project.add_plan import Ui_MainWindow as add_plan
from project.changepass import Ui_MainWindow as changepass_ui
from project.client_settings import Ui_MainWindow as client_settings
from project.delete_client import Ui_MainWindow as delete_client
from project.delete_plan import Ui_MainWindow as delete_plan
from project.general_settings import Ui_MainWindow as general_settings
from project.loginfailed import Ui_MainWindow as loginfailed
from project.loginpage import Ui_MainWindow as loginpage
from project.modify_client import Ui_MainWindow as modify_client
from project.modify_client1 import Ui_MainWindow as modify_client1
from project.modify_plan import Ui_MainWindow as modify_plan
from project.plan_settings import Ui_MainWindow as plan_settings
from project.user import Ui_MainWindow as user
from project.payentry import Ui_MainWindow as payentry_ui
from project.testday import Ui_MainWindow as testday_ui
'''import other libs'''
import xlsxwriter#for writing excel files
import time#time
import datetime#datetime
import os#for operating system functions
import sqlite3#for db integration
import re#for regular expressions used in search
from project.pack import bargraph#myown library for bargraph of report
'''trying to connect to db'''
try:
    conn = sqlite3.connect('maindb.sqlite')
    cur = conn.cursor()
#excepting failure   
except:
    print('CONNECTION ERROR')
    time.sleep(5)
import sys#importing system function
'''importing pyqt5 functions'''
from PyQt5 import QtGui,QtWidgets,QtCore
from PyQt5.QtCore import pyqtSlot,QDateTime,Qt
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow,QTableWidget,QTableWidgetItem,QHeaderView
from PyQt5.uic import loadUi
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons
name=0#global var used in forwarding data from one ui to another
class testday(QMainWindow):
    def __init__(self):
        super(testday,self).__init__()
        self.ui=testday_ui()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("GYM MANAGEMENT SYSTEM")
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        cur.execute('''
                    SELECT c_id,name from Client_data
                    ''')
        rows=cur.fetchall()
        lasttime=[]
        lastdate=[]
        for x in range(len(rows)):
            try:
                cur.execute('''
                            SELECT TIME,date FROM Attendance
                            WHERE c_id={}
                            ORDER BY c_id
                            DESC LIMIT 1;
                            '''.format(rows[x][0]))
                ls=cur.fetchall()
                lasttime.append(ls[0][0])
                lastdate.append(ls[0][1])
            except:
                lasttime.append("FIRST TIMER")
                lastdate.append("FIRST DAY")
        print(lasttime,lastdate)
        self.ui.tableWidget_2.setRowCount(len(rows))
        self.ui.tableWidget_2.setColumnCount(4)
        self.ui.tableWidget_2.setHorizontalHeaderLabels(["client id","name","last in time","last date"])
        for i in range(len(rows)):
            for j in range(4):
                if(j==2):
                    self.ui.tableWidget_2.setItem(i,j, QTableWidgetItem(str(lasttime[i])))
                    print(lasttime[i])
                elif(j==3):
                    self.ui.tableWidget_2.setItem(i,j, QTableWidgetItem(str(lastdate[i])))
                    print(lastdate[i])
                else:    
                    print(rows[i][j])
                    self.ui.tableWidget_2.setItem(i,j, QTableWidgetItem(str(rows[i][j])))
        self.ui.pushButton_3.clicked.connect(self.search)
        self.ui.pushButton_2.clicked.connect(self.back)
        self.ui.lineEdit.textChanged.connect(self.val)
        self.ui.lineEdit_4.textChanged.connect(self.val)
        self.ui.lineEdit_5.textChanged.connect(self.val)
        self.ui.lineEdit_6.textChanged.connect(self.val)
        self.ui.pushButton.clicked.connect(self.entry)
        self.ui.pushButton.setEnabled(False)
    def val(self):
        try:
            barbell=int(self.ui.lineEdit_3.text())
            repetitions=int(self.ui.lineEdit_5.text())
            dumbell=int(self.ui.lineEdit_4.text())
            tm=int(self.ui.lineEdit_6.text())
            itms=self.ui.tableWidget_2.currentRow()
            c_id=int(self.ui.tableWidget_2.item(itms,0).text())
            modified=0
            if(self.ui.checkBox.isChecked()):
                modified=1
            self.ui.pushButton.setEnabled(True)
        except:
            self.ui.pushButton.setEnabled(False)
            print('all values must be filled')
    def entry(self):
        barbell=int(self.ui.lineEdit_3.text())
        repetitions=int(self.ui.lineEdit_5.text())
        dumbell=int(self.ui.lineEdit_4.text())
        tm=int(self.ui.lineEdit_6.text())
        itms=self.ui.tableWidget_2.currentRow()
        c_id=int(self.ui.tableWidget_2.item(itms,0).text())
        modified=0
        if(self.ui.checkBox.isChecked()):
            modified=1
        dt=str(datetime.date.today()) 
        print(dt)
        cur.execute('''
                    INSERT INTO testday (c_id,barbell,dumbell,time,repetitions,modified,date) VALUES({},{},{},{},{},{},DATE())
                    '''.format(c_id,barbell,dumbell,tm,repetitions,modified))
        conn.commit()
        self.main=Admin()
        self.main.show()
        self.close()    
    def back(self):
        self.main=Admin()
        self.main.show()
        self.close()
    def search(self):
        print('search')
        self.ui.tableWidget_2.setRowCount(0)
        reg="^"+self.ui.lineEdit.text()+"*"
        if(len(reg)>2):
            print(reg)
            cur.execute('''
                        SELECT c_id,name from Client_data;
                        ''')
            rows=cur.fetchall()
            alwd=[]
            for x in range(len(rows)):
                if(re.match(reg,rows[x][1])):
                   alwd.append(rows[x]) 
            print(rows,alwd)

            lasttime=[]
            lastdate=[]
            for x in range(len(alwd)):
                try:
                    cur.execute('''
                                SELECT TIME,date FROM Attendance
                                WHERE c_id={}
                                ORDER BY c_id
                                DESC LIMIT 1;
                                '''.format(rows[x][0]))
                    ls=cur.fetchall()
                    lasttime.append(ls[0][0])
                    lastdate.append(ls[0][1])
                except:
                    lasttime.append("FIRST TIMER")
                    lastdate.append("FIRST DAY")
            print(lasttime,lastdate)
            self.ui.tableWidget_2.setRowCount(len(alwd))
            self.ui.tableWidget_2.setColumnCount(4)
            self.ui.tableWidget_2.setHorizontalHeaderLabels(["client id","name","last in time","last date"])
            for i in range(len(alwd)):
                for j in range(4):
                    if(j==2):
                        self.ui.tableWidget_2.setItem(i,j, QTableWidgetItem(str(lasttime[i])))
                        print(lasttime[i])
                    elif(j==3):
                        self.ui.tableWidget_2.setItem(i,j, QTableWidgetItem(str(lastdate[i])))
                        print(lastdate[i])
                    else:    
                        print(rows[i][j])
                        self.ui.tableWidget_2.setItem(i,j, QTableWidgetItem(str(alwd[i][j])))
        else:
            print('no text entered')
class deleteclient(QMainWindow):
    def __init__(self):
        super(deleteclient,self).__init__()
        #loadUi('delete-client.ui',self)
        self.ui = delete_client()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("GYM MANAGEMENT SYSTEM")
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        cur.execute('''
                    SELECT c_id,name from Client_data
                    ''')
        rows=cur.fetchall()
        lasttime=[]
        lastdate=[]
        for x in range(len(rows)):
            try:
                cur.execute('''
                            SELECT TIME,date FROM Attendance
                            WHERE c_id={}
                            ORDER BY c_id
                            DESC LIMIT 1;
                            '''.format(rows[x][0]))
                ls=cur.fetchall()
                lasttime.append(ls[0][0])
                lastdate.append(ls[0][1])
            except:
                lasttime.append("FIRST TIMER")
                lastdate.append("FIRST DAY")
        print(lasttime,lastdate)
        self.ui.tableWidget_2.setRowCount(len(rows))
        self.ui.tableWidget_2.setColumnCount(4)
        self.ui.tableWidget_2.setHorizontalHeaderLabels(["client id","name","last in time","last date"])
        for i in range(len(rows)):
            for j in range(4):
                if(j==2):
                    self.ui.tableWidget_2.setItem(i,j, QTableWidgetItem(str(lasttime[i])))
                    print(lasttime[i])
                elif(j==3):
                    self.ui.tableWidget_2.setItem(i,j, QTableWidgetItem(str(lastdate[i])))
                    print(lastdate[i])
                else:    
                    print(rows[i][j])
                    self.ui.tableWidget_2.setItem(i,j, QTableWidgetItem(str(rows[i][j])))        

        self.ui.pushButton_2.clicked.connect(self.back)
        self.ui.pushButton.clicked.connect(self.delete)
        self.ui.pushButton_3.clicked.connect(self.search)
        self.ui.tableWidget_2.itemSelectionChanged.connect(self.btnalt)
        self.ui.pushButton.setEnabled(False)
    def btnalt(self):
        self.ui.pushButton.setEnabled(True)
    def search(self):
        print('search')
        self.ui.tableWidget_2.setRowCount(0)
        reg="^"+self.ui.lineEdit.text()+"*"
        if(len(reg)>2):
            print(reg)
            cur.execute('''
                        SELECT c_id,name from Client_data;
                        ''')
            rows=cur.fetchall()
            alwd=[]
            for x in range(len(rows)):
                if(re.match(reg,rows[x][1])):
                   alwd.append(rows[x]) 
            print(rows,alwd)

            lasttime=[]
            lastdate=[]
            for x in range(len(alwd)):
                try:
                    cur.execute('''
                                SELECT TIME,date FROM Attendance
                                WHERE c_id={}
                                ORDER BY c_id
                                DESC LIMIT 1;
                                '''.format(rows[x][0]))
                    ls=cur.fetchall()
                    lasttime.append(ls[0][0])
                    lastdate.append(ls[0][1])
                except:
                    lasttime.append("FIRST TIMER")
                    lastdate.append("FIRST DAY")
            print(lasttime,lastdate)
            self.ui.tableWidget_2.setRowCount(len(alwd))
            self.ui.tableWidget_2.setColumnCount(4)
            self.ui.tableWidget_2.setHorizontalHeaderLabels(["client id","name","last in time","last date"])
            for i in range(len(alwd)):
                for j in range(4):
                    if(j==2):
                        self.ui.tableWidget_2.setItem(i,j, QTableWidgetItem(str(lasttime[i])))
                        print(lasttime[i])
                    elif(j==3):
                        self.ui.tableWidget_2.setItem(i,j, QTableWidgetItem(str(lastdate[i])))
                        print(lastdate[i])
                    else:    
                        print(rows[i][j])
                        self.ui.tableWidget_2.setItem(i,j, QTableWidgetItem(str(alwd[i][j])))
        else:
            print('no text entered')

    def delete(self):
        print('delete')
        itms=self.ui.tableWidget_2.currentRow()
        itms=self.ui.tableWidget_2.item(itms,0).text()
        itms="'"+itms+"'"
        cur.execute('''
                    DELETE FROM Client_data WHERE c_id={} 
                    '''.format(itms))
        conn.commit()
    def back(self):
        self.main=clientsettings()
        self.main.show()
        self.close()
class modifyclient(QMainWindow):
    def __init__(self):
        super(modifyclient,self).__init__()
        #loadUi('modify-client.ui',self)
        self.ui = modify_client()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("GYM MANAGEMENT SYSTEM")
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        cur.execute('''
                     SELECT name from Client_data
                    ''')
        rows=cur.fetchall()
        print(rows)
        ls=[]
        for x in range(len(rows)):
            ls.append(str(rows[x][0]))    
        self.ui.comboBox.addItems(ls)
        self.ui.pushButton.clicked.connect(self.proceed)
        self.ui.pushButton_2.clicked.connect(self.back)
        self.ui.label_3.hide()
    def back(self):
        self.main=clientsettings()
        self.main.show()
        self.close()
    def proceed(self):
        try:
            global var
            var=(self.ui.comboBox.currentText())
            self.main=modifyclient1()
            self.main.show()
            self.close()
        except:
            print('no clients added')
            self.ui.label_3.show()
class modifyclient1(QMainWindow):
    def __init__(self):
        super(modifyclient1,self).__init__()
        #loadUi('modify-client1.ui',self)
        self.ui = modify_client1()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("GYM MANAGEMENT SYSTEM")
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        cur.execute('''
                     SELECT p_name from Plan_data
                    ''')
        rows=cur.fetchall()
        print(rows)
        ls=[]
        for x in range(len(rows)):
            ls.append(str(rows[x][0]))    
        self.ui.comboBox.addItems(ls)
        name="'"+var+"'"
        self.ui.lineEdit.setText(var)
        print(name)
        cur.execute('''
                    SELECT c_id,m_no,p_no,Valid_from,Valid_to
                    FROM Client_data
                    WHERE name={};
                    '''.format(name))
        row=cur.fetchall()
        print(row)
        self.ui.lineEdit_2.setText(str(row[0][1]))
        cur.execute('''
                    SELECT p_name FROM Plan_data
                    WHERE p_no={}
                    '''.format("'"+str(row[0][2])+"'"))
        row1=cur.fetchall()
        self.ui.comboBox.setCurrentIndex(row[0][2]-1)
        print(row1)
        text=row1[0][0]
        print(text)
        index = self.ui.comboBox.findData(text, QtCore.Qt.MatchFixedString)
        if index >= 0:
             combo.setCurrentIndex(index)
        cur.execute('''
                     SELECT amount FROM Payhistory
                     WHERE c_id={} AND date={}
                    '''.format("'"+str(row[0][0])+"'","'"+row[0][3]+"'"))
        row2=cur.fetchall()
        self.ui.lineEdit_3.setText(str(row2[0][0]))
        self.ui.pushButton.clicked.connect(self.update)
        self.ui.pushButton_2.clicked.connect(self.back)
        self.ui.lineEdit_3.textChanged.connect(self.val)
        self.ui.lineEdit_2.textChanged.connect(self.val)
        self.ui.lineEdit.textChanged.connect(self.val)
        self.showMaximized()
    def val(self):
        try:
            name="'"+self.ui.lineEdit.text()+"'"
            con_no=int(self.ui.lineEdit_2.text())
            amt=int(self.ui.lineEdit_3.text())
            plan="'"+self.ui.comboBox.currentText()+"'"
            self.ui.pushButton.setEnabled(True)
        except:
            self.ui.pushButton.setEnabled(False)
    def back(self):
        self.main=clientsettings()
        self.main.show()
        self.close()
    def update(self):
        
        name="'"+self.ui.lineEdit.text()+"'"
        print(name)
        cur.execute('''
                    SELECT c_id,Valid_from FROM Client_data
                    WHERE name={}
                    '''.format("'"+var+"'"))
        rows=cur.fetchall()
        print(rows)
        date="'"+rows[0][1]+"'"
        c_id="'"+str(rows[0][0])+"'"
        print(c_id,date)
        con_no=int(self.ui.lineEdit_2.text())
        amt=int(self.ui.lineEdit_3.text())
        plan="'"+self.ui.comboBox.currentText()+"'"
        cur.execute('''
                    SELECT p_no from Plan_data
                    WHERE p_name={}
                    '''.format(plan))
        row=cur.fetchall()
        print(row[0][0])
        cur.execute('''
                    UPDATE Client_data
                    SET  m_no={},p_no={},name={}
                    WHERE c_id={};
                    '''.format(con_no,row[0][0],name,c_id))
        conn.commit()
        cur.execute('''
                    UPDATE Payhistory
                    SET amount={}
                    WHERE c_id={} AND date={}
                    '''.format(amt,c_id,date))
        conn.commit()
        self.main=clientsettings()
        self.main.show()
        self.close()
class addclient(QMainWindow):
    def __init__(self):
        super(addclient,self).__init__()
        #loadUi('add-client.ui',self)
        self.ui = add_client()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("GYM MANAGEMENT SYSTEM")
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        cur.execute('''
                     SELECT p_name from Plan_data
                    ''')
        rows=cur.fetchall()
        print(rows)
        ls=[]
        for x in range(len(rows)):
            ls.append(str(rows[x][0]))    
        self.ui.comboBox.addItems(ls)
        self.ui.pushButton.clicked.connect(self.add)
        self.ui.lineEdit.textChanged.connect(self.fil)
        self.ui.lineEdit_2.textChanged.connect(self.fil)
        self.ui.lineEdit_3.textChanged.connect(self.fil)
        self.ui.pushButton_2.clicked.connect(self.back)
        self.ui.pushButton.setEnabled(False)
    def fil(self):
        try:
            name="'"+self.ui.lineEdit.text()+"'"
            con_no=int(self.ui.lineEdit_2.text())
            amt=int(self.ui.lineEdit_3.text())
            plan="'"+self.ui.comboBox.currentText()+"'"
            from_date="'"+(self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd"))+"'"
            to_date="'"+(self.ui.calendarWidget_2.selectedDate().toString("yyyy-MM-dd"))+"'"
            self.ui.pushButton.setEnabled(True)
        except:
            self.ui.pushButton.setEnabled(False)
            print('all fields must be filled')
    def back(self):
        self.main=clientsettings()
        self.main.show()
        self.close()
    def add(self):
        name="'"+self.ui.lineEdit.text()+"'"
        con_no=int(self.ui.lineEdit_2.text())
        amt=int(self.ui.lineEdit_3.text())
        plan="'"+self.ui.comboBox.currentText()+"'"
        from_date="'"+(self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd"))+"'"
        to_date="'"+(self.ui.calendarWidget_2.selectedDate().toString("yyyy-MM-dd"))+"'"
        print(name,con_no,amt,plan,from_date,to_date)
        cur.execute('''
                    SELECT p_no from Plan_data
                    WHERE p_name={}
                    '''.format(plan))
        row=cur.fetchall()
        print(row[0][0])
        cur.execute('''
                    INSERT INTO Client_data (name,m_no,p_no,Valid_from,Valid_to) VALUES ({},{},{},{},{})
                    '''.format(name,con_no,row[0][0],from_date,to_date))
        conn.commit()
        cur.execute('''
                    SELECT c_id FROM Client_data
                    WHERE name={} AND m_no={}
                    '''.format(name,con_no))
        row=cur.fetchall()
        cur.execute('''
                    INSERT INTO Payhistory (c_id,amount,date) VALUES ({},{},{})
                    '''.format(row[0][0],amt,from_date))
        conn.commit()
        print('success')
        self.main=clientsettings()
        self.main.show()
        self.close()
class payentry(QMainWindow):
    def __init__(self):
        super(payentry,self).__init__()
        #loadUi('payentry.ui',self)
        self.ui = payentry_ui()
        self.ui.setupUi(self)
        self.showMaximized()
        self.showMaximized()
        self.setWindowTitle("GYM MANAGEMENT SYSTEM")
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        cur.execute('''
                    SELECT c_id,name from Client_data
                    ''')
        rows=cur.fetchall()
        lasttime=[]
        lastdate=[]
        for x in range(len(rows)):
            try:
                cur.execute('''
                            SELECT TIME,date FROM Attendance
                            WHERE c_id={}
                            ORDER BY c_id
                            DESC LIMIT 1;
                            '''.format(rows[x][0]))
                ls=cur.fetchall()
                lasttime.append(ls[0][0])
                lastdate.append(ls[0][1])
            except:
                lasttime.append("FIRST TIMER")
                lastdate.append("FIRST DAY")
        print(lasttime,lastdate)
        self.ui.tableWidget_2.setRowCount(len(rows))
        self.ui.tableWidget_2.setColumnCount(4)
        self.ui.tableWidget_2.setHorizontalHeaderLabels(["client id","name","last in time","last date"])
        for i in range(len(rows)):
            for j in range(4):
                if(j==2):
                    self.ui.tableWidget_2.setItem(i,j, QTableWidgetItem(str(lasttime[i])))
                    print(lasttime[i])
                elif(j==3):
                    self.ui.tableWidget_2.setItem(i,j, QTableWidgetItem(str(lastdate[i])))
                    print(lastdate[i])
                else:    
                    print(rows[i][j])
                    self.ui.tableWidget_2.setItem(i,j, QTableWidgetItem(str(rows[i][j])))        

        self.ui.pushButton_2.clicked.connect(self.back)
        self.ui.pushButton_3.clicked.connect(self.search)
        self.ui.pushButton.clicked.connect(self.add)
        self.ui.lineEdit_3.textChanged.connect(self.val)
        self.ui.tableWidget_2.itemSelectionChanged.connect(self.val)
        self.ui.pushButton.setEnabled(False)
    def val(self):
        try:
            from_date="'"+(self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd"))+"'"
            to_date="'"+(self.ui.calendarWidget_2.selectedDate().toString("yyyy-MM-dd"))+"'"
            amt=int(self.ui.lineEdit_3.text())
            itms=self.ui.tableWidget_2.currentRow()
            itms=self.ui.tableWidget_2.item(itms,0).text()
            self.ui.pushButton.setEnabled(True)
        except:
            self.ui.pushButton.setEnabled(False)
            print('enter all fields')
    def add(self):
        from_date="'"+(self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd"))+"'"
        to_date="'"+(self.ui.calendarWidget_2.selectedDate().toString("yyyy-MM-dd"))+"'"
        amt=int(self.ui.lineEdit_3.text())
        itms=self.ui.tableWidget_2.currentRow()
        itms=self.ui.tableWidget_2.item(itms,0).text()
        itms="'"+itms+"'"
        cur.execute('''
                    UPDATE Client_data
                    SET Valid_from={},Valid_to={}
                    WHERE c_id={}
                    '''.format(from_date,to_date,itms))
        conn.commit()
        cur.execute('''
                    INSERT INTO Payhistory (c_id,amount,date) VALUES({},{},{})
                   '''.format(itms,amt,from_date))
        conn.commit()
        self.main=clientsettings()
        self.main.show()
        self.close()
    def back(self):
        self.main=clientsettings()
        self.main.show()
        self.close()
    def search(self):
        print('search')
        self.ui.tableWidget_2.setRowCount(0)
        reg="^"+self.ui.lineEdit.text()+"*"
        if(len(reg)>2):
            print(reg)
            cur.execute('''
                        SELECT c_id,name from Client_data;
                        ''')
            rows=cur.fetchall()
            alwd=[]
            for x in range(len(rows)):
                if(re.match(reg,rows[x][1])):
                   alwd.append(rows[x]) 
            print(rows,alwd)

            lasttime=[]
            lastdate=[]
            for x in range(len(alwd)):
                try:
                    cur.execute('''
                                SELECT TIME,date FROM Attendance
                                WHERE c_id={}
                                ORDER BY TIME
                                DESC LIMIT 1;
                                '''.format(rows[x][0]))
                    ls=cur.fetchall()
                    lasttime.append(ls[0][0])
                    lastdate.append(ls[0][1])
                except:
                    lasttime.append("FIRST TIMER")
                    lastdate.append("FIRST DAY")
            print(lasttime,lastdate)
            self.ui.tableWidget_2.setRowCount(len(alwd))
            self.ui.tableWidget_2.setColumnCount(4)
            self.ui.tableWidget_2.setHorizontalHeaderLabels(["client id","name","last in time","last date"])
            for i in range(len(alwd)):
                for j in range(4):
                    if(j==2):
                        self.ui.tableWidget_2.setItem(i,j, QTableWidgetItem(str(lasttime[i])))
                        print(lasttime[i])
                    elif(j==3):
                        self.ui.tableWidget_2.setItem(i,j, QTableWidgetItem(str(lastdate[i])))
                        print(lastdate[i])
                    else:    
                        print(rows[i][j])
                        self.ui.tableWidget_2.setItem(i,j, QTableWidgetItem(str(alwd[i][j])))
        else:
            print('no text entered')
class clientsettings(QMainWindow):
    def __init__(self):
        super(clientsettings,self).__init__()
        #loadUi('client-settings.ui',self)
        self.ui = client_settings()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("GYM MANAGEMENT SYSTEM")
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.ui.pushButton_4.clicked.connect(self.back)
        self.ui.pushButton.clicked.connect(self.add)
        self.ui.pushButton_2.clicked.connect(self.modify)
        self.ui.pushButton_3.clicked.connect(self.delete)
        self.ui.pushButton_5.clicked.connect(self.pay)
    def pay(self):
        self.main=payentry()
        self.main.show()
        self.close()
    def delete(self):
        self.main=deleteclient()
        self.main.show()
        self.close()
    def modify(self):
        self.main=modifyclient()
        self.main.show()
        self.close()
    def add(self):
        self.main=addclient()
        self.main.show()
        self.close()
    def back(self):
        self.main=Admin()
        self.main.show()
        self.close()
class addplan(QMainWindow):
    def __init__(self):
        super(addplan,self).__init__()
        #loadUi('add-plan.ui',self)
        self.ui = add_plan()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("GYM MANAGEMENT SYSTEM")
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.ui.pushButton_2.clicked.connect(self.back)
        self.ui.pushButton.clicked.connect(self.add)
        self.ui.lineEdit.textChanged.connect(self.val)
        self.ui.textEdit.textChanged.connect(self.val)
        self.ui.pushButton.setEnabled(False)
    def val(self):
        try:
            pname=self.ui.lineEdit.text()
            desc=self.ui.textEdit.toPlainText()
            if(len(pname)==0 or len(desc)==0):
                self.ui.pushButton.setEnabled(False)
                raise Exception('length')
            else:
                self.ui.pushButton.setEnabled(True)
        except:
            print('all fields must be entered')
    def add(self):
        pname=self.ui.lineEdit.text()
        desc=self.ui.textEdit.toPlainText()
        pname="'"+pname+"'"
        desc="'"+desc+"'"
        cur.execute('''
                    INSERT INTO Plan_data (p_name,description) VALUES ({},{})
                   '''.format(pname,desc))
        conn.commit()
        self.main=Plansettings()
        self.main.show()
        self.close()
    def back(self):
        self.main=Plansettings()
        self.main.show()
        self.close()
class modifyplan(QMainWindow):
    def __init__(self):
        super(modifyplan,self).__init__()
        #loadUi('modify-plan.ui',self)
        self.ui = modify_plan()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("GYM MANAGEMENT SYSTEM")
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        cur.execute('''
                     SELECT p_name from Plan_data
                    ''')
        rows=cur.fetchall()
        print(rows)
        ls=[]
        for x in range(len(rows)):
            ls.append(str(rows[x][0]))    
        self.ui.comboBox.addItems(ls)    
        self.ui.pushButton_2.clicked.connect(self.back)
        self.ui.pushButton.clicked.connect(self.update)
        self.ui.textEdit.textChanged.connect(self.val)
        self.ui.pushButton.setEnabled(False)
    def val(self):
        try:
            desc=self.ui.textEdit.toPlainText()
            if(len(desc)==0):
                self.ui.pushButton.setEnabled(False)
                raise Exception('length')
            else:
                self.ui.pushButton.setEnabled(True)
        except:
            print('please enter description')
    def update(self):
        desc=self.ui.textEdit.toPlainText()
        desc="'"+desc+"'"
        pname="'"+str(self.ui.comboBox.currentText())+"'"
        #print(desc,pname)
        cur.execute('''
                    UPDATE Plan_data
                    SET description={}
                    WHERE p_name={}
                    '''.format(desc,pname))
        conn.commit()
        self.main=Plansettings()
        self.main.show()
        self.close()
    def back(self):
        self.main=Plansettings()
        self.main.show()
        self.close()
class deleteplan(QMainWindow):
    def __init__(self):
        super(deleteplan,self).__init__()
        #loadUi('delete-plan.ui',self)
        self.ui = delete_plan()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("GYM MANAGEMENT SYSTEM")
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        cur.execute('''
                     SELECT p_name from Plan_data
                    ''')
        rows=cur.fetchall()
        print(rows)
        ls=[]
        for x in range(len(rows)):
            ls.append(str(rows[x][0]))    
        self.ui.comboBox.addItems(ls)
        self.ui.pushButton_2.clicked.connect(self.back)
        self.ui.pushButton.clicked.connect(self.delete)
        self.showMaximized()
    def delete(self):
        pname="'"+str(self.ui.comboBox.currentText())+"'"
        cur.execute('''
                     DELETE FROM Plan_data
                     WHERE p_name={}
                   '''.format(pname))
        conn.commit()
        self.main=Plansettings()
        self.main.show()
        self.close()
    def back(self):
        self.main=Plansettings()
        self.main.show()
        self.close()    
class Plansettings(QMainWindow):
    def __init__(self):
        super(Plansettings,self).__init__()
        #loadUi('plan-settings.ui',self)
        self.ui = plan_settings()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("GYM MANAGEMENT SYSTEM")
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.ui.pushButton_4.clicked.connect(self.back)
        self.ui.pushButton.clicked.connect(self.add)
        self.ui.pushButton_2.clicked.connect(self.modify)
        self.ui.pushButton_3.clicked.connect(self.delete)
    def delete(self):
        self.main=deleteplan()
        self.main.show()
        self.close()
    def modify(self):
        self.main=modifyplan()
        self.main.show()
        self.close()
    def add(self):
        self.main=addplan()
        self.main.show()
        self.close()
    def back(self):
        self.main=Admin()
        self.main.show()
        self.close()
class Loginfailed(QMainWindow):
    def __init__(self):
        super(Loginfailed,self).__init__()
        #loadUi('loginfailed.ui',self)
        self.ui = loginfailed()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("GYM MANAGEMENT SYSTEM")
        #self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.ui.pushButton.clicked.connect(self.login)
    def login(self):
        uname=list(self.ui.lineEdit.text())
        pswd=(self.ui.lineEdit_2.text())
        uname.append('\'')
        uname.insert(0,'\'')
        uname=''.join(uname)
        try:
            cur.execute('''
                        SELECT u_pass,u_type FROM Users WHERE u_name={}'''.format(uname))
            psd=cur.fetchall()
            if((psd[0][0])==pswd and (psd[0][1])==1):
                print('admin')
                self.main=Admin()
                self.main.show()
                self.close()
            elif((psd[0][0])==pswd and (psd[0][1])==0):
                print('user')
                self.main=User()
                self.main.show()
                self.close()
            else:
                self.main=Loginfailed()
                self.main.show()
                self.close()
        except Exception as e:
            print(e)
            self.main=Loginfailed()
            self.main.show()
            self.close()
class adattd(QMainWindow):
    def __init__(self):
        super(adattd,self).__init__()
        #loadUi('adattd.ui',self)
        self.ui = adattd_ui()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("GYM MANAGEMENT SYSTEM")
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        cur.execute('''
                    SELECT c_id,name from Client_data
                    ''')
        rows=cur.fetchall()
        lasttime=[]
        lastdate=[]
        for x in range(len(rows)):
            try:
                cur.execute('''
                            SELECT TIME,date FROM Attendance
                            WHERE c_id={}
                            ORDER BY TIME
                            DESC LIMIT 1;
                            '''.format(rows[x][0]))
                ls=cur.fetchall()
                lasttime.append(ls[0][0])
                lastdate.append(ls[0][1])
            except:
                lasttime.append("FIRST TIMER")
                lastdate.append("FIRST DAY")
        print(lasttime,lastdate)
        self.ui.tableWidget.setRowCount(len(rows))
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(["client id","name","last in time","last date"])
        for i in range(len(rows)):
            for j in range(4):
                if(j==2):
                    self.ui.tableWidget.setItem(i,j, QTableWidgetItem(str(lasttime[i])))
                    print(lasttime[i])
                elif(j==3):
                    self.ui.tableWidget.setItem(i,j, QTableWidgetItem(str(lastdate[i])))
                    print(lastdate[i])
                else:    
                    print(rows[i][j])
                    self.ui.tableWidget.setItem(i,j, QTableWidgetItem(str(rows[i][j])))        
        
        self.ui.pushButton.clicked.connect(self.markattd)
        self.ui.pushButton_2.clicked.connect(self.search)
        self.ui.pushButton_3.clicked.connect(self.back)
        self.ui.tableWidget.itemSelectionChanged.connect(self.btnalt)
        self.ui.pushButton.setEnabled(False)
    def btnalt(self):
        self.ui.pushButton.setEnabled(True)
    def back(self):
        self.main=Admin()
        self.main.show()
        self.close()
    def markattd(self):
        #to mark attendance
        itms=self.ui.tableWidget.currentRow()
        itms=self.ui.tableWidget.item(itms,0).text()
        itms="'"+itms+"'"
        print(itms)
        tm=datetime.datetime.now()
        tm=tm.strftime("%X")
        tm="'"+tm+"'"
        dt=datetime.datetime.now()
        dt=dt.strftime('%Y-%m-%d')
        dt="'"+dt+"'"
        cur.execute('''
                        INSERT INTO Attendance (c_id,TIME,date) VALUES ({},{},{});
                        '''.format(itms,tm,dt)
                        )
        conn.commit()
        print('attendance marked')
        self.main=Admin()
        self.main.show()
        self.close()
    def search(self):
        self.ui.tableWidget.setRowCount(0)
        reg="^"+self.ui.lineEdit.text().lower()+"*"
        if(len(reg)>2):
            print(reg)
            cur.execute('''
                        SELECT c_id,name from Client_data;
                        ''')
            rows=cur.fetchall()
            alwd=[]
            for x in range(len(rows)):
                if(re.match(reg,rows[x][1].lower())):
                   alwd.append(rows[x]) 
            print(rows,alwd)

            lasttime=[]
            lastdate=[]
            for x in range(len(alwd)):
                try:
                    cur.execute('''
                                SELECT TIME,date FROM Attendance
                                WHERE c_id={}
                                ORDER BY TIME
                                DESC LIMIT 1;
                                '''.format(rows[x][0]))
                    ls=cur.fetchall()
                    lasttime.append(ls[0][0])
                    lastdate.append(ls[0][1])
                except:
                    lasttime.append("FIRST TIMER")
                    lastdate.append("FIRST DAY")
            print(lasttime,lastdate)
            self.ui.tableWidget.setRowCount(len(alwd))
            self.ui.tableWidget.setColumnCount(4)
            self.ui.tableWidget.setHorizontalHeaderLabels(["client id","name","last in time","last date"])
            for i in range(len(alwd)):
                for j in range(4):
                    if(j==2):
                        self.ui.tableWidget.setItem(i,j, QTableWidgetItem(str(lasttime[i])))
                        print(lasttime[i])
                    elif(j==3):
                        self.ui.tableWidget.setItem(i,j, QTableWidgetItem(str(lastdate[i])))
                        print(lastdate[i])
                    else:    
                        print(rows[i][j])
                        self.ui.tableWidget.setItem(i,j, QTableWidgetItem(str(alwd[i][j])))
        else:
            print('no text entered')

class User(QMainWindow):
    def __init__(self):
        super(User,self).__init__()
        #loadUi('user.ui',self)
        self.ui = user()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("GYM MANAGEMENT SYSTEM")
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        cur.execute('''
                    SELECT c_id,name from Client_data
                    ''')
        rows=cur.fetchall()
        lasttime=[]
        lastdate=[]
        for x in range(len(rows)):
            try:
                cur.execute('''
                            SELECT TIME,date FROM Attendance
                            WHERE c_id={}
                            ORDER BY TIME
                            DESC LIMIT 1;
                            '''.format(rows[x][0]))
                ls=cur.fetchall()
                lasttime.append(ls[0][0])
                lastdate.append(ls[0][1])
            except:
                lasttime.append("FIRST TIMER")
                lastdate.append("FIRST DAY")
        print(lasttime,lastdate)
        self.ui.tableWidget.setRowCount(len(rows))
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(["client id","name","last in time","last date"])
        for i in range(len(rows)):
            for j in range(4):
                if(j==2):
                    self.ui.tableWidget.setItem(i,j, QTableWidgetItem(str(lasttime[i])))
                    print(lasttime[i])
                elif(j==3):
                    self.ui.tableWidget.setItem(i,j, QTableWidgetItem(str(lastdate[i])))
                    print(lastdate[i])
                else:    
                    print(rows[i][j])
                    self.ui.tableWidget.setItem(i,j, QTableWidgetItem(str(rows[i][j])))        
        
        self.ui.pushButton.clicked.connect(self.markattd)
        self.ui.pushButton_2.clicked.connect(self.logout)
        self.ui.pushButton_3.clicked.connect(self.search)
        self.ui.pushButton.setEnabled(False)
        self.ui.tableWidget.itemSelectionChanged.connect(self.btnalt)
    def btnalt(self):
        try:
            itms=self.ui.tableWidget.currentRow()
            itms=self.ui.tableWidget.item(itms,0).text()
            itms="'"+itms+"'"
            self.ui.pushButton.setEnabled(True)
        except:
            print('please select a row')
    def search(self):
        self.ui.tableWidget.setRowCount(0)
        reg="^"+(str(self.ui.lineEdit.text())).lower()+"*"
        if(len(reg)>2):
            print(reg)
            cur.execute('''
                        SELECT c_id,name from Client_data;
                        ''')
            rows=cur.fetchall()
            alwd=[]
            for x in range(len(rows)):
                if(re.match(reg,rows[x][1].lower())):
                   alwd.append(rows[x]) 
            print(rows,alwd)

            lasttime=[]
            lastdate=[]
            for x in range(len(alwd)):
                try:
                    cur.execute('''
                                SELECT TIME,date FROM Attendance
                                WHERE c_id={}
                                ORDER BY TIME
                                DESC LIMIT 1;
                                '''.format(rows[x][0]))
                    ls=cur.fetchall()
                    lasttime.append(ls[0][0])
                    lastdate.append(ls[0][1])
                except:
                    lasttime.append("FIRST TIMER")
                    lastdate.append("FIRST DAY")
            print(lasttime,lastdate)
            self.ui.tableWidget.setRowCount(len(alwd))
            self.ui.tableWidget.setColumnCount(4)
            self.ui.tableWidget.setHorizontalHeaderLabels(["client id","name","last in time","last date"])
            for i in range(len(alwd)):
                for j in range(4):
                    if(j==2):
                        self.ui.tableWidget.setItem(i,j, QTableWidgetItem(str(lasttime[i])))
                        print(lasttime[i])
                    elif(j==3):
                        self.ui.tableWidget.setItem(i,j, QTableWidgetItem(str(lastdate[i])))
                        print(lastdate[i])
                    else:    
                        print(rows[i][j])
                        self.ui.tableWidget.setItem(i,j, QTableWidgetItem(str(alwd[i][j])))
        else:
            print('no text entered')

    def logout(self):
         self.main=LoginPage()
         self.main.show()
         self.close()
    def markattd(self):
        #to mark attendance
        itms=self.ui.tableWidget.currentRow()
        itms=self.ui.tableWidget.item(itms,0).text()
        itms="'"+itms+"'"
        print(itms)
        tm=datetime.datetime.now()
        tm=tm.strftime("%X")
        tm="'"+tm+"'"
        dt=datetime.datetime.now()
        dt=dt.strftime('%Y-%m-%d')
        dt="'"+dt+"'"
        cur.execute('''
                        INSERT INTO Attendance (c_id,TIME,date) VALUES ({},{},{});
                        '''.format(itms,tm,dt)
                        )
        conn.commit()
        cur.execute('''
                    SELECT c_id,name from Client_data
                    ''')
        rows=cur.fetchall()
        lasttime=[]
        lastdate=[]
        for x in range(len(rows)):
            try:
                cur.execute('''
                            SELECT TIME,date FROM Attendance
                            WHERE c_id={}
                            ORDER BY TIME
                             DESC LIMIT 1;
                            '''.format(rows[x][0]))
                ls=cur.fetchall()
                lasttime.append(ls[0][0])
                lastdate.append(ls[0][1])
            except:
                lasttime.append("FIRST TIMER")
                lastdate.append("FIRST DAY")
        print(lasttime,lastdate)
        self.ui.tableWidget.setRowCount(len(rows))
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(["client id","name","last in time","last date"])
        for i in range(len(rows)):
            for j in range(4):
                if(j==2):
                    self.ui.tableWidget.setItem(i,j, QTableWidgetItem(str(lasttime[i])))
                    print(lasttime[i])
                elif(j==3):
                    self.ui.tableWidget.setItem(i,j, QTableWidgetItem(str(lastdate[i])))
                    print(lastdate[i])
                else:    
                    print(rows[i][j])
                    self.ui.tableWidget.setItem(i,j, QTableWidgetItem(str(rows[i][j])))        

        print('attendance marked')
class changepass(QMainWindow):
    def __init__(self):
        super(changepass,self).__init__()
        #loadUi('changepass.ui',self)
        self.ui = changepass_ui()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("GYM MANAGEMENT SYSTEM")
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        cur.execute('''
                     SELECT u_name from Users
                    ''')
        rows=cur.fetchall()
        print(rows)
        ls=[]
        for x in range(len(rows)):
            ls.append(str(rows[x][0]))    
        self.ui.comboBox.addItems(ls)
        self.ui.pushButton_2.clicked.connect(self.back)
        self.ui.pushButton.clicked.connect(self.chgpass)
        self.ui.lineEdit.textChanged.connect(self.val)
        self.ui.lineEdit_2.textChanged.connect(self.val)
        self.ui.pushButton.setEnabled(False)
    def val(self):
        try:
            newpass=str(self.ui.lineEdit_2.text())
            oldpass=str(self.ui.lineEdit.text())
            if(len(newpass)==0 or len(oldpass)==0):
                raise Exception('length')
            u_name=self.ui.comboBox.currentText()
            self.ui.pushButton.setEnabled(True)
        except:
            self.ui.pushButton.setEnabled(False)
            print('all fields must be filled')
    def chgpass(self):
        newpass="'"+self.ui.lineEdit_2.text()+"'"
        oldpass="'"+self.ui.lineEdit.text()+"'"
        u_name="'"+self.ui.comboBox.currentText()+"'"
        cur.execute('''
                    SELECT u_pass
                    FROM Users
                    WHERE u_name={}
                    '''.format(u_name))
        row=cur.fetchall()
        print(row[0][0])
        if(oldpass=="'"+row[0][0]+"'"):
            cur.execute('''
                        UPDATE Users
                        SET u_pass={}
                        WHERE u_name={} AND u_pass={}
                        '''.format(newpass,u_name,oldpass))
            conn.commit()
            self.main=generalsettings()
            self.main.show()
            self.close()
        else:
            self.main=changepass()
            self.main.show()
            self.close()
    def back(self):
        self.main=generalsettings()
        self.main.show()
        self.close()
class generalsettings(QMainWindow):
    def __init__(self):
        super(generalsettings,self).__init__()
        #loadUi('general-settings.ui',self)
        self.ui = general_settings()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("GYM MANAGEMENT SYSTEM")
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.ui.pushButton_2.clicked.connect(self.back)
        self.ui.pushButton.clicked.connect(self.changepass)
    def changepass(self):
        self.main=changepass()
        self.main.show()
        self.close()
    def back(self):
        self.main=Admin()
        self.main.show()
        self.close()
class Admin(QMainWindow):
    def __init__(self):
        super(Admin,self).__init__()
        #loadUi('admin.ui',self)
        self.ui = admin()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("GYM MANAGEMENT SYSTEM")
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.ui.pushButton_7.clicked.connect(self.logout)
        self.ui.pushButton_4.clicked.connect(self.attd)
        self.ui.pushButton_2.clicked.connect(self.plansettings)
        self.ui.pushButton.clicked.connect(self.clientsettings)
        self.ui.pushButton_6.clicked.connect(self.generalsettings)
        self.ui.pushButton_5.clicked.connect(self.testday)
        self.startTimer(1000)
    def testday(self):
        self.main=testday()
        self.main.show()
        self.close()
    def generalsettings(self):
        self.main=generalsettings()
        self.main.show()
        self.close()
    def clientsettings(self):
        self.main=clientsettings()
        self.main.show()
        self.close()
    def plansettings(self):
        self.main=Plansettings()
        self.main.show()
        self.close()
    def attd(self):
        try:
            self.main=adattd()
            self.main.show()
            print('ui opened')
            self.close()
        except:
            print('error')
    def logout(self):
        self.main=LoginPage()
        self.main.show()
        self.close()
    def timerEvent(self,e):
        self.ui.lcdNumber.setDigitCount(20)
        #self.lcdNumber.display(QDateTime.currentDateTime().toString())
        self.ui.lcdNumber.display(str(datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")))
class LoginPage(QMainWindow):
    def __init__(self):
        super(LoginPage,self).__init__()
        #loadUi('loginpage.ui',self)
        self.ui = loginpage()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("GYM MANAGEMENT SYSTEM")
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.ui.pushButton.clicked.connect(self.login)
    def login(self):
        uname=list(self.ui.lineEdit.text())
        pswd=(self.ui.lineEdit_2.text())
        uname.append('\'')
        uname.insert(0,'\'')
        uname=''.join(uname)
        try:
            cur.execute('''
                        SELECT u_pass,u_type FROM Users WHERE u_name={}'''.format(uname))
            psd=cur.fetchall()
            if((psd[0][0])==pswd and (psd[0][1])==1):
                print('admin')
                self.main=Admin()
                self.main.show()
                self.close()
            elif((psd[0][0])==pswd and (psd[0][1])==0):
                print('user')
                self.main=User()
                self.main.show()
                self.close()
            else:
                self.main=Loginfailed()
                self.main.show()
                self.close()
        except:
            self.main=Loginfailed()
            self.main.show()
            self.close()
def dbfun():
    cur.execute('''
                CREATE TABLE IF NOT EXISTS "Payhistory"
                ("c_id" INTEGER NOT NULL,
                "amount" INTEGER NOT NULL,
                "date" TEXT NOT NULL);
                '''
                )
    cur.execute('''
                CREATE TABLE IF NOT EXISTS "Attendance"
                (
	        "c_id"	INTEGER NOT NULL,
	        "TIME"	TEXT NOT NULL,
	        "date"	REAL NOT NULL
                 );
                ''')
    cur.execute('''
                CREATE TABLE IF NOT EXISTS "Client_data"
                (
                 "c_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            	 "name"	TEXT NOT NULL,
                 "m_no"	NUMERIC NOT NULL,
                 "p_no"	INTEGER NOT NULL,
                 "Valid_from"	TEXT,
                 "Valid_to"	TEXT
                 );
                ''')
    cur.execute('''
                CREATE TABLE IF NOT EXISTS "Plan_data" (
                "p_no"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                "p_name" TEXT NOT NULL,
	        "description" TEXT NOT NULL
                );
                '''
               )
    cur.execute('''
                CREATE TABLE IF NOT EXISTS "Users" (
	       "u_name"	 REAL NOT NULL UNIQUE,
	        "u_pass" REAL NOT NULL,
	       "u_type"	INTEGER NOT NULL,
	        PRIMARY KEY("u_name")
                );
                '''
                )
    cur.execute('''
                CREATE TABLE IF NOT EXISTS "testday" (
	           "c_id"	INTEGER,
                "barbell"	INTEGER,
                "dumbell"	INTEGER,
                "time"	INTEGER,
                "repetitions"	INTEGER,
                "modified"	INTEGER,
                "date"	TEXT
                );
                ''')
    cur.execute('''
                SELECT COUNT(*) FROM Users;
                '''
                )
    var=cur.fetchall()
    if(var[0][0]==0):
        cur.execute('''
                    INSERT INTO Users (u_name,u_pass,u_type) VALUES('admin','admin','1');
                    '''
                    )
        cur.execute('''
                    INSERT INTO Users (u_name,u_pass,u_type) VALUES('user','user','0');
                    '''
                    )
        cur.execute('''
                    INSERT INTO Users (u_name,u_pass,u_type) VALUES('sudo','sudo','1');
                    '''
                    )
        cur.execute('''
                    INSERT INTO Plan_data (p_name,description) VALUES('classes','a plan to keep our clients healthy and fit')
                    ''')
        cur.execute('''
                    INSERT INTO Plan_data (p_name,description) VALUES('personal training','a plan to keep our clients healthy and fit')
                    ''')
        cur.execute('''
                    INSERT INTO Plan_data (p_name,description) VALUES('group personal training','a plan to keep our clients healthy and fit')
                    ''')
    conn.commit()
def report_fun():
    name='report-'+str(datetime.date.today())
    cur.execute('''SELECT * FROM attendance''')
    rows=cur.fetchall()
    if(len(rows)>1):
        if(os.path.exists('project/reports/{}.xlsx'.format(name))):
            return
        else:
            workbook = xlsxwriter.Workbook('project/reports/{}.xlsx'.format(name))
            due=workbook.add_worksheet('due')
            due.set_column(1,4,25)
            due.write(0,0,'name')
            due.write(0,1,'mobile number')
            due.write(0,2,'plan name')
            due.write(0,3,'valid upto')
            cur.execute(''' SELECT Client_data.name,Client_data.m_no,Plan_data.p_name,Client_data.Valid_to
                            FROM Client_data,Plan_data
                            WHERE Client_data.p_no=Plan_data.p_no AND Client_data.Valid_to<=date('now','+7 days')
                        ''')
            rows=cur.fetchall()
            r=1#row count for writing
            for row in rows:
                due.write(r,0,row[0])
                due.write(r,1,row[1])
                due.write(r,2,row[2])
                due.write(r,3,row[3])
                r=r+1
            cur.execute('''
                        SELECT p_name,p_no FROM Plan_data
                        ''')
            ls=[]
            l=cur.fetchall()
            for x in range(len(l)):
                ls.append((str(l[x][0]),l[x][1]))
            print(ls)    
            for name in ls:    
                wb=workbook.add_worksheet('{}'.format(name[0]))
                wb.set_column(1,3,25)
                wb.write(0,0,'name')
                wb.write(0,1,'date')
                wb.write(0,2,'intime')
                wb.write(0,3,'image')
                cur.execute('''
                             SELECT Client_data.name,Attendance.date,Attendance.TIME,Client_data.c_id
                             FROM Client_data,Attendance
                             WHERE Client_data.c_id=Attendance.c_id AND Attendance.date>=date('now','-7 days') AND Client_data.p_no={}
                             ORDER BY Client_data.c_id
                            '''.format(name[1]))
                rows=cur.fetchall()
                r=1
                for i in range(len(rows)):
                    wb.set_row(r,175)
                    wb.write(r,0,rows[i][0])
                    wb.write(r,1,rows[i][1])
                    wb.write(r,2,rows[i][2])
                    if(i==0):
                       cur.execute('''
                                SELECT count(*),strftime('%m',date)
                                FROM Attendance 
                                WHERE  strftime('%Y',date)=strftime('%Y','now') AND Attendance.c_id={}
                                GROUP BY strftime('%m',date);
                               '''.format(rows[i][3]))
                       temp=cur.fetchall()
                       uid=rows[i][3]
                       frequency=[]
                       month=[]
                       for x in range(len(temp)):
                           frequency.append(temp[x][0])
                           month.append(temp[x][1])
                       month=tuple(month)
                       print(month,frequency,uid)
                       imgpath=bargraph.plot(month,frequency,uid)
                       wb.insert_image(r,3,imgpath)

                    if(rows[i][3]!=rows[i-1][3] and i!=0):
                        cur.execute('''
                                SELECT count(*),strftime('%m',date)
                                FROM Attendance 
                                WHERE  strftime('%Y',date)=strftime('%Y','now') AND Attendance.c_id={}
                                GROUP BY strftime('%m',date);
                               '''.format(rows[i][3]))
                        temp=cur.fetchall()
                        uid=rows[i][3]
                        frequency=[]
                        month=[]
                        for x in range(len(temp)):
                            frequency.append(temp[x][0])
                            month.append(temp[x][1])
                        month=tuple(month)
                        print(month,frequency,uid)
                        imgpath=bargraph.plot(month,frequency,uid)
                        wb.insert_image(r,3,imgpath)
                    r=r+1
            
            absent=workbook.add_worksheet('absent')
            absent.set_column(1,3,25)
            absent.write(0,0,'name')
            absent.write(0,1,'phone')
            absent.write(0,2,'plan name')
            absent.write(0,3,'image')
            cur.execute('''
                         SELECT Client_data.name,Client_data.m_no,Plan_data.p_name,Client_data.c_id
                         FROM Client_data,Plan_data
                         WHERE Client_data.p_no=Plan_data.p_no AND Client_data.name NOT IN(SELECT Client_data.name
                         FROM Client_data,Attendance
                         WHERE Client_data.c_id=Attendance.c_id AND Attendance.date>=date('now','-7 days'))                    ''')
            rows=cur.fetchall()
            r=1
            for i in range(len(rows)):
                absent.set_row(r,175)
                absent.write(r,0,rows[i][0])
                absent.write(r,1,rows[i][1])
                absent.write(r,2,rows[i][2])
                cur.execute('''
                        SELECT count(*),strftime('%m',date)
                        FROM Attendance 
                        WHERE  strftime('%Y',date)=strftime('%Y','now') AND Attendance.c_id={}
                        GROUP BY strftime('%m',date);
                       '''.format(rows[i][3]))
                temp=cur.fetchall()
                uid=rows[i][3]
                frequency=[]
                month=[]
                for x in range(len(temp)):
                    frequency.append(temp[x][0])
                    month.append(temp[x][1])
                month=tuple(month)
                print(month,frequency,uid)
                imgpath=bargraph.plot(month,frequency,uid)
                absent.insert_image(r,3,imgpath)
                r=r+1    
            test=workbook.add_worksheet('test')
            test.set_column(1,3,25)
            test.write(0,0,'name')
            test.write(0,1,'phone')
            test.write(0,2,'plan name')
            test.write(0,3,'barbell')
            test.write(0,4,'dumbell')
            test.write(0,5,'time')
            test.write(0,6,'repetitions')
            test.write(0,7,'modified')
            test.write(0,8,'date')
            cur.execute('''
                        SELECT Client_data.name,Client_data.m_no,Plan_data.p_name,testday.barbell,testday.dumbell,testday.time,testday.repetitions,testday.modified,testday.date
                        FROM Client_data,Plan_data,testday
                        WHERE Client_data.c_id=testday.c_id AND testday.date>=date('now','-7 days') AND Client_data.p_no=Plan_data.p_no
                        ''')
            rows=cur.fetchall()
            r=1
            for i in range(len(rows)):
                for j in range(9):
                    test.set_row(r,20)
                    if(j==7):
                        if(rows[i][j]==1):
                            test.write(r,j,'yes')
                            continue
                        else:
                            test.write(r,j,'no')
                            continue
                    test.write(r,j,rows[i][j])
                r=r+1
            workbook.close()
def first():
    dbfun()
    if(datetime.datetime.today().strftime("%A")=='Saturday'):
        report_fun()
    app=QApplication(sys.argv)
    widget=LoginPage()
    widget.show()
    sys.exit(app.exec_())
