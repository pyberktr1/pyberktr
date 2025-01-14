# sözlüklerle çalışma
iklim={} # boş sözlük oluşturma
# anahtar ve karşılık şeklinde girdi ekleme
iklim["güneşli"]="3 ay"
iklim["yağmurlu"]="2 ay"
iklim["sisli"]="1 ay"
iklim["karlı"]="3 ay"
iklim["kurak"]="3 ay"
print(iklim["yağmurlu"])# yağmurlu anahtarının karşılığının yazdırılması
print(iklim)# tüm sözlük içeriğinin dökümü
iklim[0]="tanımsız" # 0 nolu anahtarın karşılığı tanımsız yapılıyor
print(iklim[0])
del iklim["kurak"]# bir anahtarın silinmesi
print(iklim)
#for döngüleri ile sözlükte gezinme
for i in iklim:
    print(i, ":",iklim[i])

