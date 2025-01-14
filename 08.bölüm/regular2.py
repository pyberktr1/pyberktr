# regex ile çalışmalar
# bir string içinde string bulma
import re
str="hedef A!"
bul=re.search(".*(A|B|C|D)", str)
if bul:
    print("hedefimiz",bul.group())
else:
    print("hedef bilinmiyor")

