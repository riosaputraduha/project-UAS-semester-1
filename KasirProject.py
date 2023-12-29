import pandas as pd
import os
import random
from tabulate import tabulate

class Pulsa:    # Kelas Pulsa // identitas Pulsa
    def __init__(self, id, tipe_pulsa, harga, nominal):
        self.id = id
        self.tipe_pulsa = tipe_pulsa
        self.harga = harga
        self.nominal = nominal

class PaketDataInternet:    # Kelas Paket Data Internet // identitas Paket Data Internet
    def __init__(self, id_internet, tipe_paket, harga, nominal):
        self.id_internet = id_internet
        self.tipe_paket = tipe_paket
        self.harga = harga
        self.nominal = nominal

class TokenListrik:     # Kelas Token Listrik // identitas Token Listrik
    def __init__(self, id_listrik, tipe_listrik, harga, nominal):
        self.id_listrik = id_listrik
        self.tipe_listrik = tipe_listrik
        self.harga = harga
        self.nominal = nominal

class Transaksi:    # Kelas Transaksi // identitas transaksi untuk cetak struk
    def __init__(self, id_transaksi, tipe_produk, harga, nominal_bayar, kembalian, nomor_hp, kode_token=None):
        self.id_transaksi = id_transaksi
        self.tipe_produk = tipe_produk
        self.harga = harga
        self.nominal_bayar = nominal_bayar
        self.kembalian = kembalian
        self.nomor_hp = nomor_hp
        self.kode_token = kode_token

class Kasir:    # Program yang akan di jalankan di 'Kelas Kasir'
    def __init__(self):
        self.pulsa_list = []    # Memasukan data pulsa
        self.token_listrik_list = []    # Memasukan data token listrik
        self.paket_internet_list = []   # Memasukan data paket data internet
        self.transaksi = []     # Menyimpan data transaksi
        self.transaksi_internet = []    # Menyimpan data transaksi paket data internet
        self.transaksi_listrik = []     # Menyimpan data transaksi token listrik
        self.masuk = False
        
    def login(self, username, password):    # Proses login
        if username == 'admin1' and password == 'admin1':
            self.masuk = True
            print("Login berhasil.")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("Login gagal. Username atau password salah.")
            
    def sudah_masuk(self):  # Pernyataan jika sudah login
        return self.masuk
    
    def main_menu(self):
        print('\n')
        table = [
            ["1. Bayar Pulsa"],
            ["2. Bayar Paket Internet"],
            ["3. Bayar Listrik"],
            ["4. Tampilkan Daftar Produk"],
            ["5. Lihat Catatan Transaksi"],
            ["6. Keluar"]
        ]
        headers = ["\n      COUNTER PULSA       "]
        print(tabulate(table, headers, tablefmt="grid"))

    def tambah_pulsa(self, id, tipe_pulsa, harga, nominal): # Proses memasukan data pulsa
        pulsa = Pulsa(id, tipe_pulsa, harga, nominal)
        self.pulsa_list.append(pulsa)

    def cari_pulsa(self, id):   # Proses mencari pulsa dalam data berdasarkan ID
        for pulsa in self.pulsa_list:
            if pulsa.id == id:
                return pulsa
        return None
    
    def tambah_paket_internet(self, id_internet, tipe_paket, harga, nominal):   # Proses memasukan data paket data internet
        paket_data = PaketDataInternet(id_internet, tipe_paket, harga, nominal)
        self.paket_internet_list.append(paket_data)
    
    def cari_paket_data_internet(self, id_internet):    # Proses mencari paket data internet dalam data berdasarkan ID
        for paket_data in self.paket_internet_list:
            if paket_data.id_internet == id_internet:
                return paket_data
        return None

    def tambah_token_listrik(self, id_listrik, tipe_listrik, harga, nominal):   # Proses memasukan data token listrik
        token_listrik = TokenListrik(id_listrik, tipe_listrik, harga, nominal)
        self.token_listrik_list.append(token_listrik)

    def cari_token_listrik(self, id_listrik):   # Proses mencari token listrik dalam data berdasarkan ID
        for token_listrik in self.token_listrik_list:
            if token_listrik.id_listrik == id_listrik:
                return token_listrik
        return None
    
    def tampilkan_daftar_pulsa(self):      # Proses menampilkan data pulsa
        data = [[pulsa.id, pulsa.tipe_pulsa, pulsa.harga, pulsa.nominal] for pulsa in self.pulsa_list]
        df = pd.DataFrame(data, columns=['ID', 'Tipe Pulsa', 'Harga', 'Nominal'])
        print("\nDaftar Pulsa yang Tersedia:")
        print(df)
    
    def tampilkan_daftar_paket_data_internet(self):      # Proses menampilkan data paket data internet
        data = [[paket_data.id_internet, paket_data.tipe_paket, paket_data.harga, paket_data.nominal] for paket_data in self.paket_internet_list]
        df = pd.DataFrame(data, columns=['ID', 'Tipe Paket Internet', 'Harga', 'Nominal'])
        print("\nDaftar Paket Internet yang Tersedia:")
        print(df)
    
    def tampilkan_daftar_token_listrik(self):      # Proses menampilkan data token listrik
        data = [[token_listrik.id_listrik, token_listrik.tipe_listrik, token_listrik.harga, token_listrik.nominal] for token_listrik in self.token_listrik_list]
        df = pd.DataFrame(data, columns=['ID', 'Tipe', 'Harga', 'Nominal'])
        print("\nDaftar Token Listrik yang Tersedia:")
        print(df)

    def generate_kode_token(self):     # Proses membuat kode token listrik 
        kode_token = random.randint(1000000000000000, 9999999999999999) # Membuat kode token acak dengan jumlah digit 16
        return kode_token
    
    def tambah_transaksi(self, id_pulsa, tipe_pulsa, harga, nominal_bayar, kembalian, nomor_hp):    # Proses pencatatan transaksi pulsa
        transaksi = {
            'ID Pulsa': id_pulsa,
            'Tipe Pulsa': tipe_pulsa,
            'Harga': harga,
            'Nominal Bayar': nominal_bayar,
            'Kembalian': kembalian,
            'Nomor HP': nomor_hp  # Menambahkan nomor HP ke dalam riwayat transaksi
        }
        self.transaksi.append(transaksi)

    def tambah_transaksi_internet(self, id_internet, tipe_paket, harga, nominal_bayar, kembalian, nomor_hp):    # Proses pencatatan transaksi paket data internet
        transaksi = {
            'ID Pulsa': id_internet,
            'Tipe Paket Internet': tipe_paket,
            'Harga': harga,
            'Nominal Bayar': nominal_bayar,
            'Kembalian': kembalian,
            'Nomor HP': nomor_hp  # Menambahkan nomor HP ke dalam riwayat transaksi
        }
        self.transaksi_internet.append(transaksi)

    def tambah_transaksi_listrik(self, id_listrik, tipe_listrik, harga, nominal_bayar, kembalian, nomor_meter, kode_token):     # Proses pencatatan transaksi token listrik
        transaksi_listrik = {
            'ID Token' : id_listrik,
            'Tipe' : tipe_listrik,
            'Harga' : harga,
            'Nominal' : nominal_bayar,
            'Kembalian' : kembalian,
            'Nomor Meteran' : nomor_meter,
            'kode token' : kode_token # Menambahkan Nomor Meter ke dalam riwayat transaksi
        }
        self.transaksi_listrik.append(transaksi_listrik)
        
    def lihat_transaksi(self):      # Proses menampilkan data catatan transaksi
        if not self.transaksi and not self.transaksi_internet and not self.transaksi_listrik:
            print("Belum ada transaksi yang dilakukan.")
        else:
            if self.transaksi:
                print("\nDaftar Transaksi Pulsa:")
                df_transaksi = pd.DataFrame(self.transaksi)
                print(df_transaksi)     # Menampilkan catatan transaksi pulsa

            if self.transaksi_internet:
                print("\nDaftar Transaksi Internet:")
                df_transaksi_internet = pd.DataFrame(self.transaksi_internet)
                print(df_transaksi_internet)   # Menampilkan catatan transaksi paket data internet
            
            if self.transaksi_listrik:
                print("\nDaftar Transaksi Listrik:")
                df_transaksi_listrik = pd.DataFrame(self.transaksi_listrik)
                print(df_transaksi_listrik)     # Menampilkan catatan transaksi token listrik


    def bayar_pulsa(self, id, nominal_bayar): # Proses melakukan transaksi pulsa
        pulsa = self.cari_pulsa(id)
        if pulsa and nominal_bayar >= pulsa.harga:
            nomor_hp = input("Masukkan nomor HP: ")  # Meminta nomor HP dari pengguna
            kembalian = nominal_bayar - pulsa.harga
            print(f"Anda telah berhasil membeli pulsa {pulsa.tipe_pulsa} seharga Rp{pulsa.harga}")
            print(f"Kembalian anda adalah Rp{kembalian}")

            # Menambahkan catatan transaksi setelah pembelian berhasil
            transaksi = self.tambah_transaksi(pulsa.id, pulsa.tipe_pulsa, pulsa.harga, nominal_bayar, kembalian, nomor_hp)
            # Memasukan hasil transaksi dan mencetak nya ke dalam struk
            struk = Transaksi(pulsa.id, pulsa.tipe_pulsa, pulsa.harga, nominal_bayar, kembalian, nomor_hp)
            # Mencetak struk transaksi
            self.cetak_struk(struk)
        elif pulsa:
            print("Nominal yang anda masukkan kurang.")
        else:
            print("ID tidak ditemukan.")
    
    def bayar_paket_data_internet(self, id, nominal_bayar): # Proses melakukan transaksi paket data internet
        paket_data_internet = self.cari_paket_data_internet(id)
        if paket_data_internet and nominal_bayar >= paket_data_internet.harga:
            nomor_hp = input("Masukkan nomor HP: ") # Meminta nomor HP dari pengguna
            kembalian = nominal_bayar - paket_data_internet.harga
            print(f"Anda telah berhasil membeli paket data internet {paket_data_internet.tipe_paket} seharga Rp{paket_data_internet.harga}")
            print(f"Kembalian anda adalah Rp{kembalian}")

            # Menambahkan catatan transaksi setelah pembelian berhasil
            transaksi_internet = self.tambah_transaksi_internet(paket_data_internet.id_internet, paket_data_internet.tipe_paket, paket_data_internet.harga, nominal_bayar, kembalian, nomor_hp)
            # Memasukan hasil transaksi dan mencetak nya ke dalam struk
            struk_internet = Transaksi(paket_data_internet.id_internet, paket_data_internet.tipe_paket, paket_data_internet.harga, nominal_bayar, kembalian, nomor_hp)
            # Mencetak struk transaksi
            self.cetak_struk_internet(struk_internet)
        elif paket_data_internet:
            print("Nominal yang anda masukkan kurang.")
        else:
            print("ID tidak ditemukan.")

    def bayar_token_listrik(self, id_listrik, nominal_bayar): # Proses melakukan transaksi token listrik
        token_listrik = self.cari_token_listrik(id_listrik)
        if token_listrik and nominal_bayar >= token_listrik.harga:
            nomor_meter = input("Masukkan nomor meter listrik: ") # Meminta nomor meter listrik dari pengguna
            kode_token = self.generate_kode_token() # Membuat kode token listrik baru
            kembalian = nominal_bayar - token_listrik.harga
            print(f"Anda telah berhasil membeli token listrik {token_listrik.tipe_listrik} seharga Rp{token_listrik.harga}")
            print(f"Kode token listrik anda adalah: {kode_token}")
            print(f"Kembalian anda adalah Rp{kembalian}")

            # Menambahkan catatan transaksi setelah pembelian berhasil
            transaksi_listrik = self.tambah_transaksi_listrik(token_listrik.id_listrik, token_listrik.tipe_listrik, token_listrik.harga, nominal_bayar, kembalian, nomor_meter, kode_token)
            # Memasukan hasil transaksi dan mencetak nya ke dalam struk
            struk_listrik = Transaksi(token_listrik.id_listrik, token_listrik.tipe_listrik, token_listrik.harga, nominal_bayar, kembalian, nomor_meter, kode_token)
            # Mencetak struk transaksi
            self.cetak_struk_token_listrik(struk_listrik)
        elif token_listrik:
            print("Nominal yang Anda masukkan kurang.")
        else:
            print("ID tidak ditemukan")

    def cetak_struk(self, struk):   # Proses melakukan pencetakan struk pulsa dari kelas Transaksi
        """Proses mencetak struk transaksi."""
        data = [
            ["ID Pulsa", struk.id_transaksi],
            ["Tipe Pulsa", struk.tipe_produk],
            ["Harga", f"Rp{struk.harga}"],
            ["Nominal Bayar", f"Rp{struk.nominal_bayar}"],
            ["Kembalian", f"Rp{struk.kembalian}"],
            ["Nomor HP", struk.nomor_hp]
        ]

        print("\nStruk Transaksi:")
        print(tabulate(data, headers=['', ''], tablefmt="plain"))
    
    def cetak_struk_internet(self, struk_internet):   # Proses melakukan pencetakan struk paket data internet dari kelas Transaksi
        """Proses mencetak struk transaksi."""
        data = [
            ["ID Pulsa", struk_internet.id_transaksi],
            ["Tipe Pulsa", struk_internet.tipe_produk],
            ["Harga", f"Rp{struk_internet.harga}"],
            ["Nominal Bayar", f"Rp{struk_internet.nominal_bayar}"],
            ["Kembalian", f"Rp{struk_internet.kembalian}"],
            ["Nomor HP", struk_internet.nomor_hp]
        ]
        
        print("\nStruk Transaksi:")
        print(tabulate(data, headers=['', ''], tablefmt="plain"))

    def cetak_struk_token_listrik(self, struk_listrik):   # Proses melakukan pencetakan struk token listrik dari kelas Transaksi
        """Proses mencetak struk transaksi."""
        data = [
            ["ID", struk_listrik.id_transaksi],
            ["Tipe", struk_listrik.tipe_produk],
            ["Harga", f"Rp{struk_listrik.harga}"],
            ["Nominal Bayar", f"Rp{struk_listrik.nominal_bayar}"],
            ["Kembalian", f"Rp{struk_listrik.kembalian}"],
            ["Kode Token Listrik", struk_listrik.kode_token]
        ]
        print("\nStruk Transaksi:")
        print(tabulate(data, headers=['', ''], tablefmt="plain"))

# Contoh penggunaan program
kasir = Kasir()
# Menambahkan data pulsa
kasir.tambah_pulsa(1, "XL", 12000, 10000)
kasir.tambah_pulsa(2, "Indosat", 22000, 20000)
kasir.tambah_pulsa(3, "Axis", 52000, 50000)
# Menambahkan data paket data internet
kasir.tambah_paket_internet(1, "Hemat XL", 15000, "5GB")
kasir.tambah_paket_internet(2, "Combo Indosat", 47000, "15GB")
kasir.tambah_paket_internet(3, "Super Combo Axis", 77000, "50GB")
# Menambahkan data token listrik
kasir.tambah_token_listrik(1, "PLN", 52000, 50000)
kasir.tambah_token_listrik(2, "PLN", 102000, 100000)
kasir.tambah_token_listrik(3, "PLN", 152000, 150000)

# Eksekusi program nya
while True:
    if not kasir.sudah_masuk():
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        kasir.login(username, password)
        if not kasir.sudah_masuk():
            continue
    
    kasir.main_menu()
    pilihan = int(input("Silakan pilih opsi: "))

    if pilihan == 1:
        id = int(input("Masukkan ID pulsa yang ingin dibeli: "))
        nominal_bayar = int(input("Masukkan nominal yang ingin dibayarkan: "))
        kasir.bayar_pulsa(id, nominal_bayar)
    elif pilihan == 2:
        id_internet = int(input("Masukkan ID Paket Internet yang ingin dibeli: "))
        nominal_bayar = int(input("Masukkan nominal yang ingin dibayarkan: "))
        kasir.bayar_paket_data_internet(id_internet, nominal_bayar)
    elif pilihan == 3:
        id_listrik = int(input("Masukkan ID Token Listrik yang ingin dibeli: "))
        nominal_bayar = int(input("Masukkan nominal yang ingin dibayarkan: "))
        kasir.bayar_token_listrik(id_listrik, nominal_bayar)
    elif pilihan == 4:
        ''' Menampilkan daftar produk pulsa'''
        kasir.tampilkan_daftar_pulsa()
        ''' Menampilkan daftar produk paket data internet'''
        kasir.tampilkan_daftar_paket_data_internet()
        ''' Menampilkan daftar produk token listrik'''
        kasir.tampilkan_daftar_token_listrik()
    elif pilihan == 5:
        kasir.lihat_transaksi()
    elif pilihan == 6:
        print("Terima kasih telah berbelanja disini, sampai jumpa kembali.")
        break
    else:
        print("Maaf, opsi yang Anda pilih tidak tersedia. Silakan pilih opsi yang lain.")
