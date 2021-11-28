# Latihan List
## Tugas Latihan
- Buat sebuah list sebanyak 5 elemen dengan nilai bebas
```bash
a = [10, 11, 13, 16, 17]
```
### Akses list:
- tampilkan elemen ke 3
```bash
print(a[2])
```
output ![Gambar 01](Image/hasil1.PNG)<P>
- ambil nilai elemen ke 2 sampai elemen ke 4
```bash
print(a[1:4])
```
output ![Gambar 02](Image/hasil2.PNG)<p>
- ambil elemen terakhir
```bash
print(a[-1])
```
output ![Gambar 03](Image/hasil3.PNG)<p>
### Ubah elemen list:
- ubah elemen ke 4 dengan nilai lainnya
```bash
a[3] = 20
print(a)
```
output ![Gambar 04](Image/hasil4.PNG)<p>
- ubah elemen ke 4 sampai dengan elemen terakhir
```bash
a[3:] = [30, 22]
print(a)
```
output ![Gambar 05](Image/hasil5.PNG)<p>
### tambah elemen list:
- ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
```bash
b = a[0:2]
print (b)
```
output ![Gambar 06](Image/hasil6.PNG)<p>
- tambah list B dengan nilai string
```bash
b.append('belajar')
print(b)
```
output ![Gambar 07](Image/hasil7.PNG)<p>
- tambah list B dengan 3 nilai
```bash
b.extend([100, 30, 21])
print(b)
```
output ![Gambar 08](Image/hasil8.PNG)<p>
- gabungkan list B dengan list A
```bash
b.extend(a)
print(b)
```
output ![Gambar 09](Image/hasil9.PNG)<p>

### full my program
![Gambar 10](Image/program.PNG)<p>
- Output
![Gambar 11](Image/Hasil.PNG)<p>
# END