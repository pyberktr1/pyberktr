# miras bırakma ve baskılama
class dersler():
    def __init__(self):
        self.deger=2000

    def getir(self):
        print(self.deger, " ders ücretidir")

class ucretler(dersler):
    # bu çok satırlı yorum bloğu denemeler için konulmuştur

    def __init__(self):
        self.sayac=0
        dersler.__init__(self)
    
    def getir(self):
        self.deger+=3000
        self.sayac+=1
        print(self.deger," dersin artırılmış ücretidir sayac=", self.sayac)

c=dersler()
c.getir()# deger 2000 ile başlatılır
f=ucretler()# deger değişkeninin bir kopyası miras yoluyla alınır 
f.getir()
f.getir()
c.getir()# f nesnesinin defalarca çağırılmasına rağmen deger değişkeni değişmez
f.getir()# c nesnesinin tekrar çağrılmasına rağmen deger değişkeninde değişiklik olmaz
g=ucretler() # ucretler sınıfına dayalı yeni bir g nesnesi oluşturuluyor
g.getir()# deger değişkeninin bir kopyası dersler sınıfından çağrıldığı için f nesnesinden farklı bir değer alır
