# kümelerle çalışma
set1={11, 21,33,44,55}          # küme tanımı
set2=set([23,77,67,12,11,21])   # diziyi kümeye dönüştürme
print("set1:",set1)
print("set2:",set2)
birlesim=set1|set2              # birleşim işlemi
print("birleşim:",birlesim)
kesisim=set1&set2               # kesişim işlemi
print("kesişim:",kesisim)
fark=set1-set2                  # fark işlemi
print("set1-set2:",fark)
fark=set2-set1                  # fark işleminde değişim özelliği
print("set2-set1:",fark)
set1.add(77)                    # kümeye yeni eleman ekleme
print(set1&set2)
set2.remove(11)                 # kümeden eleman silme
print(set1&set2)
