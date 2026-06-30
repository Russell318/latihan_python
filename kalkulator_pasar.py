# Kalkulator Harga Daging Sederhana
harga = {"daging_ayam": 17000, "daging_sapi": 23000, "daging_babi": 21000}
label_daging = {"daging_ayam": "Ayam", "daging_sapi": "Sapi", "daging_babi": "Babi"}
ayamtotal = 0.0
sapitotal = 0.0
babitotal = 0.0
total_keseluruhan = 0.0
sejarah_pembelian = []



print("=== Kalkulator Pasar ===")
print("Harga per kilogram:")
for jenis, nilai in harga.items():
    print(f"- {jenis}: Rp {nilai:,.0f} per kg")

while True:
    pilihan = input("\nApakah Anda akan menghitung harga daging? (Ya/Cukup): ").strip().title()
    if pilihan == "Cukup":
        print("\nRingkasan pembelian:")
        print(f"Total harga ayam: Rp {ayamtotal:,.0f}")
        print(f"Total harga sapi: Rp {sapitotal:,.0f}")
        print(f"Total harga babi: Rp {babitotal:,.0f}")
        print(f"Total harga keseluruhan: Rp {total_keseluruhan:,.0f}")
        print("Terima kasih telah berbelanja.")
        break
    if pilihan != "Ya":
        print("Pilihan tidak valid! Silakan pilih Ya atau Cukup.")
        continue

    print("Pilihan daging:")
    print("1. daging_ayam")
    print("2. daging_sapi")
    print("3. daging_babi")
    pilihan_daging = input("Masukkan pilihan daging (1=ayam, 2=sapi, 3=babi): ").strip()
    if pilihan_daging == "1":
        jenis_daging = "daging_ayam"
    elif pilihan_daging == "2":
        jenis_daging = "daging_sapi"
    elif pilihan_daging == "3":
        jenis_daging = "daging_babi"
    else:
        print("Pilihan daging tidak tersedia. Silakan coba lagi.")
        continue

    try:
        jumlah_kg = float(input("Masukkan jumlah (kg): "))
        if jumlah_kg <= 0:
            raise ValueError
    except ValueError:
        print("Jumlah harus angka positif. Silakan coba lagi.")
        continue

    total_harga = harga[jenis_daging] * jumlah_kg
    if jenis_daging == "daging_ayam":
        diskon_rate = 0.10 if jumlah_kg > 5 else 0.0
    elif jenis_daging == "daging_sapi":
        diskon_rate = 0.15 if jumlah_kg > 2 else 0.0
    else:
        diskon_rate = 0.12 if jumlah_kg > 3 else 0.0

    diskon = total_harga * diskon_rate
    total_bayar = total_harga - diskon
    total_keseluruhan += total_bayar
    if jenis_daging == "daging_ayam":
        ayamtotal += total_bayar
    elif jenis_daging == "daging_sapi":
        sapitotal += total_bayar
    elif jenis_daging == "daging_babi":
        babitotal += total_bayar

    diskon_label = f"{int(diskon_rate * 100)}%" if diskon_rate > 0 else "0%"
    sejarah_pembelian.append(
        f"{len(sejarah_pembelian) + 1}. {jumlah_kg:.2f} kg {label_daging[jenis_daging]} : Rp {total_harga:,.0f} diskon {diskon_label} Rp {total_bayar:,.0f}"
    )

    print("\n===== STRUK PEMBELIAN =====")
    print(f"Jenis daging        : {label_daging[jenis_daging]}")
    print(f"Harga per kg        : Rp {harga[jenis_daging]:,.0f}")
    print(f"Berat               : {jumlah_kg:.2f} kg")
    print(f"Total Harga         : Rp {total_harga:,.0f}")
    print(f"Diskon              : Rp {diskon:,.0f}")
    print(f"Total Pembayaran    : Rp {total_bayar:,.0f}")
    print("===========================\n")

    print("Daftar transaksi:")
    for baris in sejarah_pembelian:
        print(baris)
    print(f"\nTotal harga keseluruhan sementara: Rp {total_keseluruhan:,.0f}.")
    print("Silakan ulangi untuk hitung jenis lain, atau ketik 'Cukup' untuk keluar.")
