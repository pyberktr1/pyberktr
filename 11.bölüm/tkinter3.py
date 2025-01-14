# tkinter GUI
# butona basılma durumunu ele alan pencere örneği
import tkinter as tk
klik_sayac=0 # klik_sayac değişkeni butona basılma sayısını tutan globla değişkendir
def btnklik(artim):     # butona basıldığında çağırılacak işlem fonksiyon
    global klik_sayac   # klik_sayac değişkeni butona basılma sayısını tutan globla değişkendir
    klik_sayac+=artim   # klik_sayac artır
    # etiket yazısını her klikle beraber güncelliyoruz
    lbl.config(text="Klik sayısı> "+format(klik_sayac)) 
    
root=tk.Tk()
root.title("buton pencere örneği")
root.geometry("300x200+200+100")
# Ekrana bir yazı (label) ekleyelim
lbl=tk.Label(root, text="Buton buraya")
# pencerenin görünmesi için pack() geometri yönetim metodunu kullanacağız
lbl.pack(pady=10) # dikeyde 10px aralıkla paketle
# butonumuzu oluşturalım
# nesnemizin command özelliği ile bir btnklik() fonksiyonu atıyoruz
# btnklik fonksiyonu artım parametresinin doğru aktarımı için lambda (isimsiz) fonksiyon olmak zorunda
btn=tk.Button(root, text="Bana Tıkla!", command=lambda: btnklik(1)) 
# buton widget (pencere aracı) görülmesi için pack() yapıyoruz
btn.pack()
# GUI ana program döngüsünü kuralım
# ana döngü tüm pencere ve pencere araçlarının güncellenmesi, 
# pencerelerde olay yakalanması ve işlenmesi için gereklidir
root.mainloop()
