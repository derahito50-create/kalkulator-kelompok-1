print("Python, calculator kelompok 1")
print("Pilih nomor:")
print("1. Tambah (+)")
print("2. Kurang (-)")
print("3. Kali ()")
print("4. Bagi (/)")
print("5. Modulus (%)")
print("6. Eksponen (**)")


pilihan = input("Masukkan pilihan (1/2/3/4/5/6):")

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

if pilihan == "1":
    hasil = angka1 + angka2
    print(f"Hasil: {hasil:.0f}", )
elif pilihan == "2":
    hasil = angka1 - angka2
    print(f"Hasil: {hasil:.0f}")
elif pilihan == "3":
    hasil = angka1 angka2
    print(f"Hasil: {hasil:.0f}")
elif pilihan == "4":
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil: {hasil:.0f}")
    else:
        print("Tidak bisa dibagi 0")
elif pilihan == "5":
    hasil = angka1 % angka2
    print(f"Hasil: {hasil:.0f}")
elif pilihan == "6":
    hasil = angka1 ** angka2
    print(f"Hasil: {hasil:.0f}")
else:
    print("Input harus angka")
