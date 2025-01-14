# generate deyiminin iterasyon oluşturmak için kullanımı
from gen_module import sehir_gen
# üreteç fonksiyonu burada çağrılıyor
sehir=sehir_gen()
# ilk iki kayıt art arda ekrana yazdırılıyor
print(next(sehir))
print(next(sehir))
