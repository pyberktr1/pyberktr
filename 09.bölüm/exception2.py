# hatalı veritip hatasının ele alınması
import sys
try:
    i=5
    j="7"
    #k=i+int(j)
    k=i+j
except TypeError:# tip hatası burada yakalanıyor
    print("Veritip hatası: farklı tipleri karıştırarak kullanmayın")
    sys.exit()
print("toplam =",k)
