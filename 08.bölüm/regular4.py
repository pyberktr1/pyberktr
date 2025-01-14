# regex ile çalışmalar
# alfanumeric değerlerin doğrulanması
import re
x=r'\b[a-zA-Z]+\b' # alfanumerik girdiler için bir karşılaştırma kalıbı
ad=input("Adınız>")
if (re.findall(x,ad)):
    print("Hoşgeldin",ad)
else:
    print("Girdiniz geçerli değildir. lütfen nümerik değer girmeyin")
