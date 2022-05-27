import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password="",
    db = "dbpersediaan"
)
if con.is_connected():
    print("Koneksi ke server database berhasil")
    
dbcursor = con.cursor()
sql = "select * from tblbarang order by nm_barang"

dbcursor.execute(sql)
dt = dbcursor.fetchall()

for data in dt:
    print(data)