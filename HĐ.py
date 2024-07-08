from PyQt6 import QtCore, QtGui, QtWidgets
from Database.DBConnect import DbManager
from Controller.hoadon import QLHD
import xlsxwriter 

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Hóa Đơn")
        Form.resize(700, 600)  # Tăng kích thước form để phù hợp với các widget

        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(200, 10, 311, 31))
        self.frame.setStyleSheet("background-color: rgb(170, 170, 255);")  # Background color for the header
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 0, 201, 31))
        self.label_2.setStyleSheet("font: 75 16pt 'Times New Roman'; color: white;")  # Font style and color for the header label
        self.label_2.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 71, 21))
        self.label_3.setStyleSheet("font: 10pt 'Times New Roman';")  # Font style for labels
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(60, 100, 101, 21))
        self.label_4.setStyleSheet("font: 10pt 'Times New Roman';")  # Font style for labels
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(60, 140, 101, 21))
        self.label_5.setStyleSheet("font: 10pt 'Times New Roman';")  # Font style for labels
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(60, 180, 141, 21))
        self.label_6.setStyleSheet("font: 10pt 'Times New Roman';")  # Font style for labels
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(390, 100, 101, 21))
        self.label_7.setStyleSheet("font: 10pt 'Times New Roman';")  # Font style for labels
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setGeometry(QtCore.QRect(390, 140, 101, 21))
        self.label_8.setStyleSheet("font: 10pt 'Times New Roman';")  # Font style for labels
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(parent=Form)
        self.label_9.setGeometry(QtCore.QRect(390, 180, 121, 21))
        self.label_9.setStyleSheet("font: 10pt 'Times New Roman';")  # Font style for labels
        self.label_9.setObjectName("label_9")

        # Update the size for QLineEdit and QDateEdit to make them more visible
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(200, 100, 150, 25))  # Increase width and adjust height
        self.lineEdit.setStyleSheet("border: 1px solid #C0C0C0; border-radius: 5px; padding: 5px;")  # Border and padding for lineEdit
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 140, 150, 25))  # Increase width and adjust height
        self.lineEdit_2.setStyleSheet("border: 1px solid #C0C0C0; border-radius: 5px; padding: 5px;")  # Border and padding for lineEdit
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.dateEdit = QtWidgets.QDateEdit(parent=Form)
        self.dateEdit.setGeometry(QtCore.QRect(200, 180, 150, 25))  # Increase width and adjust height
        self.dateEdit.setStyleSheet("border: 1px solid #C0C0C0; border-radius: 5px; padding: 5px;")  # Border and padding for dateEdit
        self.dateEdit.setObjectName("dateEdit")

        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(510, 100, 150, 25))  # Increase width and adjust height
        self.lineEdit_3.setStyleSheet("border: 1px solid #C0C0C0; border-radius: 5px; padding: 5px;")  # Border and padding for lineEdit
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(510, 140, 150, 25))  # Increase width and adjust height
        self.lineEdit_4.setStyleSheet("border: 1px solid #C0C0C0; border-radius: 5px; padding: 5px;")  # Border and padding for lineEdit
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.spinBox = QtWidgets.QSpinBox(parent=Form)
        self.spinBox.setGeometry(QtCore.QRect(510, 180, 60, 25))  # Increase height to match other widgets
        self.spinBox.setStyleSheet("border: 1px solid #C0C0C0; border-radius: 5px; padding: 5px;")  # Border and padding for spinBox
        self.spinBox.setObjectName("spinBox")

        self.btnAddHD = QtWidgets.QPushButton(parent=Form)
        self.btnAddHD.setGeometry(QtCore.QRect(150, 230, 100, 35))  # Increase size of the button
        self.btnAddHD.setStyleSheet("""
            background-color: #2196F3; 
            color: white; 
            border: none; 
            border-radius: 5px; 
            padding: 5px;
            font: 10pt 'Times New Roman';
        """)  # Styling for the "Add" button
        self.btnAddHD.setObjectName("btnAddHD")

        self.btnXuatHD = QtWidgets.QPushButton(parent=Form)
        self.btnXuatHD.setGeometry(QtCore.QRect(270, 230, 100, 35))  # Increase size of the button
        self.btnXuatHD.setStyleSheet("""
            background-color: #2196F3; 
            color: white; 
            border: none; 
            border-radius: 5px; 
            padding: 5px;
            font: 10pt 'Times New Roman';
        """)  # Styling for the "Export" button
        self.btnXuatHD.setObjectName("btnXuatHD")

        self.btnEditHD = QtWidgets.QPushButton(parent=Form)
        self.btnEditHD.setGeometry(QtCore.QRect(390, 230, 100, 35))  # Increase size of the button
        self.btnEditHD.setStyleSheet("""
            background-color: #2196F3; 
            color: white; 
            border: none; 
            border-radius: 5px; 
            padding: 5px;
            font: 10pt 'Times New Roman';
        """)  # Styling for the "Edit" button
        self.btnEditHD.setObjectName("btnEditHD")

        self.tableHD = QtWidgets.QTableWidget(parent=Form)
        self.tableHD.setGeometry(QtCore.QRect(10, 280, 680, 290))  # Increase size of the table
        self.tableHD.setObjectName("tableHD")
        self.tableHD.setColumnCount(6)
        self.tableHD.setRowCount(0)

        # Set column widths
        self.tableHD.setColumnWidth(0, 100)  # Adjust the column width as needed
        self.tableHD.setColumnWidth(1, 100)
        self.tableHD.setColumnWidth(2, 100)
        self.tableHD.setColumnWidth(3, 100)
        self.tableHD.setColumnWidth(4, 100)
        self.tableHD.setColumnWidth(5, 100)

        # Set table headers
        self.tableHD.setHorizontalHeaderLabels(["Mã HD", "Khách Hàng", "Ngày", "Số Lượng", "Giá", "Tổng"])

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.btnAddHD.clicked.connect(self.add_hd)
        self.btnEditHD.clicked.connect(self.edit_hd)
        self.tableHD.cellClicked.connect(self.display)
        self.btnXuatHD.clicked.connect(self.export_txt)
        
        self.spinBox.valueChanged.connect(self.update_total_price)  # Connect spinBox value change to update total price

        self.load_data()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setToolTip(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Thông tin Hóa Đơn</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Hóa đơn</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Mã hóa đơn :</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Khách Hàng :</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Ngày lập hóa đơn :</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Nhân viên :</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Tổng tiền :</span></p></body></html>"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Tổng số lượng :</span></p></body></html>"))
        self.btnAddHD.setText(_translate("Form", "Thêm hóa đơn"))
        self.btnXuatHD.setText(_translate("Form", "Xuất hóa đơn"))
        self.btnEditHD.setText(_translate("Form", "Sửa hóa đơn"))
        item = self.tableHD.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Mã hóa đơn"))
        item = self.tableHD.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Khách hàng"))
        item = self.tableHD.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Ngày lập hóa đơn"))
        item = self.tableHD.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Nhân viên"))
        item = self.tableHD.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Tổng tiền"))
        item = self.tableHD.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Tổng số lượng"))

    def load_data(self):
        qlhd = QLHD()
        data = qlhd.fetch_all_hd()
        self.tableHD.setRowCount(0)
        for row_number, row_data in enumerate(data):
            self.tableHD.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableHD.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def add_hd(self):
        mahd = self.lineEdit.text()
        name = self.lineEdit_2.text()
        ngaylapHD = self.dateEdit.date().toString("yyyy-MM-dd")
        usernameNV = self.lineEdit_3.text()
        tongtien = self.lineEdit_4.text().replace(',', '')  # Remove commas for SQL query
        soluong = self.spinBox.text()

        db = DbManager()
        conn = db.getConnection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO hoa_don (mahd, name, ngaylapHD, usernameNV, tongtien, soluong) VALUES (%s, %s, %s, %s, %s, %s)",
                (mahd, name, ngaylapHD, usernameNV, tongtien, soluong))
            conn.commit()
            QtWidgets.QMessageBox.information(None, "Thông báo", "Thêm hóa đơn thành công")
            self.load_data()
        except Exception as e:
            conn.rollback()
            QtWidgets.QMessageBox.critical(None, "Thông báo", f"Thêm hóa đơn thất bại: {str(e)}")
        finally:
            db.closeConnection()

    def export_txt(self):
        try:
            workbook = xlsxwriter.Workbook('DanhSachHD.xlsx')
            worksheet = workbook.add_worksheet()
            headers = ["Mã hóa đơn", "Khách hàng", "Ngày lập hóa đơn", "Nhân viên", "Tổng tiền", "Tổng số lượng"]
            
            # Write headers
            for col, header in enumerate(headers):
                worksheet.write(0, col, header)
                
            # Write data
            for row in range(self.tableHD.rowCount()):
                for col in range(self.tableHD.columnCount()):
                    item = self.tableHD.item(row, col)
                    if item is not None:
                        worksheet.write(row + 1, col, item.text())
            
            # Adjust column widths
            column_widths = [len(header) for header in headers]
            for row_num in range(self.tableHD.rowCount()):
                for col_num in range(self.tableHD.columnCount()):
                    cell_data = self.tableHD.item(row_num, col_num).text()
                    column_widths[col_num] = max(column_widths[col_num], len(cell_data))
            for col_num, width in enumerate(column_widths):
                worksheet.set_column(col_num, col_num, width + 2)
            
            workbook.close()
            QtWidgets.QMessageBox.information(None, "Thông báo", "Xuất file thành công")
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Thông báo", f"Xuất file thất bại: {str(e)}")

    def edit_hd(self):
        mahd = self.lineEdit.text()
        name = self.lineEdit_2.text()
        ngaylapHD = self.dateEdit.date().toString("yyyy-MM-dd")
        usernameNV = self.lineEdit_3.text()
        tongtien = self.lineEdit_4.text().replace(',', '')  # Remove commas for SQL query
        soluong = self.spinBox.text()

        db = DbManager()
        conn = db.getConnection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE hoa_don SET name=%s, ngaylapHD=%s, usernameNV=%s, tongtien=%s, soluong=%s WHERE mahd=%s",
                (name, ngaylapHD, usernameNV, tongtien, soluong, mahd))
            conn.commit()
            QtWidgets.QMessageBox.information(None, "Thông báo", "Sửa hóa đơn thành công")
            self.load_data()
        except Exception as e:
            conn.rollback()
            QtWidgets.QMessageBox.critical(None, "Thông báo", f"Sửa hóa đơn thất bại: {str(e)}")
        finally:
            db.closeConnection()

    def display(self, row, column):
        self.lineEdit.setText(self.tableHD.item(row, 0).text())
        self.lineEdit_2.setText(self.tableHD.item(row, 1).text())
        self.dateEdit.setDate(QtCore.QDate.fromString(self.tableHD.item(row, 2).text(), "yyyy-MM-dd"))
        self.lineEdit_3.setText(self.tableHD.item(row, 3).text())
        self.lineEdit_4.setText(self.tableHD.item(row, 4).text())
        self.spinBox.setValue(int(self.tableHD.item(row, 5).text()))

    def update_total_price(self):
        try:
            # Lấy tổng tiền từ lineEdit_4 và số lượng từ spinBox
            tongtien_str = self.lineEdit_4.text().replace(',', '')
            soluong = self.spinBox.value()
            tongsotien = int(tongtien_str) * soluong
            self.lineEdit_4.setText(f"{tongsotien:,}")  # Update total price with commas
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, 'Error', str(e))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
