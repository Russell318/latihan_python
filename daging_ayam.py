HARGA_DAGING = 17000

print("================================")
print("      PASAR DAGING ALI MAKMUR")
print("================================")

while True:
    pilihan = int(input("Apakah Anda akan menghitung harga ayam? (1=Ya, 0=Tidak): "))

    if pilihan == 0:
        print("\nTerima kasih telah berbelanja.")
        break

    if pilihan != 1:
        print("Pilihan tidak valid!\n")
        continue

    berat = float(input("Masukkan berat daging ayam (kg): "))

    total_harga = HARGA_DAGING * berat

    if berat > 5:
        diskon = 7000
    elif berat >= 2:
        diskon = 5000
    else:
        diskon = 0

    total_bayar = total_harga - diskon

    print("\n===== STRUK PEMBELIAN =====")
    print(f"Harga per kg      : Rp {HARGA_DAGING:,.0f}")
    print(f"Berat             : {berat:.0f} kg")
    print(f"Total Harga       : Rp {total_harga:,.0f}")
    print(f"Diskon            : Rp {diskon:,.0f}")
    print(f"Total Pembayaran  : Rp {total_bayar:,.0f}")
    print("===========================\n")