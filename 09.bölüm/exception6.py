# hata denetiminde assert deyiminin kullanımı
def bol(a,b):
    # aşağıdaki satırı yorum satırı yaparak sonucun nasıl olduğunu görün
    assert b!=0,"Sıfıra bölme hatası meydana geldi"
    return a/b
a=int(input("Bölünen> "))
b=int(input("Bölücü> "))
print("bölüm=", bol(a,b))
