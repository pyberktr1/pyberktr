# tkinter modülüyle grafik kullanıcı arabirimi (GUI) oluşturmak
import tkinter as tk # tkinter modülü tk nesnesi olarak kod içinde ele alınır
# Tk() sınıfını kullanarak bir ana pencere (root) oluşturalım
root=tk.Tk()
# nesnenin title özelliğini kullanarak ana pencereye bir başlık atayalım
root.title("ANA PENCERE")
# penceremizin pixel ölçüleri (x,y pixel)+x-poz+y-poz
root.geometry("500x300+200+100")# penceremiz 500 pixel geniş, 300 pixel yükseklik, 
                                # ekran sol üst köşeden 200 px aşağı 100px sağ tarafta
                                # oluşur
#root.config(height=300, width=500)# pencere ebadını değiştirmenin alternatif yolu
