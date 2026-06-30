import random


def tampilkan_pembuka():
    print("=== Game Tebak Angka ===")
    print("Saya memilih angka antara 1 sampai 20.")
    print("Coba tebak sebelum kehabisan 5 kesempatan!")
    print()


def dapatkan_tebakan():
    while True:
        tebakan = input("Masukkan tebakan Anda: ").strip()
        if not tebakan.isdigit():
            print("Masukkan angka yang valid.")
            continue
        return int(tebakan)


def main():
    angka_rahasia = random.randint(1, 20)
    kesempatan = 5

    tampilkan_pembuka()

    while kesempatan > 0:
        print(f"Sisa kesempatan: {kesempatan}")
        tebakan = dapatkan_tebakan()

        if tebakan == angka_rahasia:
            print("Selamat! Tebakan Anda benar.")
            break
        if tebakan < angka_rahasia:
            print("Terlalu kecil.")
        else:
            print("Terlalu besar.")

        kesempatan -= 1
        print()

    if kesempatan == 0 and tebakan != angka_rahasia:
        print(f"Maaf, kesempatan habis. Angka yang benar adalah {angka_rahasia}.")

    print("Terima kasih sudah bermain!")


if __name__ == '__main__':
    main()
