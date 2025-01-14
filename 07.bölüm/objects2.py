# sınıfa metot (fonksiyon) tanımlamak
# bir şirketteki çalışan sayısını ve kimlik bilgilerine takip etmek için bir sınıf yazalım
# bu taban (ebeveyn) sınıf olacak 
class calisan:
    sayac=0 # çalışan sayısını takip eden sayaç
    def __init__(self, ad, maas):
        self.ad=ad
        self.maas=maas
        calisan.sayac+=1 # sınıfın her çağrılışında sayaçı artır
# sınıfın mevcuttaki çağrısında tutulan kayıtları gösteren metot veya fonksiyon
    def goster(self): 
        print("Ad:", self.ad, ", maaş:", self.maas)

# calisan sınıfına dayalı ilk nesnemiz
cal1=calisan("Mert DEMİR","80000")
# ikinci ve diğer nesneler
cal2=calisan("Cansu KARACA","90000")
cal3=calisan("Hayri KARACA","70000")
# nesnelerde tutulan kayıtlar goster metotu kullanılarak ekrana dökülüyor
cal1.goster()
cal2.goster()
cal3.goster()
print("Şirketteki toplam çalışan sayısı >",calisan.sayac)

