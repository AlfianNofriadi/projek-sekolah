class tiket_pesawat:
    def __init__(self, nama, tujuan, harga, stok):
        self.nama = nama
        self.tujuan = tujuan
        self.harga = harga
        self.stok = stok

    def info(self):
        return f"{self.nama} - {self.tujuan} - Rp{self.harga} - Stok: {self.stok}"
    

class kasir(tiket_pesawat):
    def __init__ (self, nama, tujuan, harga, stok):
        super().__init__(nama, tujuan, harga, stok)
        self.total = 0

    def beli(self, jumlah):
        harga_total = self.harga * jumlah
        self.total = harga_total
        if jumlah > self.stok:
            print(f"Stok tiket ke {self.tujuan} tidak cukup.")
        else:
            self.stok -= jumlah
            print(f"Beli {jumlah} tiket ke {self.tujuan}")
            print(f"Subtotal: Rp{harga_total}")
            print(f"Total sementara: Rp{self.total}")

beijing = kasir("Admin", "Beijing", 500000, 5)
new_york = kasir("Admin", "New York", 1000000, 3)

while True:
    user_name = str(input("\nMasukkan username Anda: "))
    password = str(input("Masukkan password Anda: "))

    if user_name in ["alfian", "eksha", "admin"]:
        if user_name == "alfian" and password == "15112009":
            print(f"Login sebagai admin berhasil! Selamat datang, {user_name}!")
        elif user_name == "eksha" and password == "20032010":
            print(f"Login sebagai admin berhasil! Selamat datang, {user_name}!")
        elif user_name == "admin" and password == "admin123":
            print(f"Login sebagai admin berhasil! Selamat datang, {user_name}!")
        else:
            back = input("Username atau password salah. Apakah Anda ingin mencoba lagi? (y/n): ")
            if back.lower() == 'y':
                continue
            else:
                print("Terima kasih! Sampai jumpa!")
                break
        kembali_ke_login = False
        while True:
            print("\nAnda memiliki akses ke semua fitur admin.")
            admin_menu = input("Apa yang ingin Anda lakukan? (Tambah Stok / Cek Stok / Keluar): ")
            if admin_menu.lower() == 'tambah stok':
                nama_tiket = input("Masukkan nama tiket yang ingin ditambahkan stoknya: ")
                jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin ditambahkan: "))
                if jumlah_tiket <= 0:
                    print("Jumlah tiket harus lebih dari 0.")
                    continue
                elif nama_tiket.lower() == "beijing":
                    beijing.stok += jumlah_tiket
                elif nama_tiket.lower() == "new york":
                    new_york.stok += jumlah_tiket
                else:
                    print("Nama tiket tidak ditemukan.")
                    continue
                print(f"Stok tiket {nama_tiket} berhasil ditambahkan sebanyak {jumlah_tiket}.")
                kembali_menu = input("Apakah Anda ingin kembali ke menu admin? (y/n): ")
                if kembali_menu.lower() == 'y':
                    continue
                elif kembali_menu.lower() == 'n':
                    print("Anda telah keluar dari menu admin dan kembali ke login.")
                    kembali_ke_login = True
                    break
            elif admin_menu.lower() == 'cek stok':
                print(f"Stok tiket Beijing: {beijing.stok}")
                print(f"Stok tiket New York: {new_york.stok}")
                kembali_menu = input("Apakah Anda ingin kembali ke menu admin? (y/n): ")
                if kembali_menu.lower() == 'y':
                    continue
                elif kembali_menu.lower() == 'n':
                    print("Anda telah keluar dari menu admin dan kembali ke login.")
                    kembali_ke_login = True
                    break
            elif admin_menu.lower() == 'keluar':
                print("Anda telah keluar dari menu admin dan kembali ke login.")
                kembali_ke_login = True
                break
            else:
                print("Menu tidak valid. Silakan pilih menu yang tersedia.")
                continue
        if kembali_ke_login:
            continue

    elif user_name in ["akthar", "justin", "jayden", "juna", "abay", "ian", "arshaka"]:
        print(f"Login sebagai user berhasil! Selamat datang, {user_name}!")
    else:
        back = input("Username atau password salah!. Apakah Anda ingin mencoba lagi? (y/n): ")
        if back.lower() == 'y':
            continue
        else:
            print("Terima kasih! Sampai jumpa!")
            break

    if user_name in ["akthar", "justin", "jayden", "juna", "abay", "ian", "arshaka"]:
        print("\nINFORMASI TIKET")
        print("1. Informasi Tiket")
        print(f"Beijing - Rp500000 - Stok: {beijing.stok}")
        print("2. Informasi Tiket")
        print(f"New York - Rp1000000 - Stok: {new_york.stok}")
        print("Apakah Anda ingin membeli tiket? (y/n): ")
        beli_tiket = input()
        if beli_tiket.lower() == 'y':
            pilih_tiket = input("Pilih tiket yang ingin dibeli (Beijing/New York): ")
            if pilih_tiket.lower() == "beijing":
                jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
                beijing.beli(jumlah_tiket)
            elif pilih_tiket.lower() == "new york":
                jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
                new_york.beli(jumlah_tiket)
        break
