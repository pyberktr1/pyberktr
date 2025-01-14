# tkinter GUI
# buton ekleme örneği
import tkinter as tk
root=tk.Tk()
root.title("butonlu pencere")
root.geometry("300x200+200+100")
# Ekrana bir yazı (label) ekleyelim
lbl=tk.Label(root, text="Buton buraya")
# pencerenin görünmesi için pack() geometri yönetim metodunu kullanacağız
lbl.pack(pady=10) # dikeyde 10px aralıkla paketle
# butonumuzu oluşturalım
btn=tk.Button(root, text="Bana Tıklasana!")
# buton widget (pencere aracı) görülmesi için pack() yapıyoruz
btn.pack()
# GUI ana program döngüsünü kuralım
# ana döngü tüm pencere ve pencere araçlarının güncellenmesi, 
# olay yakalanması ve işlenmesi için gereklidir
root.mainloop()
