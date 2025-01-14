# hataların ele alınması
# değer hatalarının ele alınması
import sys
try:
    n=int(input("Bir tamsayı giriniz> "))
except ValueError: # değer hatası burada yakalanır
    print("HATA!: sadece tamsayı giriniz! program sonlandırılıyor...")
    sys.exit()
print("Girdiğiniz tamsayı",n)

    
