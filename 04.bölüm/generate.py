# üreteçlerin for döngüleriyle kullanımı
from gen_module import sehir_gen
# üreteç fonksiyonu buradan çağrılıyor
sehir=sehir_gen()
for i in sehir: # tüm kayıtlar yazdırılıyor
    print(i)
