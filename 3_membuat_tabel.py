import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password="",
    db = "dbpersediaan"
)
if con.is_connected():
    print("Koneksi ke server database berhasil")

tabel = con.cursor()
tabel.execute("create table if not exists tblbarang(kd_barang varchar(10),"
              "nm_barang varchar(50), satuan varchar(12), harga int(10), stok int(8))")
