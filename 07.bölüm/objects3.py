# sınıflarda miras bırakma
class dersler:
    def __init__(self, ders, sure):
        self.ad=ders
        self.sure=sure

    def goster(self):
        return self.ad + " " + self.sure

class ucretler(dersler): # ucretler sınıfı dersler sınıfının mirasçısı durumundadır
# ucretler derslerin çocuğudur
    def __init__(self, ders, sure, ucret):
        dersler.__init__(self , ders, sure)
        self.ucret=ucret

    def detay_goster(self):
        return self.goster() + " " + self.ucret

# yeni sınıflarla yeni nesneler tanımlayalım
az_detay=dersler("Java", "6 hafta")
daha_detay=ucretler("Python", "4 hafta","5000")
print(az_detay.goster())
print(daha_detay.detay_goster())

