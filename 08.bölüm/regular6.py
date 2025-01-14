# regex ile çalışmalar
# telefon numarası doğrulama
import re
# doğrulama fonksiyonu
def telno_dogrula(telno):
    x=r'^\d{10}$'# sadece 10 haneli nümerik girdileri kabul eden elek kalıbı
    if re.match(x,telno):
        return True
    else:
        return False

telno=input("Telefon numaranızı giriniz>")
while not(telno_dogrula(telno)):
    print(telno," geçerli bir telefon numarası değil")
    telno=input("Telefon numaranızı giriniz>")

print("girdiğiniz telefon numarası geçerlidir")

