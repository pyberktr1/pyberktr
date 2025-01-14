# veritabanları ile çalışmak
# mysql veriatabanına bağlanmak için gerekli modül yükleniyor
import mysql.connector
# mysql hizmetçisine bağlanılıyor
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Elma%55sema"
    )
# veritabanı oluşturuluyor
dbname="ogrenci"# veriatabanı ismi
sqlquery="CREATE DATABASE IF NOT EXISTS "+dbname # sorgu satırı
crs=con.cursor() # komut ve sorgulamalar için bir kürsor oluşturuluyor
crs.execute(sqlquery)# kürsor aracılığı ile sorgu işletiliyor
# yeni oluşturulan veritabanına bağlanılıyor
con.database=dbname # veritabanı ismi ile bağlantı sağlanıyor
# yeni veritabanı üzerinde tablo oluşturuluyor
crs.execute("""CREATE TABLE IF NOT EXISTS ogr_tablo (ogr_no INT AUTO_INCREMENT PRIMARY KEY, ad VARCHAR(255)
    NOT NULL, soyad VARCHAR(255) NOT NULL, ders VARCHAR(255), telno INT)""")
con.commit()# değişiklikler veritabanına işleniyor,
            # rollback() metodu commit() metodu ile işlenen değişiklikleri geri almak için 
            # kullanılabilir 
con.close() # veritabanı kapatılıyor
print("veritabanı %s oluşturuldu ve ogr_tablo tablosu ile dolduruldu"%dbname)


    



