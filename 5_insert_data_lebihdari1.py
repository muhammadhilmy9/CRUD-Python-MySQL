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
sql = "insert into tblbarang (kd_barang, nm_barang, satuan, harga, stok) values(%s,%s,%s,%s,%s)"
data = [("0002","Penggaris","Lusin",20000,15),
        ("0003","Penghapus","Lusin",25000,30),
        ("0004","Pulpen","Lusin",40000,80),  
        ("0005","Pensil","Lusin",35000,15)]

#PErulangan untuk memasukan data
for val in data:
    dbcursor.execute(sql,val)
    con.commit()

print("Data Barang berhasil di simpan")