nik_karyawan = [
    {'nama': 'ABI', 'nik': 20250001},
    {'nama': 'BUDI', 'nik': 20250002},
    {'nama': 'CACA', 'nik': 20250003}
]

token_jabatan = [
    {'jabatan': 'Helper', 'token': 500},
    {'jabatan': 'Engineer', 'token': 1000},
    {'jabatan': 'Superintendent', 'token': 2000}
]

warehouse_mro = [
    {'nama': 'Bolt Nut', 'stock': 1300, 'satuan' : 'Pasang', 'token': 1},
    {'nama': 'Elektroda', 'stock': 150, 'satuan' : 'Kawat', 'token': 2},
    {'nama': 'Pylox', 'stock': 20, 'satuan' : 'Botol', 'token': 3},
    {'nama': 'Grind Saw', 'stock': 30, 'satuan' : 'PCS', 'token': 4},
    {'nama': 'Rubber Pad', 'stock': 100, 'satuan' : 'Lembar', 'token': 5}
]

stock_opname = []

def menampilkan():
    print("\n Index |    Nama    |  Stock  |  Satuan |  Token  \n")
    for i, barang in enumerate(warehouse_mro):
        print(f"{i:<6} | {barang['nama']:<10} | {barang['stock']:<7} | {barang['satuan']:<7} | {barang['token']:<7}")

def menambahkan():
    nama = input("\nMasukkan Nama Barang: ")
    stock = int(input("Masukkan Stock Barang: "))
    satuan = input("Masukkan Satuan Jumlah: ")
    token = int(input("Masukkan Token: "))
    warehouse_mro.append({'nama': nama, 'stock': stock, 'satuan': satuan, 'token': token})

    menampilkan()

def menghapus():
    menampilkan()
    index = int(input("\nMasukkan index barang yang ingin dihapus: "))
    if 0 <= index < len(warehouse_mro):
        del warehouse_mro[index]        
        menampilkan()
    else:
        print("\nIndex tidak valid.")

def menampilkan_stock_opname():
    print("\nIsi Stock Opname Gudang: ")
    print("\n    Nama   |   Stock  |  Satuan |  Token  \n")
    for item in stock_opname:
        print(f"{item['nama']:<10} | {item['stock']:<7} | {item['satuan']:<10} | {item['token']:<7}")

def menampilkan_list_ambil():
    print("\nDaftar List Ambil:")
    print("\n    Nama   |   Stock  |  Satuan |  Token  \n")
    total_cost = 0
    for item in stock_opname:
        total_ambil = item['stock'] * item['token']
        print(f"{item['nama']}\t{item['stock']}\t{item['satuan']}\t{item['token']}\t{total_ambil}")
        total_cost += total_ambil
    print(f"Total Token yang Harus Dibayar = {total_cost}")
    return total_cost

def pengambilan_barang():
    """Pengambilan Barang"""
    menampilkan()
    index = int(input("\nMasukkan index barang yang ingin diambil: "))
    if 0 <= index < len(warehouse_mro):
        jumlah = int(input("Masukkan jumlah barang yang ingin diambil: "))
        if jumlah <= warehouse_mro[index]['stock']:
            warehouse_mro[index]['stock'] -= jumlah

            barang_di_gudang = None
            for item in stock_opname:
                if item['nama'] == warehouse_mro[index]['nama']:
                    barang_di_gudang = item
                    break
                
            if barang_di_gudang:
                barang_di_gudang['stock'] += jumlah
            else:
                stock_opname.append({'nama': warehouse_mro[index]['nama'], 'stock': jumlah, 'satuan': warehouse_mro[index]['satuan'], 'token': warehouse_mro[index]['token']})
            menampilkan_stock_opname()
        else:
            print(f"Stok tidak cukup, stock {warehouse_mro[index]['nama']} tersisa: {warehouse_mro[index]['stock']}")
            menampilkan_stock_opname()
    else:
        print("Index tidak valid.")
    
    lanjut = input("Mau ambil yang lain? (y/x) = ")
    if lanjut == "y":
        pengambilan_barang()

    kembalian = int()
    total_bayar = menampilkan_list_ambil()
    print("Silakan login:")
    print("0. Helper")
    print("1. Engineer")
    print("2. Superintendent\n")

    jab = int(input("Masukkan jabatan Anda: "))
    jumlah_token = token_jabatan[jab]['token']

    for kembalian in stock_opname:
        kembalian = jumlah_token - total_bayar
        if 1000 < total_bayar <= 2000 and jumlah_token <= 1000 :
            print("Jabatan minimal Superintendent")
            break
        elif 500 < total_bayar <= 1000 and jumlah_token <= 500 :
            print("Jabatan minimal Engineer")
            break
        elif total_bayar > 2000 :
            print("AKSES DITOLAK")
            break
        else :
            print(f"\nTerima kasih\nSisa token Anda : {kembalian}")
            break

def menu():
    while True:
        print("\nList Menu:")
        print("1. Menampilkan Daftar Barang")
        print("2. Menambah Barang")
        print("3. Menghapus Barang")
        print("4. Pengambilan Barang")
        print("5. Exit Warehouse\n")

        pilihan = input("Masukkan angka Menu yang ingin dijalankan: ")

        if pilihan == '1':
            menampilkan()
        elif pilihan == '2':
            menambahkan()
        elif pilihan == '3':
            menghapus()
        elif pilihan == '4':
            pengambilan_barang()
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid.")

def main():
    while True:
        print("\nWelcome to the Warehouse of")
        print("Maintenance Repair & Operations")
        print("\nPT. HYUNDAE MANUFACTURING, Ltd\n")
        print("Silakan login terlebih dahulu\n")

        masukan_nik = int(input("Masukkan NIK karyawan Anda : "))

        found = True
        for employee in nik_karyawan:
            if employee['nik'] == masukan_nik:
                print(f"Selamat datang {employee['nama']}")
                found = True
                menu()
            if not found:
                print(f"AKSES DITOLAK! Tidak ada NIK {masukan_nik}")

if __name__ == "__main__":
    main()
