from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QTableWidgetItem 
from GUIDaftarTelepon import Ui_MainWindow
import sys
import sqlite3 as sql
import os 
os.system('python Connection.py')
os.system('python CreateTable.py')

global id, nama, marga, kota, telepon, email

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()  
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)     

        self.btnDaftarClick()
        self.ui.btnDaftar.clicked.connect(self.btnDaftarClick)
        self.ui.btnSimpan.clicked.connect(self.btnSimpanClick)
        self.ui.btnHapus.clicked.connect(self.btnHapusClick)
        self.ui.btnPerbarui.clicked.connect(self.btnPerbaruiClick)
        self.ui.tblDaftar.clicked.connect(self.ListOnClick) 
 
    def btnReset(self):
        self.ui.txtID.clear()
        self.ui.txtNama.clear()
        self.ui.txtMarga.clear()
        self.ui.txtKota.clear()
        self.ui.txtTelepon.clear()
        self.ui.txtEmail.clear()

    def ListOnClick(self): 
        self.ui.txtID.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 0).text())
        self.ui.txtNama.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 1).text())
        self.ui.txtMarga.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 2).text())
        self.ui.txtKota.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 3).text())
        self.ui.txtTelepon.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 4).text())
        self.ui.txtEmail.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 5).text())
 
    def btnSimpanClick(self): 
        id = self.ui.txtID.text()
        nama = self.ui.txtNama.text()
        marga = self.ui.txtMarga.text()
        kota = self.ui.txtKota.text()
        telepon = self.ui.txtTelepon.text()
        email = self.ui.txtEmail.text()

        try:
            self.conn = sql.connect("DaftarTelepon.db")
            self.c = self.conn.cursor() 
            self.c.execute('INSERT INTO "Pengguna" VALUES (?,?,?,?,?,?)',(id,nama,marga,kota,telepon,email))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User is added successfully to the database.')
        except Exception:
            print('Error', 'Could not add student to the database.')
        
        self.btnReset()
        self.btnDaftarClick()

    def btnDaftarClick(self):  
        self.ui.tblDaftar.clear()
        self.ui.tblDaftar.setColumnCount(6)
        self.ui.tblDaftar.setHorizontalHeaderLabels(('ID','Nama','Marga','Kota','Telepon','Email'))
        self.ui.tblDaftar.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        db = sql.connect('DaftarTelepon.db')
        cur = db.cursor()
        selectquery = "SELECT * FROM Pengguna"
        cur.execute(selectquery) 
        rows = cur.fetchall()
         
        self.ui.tblDaftar.setRowCount(len(rows))
        
        for barisIndeks, barisData in enumerate(rows):
            for kolomIndeks, kolomData in enumerate (barisData):
                self.ui.tblDaftar.setItem(barisIndeks,kolomIndeks,QTableWidgetItem(str(kolomData))) 
    
    def btnPerbaruiClick(self):  
        id = self.ui.txtID.text()
        nama = self.ui.txtNama.text()
        marga = self.ui.txtMarga.text()
        kota = self.ui.txtKota.text()
        telepon = self.ui.txtTelepon.text()
        email = self.ui.txtEmail.text()

        try:
            self.conn = sql.connect("DaftarTelepon.db")
            self.c = self.conn.cursor()  
            self.c.execute("UPDATE Pengguna SET Nama = ?, Marga = ?, Kota = ?, \
                Telepon = ?, Email = ? WHERE id = ?",(nama,marga,kota,telepon,email,id))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User is updated successfully to the database.')
        except Exception:
            print('Error', 'Could not update student to the database.')

        self.btnReset()
        self.btnDaftarClick()

    def btnHapusClick(self): 
        id = self.ui.txtID.text() 

        try:
            self.conn = sql.connect("DaftarTelepon.db")
            self.c = self.conn.cursor() 
            self.c.execute('DELETE FROM Pengguna WHERE id = ?  ', (id,))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User is deleted successfully from the database.')
        except Exception:
            print('Error', 'Could not delete student to the database.')
        
        self.btnReset()
        self.btnDaftarClick()

            
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()