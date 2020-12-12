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
