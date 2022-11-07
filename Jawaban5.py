NIM= (input("Masukan NIM  : "))
Nama= (input("Masukan Nama : "))

print("   PILIHAN")
print("1. Capucino")
print("2. teh")
print("3. Exit")

nomor=int(input("Masukan Pilihan : "))

if nomor==1:
    print("Memilih Capucino")

elif nomor==2:
    print("Memilih teh")

elif nomor==3:
    print("Exit")

else:
    print("Pilihan anda tidak tersedia")

harga= float(input("Masukan harga : "))

PPN = (harga*0.10)
totalharga = (harga+PPN)

print("Total PPN : " , PPN)
print("Total yang harus di bayarkan : " , totalharga)