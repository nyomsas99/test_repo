warna = [0,1,2,3,4,5,6,7,8,9]
resistan = [0.05,0.10,0.20]

c1 = str(input("Masukan warna pertama: "))
c2 = str(input("Masukan warna kedua: "))
c3 = str(input("Masukan warna ketiga: "))
c4 = str(input("Masukan warna ke empat: "))


if(c1 == "coklat" and c2 == "hitam"):
   result = warna[1] * warna[0] * warna[3] * resistan[0]
   print(result)
   