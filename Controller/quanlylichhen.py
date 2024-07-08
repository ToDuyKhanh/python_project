from Database.DBConnect import DbManager

class QLLH:
    def __init__(self):
        self.db_manager = DbManager()
    def fetch_all_lh(self):
        conn = self.db_manager.getConnection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT * FROM lichhen")
                result = cursor.fetchall()
                return result
            except Exception as e:
                raise e
            finally:
                self.db_manager.closeConnection()
        else:
            return []
    def add_lh(self, malh, tenkh, sdt, diachi, ngayhen, trangthai):
        conn = self.db_manager.getConnection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO lichhen (malh, tenkh, sdt, diachi, ngayhen, trangthai) VALUES (%s, %s, %s, %s, %s, %s)",
                               (malh, tenkh, sdt, diachi, ngayhen, trangthai))
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                self.db_manager.closeConnection()
    def update_lh(self, malh, tenkh, sdt, diachi, ngayhen, trangthai):
        conn = self.db_manager.getConnection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("UPDATE lichhen SET tenkh=%s, sdt=%s, diachi=%s, ngayhen=%s, trangthai=%s WHERE malh=%s",
                               (tenkh, sdt, diachi, ngayhen, trangthai, malh))
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                self.db_manager.closeConnection()
    def delete_lh(self, malh):
        conn = self.db_manager.getConnection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM lichhen WHERE malh=%s", (malh,))
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                self.db_manager.closeConnection()
                
        