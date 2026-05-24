import pandas as pd

makanan_favorit = ["Mie ayam", "Sate", "Mie", "Ayam", "Bakso", "Nasi goreng", "Seblak"]
minuman_favorit = ["Matcha", "Kopi", "Coklat susu", "Es coklat", "cappucino", 
                   "Air dingin", "Teh es", "Milo", "Air putih", "Green tea", "Americano"]

makanan = [0, 1, 2, 3, 4, 0, 2, 5, 0, 0, 5, 3, 0, 0, 5, 6]
minuman = [0, 1, 2, 3, 4, 5, 0, 2, 0, 6, 7, 8, 9, 2, 10, 0]

nama = [
    "Alfian", "Langkar", "Aditya", "M. Bahi", "Naila",
    "Putri", "Ainun", "Handra", "Aulia", "Septian",
    "Marco", "M. Ramadhan Rhay", "Sami", "Dede", "Morino", "Safa"
]

df = pd.DataFrame({
    "Nama": nama,
    "Makanan": [makanan_favorit[a] for a in makanan]
    ,"Minuman": [minuman_favorit[a] for a in minuman]
})

print("Tabel makanan dan minuman favorit")
print(df)

print()
makanan_favorit = df["Makanan"].value_counts().idxmax()
print("Makanan terfavorit:", makanan_favorit)
minuman_favorit = df["Minuman"].value_counts().idxmax()
print("Makanan terfavorit:", minuman_favorit)
