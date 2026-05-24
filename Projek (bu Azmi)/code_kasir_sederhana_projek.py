class TiketPesawat:
    def __init__(self, nama, tujuan, harga, stok):
        self.nama = nama
        self.tujuan = tujuan
        self.harga = harga
        self.stok = stok

    def info(self):
        return f"{self.nama} - {self.tujuan} - Rp{self.harga} - Stok: {self.stok}"


class Kasir:
    def __init__(self):
        self.total = 0

    def beli(self, tiket, jumlah):
        if jumlah <= 0:
            print("Jumlah tiket harus lebih dari 0.")
            return

        if jumlah > tiket.stok:
            print(f"Stok tiket ke {tiket.tujuan} tidak cukup.")
            return

        subtotal = tiket.harga * jumlah
        tiket.stok -= jumlah
        self.total += subtotal

        print(f"Beli {jumlah} tiket ke {tiket.tujuan}")
        print(f"Subtotal: Rp{subtotal}")
        print(f"Total sementara: Rp{self.total}")


beijing = TiketPesawat("Alfian", "Beijing", 500000, 5)
new_york = TiketPesawat("Eksha", "New York", 1000000, 3)
kasir = Kasir()

print("KASIR SEDERHANA")
print("1. Informasi Tiket")
print(beijing.info())
print("\n2. Informasi Tiket")
print(new_york.info())

print("\n3. Beli")
print(beijing.info())
kasir.beli(beijing, 2)

print("\n4. Beli Lagi")
print(beijing.info())
kasir.beli(beijing, 1)

print("\nSELESAI!")
