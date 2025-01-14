# nesnelerde enkapsülasyon (kuşatma)
class dersler:
    __ucret=0 # korunmuş (kuşatılmış) parametreler
    __ad="None" # bu parametreler ancak sınıf içinde değiştirilebilirler
    def __init__(self):
        self.__ucret=5000
        self.__ad="Python"

    def goster(self):
        print("dersin adı:",self.__ad)
        print("dersin ücreti: =",self.__ucret)

a1=dersler()
a1.goster()
a1.__ucret=8000
a1.__ad="C++"
a1.goster() # ilk gösterimden farklı sonuç olmaz

        
