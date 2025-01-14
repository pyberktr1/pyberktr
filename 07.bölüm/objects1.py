# nesneler ve sınıflarla çalışma
# yeni bir sınıf tanımlayalım
class sinifim:
    def __init__(self, A):# sınıfın başlatma bölümü (her sınıfta mutlaka olamlıdır)
        self.oz=A # sınıfımızın bir özelliği

# yeni oluşturduğumuz sınıfımızı yeni bir nesne olarak çağıralım
nesnem=sinifim(33)  # başlatma paramatresi A, 33 olarak veriliyor
print(nesnem.oz)    # nesnem nesnesinin oz özelliği yazdırılıyor (başlatma paramatresi A ya eşit)
nesnem.oz= 22       # oz özelliği yeni değer alıyor
print(nesnem.oz)    # oz özelliğinin son durumu
