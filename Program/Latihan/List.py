#Membuat list sebanyak 5 elemen dengan nilai bebas
#akses list:
a = [10, 11, 13, 16, 17]
print(a[2]) #menampilakn elemen ke 3
print(a[1:4]) #mengambil nilai elemen ke 2 sampai ke 4
print(a[-1]) #mengambil elemen terakhir

#ubah elemen list:
#mengubah elemen ke 4
a[3] = 20
print(a)

#Mengubah elemen ke 4 sampai dengan elemen terakhir
a[3:] = [30, 22]
print(a)

#Tambah elemen list:
#ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
b = a[0:2]
print (b)

#Tambah list B dengan nilai string
b.append('belajar')
print(b)

#Tambah list B dengan 3 nilai
b.extend([100, 30, 21])
print(b)

#gabungkan list B dengan list A
b.extend(a)
print(b)