from PyQt6 import QtCore, QtGui, QtWidgets
from Database.DBConnect import DbManager
from Controller.quanlykhachhang import CustomerManager  

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(675, 470)
        Form.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(200, 10, 311, 31))
        self.frame.setStyleSheet("background-color:rgb(170, 170, 255); border-radius: 5px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(70, 0, 201, 31))
        self.label.setStyleSheet("font: 75 16pt 'Times New Roman'; color: white;")
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 151, 21))
        self.label_2.setStyleSheet("font: 11pt 'Times New Roman'; font-weight: bold;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(50, 80, 61, 21))
        self.label_3.setStyleSheet("font: 10pt 'Times New Roman'; font-weight: bold;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(50, 120, 61, 21))
        self.label_4.setStyleSheet("font: 10pt 'Times New Roman'; font-weight: bold;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(50, 160, 71, 21))
        self.label_5.setStyleSheet("font: 10pt 'Times New Roman'; font-weight: bold;")
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 80, 101, 20))
        self.lineEdit.setStyleSheet("border: 1px solid #aaa; border-radius: 5px; padding: 5px; font: 10pt 'Times New Roman';")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 120, 191, 20))
        self.lineEdit_2.setStyleSheet("border: 1px solid #aaa; border-radius: 5px; padding: 5px; font: 10pt 'Times New Roman';")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(410, 70, 61, 21))
        self.label_6.setStyleSheet("font: 10pt 'Times New Roman'; font-weight: bold;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(410, 120, 61, 21))
        self.label_7.setStyleSheet("font: 10pt 'Times New Roman'; font-weight: bold;")
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(470, 70, 111, 20))
        self.lineEdit_3.setStyleSheet("border: 1px solid #aaa; border-radius: 5px; padding: 5px; font: 10pt 'Times New Roman';")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(470, 120, 191, 20))
        self.lineEdit_4.setStyleSheet("border: 1px solid #aaa; border-radius: 5px; padding: 5px; font: 10pt 'Times New Roman';")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.btnAddKH = QtWidgets.QPushButton(parent=Form)
        self.btnAddKH.setGeometry(QtCore.QRect(130, 200, 61, 31))
        self.btnAddKH.setStyleSheet("""
            background-color: rgb(185, 219, 255);
            border: 1px solid #aaa;
            border-radius: 5px;
            padding: 5px;
            font: 10pt 'Times New Roman';
            font-weight: bold;
        """)
        self.btnAddKH.setObjectName("btnAddKH")
        self.btnDeleteKH = QtWidgets.QPushButton(parent=Form)
        self.btnDeleteKH.setGeometry(QtCore.QRect(260, 200, 61, 31))
        self.btnDeleteKH.setStyleSheet("""
            background-color: rgb(185, 219, 255);
            border: 1px solid #aaa;
            border-radius: 5px;
            padding: 5px;
            font: 10pt 'Times New Roman';
            font-weight: bold;
        """)
        self.btnDeleteKH.setObjectName("btnDeleteKH")
        self.btnEditKH = QtWidgets.QPushButton(parent=Form)
        self.btnEditKH.setGeometry(QtCore.QRect(380, 200, 61, 31))
        self.btnEditKH.setStyleSheet("""
            background-color: rgb(185, 219, 255);
            border: 1px solid #aaa;
            border-radius: 5px;
            padding: 5px;
            font: 10pt 'Times New Roman';
            font-weight: bold;
        """)
        self.btnEditKH.setObjectName("btnEditKH")
        self.dateEdit = QtWidgets.QDateEdit(parent=Form)
        self.dateEdit.setGeometry(QtCore.QRect(140, 160, 111, 22))
        self.dateEdit.setStyleSheet("border: 1px solid #aaa; border-radius: 5px; padding: 5px; font: 10pt 'Times New Roman';")
        self.dateEdit.setObjectName("dateEdit")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(0, 240, 681, 231))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 681, 231))  # Điều chỉnh kích thước của TableWidget
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)  # Kéo dài các cột
        self.tableWidget.setStyleSheet("""
            font: 10pt 'Times New Roman';
            border: 1px solid #aaa;
        """)
        self.btnAddKH.clicked.connect(self.add_record)
        self.btnEditKH.clicked.connect(self.edit_record)
        self.btnDeleteKH.clicked.connect(self.delete_record)
        self.tableWidget.cellClicked.connect(self.display_record)
        self.retranslateUi(Form)
        self.loaddata()
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def loaddata(self):
        db = DbManager()
        customer_manager = CustomerManager()  # Initialize CustomerManager
        result = customer_manager.fetch_all_customers()  # Fetch all customers from database
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # Căn giữa văn bản
                self.tableWidget.setItem(row_number, column_number, item)
        self.tableWidget.resizeColumnsToContents()
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Customer Management"))
        self.label.setText(_translate("Form", "Quản lý khách hàng"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Thông tin khách hàng</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Mã KH :</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tên KH :</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Ngày sinh :</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">SDT :</span></p><p><br/></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Địa Chỉ :</span></p></body></html>"))
        self.btnAddKH.setText(_translate("Form", "Thêm KH"))
        self.btnDeleteKH.setText(_translate("Form", "Xóa KH"))
        self.btnEditKH.setText(_translate("Form", "Sửa KH"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Mã KH"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Tên KH"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Ngày Sinh"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "SĐT"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Địa chỉ"))
    
    def add_record(self):
        idkhachhang = self.lineEdit.text()
        name = self.lineEdit_2.text()
        ngaysinh = self.dateEdit.date().toString('yyyy-MM-dd')
        sdt = self.lineEdit_3.text()
        diachi = self.lineEdit_4.text()

        if not idkhachhang or not name or not sdt or not diachi:
            QtWidgets.QMessageBox.warning(None, 'Cảnh báo', 'Vui lòng điền vào tất cả các trường')
            return

        customer_manager = CustomerManager()  # Initialize CustomerManager
        try:
            customer_manager.add_customer(idkhachhang, name, ngaysinh, sdt, diachi)
            QtWidgets.QMessageBox.information(None, 'Thông báo', 'Thêm khách hàng thành công')
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, 'Error', str(e))
        self.loaddata()

    def edit_record(self):
        idkhachhang = self.lineEdit.text()
        name = self.lineEdit_2.text()
        ngaysinh = self.dateEdit.date().toString('yyyy-MM-dd')
        sdt = self.lineEdit_3.text()
        diachi = self.lineEdit_4.text()

        if not idkhachhang or not name or not sdt or not diachi:
            QtWidgets.QMessageBox.warning(None, 'Cảnh báo','Vui lòng điền vào tất cả các trường')
            return

        customer_manager = CustomerManager()  # Initialize CustomerManager
        try:
            customer_manager.update_customer(idkhachhang, name, ngaysinh, sdt, diachi)
            QtWidgets.QMessageBox.information(None, 'Thông báo', 'Cập nhật thông tin khách hàng thành công')
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, 'Error', str(e))
        self.loaddata()

    def delete_record(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(None, 'Cảnh báo', 'Vui lòng chọn một bản ghi để xóa')
            return

        idkhachhang_item = self.tableWidget.item(selected_row, 0)
        idkhachhang = idkhachhang_item.text()

        customer_manager = CustomerManager()  # Initialize CustomerManager
        try:
            customer_manager.delete_customer(idkhachhang)
            QtWidgets.QMessageBox.information(None, 'Thông báo', 'Xóa khách hàng thành công')
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, 'Error', str(e))
        self.loaddata()

    def display_record(self, row, column):
        self.lineEdit.setText(self.tableWidget.item(row, 0).text())
        self.lineEdit_2.setText(self.tableWidget.item(row, 1).text())
        self.dateEdit.setDate(QtCore.QDate.fromString(self.tableWidget.item(row, 2).text(), 'yyyy-MM-dd'))
        self.lineEdit_3.setText(self.tableWidget.item(row, 3).text())
        self.lineEdit_4.setText(self.tableWidget.item(row, 4).text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
