import json
from pathlib import Path

MENU_PATH = Path(__file__).resolve().parent / 'menu.json'


def load_menu(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File menu tidak ditemukan: {path}")
    except json.JSONDecodeError as error:
        print(f"Gagal memuat menu: {error}")
    return {}


def build_products(menu_data):
    products = []
    for kategori, items in menu_data.items():
        for item in items:
            product = {
                'id': item['id'],
                'nama': item['nama'],
                'harga': item['harga'],
                'kategori': kategori
            }
            products.append(product)
    return products


def display_products(products):
    print('=== KASIR FISH&COW ===')
    print('Daftar Produk:')
    print('ID\tNama\t\tKategori\tHarga')
    print('-------------------------------------------------')
    for product in products:
        print(f"{product['id']}\t{product['nama']}\t{product['kategori']}\tRp {product['harga']:,.0f}")
    print()


def get_discount_rate(product_name, berat):
    nama = product_name.lower()
    if 'ayam' in nama and berat > 5:
        return 0.10
    if 'sapi' in nama and berat > 2:
        return 0.15
    if 'kambing' in nama and berat > 3:
        return 0.12
    if 'salmon' in nama and berat > 3:
        return 0.10
    if 'tuna' in nama and berat > 2:
        return 0.05
    if 'lele' in nama and berat > 5:
        return 0.10
    return 0.0


def print_receipt(cart):
    print('\n===== STRUK PEMBAYARAN =====')
    total_semua = 0
    for i, item in enumerate(cart, start=1):
        print(f"{i}. {item['berat']:.2f} kg {item['nama']} - Rp {item['subtotal']:,.0f} | Diskon {int(item['rate']*100)}% = Rp {item['discount']:,.0f} | Bayar Rp {item['total']:,.0f}")
        total_semua += item['total']
    print('-----------------------------')
    print(f"Total Bayar: Rp {total_semua:,.0f}")
    print('=============================')
    print('Terima kasih telah berbelanja di KASIR FISH&COW.')


def main():
    menu_data = load_menu(MENU_PATH)
    products = build_products(menu_data)
    if not products:
        return

    cart = []
    print('Selamat datang di kasir Fish & Cow!')

    while True:
        display_products(products)
        choice = input("Masukkan ID produk atau ketik 'selesai' untuk bayar: ").strip().lower()
        if choice == 'selesai':
            break
        if not choice.isdigit():
            print('Masukkan ID yang valid.')
            continue

        product_id = int(choice)
        selected = next((p for p in products if p['id'] == product_id), None)
        if not selected:
            print('Produk tidak ditemukan.')
            continue

        try:
            berat = float(input(f"Masukkan berat {selected['nama']} (kg): "))
            if berat <= 0:
                raise ValueError
        except ValueError:
            print('Berat harus angka positif.')
            continue

        subtotal = selected['harga'] * berat
        rate = get_discount_rate(selected['nama'], berat)
        discount = subtotal * rate
        total = subtotal - discount
        cart.append({
            'nama': selected['nama'],
            'berat': berat,
            'subtotal': subtotal,
            'rate': rate,
            'discount': discount,
            'total': total,
        })

        print(f"{selected['nama']} {berat:.2f} kg ditambahkan.")
        print(f"Subtotal: Rp {subtotal:,.0f}, Diskon {int(rate*100)}% = Rp {discount:,.0f}, Bayar: Rp {total:,.0f}\n")

    if cart:
        print_receipt(cart)
    else:
        print('Tidak ada produk yang dibeli.')


if __name__ == '__main__':
    main()
