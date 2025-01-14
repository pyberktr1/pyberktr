# break ve continue deyimleri
# for döngüsünde break kullanımı

for i in "dersler":
    # i 'r' harfine eşit olduğunda döngüden çık
    if i == "r": 
        break
    else:
        print(i)

print("aynı işlemi continue ile yapalım")

for i in "dersler":
    # i 'r' harfine eşit olduğunda döngü başa sarsın
    if i == "r":
        continue
    else:
        print(i)
