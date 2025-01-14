# regex ile çalışmalar
# nümerik değerlerin doğrulanması
import re
x=r'\b[0-9]+\b'
fiyat=input("Fiyatı giriniz>")
if (re.findall(x,fiyat)):
    print("Ürünün KDV si", float(fiyat)*0.18)
else:
    print("HATA!:Sadece nümerik değerler giriniz!")
    
