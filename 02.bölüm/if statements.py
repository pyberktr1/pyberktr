# if deyimi
import sys # sys.exit() fonksiyonu için gerekli olan sys modülünü yüklüyoruz
x=list(map(int, input("İki sayı giriniz> ").split()))
print("sayılar listeleniyor ", x)
z=len(x)# liste uzunluğu
print("listedeki eleman sayısı ", z)
if z<2:
    print("Hata!:liste çok kısa ")
    sys.exit("Hata!:liste çok kısa ")
    #quit() # alternatif çıkış metotu
    #exit() # alternatif çıkış metotu
print("ilk eleman",x[0])
print("ikinci eleman",x[1])

print("Basit if deyimi:")

if x[0]>x[1]:
    print("ilk sayı ikinciden büyüktür")
          
if x[0]<x[1]:
    print("ilk sayı ikinciden küçüktür")

if x[0]==x[1]:
    print("sayılar birbirine eşittir")

print("tam if deyimleri:")

if x[0]>x[1]:
    print("büyüktür")
else:
    print("küçüktür")

print("yuvalı if deyimleri")

if x[0]>x[1]:
    print("büyüktür")
else:
    if x[0]<x[1]:
        print("küçüktür")
    else:
        print("eşittir")

print("Elif ile yuvalı if deyimleri")
# match case yapıları yerine kullanılır
if x[0]>x[1]:
    print("büyüktür")
elif x[0]<x[1]:
    print("küçüktür")
else:
    print("eşittir")



          
          

