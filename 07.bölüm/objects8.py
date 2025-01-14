# nesnelerde kuşatma
class dersler:
    ucret=0 # korunmamış (kuşatılmamış) parametreler
    ad="None"
    def __init__(self):
        self.ucret=5000
        self.ad="Python"

    def goster(self):
        print("dersin ismi:",self.ad)
        print("dersin ücreti=",self.ucret)

a1=dersler()
a1.goster()
a1.ucret=8000
a1.ad="C++"
a1.goster() # ilk gosterimden farklı sonuçlar gelir

        
