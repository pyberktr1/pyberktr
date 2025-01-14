# veritabanına veri girmek
import mysql.connector
# mysql serverine bağlanıyor
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Elma%55sema",
    database="ogrenci"
    )
crs=con.cursor() # kursör oluşturuluyor
# ogrenci veritabanında ogr_tablo tablosuna veri girmek için gerekli komut
crs.execute("""INSERT INTO ogr_tablo(ad,soyad,ders,telno) VALUES("Mert", "Erkan", "C++", 312255)""")
con.commit()    # veri işleniyor
crs.close()     # kursör kapatılıyor
con.close()     # veritabanı kapatılıyor
print("Yeni kayıt ogr_tablo tablosuna işlendi")



