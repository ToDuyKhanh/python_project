# customer_manager.py

from Database.DBConnect import DbManager

class CustomerManager:
    def __init__(self):
        self.db_manager = DbManager()

    def fetch_all_customers(self):
        conn = self.db_manager.getConnection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT * FROM khachhang")
                result = cursor.fetchall()
                return result
            except Exception as e:
                raise e
            finally:
                self.db_manager.closeConnection()
        else:
            return []

    def add_customer(self, idkhachhang, name, ngaysinh, sdt, diachi):
        conn = self.db_manager.getConnection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO khachhang (idkhachhang, name, ngaysinh, sdt, diachi) VALUES (%s, %s, %s, %s, %s)",
                               (idkhachhang, name, ngaysinh, sdt, diachi))
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                self.db_manager.closeConnection()

    def update_customer(self, idkhachhang, name, ngaysinh, sdt, diachi):
        conn = self.db_manager.getConnection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("UPDATE khachhang SET name=%s, ngaysinh=%s, sdt=%s, diachi=%s WHERE idkhachhang=%s",
                               (name, ngaysinh, sdt, diachi, idkhachhang))
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                self.db_manager.closeConnection()

    def delete_customer(self, idkhachhang):
        conn = self.db_manager.getConnection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM khachhang WHERE idkhachhang=%s", (idkhachhang,))
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                self.db_manager.closeConnection()
