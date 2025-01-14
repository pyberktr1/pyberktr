# hata yakalama: IOError hatası

try:
    f=open("text2.txt","r")
    #f=open("text.txt","r")
except IOError:
    print("Dosya G/Ç hatası: dosya bulunamadı")
else:
    print("dosyadan okuma işlemi başarılı")

print("program kapanıyor...")
