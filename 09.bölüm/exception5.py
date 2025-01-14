# Sıfıra bölme hatası
try:
    n=int(input("Bir bölücü girin> "))
    sonuc=10/n
except ZeroDivisionError:
    print("sıfıra bölme hatası")
else:
    print("bölüm=",sonuc)
    
    
          
