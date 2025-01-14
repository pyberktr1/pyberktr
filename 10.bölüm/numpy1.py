# numpy modülü ile diziler üzerinde aritmetik işlemler gerçekleştirmek
import numpy as nm # modül nm adıyla kodun içinde kullanılır
# tek boyutlu bir dizi oluşturalım
a=nm.array([1, 2, 3, 4, 5, 6])
print(a)
# a dizisi elemanlarının toplam, ortalama, min ve max ını bulalım
print("TOPLAM  :",nm.sum(a))
print("ORTALAMA :",nm.mean(a))
print("MAX  :",nm.max(a))
print("MIN  :",nm.min(a))
# diziler üzerinde aritmetik işlemler eleman başına gerçekleşir
b=nm.array([1, 2, 3, 4, 5, 6])
c=a+b
d=a-b
e=a*b
print("\n")
print("TOPLAM\n",c)
print("FARK\n",d)
print("ÇARPIM\n",e)

# yeni bir dizi tanımlayalım
k=nm.arange(1,7)
print("\ndizi k:\n",k)
# aşağıdaki çarpımların her ikisinde de sonuçlar aynı olur ( a ve k birer dizidir, matrix değil)
# dolayısıyla çarpımda değişme özelliği vardır, çünkü işlem eleman başına gerçekleşir
print("\na*k=\n",a*k)
print("\nk*a=\n",k*a)

# bir diziyi matrix haline getirelim
p=nm.asmatrix(nm.atleast_2d(nm.arange(1,7)).T)

# matrix ler arasındaki çarpım işleminde değişim özelliği geçerli değildir
# aşağıdaki çarpımlar bir matrix çarpımıdır
print("\nmatrix p:\n",p)
print("\na*p=\n",a*p)
print("\np*a=\n",p*a)

