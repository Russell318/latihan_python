# Program Kriptografi Dasar Python
# Contoh ini menggunakan sandi Caesar untuk enkripsi dan dekripsi.


def caesar_encrypt(teks, geser):
    """Enkripsi teks menggunakan sandi Caesar dengan pergeseran geser."""
    hasil = []
    for karakter in teks:
        if karakter.isalpha():
            offset = 65 if karakter.isupper() else 97
            kode = ord(karakter) - offset
            kode = (kode + geser) % 26
            hasil.append(chr(kode + offset))
        else:
            hasil.append(karakter)
    return ''.join(hasil)


def caesar_decrypt(teks, geser):
    """Dekripsi teks sandi Caesar dengan pergeseran yang sama."""
    return caesar_encrypt(teks, -geser)


def main():
    print("=== Program Kriptografi Dasar ===")
    print("Pilih mode:")
    print("1. Enkripsi")
    print("2. Dekripsi")

    pilihan = input("Masukkan pilihan (1 atau 2): ").strip()
    if pilihan not in ('1', '2'):
        print("Pilihan tidak valid. Silakan jalankan ulang program.")
        return

    pesan = input("Masukkan pesan: ")
    try:
        geser = int(input("Masukkan nilai geser (0-25): "))
        if geser < 0 or geser > 25:
            raise ValueError
    except ValueError:
        print("Nilai geser harus berupa angka antara 0 dan 25.")
        return

    if pilihan == '1':
        hasil = caesar_encrypt(pesan, geser)
        print(f"Hasil enkripsi: {hasil}")
    else:
        hasil = caesar_decrypt(pesan, geser)
        print(f"Hasil dekripsi: {hasil}")

    print("\nCatatan: Non-huruf tetap tidak berubah.")


if __name__ == "__main__":
    main()
