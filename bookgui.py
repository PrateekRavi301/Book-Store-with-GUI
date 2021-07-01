# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookstoregui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(140, 20, 221, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txttitle = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.txttitle.setObjectName("txttitle")
        self.txttitle.textChanged.connect(self.bookvalue)
        self.horizontalLayout.addWidget(self.txttitle)
        self.btnprice = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btnprice.setFont(font)
        self.btnprice.setAutoDefault(False)
        self.btnprice.setDefault(True)
        self.btnprice.setFlat(False)
        self.btnprice.setObjectName("btnprice")
        self.btnprice.setCheckable(True)
        self.btnprice.clicked.connect(self.btnstate)
        self.horizontalLayout.addWidget(self.btnprice)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 111, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(140, 100, 221, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblprice = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.lblprice.setText("")
        self.lblprice.setObjectName("lblprice")
        self.horizontalLayout_2.addWidget(self.lblprice)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(140, 170, 221, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.txtqty = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.txtqty.setObjectName("txtqty")
        
        validator = QtGui.QIntValidator()
        self.txtqty.setValidator(validator)
        self.horizontalLayout_3.addWidget(self.txtqty)
        self.btntotal = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btntotal.setFont(font)
        self.btntotal.setAutoDefault(False)
        self.btntotal.setDefault(True)
        self.btntotal.setFlat(False)
        self.btntotal.setObjectName("btntotal")
        self.btntotal.setCheckable(True)
        self.btntotal.clicked.connect(self.btnstate)
        self.horizontalLayout_3.addWidget(self.btntotal)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(140, 240, 221, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbltotal = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.lbltotal.setText("")
        self.lbltotal.setObjectName("lbltotal")
        self.horizontalLayout_4.addWidget(self.lbltotal)
        self.btnreset = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnreset.setFont(font)
        self.btnreset.setDefault(True)
        self.btnreset.setObjectName("btnreset")
        self.horizontalLayout_4.addWidget(self.btnreset)

        self.retranslateUi(Form)
        
        self.btnreset.clicked.connect(self.txtqty.clear)
        self.btnreset.clicked.connect(self.lblprice.clear)
        self.btnreset.clicked.connect(self.lbltotal.clear)
        self.btnreset.clicked.connect(self.txttitle.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnprice.setText(_translate("Form", "Find Price"))
        self.label_2.setText(_translate("Form", "Book Title"))
        self.label_3.setText(_translate("Form", "Price"))
        self.label_4.setText(_translate("Form", "Quantity"))
        self.label.setText(_translate("Form", "Total"))
        self.btntotal.setText(_translate("Form", "Find Total"))
        self.btnreset.setText(_translate("Form", "RESET"))
    
    def btnstate(self):
        if self.btnprice.isChecked():
            bprice=self.findprice(self.txttitle.text())
            if type(bprice)==float:
                self.lblprice.setText("Rs."+str(bprice))
            else:
                self.lblprice.setText(bprice)              
        if self.btntotal.isChecked():
            self.lbltotal.setText("Rs."+str(int(self.txtqty.text())*float(bprice)))
            
    def findprice(self,btitle):
        btitle=str(btitle)
        MyStore=sqlite3.connect('mybookstore.db')
        curstore=MyStore.cursor()
        try:
            curstore.execute("select * from books where title= '"+btitle+"';")
            record=curstore.fetchone()
            return record[3]
            
        except:
            return "Enter Correct Title!"
        MyStore.close()         

    def bookvalue(self):
        btitle=self.txttitle.text()
        
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())



    
