class Mahasiswa:
    def __init__(self, nama, nilai_rata_rata=0):
        self.nama = nama
        self.__nilai_rata_rata = nilai_rata_rata
        self.set_nilai_rata_rata(nilai_rata_rata)

    def get_nilai_rata_rata(self):
        return self.__nilai_rata_rata

    def set_nilai_rata_rata(self, remedi):
        if 0 <= remedi <= 100:
            self.__nilai_rata_rata = remedi
        else:
            print("Nilai harus antara 0 sampai 100")
    
    def status_kelulusan(self):
        if self.__nilai_rata_rata >= 80 and self.__nilai_rata_rata <= 100:
            return "Tuntas"
        elif self.__nilai_rata_rata < 80 and self.__nilai_rata_rata >= 0:
            return "Tidak tuntas"
        else:
            return "Nilai tidak valid"
    
    def tampil_info(self):
        print(f"\nNama Mahasiswa: {self.nama}")
        print(f"Nilai rata-rata: {self.get_nilai_rata_rata()}")
        print(f"Status: {self.status_kelulusan()}")
        
mahasiswa1 = Mahasiswa("Arkie", 212)

print(f"Nilai rata-rata awal {mahasiswa1.nama}:", mahasiswa1.get_nilai_rata_rata())
mahasiswa1.tampil_info()

mahasiswa1.set_nilai_rata_rata(98)

print(f"\nNilai rata-rata {mahasiswa1.nama} setelah remedial: {mahasiswa1.get_nilai_rata_rata()}")
mahasiswa1.tampil_info()
