class pendaftaran:
    def __init__(self, nama, NIS, kelas):
        self.nama = nama
        self.__NIS = NIS
        self.kelas = kelas

    def get_NIS(self):
        return self.__NIS
    

class biodata(pendaftaran):
    def __init__(self, nama, NIS, kelas, tanggal_p, bulan_p, tahun_p):
        super().__init__(nama, NIS, kelas)
        self.tanggal_pendaftaran = tanggal_p
        self.bulan_pendaftaran = bulan_p
        self.tahun_pendaftaran = tahun_p
        self.biaya = biaya
    
    def info(self):
        print("\n----------Detail Pendaftaran----------")
        print(f"Nama: {self.nama}")
        print(f"NIS: {self.get_NIS()}")
        print(f"Kelas: {self.kelas}")
        print(f"Tanggal Pendaftaran: {self.tanggal_pendaftaran:02d}-{self.bulan_pendaftaran:02d}-{self.tahun_pendaftaran}")
        print(f"Biaya: Rp. {self.biaya}")

nama = str(input("\nNama Siswa: "))

while True:
    try:
        NIS = int(input("NIS: "))
        break
    except ValueError:
        print("Inputan harus berupa angka tanpa adanya huruf!")

print("\nDaftar Kelas:")
print("1. Reguler")
print("2. Olimpiade")
print("-" * 20)
while True:
    try:
        pilih_kelas = int(input("Kelas (1/2): "))
        if pilih_kelas == 1:
            kelas = "Reguler"
            biaya = 500000
            break
        elif pilih_kelas == 2:
            kelas = "Olimpiade"
            biaya = 750000
            break
        else:
            print("Kelas tidak valid.")
    except ValueError:
        print("Inputan harus berupa angka tanpa adanya huruf!")

while True:
    try:
        tanggal_p = int(input("Tanggal Pendaftaran (DD): "))
        break
    except ValueError:
        print("Inputan harus berupa angka tanpa adanya huruf!")

while True:
    try:
        bulan_p = int(input("Bulan Pendaftaran (MM): "))
        break
    except ValueError:
        print("Inputan harus berupa angka tanpa adanya huruf!")

while True:
    try:
        tahun_p = int(input("Tahun Pendaftaran (YYYY): "))
        break
    except ValueError:
        print("Inputan harus berupa angka tanpa adanya huruf!")

siswa = biodata(nama, NIS, kelas, tanggal_p, bulan_p, tahun_p)
siswa.info()