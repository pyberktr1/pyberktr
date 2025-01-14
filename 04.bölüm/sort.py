# bir dizinin elemanlarını sıralama
n=[3, 5, 1, 17, 7, -80, -5, -93, 18, -3, 6, 10, 5, 3]
print("Karışık dizi \n", n)
n.sort() # sıralama işlemi
print("sıralı dizi \n", n)
n.sort(reverse=True) # ters sıralama işlemi
print("ters sıralı dizi \n", n)
# string dizilerinde sıralama
m=["elma", "ayva", "ay", "ayi", "mayis", "meyve"]
print("karışık dizi \n", m)
m.sort() # sıralama işlemi
print("sıralı dizi \n", m)
m.sort(reverse=True) # ters sıralama işlemi
print("ters sıralı dizi \n", m)
m.sort(key=len) # kelime uzunluğuna göre sıralama
print("harf sayısına göre sıralama \n", m)
