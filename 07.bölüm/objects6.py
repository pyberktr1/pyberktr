# miras bırakma ve baskılama
class dersler():
    deger=500
    def __init__(self):
        dersler.deger+=2000

    def getir(self):
        print(self.deger, "dersin ücretidir")

class ucretler(dersler):
    def __init__(self):
        self.sayac=0
        dersler.__init__(self)   
    def getir(self):
        self.deger+=3000
        self.sayac+=1
        print(self.deger,"artırılmış ders ücretidir sayac=", self.sayac)

c=dersler()
c.getir()# deger 2500 olur
f=ucretler()# degerin bir kopyası alınır
f.getir()
f.getir()
c.getir()
f.getir()
g=ucretler()
g.getir()
h=dersler()
h.getir()
k=ucretler()
k.getir()
