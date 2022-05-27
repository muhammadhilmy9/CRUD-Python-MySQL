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
sql = "Delete from tblbarang Where nm_barang = 'Pensil'"

dbcursor.execute(sql)
con.commit()