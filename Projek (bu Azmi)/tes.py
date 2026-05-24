print("Nomor 2")
data = ("Jean", "Athar", "Eksha", "Juna", "Abay", "Ian", "Arshaka")
print("Banyak siswa:", len(data))


print("\nNomor 3")
nilai = (80, 85, 90, 75, 70, 44, 67, 89, 95, 60)
print(sum(nilai))


print("\nNomor 4")
rata_rata = (80, 85, 90, 80, 70, 44, 67, 90, 95, 80)
rata = sum(rata_rata) / len(rata_rata)
print("Nilai rata-rata:", rata)


print("\nNomor 5")
suhu = (35, 25, 30, 16, 28, 40, 20)
print("Suhu tertinggi:", max(suhu))
print("Suhu terendah:", min(suhu))


print("\nNomor 6")
ekskul_siswa = ("Futsal", "Basket", "Futsal", "Pramuka", "Futsal", "Voili", "Rohis", "Voli", "Futsal", "Basket", "Futsal")
print("Jumlah yang masuk di Ekskul Futsal:", ekskul_siswa.count("Futsal"))


print("\nNomor 7")
belanja = ["Beras", "Minyak", "Gula"]
belanja.append("Telur")
print("Daftar belanja:", belanja)


print("\nNomor 8")
nilai_uas = [45, 60, 90, 83, 98, 70, 55, 80, 92, 35]
nilai_uas.sort()    
print("Nilai UAS setelah diurutkan dari yang terkecil:", nilai_uas)


print("\nNomor 9")
hadir = ("H", "I", "I", "H", "I", "H", "H", "H", "I", "H")
print("Daftar kehadiran siswa:", hadir)
print("Jumlah siswa yang hadir:", hadir.count("H"))
print("Jumlah siswa yang tidak hadir:", hadir.count("I"))


print("\nNomor 10")
kelas_a = [80, 85, 72, 98, 89]
kelas_b = [75, 90, 88, 92, 80]
rata_kelas_a = sum(kelas_a) / len(kelas_a)
rata_kelas_b = sum(kelas_b) / len(kelas_b)

print("Rata-rata kelas A: ", rata_kelas_a)
print("Rata-rata kelas B: ", rata_kelas_b)

if rata_kelas_a > rata_kelas_b:
    print("Kelas A lebih baik dari kelas B.")
elif rata_kelas_a < rata_kelas_b:
    print("Kelas B lebih baik dari kelas A.")
else:
    print("Kelas A dan kelas B sama baik.")


print("\n")
class Mobil:
    def __init__(self, merk, kecepatan=0):
        self.merk = merk
        self.__kecepatan = kecepatan
    
    def get_kecepatan(self):
        return self.__kecepatan
    
    def set_kecepatan(self, kecepatan_baru):
        if kecepatan_baru >= 0 and kecepatan_baru <= 200:
            self.__kecepatan = kecepatan_baru
        else:
            print("Kecepatan tidak valid!")
    
    def tampil_info(self):
        print(f"Mobil: {self.merk}")
        print(f"Kecepatan: {self.get_kecepatan()} km/jam")

mobil1 = Mobil("Toyota", 60)

print("Merk mobil:", mobil1.merk)
print("Kecepatan sekarang:", mobil1.get_kecepatan())
mobil1.set_kecepatan(80)
mobil1.tampil_info()