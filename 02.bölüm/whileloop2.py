# while döngülerinin string değerlerle kullanımı
list=["a","b","c","d","e","f"]
print("liste elemanları\n",list)
i=" " # başlangıç değeri
while not (i in list):
    i=input("bir menü elemanı giriniz (a-f)")

print("menü elemanı:", i)
