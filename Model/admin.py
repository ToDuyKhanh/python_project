from Database.DBConnect import DbManager

class admin(object):
    def __init__(self, username, password):
        self.name = username
        self.password = password

    def login(self):
        db = DbManager()
        conn = db.getConnection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admin WHERE username=%s AND password=%s", (self.name, self.password))
        record = cursor.fetchone()
        db.closeConnection()
        if record is not None:
            return True
        else:
            return False