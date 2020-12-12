# Dasar-Pemrograman-Fricilia-dan-Triana
#program kasir sederhana
#Program Fricillia dan Triana

total1=0
total2=0
totalsemua=0
jenis1=""
jenis2=""

print("=== Program Kasir Sederhana Warung Laperpool ===")
nama = input("Masukkan nama Konsumen: ")
print ("Nama Konsumen :", nama)
print("")
print ("Menu Makanan")



def pilihan(i):
        switcher={
                1:'----Nasi Goreng 15000----',
                2:'----Soto 7000----',
                3:'----Mie Ayam 10000----'
             }
        return switcher.get(i,"Masukan Pilihan yang Benar!")


print("1. Nasi Goreng")
print("2. Soto")
print("3. Mie Ayam")
nomor=int(input("Masukan Pilihan: "))
menu=pilihan(nomor)
print (menu)
porsi1= int(input("Berapa Porsi: "))

if nomor==1:
    total1=total1+porsi1*15000
    print ("Hasilnya = ", total1)
    jenis1=("Nasi Goreng")
if nomor==2:
    total1=total1+porsi1*7000
    print ("Hasilnya = ", total1)
    jenis1=("Soto")
if nomor==3:
    total1=total1+porsi1*10000
    print ("Hasilnya = ", total1)
    jenis1=("Mie Ayam")
