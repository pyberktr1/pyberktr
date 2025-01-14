# dosyalarla çalışmak
f=open("dosya.txt","r") # çalışılacak dosyaya ait bir kulp (handle) atanıyor
print(f.read())# tüm içerik okunuyorve yazdırılıyor

with open("dosya2.txt", "w") as f2:# with deyimiyle dosya açma ve yazma
    f2.write("Yazma modu.\n")
    f2.write("ikinci bir satir yaziliyor.\n")
# with deyimi sonunda dosya otomatik kapatılır
    
# içeriğin satır satır for döngüsü ile yazdırılması
f2=open("dosya2.txt","r")
satirlar=f2.readlines()
print(satirlar)
for satir in satirlar:
    print(satir, end="") # her bir satırı sonuna kadar yazdırıyoruz

print() # boş satır
print("Dosyaya ekleme sonrasi durum>>")
# dosyaya yeni satırlar ekleniyor
f2.close()# mod değişimi öncesinde dosya kapatılmalı
f2=open("dosya2.txt", "a") # ekleme modu ile tekrar açılıyor
f2.write("Bu yeni bir satirdir \n")
f2.write("bu daha baska bir yeni satirdir \n")
f2.close # mod değişimi öncesinde dosya kapatılıyor
f2=open("dosya2.txt","r+") # okuma-yazma modu
f2.write("En basa satir ekleme \n") # ilk satır üzerine yazılıyor
print(f2.read())# okuma kalan yerden devam eder
# istenilen kısmı okuyabilmek ve yazabilmek için kursör konumlandırma yapılmalıdır.
# açılan tüm dosyalar with deyimi kullanılmadıysa mutlaka kapatılmalıdır.
f.close()
f2.close()
