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
sql = "insert into tblsuplier (kodesup, namasup, alamat, telp) values(%s,%s,%s,%s)"
data = ("S001","PT. Tiga Raksa Saja","Jalan Tembesu No. 1",628128102101)

dbcursor.execute(sql,data)
con.commit()

print("Data Barang berhasil di simpan")