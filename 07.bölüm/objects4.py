# bir sınıfta baskılama (override) yapmak
class dersler():
    def __init__(self, sure, ucret):
        self.sure=sure
        self.ucret=ucret

    def goster(self): # diğer sınıfta miras esnasında baskılanacak fonksiyon
        print(self.sure, "ders süresi olup ücreti ise", self.ucret)

class adlar(dersler):
    def __init__(self, ad):
        self.ad=ad

    def goster(self): # bu metot miras alınan dersler sınıfındaki aynı adlı metotu baskılar
        print(self.ad, "dersimizin adıdır")

f=adlar("C++")
c=dersler("4 hafta","5000")
# aynı adlı metotlar farklı sınıftaki nesnelerde farklı işlemler gerçekleştirir
f.goster()
c.goster()
