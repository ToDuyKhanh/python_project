from PyQt6.QtWidgets import QMessageBox
from Database.DBConnect import DbManager

class QLHD:
    
    def __init__(self):
        self.db_manager = DbManager()

    def fetch_all_hd(self):
        conn = self.db_manager.getConnection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT * FROM hoa_don")
                result = cursor.fetchall()
                return result
            except Exception as e:
                raise e
            finally:
                self.db_manager.closeConnection()
        else:
            return []

    def add_hd(self, mahd, name, ngaylapHD, usernameNV, tongtien, soluong):
        conn = self.db_manager.getConnection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO hoa_don (mahd, name, ngaylapHD, usernameNV, tongtien, soluong) VALUES (%s, %s, %s, %s, %s, %s)",
                               (mahd, name, ngaylapHD, usernameNV, tongtien, soluong))
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                self.db_manager.closeConnection()

    def edit_hd(self, mahd, name, ngaylapHD, usernameNV, tongtien, soluong):
        conn = self.db_manager.getConnection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("UPDATE hoa_don SET mahd=%s, name=%s, ngaylapHD=%s, usernameNV=%s, tongtien=%s, soluong=%s WHERE mahd=%s",
                               (mahd, name, ngaylapHD, usernameNV, tongtien, soluong, mahd))
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                self.db_manager.closeConnection()