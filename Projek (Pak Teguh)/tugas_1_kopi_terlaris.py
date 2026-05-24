import pandas as pd

df = pd.DataFrame({
    "rasa_kopi": ["Latte", "Cappucino", "Expreso", "Latte"],
    "jumlah_terjual": [10, 8, 12, 7]
})

ringkas = df.groupby("rasa_kopi")["jumlah_terjual"].sum()
kopi_terlaris = ringkas.idxmax()

print("Nama: Alfian Nofriadi")
print("Kelas: X PPLG A\n")
print("Ringkas per rasa: ")
print(ringkas.to_string())
print("Kopi terlaris adalah",kopi_terlaris)