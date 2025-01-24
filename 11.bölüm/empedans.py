
# Python tkinter kullanarak GUI uygulama gelistirme
# Seri RLC devrede empedans hesabı
import tkinter as tk
import math as m
# Menü burada olusturuluyor
def menu(secim):
    try: # hata yakalama aktif
        R=float(tbox1.get())# direnc degeri (ohm)
        L=float(tbox2.get())# enduktans degeri (mili Henry)
        C=float(tbox3.get())# kapasitans degeri (mikro Farad)
        f=float(tbox4.get())# frekans (Hz)
        XL=(2*m.pi*f*L*0.001)  # endüktif reaktans (ohm)
        XC=1/(2*m.pi*f*C*1E-6) # kapasitif reaktans (ohm)
        X=XL-XC                # net reaktans (ohm)
        # empedans açısı (radyan)
        # tanimli bir sifira bölme hatasi var 
        if (R==0):                        
            if (X>0):       # aci pozitif (saf endüktif reaktans)
                fi=m.pi/2
            else:
                fi=-m.pi/2  # aci negatif (saf kapasitif reaktans)
        else:
            fi=m.atan(X/R)
            
        derece=fi*180/m.pi       # empedans açısı (derece)
        Z=m.sqrt(R*R+m.pow(X,2)) # empedans büyüklüğü (ohm)
        
        if (R<0) or (L<0) or (C<0) or (f<0):
            sonuc.set("HATA!: Negatif deger girilemez")
        elif secim==1:# Empedans, Z (ohm)            
            sonuc.set("Empedans, Z (ohm)="+format(Z))
        elif secim==2:# Rezistans, R (ohm)
            sonuc.set("Rezistans (ohm)="+format(R))
        elif secim==3:# Reaktans, X (ohm)
            sonuc.set("Reaktans (ohm)="+format(X))
        elif secim==4:# Fi, (radyan)
            sonuc.set("Fi (radyan)="+format(fi))
        elif secim==5:# Fi, (derece)
            sonuc.set("Fi (derece)="+format(derece))
           
    except ValueError:# deger hatasi burada ele aliniyor
        sonuc.set("HATA!: Ondalık deger girin")
    except ZeroDivisionError:# sıfıra bölme hatası burada ele alınıyor
        sonuc.set("HATA!: Kapasite veya frekans sifir olamaz")
# Ana pencere olusturuluyor
root=tk.Tk()
root.geometry("600x150+100+200")
root.title("+*-/     Seri Empedans Hesabı     /-*+")

# girdi arabirimi (etiket, metin kutusu ve butonlar) olusturuluyor
lbl1=tk.Label(root, text="Direnci, R Giriniz (ohm)",fg="green",bg="white")
tbox1=tk.Entry(root,width=20)

lbl2=tk.Label(root, text="Enduktansi, L Giriniz (mH)",fg="red",bg="yellow")
tbox2=tk.Entry(root,width=20)

lbl3=tk.Label(root, text="Kapasitansi, C Giriniz (uF)",fg="blue",bg="yellow")
tbox3=tk.Entry(root,width=20)

lbl4=tk.Label(root, text="Frekansi, f Giriniz (Hz)",fg="yellow",bg="blue")
tbox4=tk.Entry(root,width=20)

btn1=tk.Button(root,text="EMPEDANS    ",command=lambda: menu(1),width=17)
btn2=tk.Button(root,text="REZISTANS   ",command=lambda: menu(2),width=17)
btn3=tk.Button(root,text="REAKTANS    ",command=lambda: menu(3),width=17)
btn4=tk.Button(root,text="FI (rad)    ",command=lambda: menu(4),width=17)
btn5=tk.Button(root,text="FI (derece) ",command=lambda: menu(5),width=17)

# araçlar gridleniyor
lbl1.grid(column=0, row=0, padx=5, pady=5)
lbl2.grid(column=1, row=0, padx=5, pady=5)
lbl3.grid(column=2, row=0, padx=5, pady=5)
lbl4.grid(column=3, row=0, padx=5, pady=5)

tbox1.grid(column=0, row=1, padx=5, pady=5)
tbox2.grid(column=1, row=1, padx=5, pady=5)
tbox3.grid(column=2, row=1, padx=5, pady=5)
tbox4.grid(column=3, row=1, padx=5, pady=5)

btn1.grid(column=0, row=2, padx=5, pady=5)
btn2.grid(column=1, row=2, padx=5, pady=5)
btn3.grid(column=2, row=2, padx=5, pady=5)
btn4.grid(column=3, row=2, padx=5, pady=5)
btn5.grid(column=3, row=3, padx=5, pady=5)

# sonuc icin deðisken olusturuluyor
sonuc=tk.StringVar()# stringvar nesnesi
                    # bir fonksiyona sunmak uzere bir string deger tutar

sonuc.set("CEVAP=?")# ilk deger atamasi yapiliyor
# lbl5 etiketi, sonuc stringvar nesnesi ile otomatik güncellenir
lbl5=tk.Label(root,textvariable=sonuc, width=40)                                                  
lbl5.grid(column=0, columnspan=3, row=3, padx=5, pady=5)
# ana döngü baslatiliyor
root.mainloop()
