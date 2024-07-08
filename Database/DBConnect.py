import mysql.connector

class DbManager:
    def __init__(self):

        self.mydb = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="123456",
            db="qldv_chothueaocuoi"
        )
    def getConnection(self):
        if self.mydb.is_connected():
            print("Kết nối thành công")
            return self.mydb
        else:
            print("Kết nối đã bị đóng")
            return None

    def closeConnection(self):
        if self.mydb.is_connected():
            self.mydb.close()
            print("Đã đóng kết nối")
        else:
            print("Kết nối đã đóng")