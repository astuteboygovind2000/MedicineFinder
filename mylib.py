import pymysql
def make_connection():
    cn = pymysql.connect(host="localhost", user="root", passwd="", port=3306, db="govind", autocommit=True)
    cur = cn.cursor()
    return cur

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
