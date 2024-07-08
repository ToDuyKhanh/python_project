# MainFormLogic.py

from PyQt6.QtWidgets import QMessageBox
from Database.DBConnect import DbManager

class QLCGDV:
    def __init__(self):
        self.db_manager = DbManager()

    def fetch_all_dv(self):
        conn = self.db_manager.getConnection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT * FROM dichvu")
                result = cursor.fetchall()
                return result
            except Exception as e:
                raise e
            finally:
                self.db_manager.closeConnection()
        else:
            return []

    def add_dv(self, ma_dv, goi_dv, mo_ta, gia_tien):
        conn = self.db_manager.getConnection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO dichvu (ma_dv, goi_dv, mo_ta, gia_tien) VALUES (%s, %s, %s, %s)",
                               (ma_dv, goi_dv, mo_ta, gia_tien))
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                self.db_manager.closeConnection()


    def update_dv(self, ma_dv, goi_dv, mo_ta, gia_tien):
        conn = self.db_manager.getConnection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("UPDATE dichvu SET ma_dv=%s, goi_dv=%s, mo_ta=%s ,gia_tien=%s WHERE ma_dv=%s",
                               (ma_dv, goi_dv, mo_ta, gia_tien ,ma_dv))
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                self.db_manager.closeConnection()
              

    def delete_dv(self, ma_dv):
        conn = self.db_manager.getConnection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM dichvu WHERE ma_dv=%s", (ma_dv,))
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                self.db_manager.closeConnection()
               

    def timkiem_dv(self, ma_dv):
        conn = self.db_manager.getConnection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT * FROM dichvu WHERE ma_dv=%s", (ma_dv,))  # Search service by service code
                result = cursor.fetchone()
                return result  # Return the result directly (it could be None)
            except Exception as e:
                raise e
            finally:
                self.db_manager.closeConnection()
        return None  # Return None if connection failed


