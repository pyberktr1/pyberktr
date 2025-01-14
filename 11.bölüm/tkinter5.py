
# Python tkinter kullanarak GUI uygulama gelistirme
import tkinter as tk
# Menü burada olusturuluyor
def menu(secim):
    try: # hata yakalama aktif
        a=int(tbox1.get())# ilk sayiyi alalim
        b=int(tbox2.get())# ikinci sayiyi alalim
        if secim==1:#toplam
            res.set("A+B="+format(a+b))
        elif secim==2:#fark
            res.set("A-B="+format(a-b))
        elif secim==3:#carpim
            res.set("A*B="+format(a*b))
        elif secim==4:#bölme
            res.set("A/B="+format(a/b))
    except ValueError:# deger hatasi burada ele aliniyor
        res.set("HATA!: Sadece tamsayi deger giriniz...")
# Ana pencere olusturuluyor
root=tk.Tk()
root.geometry("500x300+100+200")
root.title("+*-/     HESAP MAKINESI     /-*+")
# girdi arabirimi (metin kutusu) olusturuluyor
lbl1=tk.Label(root, text="Ilk sayiyi giriniz (A)",bg="yellow",fg="blue")
lbl1.pack(pady=5)
tbox1=tk.Entry(root,width=20)
tbox1.pack()

lbl2=tk.Label(root, text="Ikinci sayiyi giriniz (B)",bg="red",fg="yellow")
lbl2.pack(pady=5)
tbox2=tk.Entry(root,width=20)
tbox2.pack(pady=5)
# butonlar olusturuluyor
btn1=tk.Button(root,text="TOPLAMA   ",command=lambda: menu(1),width=20)
btn2=tk.Button(root,text="FARK      ",command=lambda: menu(2),width=20)
btn3=tk.Button(root,text="CARPMA    ",command=lambda: menu(3),width=20)
btn4=tk.Button(root,text="BOLME     ",command=lambda: menu(4),width=20)
# butonlar paketleniyor
btn1.pack(pady=5)
btn2.pack(pady=5)
btn3.pack(pady=5)
btn4.pack(pady=5)

# sonuc icin deðisken olusturuluyor
res=tk.StringVar()# stringvar nesnesi
                  # bir fonksiyona sunmak uzere bir string deger tutar

res.set("CEVAP=?")# ilk deger atamasi yapiliyor
lbl3=tk.Label(root,textvariable=res) # lbl3 etiketi res stringvar nesnesi
                                     # ile otomatik güncellenir
lbl3.pack(pady=10)
# ana döngü baslatiliyor
root.mainloop()
