import pandas as pd
from tabulate import tabulate

class Produk:
    def __init__(self, kode, nama, kategori, harga):
        self.kode = kode
        self.nama = nama
        self.kategori = kategori
        self.harga = harga

class KiosDigital:
    def __init__(self):
        self.produk_list = []
        self.transaksi_list = []
        self.load_produk()

    def load_produk(self):
        data_produk = [
            {'kode': 'P001', 'nama': 'Pulsa 10K', 'kategori': 'Pulsa', 'harga': 12000},
            {'kode': 'P002', 'nama': 'Pulsa 25K', 'kategori': 'Pulsa', 'harga': 27000},
            {'kode': 'P003', 'nama': 'Pulsa 50K', 'kategori': 'Pulsa', 'harga': 52000},
            {'kode': 'D001', 'nama': 'Data 3GB', 'kategori': 'Data', 'harga': 23000},
            {'kode': 'D002', 'nama': 'Data 5GB', 'kategori': 'Data', 'harga': 49000},
            {'kode': 'D003', 'nama': 'Data 12GB', 'kategori': 'Data', 'harga': 82000},
        ]

        for item in data_produk:
            produk = Produk(item['kode'], item['nama'], item['kategori'], item['harga'])
            self.produk_list.append(produk)

    def lihat_produk(self):
        data = []
        for produk in self.produk_list:
            data.append([produk.kode, produk.nama, produk.kategori, produk.harga])

        print(tabulate(data, headers=['Kode', 'Nama Produk', 'Kategori', 'Harga'], tablefmt='grid'))

class Transaksi:
    def __init__(self, nomor_hp):
        self.nomor_hp = nomor_hp
        self.belanjaan = []

    def tambah_produk(self, produk, qty):
        total_harga = produk.harga * qty
        self.belanjaan.append({'produk': produk, 'qty': qty, 'total_harga': total_harga})

    def hitung_total(self):
        total = 0
        for item in self.belanjaan:
            total += item['total_harga']
        return total

    def cetak_struk(self):
        print("===== Struk Pembelian =====")
        print(f"Nomor HP Pelanggan: {self.nomor_hp}")
        for i, item in enumerate(self.belanjaan, 1):
            produk = item['produk']
            qty = item['qty']
            harga_satuan = produk.harga
            total_harga = item['total_harga']
            print(f"{i}. {produk.nama} - {qty} x {harga_satuan} = {total_harga}")

        total_harga_keseluruhan = self.hitung_total()
        print(f"Total Harga Keseluruhan: {total_harga_keseluruhan}")

        pembayaran = 0
        while pembayaran < total_harga_keseluruhan:
            pembayaran += int(input("Masukkan jumlah pembayaran: "))
            if pembayaran < total_harga_keseluruhan:
                print(f"Jumlah pembayaran kurang. Total yang masih harus dibayar: {total_harga_keseluruhan - pembayaran}")

        kembalian = pembayaran - total_harga_keseluruhan
        print(f"Pembayaran berhasil! Uang kembalian: {kembalian}")
        print("===========================")
class Program:
    def __init__(self):
        self.kios_digital = KiosDigital()
        self.current_transaksi = None
        self.menu()

    def login(self):
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username == "admin" and password == "1234":
            print("Login berhasil!")
            return True
        else:
            print("Login gagal. Coba lagi.")
            return False

    def menu(self):
        if self.login():
            while True:
                print("\n===== Menu Pilihan =====")
                print("1. Lakukan Transaksi")
                print("2. Lihat Produk")
                print("3. Keluar Aplikasi")
                pilihan = input("Pilih menu (1/2/3): ")

                if pilihan == '1':
                    self.lakukan_transaksi()
                elif pilihan == '2':
                    self.kios_digital.lihat_produk()
                elif pilihan == '3':
                    print("Terima kasih! Aplikasi ditutup.")
                    break
                else:
                    print("Pilihan tidak valid. Coba lagi.")

    def lakukan_transaksi(self):
        nomor_hp = input("Masukkan nomor HP pelanggan: ")
        self.current_transaksi = Transaksi(nomor_hp)

        while True:
            self.kios_digital.lihat_produk()
            kode_produk = input("Masukkan kode produk ('selesai' untuk mengakhiri pembelian): ")

            if kode_produk.lower() == 'selesai':
                total_harga = self.current_transaksi.hitung_total()
                print(f"\nTotal harga yang harus dibayar: {total_harga}")
                self.current_transaksi.cetak_struk()
                self.kios_digital.transaksi_list.append(self.current_transaksi)
                break

            qty = int(input("Masukkan jumlah pembelian: "))
            produk = next((item for item in self.kios_digital.produk_list if item.kode == kode_produk), None)

            if produk:
                self.current_transaksi.tambah_produk(produk, qty)
                print(f"{produk.nama} ditambahkan ke keranjang.")
            else:
                print("Kode produk tidak valid. Coba lagi.")

if __name__ == "__main__":
    Program()