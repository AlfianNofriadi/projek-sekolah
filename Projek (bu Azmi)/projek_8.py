class mahasiswa:
    def __init__(self, nama, matkul, umur, nim):
        self.nama = nama
        self.matkul = matkul
        self.__umur = umur
        self.__nim = nim

    def get_umur(self):
        return self.__umur

    def get_nim(self):
        return self.__nim

    def info(self):
        print(f"Informasi Mahasiswa:")
        print(f"Nama: {self.nama}")
        print(f"Mata Kuliah: {self.matkul}")
        print(f"Umur: {self.get_umur()}")
        print(f"Nomor Induk Mahasiswa (NIM): {self.get_nim()}")

mahasiswa1 = mahasiswa("Arkie", "Teknik Informatika", 24, "T123456789")
mahasiswa2 = mahasiswa("Eksha", "Sastra Indonesia", 20, "S987654321")

mahasiswa1.info()
print("\n")
mahasiswa2.info()

response = input("\nApakah Anda ingin mencari data lain y/n: ")
if response == "y":
    username = input("Masukkan username: ")
    if username == "alfiann":
        mahasiswa_baru = mahasiswa("Alfian", "Teknik Informatika", 22, "T112233445")
        print("\nData berhasil ditemukan!")
        mahasiswa_baru.info()
    elif username == "eksha":
        mahasiswa_baru = mahasiswa("Eksha", "Sastra Indonesia", 20, "S987654321")
        print("\nData berhasil ditemukan!")
        mahasiswa_baru.info()
    elif username == "azra":
        mahasiswa_baru = mahasiswa("Azra", "Teknik Informatika", 21, "T998877665")
        print("\nData berhasil ditemukan!")
        mahasiswa_baru.info()
    else:
        print("Username tidak ditemukan/tidak dikenali")
else:
    print("Terima kasih!")