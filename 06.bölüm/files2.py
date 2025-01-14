# dosya içinde kursörleri kullanarak gezinme
f=open("dosya.txt","r") # dosya ile çalışmak için bir kulp atanıyor
print("okuma öncesi kursörün pozisyonu :",f.tell())# kürsorün pozisyonu
print(f.read())# tüm içerik ekrana dökülüyor
print("okuma sonrası kürsor pozisyonu:",f.tell())
f.seek(10)# kürsor 10. karaktere pozisyonlandırılıyor
print(f.read(1))# kursörün yeni noktasından 1 karakter okunuyor
print(f.tell()) # kursörün yeni pozisyonu
print(f.read(3))# son kalınan yerden itibaren 3 karakter okunuyor
pos=f.tell()
print("kursorun son pozisyonu",pos)
f.seek(5,0)# 5. karakatere pozisyon alınıyor
print(f.read())
f.seek(0,2)# dosyanın en sonuna gidiliyor
print("doyada %i karakter var"%f.tell()) # kursorun son pozisyonu karakter sayısını verir
f.close()# açık dosyalar iş bittikten sonra mutlaka kapatılmalıdır
