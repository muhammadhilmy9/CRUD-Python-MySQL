#Membuat database dan tabel dengan python
#1. Membuat database "dbPersediaan"
#kd_barang varchar (10),
#nm_barang varchar (50),
#satuan varchar (12),
#harga int (10)
#stok int(8)
#primary key (kd_barang)
import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password=""
)
if con.is_connected():
    print("Koneksi ke server database berhasil")
    
db= con.cursor()
db.execute("create database dbPersediaan")
