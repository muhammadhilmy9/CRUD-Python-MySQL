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
sql = "UPDATE tblbarang SET nm_barang=%s, satuan=%s WHERE kd_barang=%s"
data = "Kertas HVS","Rim", "0004"
dbcursor.execute(sql,data)

con.commit()