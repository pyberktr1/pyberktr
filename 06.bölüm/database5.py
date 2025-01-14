# veritabanından kayıt silmek
import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Elma%55sema",
    database="ogrenci"
    )
crs=con.cursor() 
# ogr_tablo tablosundan kayıt silmek için gerekli komut
crs.execute("""DELETE FROM ogr_tablo WHERE ogr_no=1""")
# tüm kayıtlar getiriliyor ve gösteriliyor
crs.execute("""SELECT * FROM ogr_tablo""")
records=crs.fetchall()
print("no    ad    soyad  ders  telno")
print("------------------------------------")
for data in records:
    print(data,"\n")

con.commit()
crs.close()
con.close()
print("ogr_tablo tablosundan bir kayıt silindi")
