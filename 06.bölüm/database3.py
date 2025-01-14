# veritabanından veri çekmek
import mysql.connector
# mysql serverina bağlanıyor
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Elma%55sema",
    database="ogrenci"
    )
crs=con.cursor() # kürsor
# ogrenci veritabanında ogr_tablo tablosundan veri çekmek için gerekli komut
crs.execute("""SELECT * FROM ogr_tablo""")
# tüm kayıtlar alınıyor ve yazdırılıyor
record=crs.fetchall()
print("no    ad    soyad  ders  telno")
print("------------------------------------")
for data in record:
    print(data,"\n")

con.commit()    # değişiklikler veritabanına işleniyor
crs.close()     # kürsor kapatılıyor
con.close()     # veritabanı kapatılıyor
print("ogr_tablo tablosundaki tüm kayıtlar getirildi")


    



