# lokal ve global değişken tanımları
gdeg1 = 25 # global bir değişken
gdeg2 = 22 # global başka bir değişken

def gfonk():
    ldeg1 = 10 # bu değişken fonksiyona lokaldir
    gdeg1 = ldeg1 # gdeg1 fonksiyon içinde lokal bir değişkendir
    global gdeg2  # gdeg2 fonksiyon içinde global tanımlıdır
    gdeg2 = ldeg1 + gdeg1
    print("fonksiyon içi değerler \ngdeg1 %i gdeg2 %i ldeg1 %i"%(gdeg1, gdeg2, ldeg1))
    return ldeg1*3 # geri döndürülen değer

print("fonksiyon çağrısı öncesi >>> gdeg1 %i gdeg2 %i "%(gdeg1, gdeg2))
print("fonksiyon sonucu ", format(gfonk()))
print("fonksiyon çağrısı sonrası >>> gdeg1 %i gdeg2 %i "%(gdeg1, gdeg2))


