import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "python_db"
)

print("Koneksi ke database pyhton_db berhasil")