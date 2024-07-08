from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector
from PyQt6.QtWidgets import QMessageBox
from QLKH import Ui_Form as Ui_Form_KH
from HĐ import Ui_Form as Ui_Form_HD
from muontra import Ui_Form as Ui_Form_MT
from QLcacgoidv import Ui_Form as Ui_Form_CGDV
from QLLichHen import Ui_Form as Ui_Form_LH
from QLBaogia import Ui_Form as Ui_Form_BG
from thongke import StatisticsForm

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(879, 550)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 0, 171, 501))
        self.widget.setStyleSheet("background-color: rgb(217, 238, 255);")
        self.widget.setObjectName("widget")

        # Define button style with border
        button_style = """
            QPushButton {
                background-color: rgb(127, 147, 160);
                border: 2px solid black;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:checked {
                background-color: rgb(107, 127, 140);
            }
        """

        self.btnKH = QtWidgets.QPushButton(parent=self.widget)
        self.btnKH.setGeometry(QtCore.QRect(20, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnKH.setFont(font)
        self.btnKH.setStyleSheet(button_style)
        self.btnKH.setCheckable(True)
        self.btnKH.setAutoExclusive(True)
        self.btnKH.setObjectName("btnKH")

        self.btnGoidv = QtWidgets.QPushButton(parent=self.widget)
        self.btnGoidv.setGeometry(QtCore.QRect(20, 70, 131, 31))
        self.btnGoidv.setFont(font)
        self.btnGoidv.setStyleSheet(button_style)
        self.btnGoidv.setCheckable(True)
        self.btnGoidv.setAutoExclusive(True)
        self.btnGoidv.setObjectName("btnGoidv")

        self.btnBaogia = QtWidgets.QPushButton(parent=self.widget)
        self.btnBaogia.setGeometry(QtCore.QRect(20, 170, 131, 31))
        self.btnBaogia.setFont(font)
        self.btnBaogia.setStyleSheet(button_style)
        self.btnBaogia.setCheckable(True)
        self.btnBaogia.setAutoExclusive(True)
        self.btnBaogia.setObjectName("btnBaogia")

        self.btnThoat = QtWidgets.QPushButton(parent=self.widget)
        self.btnThoat.setGeometry(QtCore.QRect(40, 450, 91, 21))
        self.btnThoat.setFont(font)
        self.btnThoat.setStyleSheet(button_style)
        self.btnThoat.setCheckable(True)
        self.btnThoat.setAutoExclusive(True)
        self.btnThoat.setObjectName("btnThoat")

        self.btlLichhen = QtWidgets.QPushButton(parent=self.widget)
        self.btlLichhen.setGeometry(QtCore.QRect(20, 220, 131, 31))
        self.btlLichhen.setFont(font)
        self.btlLichhen.setStyleSheet(button_style)
        self.btlLichhen.setCheckable(True)
        self.btlLichhen.setAutoExclusive(True)
        self.btlLichhen.setObjectName("btlLichhen")

        self.btnThuetra = QtWidgets.QPushButton(parent=self.widget)
        self.btnThuetra.setGeometry(QtCore.QRect(20, 270, 131, 31))
        self.btnThuetra.setFont(font)
        self.btnThuetra.setStyleSheet(button_style)
        self.btnThuetra.setCheckable(True)
        self.btnThuetra.setAutoExclusive(True)
        self.btnThuetra.setObjectName("btnThuetra")

        self.btnThanhtoan = QtWidgets.QPushButton(parent=self.widget)
        self.btnThanhtoan.setGeometry(QtCore.QRect(20, 320, 131, 31))
        self.btnThanhtoan.setFont(font)
        self.btnThanhtoan.setStyleSheet(button_style)
        self.btnThanhtoan.setCheckable(True)
        self.btnThanhtoan.setAutoExclusive(True)
        self.btnThanhtoan.setObjectName("btnThanhtoan")

        self.btnThongke = QtWidgets.QPushButton(parent=self.widget)
        self.btnThongke.setGeometry(QtCore.QRect(20, 370, 131, 31))
        self.btnThongke.setFont(font)
        self.btnThongke.setStyleSheet(button_style)
        self.btnThongke.setCheckable(True)
        self.btnThongke.setAutoExclusive(True)
        self.btnThongke.setObjectName("btnThongke")

        self.widget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(190, 0, 701, 501))
        self.widget_2.setStyleSheet("background-color: rgb(222, 249, 255);")
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(130, 0, 561, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=self.widget_2)
        self.label.setGeometry(QtCore.QRect(50, 50, 611, 391))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/2.jpg"))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 879, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btnGoidv.clicked.connect(self.openGoidv)   
        self.btnKH.clicked.connect(self.openKH)
        self.btnBaogia.clicked.connect(self.openBaogia)
        self.btlLichhen.clicked.connect(self.openLichhen)
        self.btnThuetra.clicked.connect(self.openThuetra)
        self.btnThanhtoan.clicked.connect(self.openThanhtoan)
        self.btnThongke.clicked.connect(self.openThongke)
    def openThongke(self):
        self.statisticsWindow = QtWidgets.QWidget()  # Bước 1: Sử dụng thuộc tính của lớp
        self.ui = StatisticsForm()
        self.ui.setupUi(self.statisticsWindow)  # Bước 2: Gán cửa sổ mới vào thuộc tính
        self.statisticsWindow.show()  # Bước 3: Hiển thị cửa sổ
        self.btnThoat.clicked.connect(self.openThoat)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnKH.setText(_translate("MainWindow", "KHÁCH HÀNG"))
        self.btnGoidv.setText(_translate("MainWindow", "CÁC GÓI DỊCH VỤ"))
        self.btnBaogia.setText(_translate("MainWindow", "BÁO GIÁ"))
        self.btnThoat.setText(_translate("MainWindow", "Logout"))
        self.btlLichhen.setText(_translate("MainWindow", "LỊCH HẸN"))
        self.btnThuetra.setText(_translate("MainWindow", "THUÊ TRẢ"))
        self.btnThanhtoan.setText(_translate("MainWindow", "THANH TOÁN "))
        self.btnThongke.setText(_translate("MainWindow", "THỐNG KÊ"))
        self.label_2.setText(_translate("MainWindow", "CỬA HÀNG DỊCH VỤ CHO THUÊ ÁO CƯỚI"))
    def openGoidv(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_CGDV()
        self.ui.setupUi(self.window)
        self.window.show()
    def openKH(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_KH()
        self.ui.setupUi(self.window)
        self.window.show()
    def openBaogia(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_BG()
        self.ui.setupUi(self.window)
        self.window.show()
    def openLichhen(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_LH()
        self.ui.setupUi(self.window)
        self.window.show()
    def openThuetra(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_MT()
        self.ui.setupUi(self.window)
        self.window.show()
    def openThanhtoan(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_HD()
        self.ui.setupUi(self.window)
        self.window.show()
    def openThongke(self):
        self.statisticsWindow = QtWidgets.QWidget()  # Bước 1: Sử dụng thuộc tính của lớp
        self.ui = StatisticsForm()
        self.ui.show()  # Bước 3: Hiển thị cửa sổ
    def openThoat(self):
       QtWidgets.QApplication.instance().quit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
