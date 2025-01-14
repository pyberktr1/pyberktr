# tkinter GUI
# textbox aracı ile girdi kabulü
import tkinter as tk
# butona tıklandığında textbox aracından girdiyi kabul eden fonksiyon
def getir(): 
    girdi=tbox1.get()
    # buton yazısını girdi ile güncelliyoruz
    btn1.config(text="Selam "+format(girdi)) 
    
root=tk.Tk()
root.geometry("500x100+200+100")
root.title("buton textbox penceresi")
# Bilgi mesajı
lbl1=tk.Label(root, text="Adınızı buraya giriniz")
lbl1.pack(pady=5)
# Girdi kabul etmek için textbox aracını oluşturalım
tbox1=tk.Entry(root, width=40)
tbox1.pack(pady=5)
# Butonu oluşturalım
# getir() komut fonksiyonunun parantez olmadan (anonim) verilmiş olmasına dikkat edin
# doğrudan parametre geçmeyen fonksiyonlar bu şekilde verilebilir
btn1=tk.Button(root, text="Tıklayın!", command=getir) 
btn1.pack()
# GUI ana program döngüsünü kuralım
# ana döngü tüm pencere ve pencere araçlarının güncellenmesi, 
# olay yakalanması ve işlenmesi için gereklidir
root.mainloop()
