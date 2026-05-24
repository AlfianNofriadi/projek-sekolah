import random

choices = ["gunting","batu","kertas"]
pemain = input("Masukan (gunting, batu, atau kertas): ")
komputer = random.choice(choices)

if pemain == komputer:
    hasil = "Seri"
elif (pemain == "gunting" and komputer == "kertas") or (pemain == "batu" and komputer == "gunting") or (pemain == "kertas" and komputer == "batu"):
    hasil = "Pemain Menang"
else:
    hasil = "Komputer Menang"

print("Pemain memilih: ", pemain)
print("Komputer memilih: ", komputer)
print("Hasil: ", hasil)