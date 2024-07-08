from PyQt6 import QtCore, QtGui, QtWidgets
from Database.DBConnect import DbManager
from Controller.qlcgdv import QLCGDV

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1020, 600)  # Tăng kích thước form để phù hợp với các widget

        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(350, 0, 311, 31))
        self.frame.setStyleSheet("background-color:rgb(170, 170, 255)")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(60, 0, 201, 31))
        self.label.setStyleSheet("font: 75 16pt 'Times New Roman'; color: white;")
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")

        self.tableWidget = QtWidgets.QTableWidget(parent=Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 270, 1020, 321))  # Kích thước của bảng
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["Mã dịch vụ", "Gói dịch vụ", "Mô tả gói dịch vụ", "Giá tiền"])

        # Thiết lập các thuộc tính cho bảng
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                background-color: rgb(255, 255, 255);
                border: 1px solid #aaa;
                border-radius: 5px;
            }
            QTableWidget::item {
                padding: 5px;
            }
            QHeaderView::section {
                background-color: rgb(170, 170, 255);
                color: white;
                padding: 5px;
                font: bold 10pt 'Times New Roman';
            }
            QTableWidget::horizontalHeader {
                border: 1px solid #aaa;
            }
            QTableWidget::item:selected {
                background-color: rgb(85, 170, 255);
                color: white;
            }
        """)

        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(0, 40, 1020, 231))
        self.widget.setStyleSheet("background-color: rgb(206, 228, 255);")
        self.widget.setObjectName("widget")

        # Các nút thêm, sửa, xóa dịch vụ
        self.btnEditDV = QtWidgets.QPushButton(parent=self.widget)
        self.btnEditDV.setGeometry(QtCore.QRect(200, 180, 81, 31))  # Cải thiện kích thước nút
        self.btnEditDV.setStyleSheet("""
            background-color: rgb(85, 170, 255);
            border: 1px solid #aaa;
            border-radius: 5px;
            padding: 5px;
            font: 10pt 'Times New Roman';
            font-weight: bold;
            box-shadow: 2px 2px 5px grey;
        """)
        self.btnEditDV.setObjectName("btnEditDV")

        self.btnDeleteDV = QtWidgets.QPushButton(parent=self.widget)
        self.btnDeleteDV.setGeometry(QtCore.QRect(320, 180, 81, 31))  # Cải thiện kích thước nút
        self.btnDeleteDV.setStyleSheet("""
            background-color: rgb(85, 170, 255);
            border: 1px solid #aaa;
            border-radius: 5px;
            padding: 5px;
            font: 10pt 'Times New Roman';
            font-weight: bold;
            box-shadow: 2px 2px 5px grey;
        """)
        self.btnDeleteDV.setObjectName("btnDeleteDV")

        self.btnAddDV = QtWidgets.QPushButton(parent=self.widget)
        self.btnAddDV.setGeometry(QtCore.QRect(80, 180, 81, 31))  # Cải thiện kích thước nút
        self.btnAddDV.setStyleSheet("""
            background-color: rgb(85, 170, 255);
            border: 1px solid #aaa;
            border-radius: 5px;
            padding: 5px;
            font: 10pt 'Times New Roman';
            font-weight: bold;
            box-shadow: 2px 2px 5px grey;
        """)
        self.btnAddDV.setObjectName("btnAddDV")

        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 231, 21))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 91, 21))
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 50, 121, 31))  # Cải thiện kích thước ô nhập mã dịch vụ
        self.lineEdit.setStyleSheet("""
            border: 1px solid #aaa;
            border-radius: 5px;
            padding: 5px;
            font: 10pt 'Times New Roman';
        """)
        self.lineEdit.setObjectName("lineEdit")

        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setGeometry(QtCore.QRect(240, 50, 81, 21))
        self.label_4.setObjectName("label_4")

        self.comboBox = QtWidgets.QComboBox(parent=self.widget)
        self.comboBox.setGeometry(QtCore.QRect(320, 50, 181, 31))  # Cải thiện kích thước combobox
        self.comboBox.setStyleSheet("""
            border: 1px solid #aaa;
            border-radius: 5px;
            padding: 5px;
            font: 10pt 'Times New Roman';
        """)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Chụp hình cưới")
        self.comboBox.addItem("Cho thuê áo cưới")
        self.comboBox.addItem("Dịch vụ khác")

        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setGeometry(QtCore.QRect(700, 0, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(560, 30, 381, 91))  # Cải thiện kích thước ô nhập mô tả dịch vụ
        self.lineEdit_2.setStyleSheet("""
            border: 1px solid #aaa;
            border-radius: 5px;
            padding: 5px;
            font: 10pt 'Times New Roman';
        """)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.textEdit = QtWidgets.QTextEdit(parent=self.widget)
        self.textEdit.setGeometry(QtCore.QRect(590, 180, 231, 31))  # Cải thiện kích thước ô nhập tìm kiếm
        self.textEdit.setStyleSheet("""
            border: 1px solid #aaa;
            border-radius: 5px;
            padding: 5px;
            font: 10pt 'Times New Roman';
        """)
        self.textEdit.setObjectName("textEdit")

        self.btnTimKIem = QtWidgets.QPushButton(parent=self.widget)
        self.btnTimKIem.setGeometry(QtCore.QRect(840, 180, 81, 31))  # Cải thiện kích thước nút tìm kiếm
        self.btnTimKIem.setStyleSheet("""
            background-color: rgb(85, 170, 255);
            border: 1px solid #aaa;
            border-radius: 5px;
            padding: 5px;
            font: 10pt 'Times New Roman';
            font-weight: bold;
            box-shadow: 2px 2px 5px grey;
        """)
        self.btnTimKIem.setObjectName("btnTimKIem")

        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        self.label_6.setGeometry(QtCore.QRect(20, 110, 91, 21))
        self.label_6.setObjectName("label_6")

        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 110, 121, 31))  # Cải thiện kích thước ô nhập giá tiền
        self.lineEdit_3.setStyleSheet("""
            border: 1px solid #aaa;
            border-radius: 5px;
            padding: 5px;
            font: 10pt 'Times New Roman';
        """)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.btnAddDV.clicked.connect(self.add_dv)
        self.btnEditDV.clicked.connect(self.edit_dv)
        self.btnDeleteDV.clicked.connect(self.delete_dv)
        self.btnTimKIem.clicked.connect(self.timkiem)
        self.tableWidget.cellClicked.connect(self.display_record)
        self.load_data()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setToolTip(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">CÁC GÓI DỊCH VỤ</span></p></body></html>"))
        self.btnEditDV.setText(_translate("Form", "Sửa DV"))
        self.btnDeleteDV.setText(_translate("Form", "Xóa DV"))
        self.btnAddDV.setText(_translate("Form", "Thêm DV"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Chi tiết các gói dịch vụ</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Mã DV:</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Gói dịch vụ:</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "Mô tả dịch vụ:"))
        self.btnTimKIem.setText(_translate("Form", "Tìm kiếm"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Giá tiền:</span></p><p><br/></p></body></html>"))

    def load_data(self):
        try:
            quanlycacgoidv = QLCGDV()
            result = quanlycacgoidv.fetch_all_dv()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number == 3:  # Cột giá tiền
                        data = f"{data:,}"  # Định dạng số tiền với dấu phẩy
                    item = QtWidgets.QTableWidgetItem(str(data))
                    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # Căn giữa các mục
                    self.tableWidget.setItem(row_number, column_number, item)

            # Tự động điều chỉnh kích thước các cột
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, 'Error', str(e))

    def add_dv(self):
        try:
            ma_dv = self.lineEdit.text()
            goi_dv = self.comboBox.currentText()
            mo_ta = self.lineEdit_2.text()
            gia_tien = self.lineEdit_3.text()
            if not ma_dv or not goi_dv or not mo_ta or not gia_tien:
                QtWidgets.QMessageBox.warning(None, 'Cảnh báo', 'Vui lòng điền vào tất cả')
                return

            gia_tien = gia_tien.replace(',', '')  # Xóa dấu phẩy nếu có
            quanlycacgoidv = QLCGDV()
            quanlycacgoidv.add_dv(ma_dv, goi_dv, mo_ta, gia_tien)
            QtWidgets.QMessageBox.information(None, 'Thông báo', 'Thêm dịch vụ thành công')
            self.load_data()
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, 'Error', str(e))

    def edit_dv(self):
        try:
            ma_dv = self.lineEdit.text()
            goi_dv = self.comboBox.currentText()
            mo_ta = self.lineEdit_2.text()
            gia_tien = self.lineEdit_3.text()
            if not ma_dv or not goi_dv or not mo_ta or not gia_tien:
                QtWidgets.QMessageBox.warning(None, 'Cảnh báo', 'Vui lòng điền vào tất cả')
                return

            gia_tien = gia_tien.replace(',', '')  # Xóa dấu phẩy nếu có
            quanlycacgoidv = QLCGDV()
            quanlycacgoidv.update_dv(ma_dv, goi_dv, mo_ta, gia_tien)
            QtWidgets.QMessageBox.information(None, 'Thông báo', 'Cập nhật dịch vụ thành công')
            self.load_data()
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, 'Error', str(e))

    def delete_dv(self):
        try:
            selected_row = self.tableWidget.currentRow()
            if selected_row == -1:
                QtWidgets.QMessageBox.warning(None, 'Cảnh báo', 'Vui lòng chọn dịch vụ cần xóa')
                return

            ma_dv = self.tableWidget.item(selected_row, 0).text()
            quanlycacgoidv = QLCGDV()
            quanlycacgoidv.delete_dv(ma_dv)
            QtWidgets.QMessageBox.information(None, 'Thông báo', 'Xóa dịch vụ thành công')
            self.load_data()
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, 'Error', str(e))

    def timkiem(self):
        try:
            ma_dv = self.textEdit.toPlainText().strip()
            if not ma_dv:
                QtWidgets.QMessageBox.warning(None, 'Cảnh báo', 'Vui lòng nhập mã dịch vụ cần tìm')
                return

            quanlycacgoidv = QLCGDV()
            result = quanlycacgoidv.timkiem_dv(ma_dv)
            if result:
                self.display_data([result])  # Sử dụng danh sách chứa tuple kết quả duy nhất
            else:
                QtWidgets.QMessageBox.warning(None, 'Cảnh báo', 'Không tìm thấy dịch vụ')
                self.display_data([])  # Xóa bảng nếu không tìm thấy kết quả
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, 'Error', str(e))

    def display_data(self, data):
        try:
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(data):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number == 3:  # Cột giá tiền
                        data = f"{data:,}"  # Định dạng số tiền với dấu phẩy
                    item = QtWidgets.QTableWidgetItem(str(data))
                    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # Căn giữa các mục
                    self.tableWidget.setItem(row_number, column_number, item)

            # Tự động điều chỉnh kích thước các cột
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, 'Error', str(e))

    def display_record(self, row, column):
        self.lineEdit.setText(self.tableWidget.item(row, 0).text())
        self.comboBox.setCurrentText(self.tableWidget.item(row, 1).text())
        self.lineEdit_2.setText(self.tableWidget.item(row, 2).text())
        gia_tien = self.tableWidget.item(row, 3).text()
        self.lineEdit_3.setText(gia_tien.replace(',', ''))  # Xóa dấu phẩy trước khi đưa vào ô nhập

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
