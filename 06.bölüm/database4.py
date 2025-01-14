# veritabanında kayıt güncellemek
import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Elma%55sema",
    database="ogrenci"
    )
crs=con.cursor() 
# güncelleme komutu
crs.execute("""UPDATE ogr_tablo SET ad="Tamer", soyad="ALACA", ders="Java", telno="212322" WHERE ogr_no=2""")
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
print("ogr_tablo tablosundaki kayıtlar güncellendi")


    



