from PyQt6 import QtCore, QtGui, QtWidgets
from Database.DBConnect import DbManager
import xlsxwriter

class StatisticsForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Thống Kê Hóa Đơn")
        self.resize(800, 600)

        # Tiêu đề
        self.labelTitle = QtWidgets.QLabel(self)
        self.labelTitle.setGeometry(QtCore.QRect(300, 20, 200, 30))
        self.labelTitle.setStyleSheet("font: 75 16pt 'Times New Roman';")
        self.labelTitle.setText("Thống Kê Hóa Đơn")

        # Từ ngày
        self.labelFromDate = QtWidgets.QLabel(self)
        self.labelFromDate.setGeometry(QtCore.QRect(50, 70, 100, 30))
        self.labelFromDate.setText("Từ ngày:")

        self.fromDateEdit = QtWidgets.QDateEdit(self)
        self.fromDateEdit.setGeometry(QtCore.QRect(150, 70, 150, 30))
        self.fromDateEdit.setCalendarPopup(True)
        self.fromDateEdit.setDate(QtCore.QDate.currentDate())

        # Đến ngày
        self.labelToDate = QtWidgets.QLabel(self)
        self.labelToDate.setGeometry(QtCore.QRect(400, 70, 100, 30))
        self.labelToDate.setText("Đến ngày:")

        self.toDateEdit = QtWidgets.QDateEdit(self)
        self.toDateEdit.setGeometry(QtCore.QRect(500, 70, 150, 30))
        self.toDateEdit.setCalendarPopup(True)
        self.toDateEdit.setDate(QtCore.QDate.currentDate())

        # Nút tạo báo cáo
        self.btnGenerateReport = QtWidgets.QPushButton(self)
        self.btnGenerateReport.setGeometry(QtCore.QRect(330, 120, 120, 40))
        self.btnGenerateReport.setText("Tạo Báo Cáo")
        self.btnGenerateReport.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; /* Green */
                border: none;
                color: white;
                padding: 10px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 14px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.btnGenerateReport.clicked.connect(self.generate_report)

        # Bảng thống kê
        self.tableStatistics = QtWidgets.QTableWidget(self)
        self.tableStatistics.setGeometry(QtCore.QRect(50, 180, 700, 400))
        self.tableStatistics.setColumnCount(6)
        self.tableStatistics.setHorizontalHeaderLabels(["Mã hóa đơn", "Khách hàng", "Ngày lập hóa đơn", "Nhân viên", "Tổng tiền", "Tổng số lượng"])
        self.tableStatistics.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

    def generate_report(self):
        from_date = self.fromDateEdit.date().toString("yyyy-MM-dd")
        to_date = self.toDateEdit.date().toString("yyyy-MM-dd")

        db = DbManager()
        conn = db.getConnection()
        cursor = conn.cursor()
        try:
            query = """
                SELECT mahd, name, ngaylapHD, usernameNV, tongtien, soluong
                FROM hoa_don
                WHERE ngaylapHD BETWEEN %s AND %s
            """
            cursor.execute(query, (from_date, to_date))
            data = cursor.fetchall()
            
            if not data:
                QtWidgets.QMessageBox.information(None, "Thông báo", "Không có dữ liệu trong khoảng thời gian này.")
                return
            
            self.tableStatistics.setRowCount(0)
            for row_number, row_data in enumerate(data):
                self.tableStatistics.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableStatistics.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            
            # Xuất báo cáo ra file Excel
            workbook = xlsxwriter.Workbook('BaoCaoThongKe.xlsx')
            worksheet = workbook.add_worksheet()
            headers = ["Mã hóa đơn", "Khách hàng", "Ngày lập hóa đơn", "Nhân viên", "Tổng tiền", "Tổng số lượng"]
            
            # Write headers
            for col, header in enumerate(headers):
                worksheet.write(0, col, header)
            
            # Write data
            for row in range(self.tableStatistics.rowCount()):
                for col in range(self.tableStatistics.columnCount()):
                    worksheet.write(row + 1, col, self.tableStatistics.item(row, col).text())

            # Điều chỉnh kích thước cột để phù hợp với dữ liệu
            column_widths = [len(header) for header in headers]
            for row_num, row_data in enumerate(data, start=1):
                for col_num, cell_data in enumerate(row_data):
                    cell_str = str(cell_data)
                    column_widths[col_num] = max(column_widths[col_num], len(cell_str))

            for col_num, width in enumerate(column_widths):
                worksheet.set_column(col_num, col_num, width + 2)  # Thêm một ít độ rộng để tạo khoảng trống
            
            workbook.close()
            QtWidgets.QMessageBox.information(None, "Thông báo", "Tạo báo cáo thành công")
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Thông báo", f"Tạo báo cáo thất bại: {str(e)}")
        finally:
            cursor.close()
            db.closeConnection()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = StatisticsForm()
    ui.show()
    sys.exit(app.exec())
