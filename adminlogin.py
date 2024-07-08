from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import Error
from home import Ui_MainWindow as HomeWindow
from Database.DBConnect import DbManager
from Model.admin import admin

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainWindow = MainWindow

        # Set background image
        palette = QtGui.QPalette()
        #thêm ảnh background
        #palette.setBrush(QtGui.QPalette.ColorRole.Window, QtGui.QBrush(QtGui.QPixmap("img.jpg")))
        MainWindow.setPalette(palette)

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 120, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 180, 47, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 190, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 290, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        
        # Apply stylesheet for the pushButton
        self.pushButton.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; /* Green background */
                color: white; /* White text */
                border-radius: 10px; /* Rounded corners */
                border: 2px solid #4CAF50; /* Green border */
                padding: 10px 20px; /* Padding inside the button */
            }
            QPushButton:hover {
                background-color: #45a049; /* Darker green when hovered */
            }
        """)

        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 30, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 120, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
# Apply stylesheet for lineEdit (Username)
        self.lineEdit.setStyleSheet("""
            QLineEdit {
                border-radius: 10px; /* Rounded corners */
                border: 2px solid #4CAF50; /* Green border */
                padding: 5px; /* Padding inside the input */
            }
        """)

        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 190, 221, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # Hide password input
        
        # Apply stylesheet for lineEdit_2 (Password)
        self.lineEdit_2.setStyleSheet("""
            QLineEdit {
                border-radius: 10px; /* Rounded corners */
                border: 2px solid #4CAF50; /* Green border */
                padding: 5px; /* Padding inside the input */
            }
        """)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the login button to the login function
        self.pushButton.clicked.connect(self.login)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login Form"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Log in"))
        self.label_4.setText(_translate("MainWindow", "ADMIN"))

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        admin_login = admin(username, password)
        success = admin_login.login()

        if success:
            self.window = QtWidgets.QMainWindow()
            self.ui = HomeWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            self.MainWindow.close()
        else:
            QtWidgets.QMessageBox.warning(None, 'Error', 'Đăng nhập thất bại. Vui lòng thử lại.')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)  # Pass MainWindow instance
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
