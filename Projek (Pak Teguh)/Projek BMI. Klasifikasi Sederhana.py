br = float(input("Masukkan Berat badan (kg): "))
tb = float(input("Masukkan Tinggi badan (m): "))

BMI = br / (tb * tb)

if BMI < 18.5:
    kategori = "Kurus"
elif BMI < 25:
    kategori = "Normal"
else:
    kategori = "Gemuk"

print("BMI: ",BMI)
print("Kategori: ",kategori)