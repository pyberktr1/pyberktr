# regex düzenli ifadelerle çalışma
# verilen stringte arama yaparak belli bir stringi değiştirmek
import re
str="Evet bana evet demişti ama şimdi hayır diyor"
# bütün evetleri (büyük E ile başlayan dahil) bulup hayır ile değiştiren regex
sonuc=re.sub("[eE]vet", "hayır", str)
print(str)
print(sonuc)
