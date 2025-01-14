# sözlüklerle alakalı uygulama
# bir cümledeki harflerin sayılması
msj=input("Bir cümle yazınız >")
sayi_soz={"rakam":0, "küçük":0, "büyük":0, "sesli":0}
sesli="aeiouAEIOU"
# harflerin rakam, küçük, büyük ve sesli olmak üzere sayılarını bulalım 
for char in msj:
    if char.isdigit():
        sayi_soz["rakam"]+=1
    elif char.isupper():
        sayi_soz["büyük"]+=1
    elif char.islower():
        sayi_soz["küçük"]+=1
    # sesli harf sayısını bulalım
    if char in sesli:
        sayi_soz["sesli"]+=1

# Sonuçlar yazdırılıyor

print("sesli harf sayısı>",sayi_soz["sesli"])
print("rakam sayısı>",sayi_soz["rakam"])
print("büyük harf sayısı>",sayi_soz["büyük"])
print("küçük harf sayısı>",sayi_soz["küçük"])

