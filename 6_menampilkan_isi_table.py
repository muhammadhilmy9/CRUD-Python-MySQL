#Menampilkan isi data dalam tabel
#fetchall() : untuk mengambil semua data
#fetchmay(3) : untuk mengambil data sebanyak 3 record
#fetchone(): untuk mengambil satu data pertama saja
#fungsi-fungsi akan mengembalikan data list yang bersi record/tuple

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
sql ="select*from tblbarang"
dbcursor.execute(sql)
dt = dbcursor.fetchall()

for data in dt:
    print(data)