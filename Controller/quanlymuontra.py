from Database.DBConnect import DbManager

class QuanLyMuonTra:
    def __init__(self):
        self.db = DbManager()
    def fetch_all_mt(self):
        conn = self.db.getConnection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT * FROM muon_tra")
                result = cursor.fetchall()
                return result
            except Exception as e:
                raise e
            finally:
                self.db.closeConnection()
        else:
            return []
    def add_mt(self,mamt,idkhachhang,ma_dv,ngaymuon,ngaytra,trangthai):
        conn = self.db.getConnection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO muon_tra (mamt,idkhachhang,ma_dv,ngaymuon,ngaytra,trangthai) VALUES (%s, %s, %s, %s, %s, %s)",
                               (mamt,idkhachhang,ma_dv,ngaymuon,ngaytra,trangthai))
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                self.db.closeConnection()
    def update_mt(self,mamt,idkhachhang,ma_dv,ngaymuon,ngaytra,trangthai):
        conn = self.db.getConnection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("UPDATE muon_tra SET idkhachhang=%s, ma_dv=%s, ngaymuon=%s, ngaytra=%s, trangthai=%s WHERE mamt=%s",
                               (idkhachhang,ma_dv,ngaymuon,ngaytra,trangthai,mamt))
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                self.db.closeConnection()
    def delete_mt(self,mamt):
        conn = self.db.getConnection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM muon_tra WHERE mamt=%s", (mamt,))
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                self.db.closeConnection()