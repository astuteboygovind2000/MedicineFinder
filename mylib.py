import pymysql
import os

def make_connection():
    try:
        cn = pymysql.connect(
            host=os.getenv("MYSQLHOST"),
            user=os.getenv("MYSQLUSER"),
            passwd=os.getenv("MYSQLPASSWORD"),
            port=int(os.getenv("MYSQLPORT")),
            db=os.getenv("MYSQLDATABASE"),
            autocommit=True
        )
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS logindata;")
        return cursor
    except Exception as e:
        print(f"[DB ERROR] {e}")
        raise

def check_photo(email):
    cur = make_connection()
    sql = "select * from photo_data where email='" + email + "'"
    cur.execute(sql)
    n = cur.rowcount
    photo = "no"
    if n > 0:
        row = cur.fetchone()
        photo = row[1]
    return photo
