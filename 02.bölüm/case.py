# match case yapıları(sadece python 3.10 veya üstü yorumcularda çalışır)

num=int(input("bir menü nosu girin (1-5)"))

#match case
match num:
    case 1:
        print("Menu #1")
    case 2:
        print("Menu #2")
    case 3:
        print("Menu #3")
    case 4:
        print("Menu #4")
    case 5:
        print("Menu #5")
    case _:
        print("Hata! tekrar deneyiniz")

