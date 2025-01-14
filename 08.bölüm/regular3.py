# regex ile çalışmalar
# bir string içinde string karşılaştırma
import re
# match() metodunu kullanarak email doğrulama
def email_dogrula(email):
    # bir email adresinin kalıbını karşılaştırma kalıbı olarak oluşturuyoruz
    x=r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(x,email):
        return True # doğrula
    else:
        return False # yanlışla

# bir email adresi gir
email=input("Geçerli bir email adresi giriniz>")
if email_dogrula(email):
    print(email," geçerli")
else:
    print("Girdiğiniz email",email,"geçersizdir")
