# liste kullanımı
lst=range(1,10,1)   # 1-9 arası 1 artımlı seri oluşturma
print(len(lst))     # liste uzunluğu (eleman sayısı)
print(lst[2])       # 3 nolu elemanı yazdır
print(lst)          # tüm listeyi yazdır
lst2=lst[2:7:2]     # listeyi kıyarak yeni liste oluşturma
                    
print(lst2)         # kıyılmış listeyi yazdır
print(len(lst2))    # kıyılmış liste boyu
print(lst[::-1])    # lst sıralamasını tersle
print(lst[3::2])    # 4. elemandan sona kadar 2 atlayarak
print(lst[:7:3])    # ilk elemandan 7 elemana kadar 3 atlayarak
lst3="AKDENİZ KARADENİZ"    # string listesi
print(lst3)                 # tüm üyeleri yaz
print(lst3[:5])             # baştan 5. karakatere kadar yaz
print(lst3[::2])            # baştan sona 2 atlayarak yaz
print(lst3[::-1])           # ters sırada yaz
# bir range nesnesine append yapmaya çalışmak genel bir hatadır
# önce range nesnesinin bir listeye dönüştürülmesi gerekir
# aşağıdaki satırları değiştirerek denemeler yapın
lst2=[lst2]#, lst, 12, 45, -7] 
lst2.append(77)
print(lst2)
lst3=lst3+" MARMARA EGE"
print(lst3)
lst3=[lst3]
lst3.append(66)
print(lst3)
