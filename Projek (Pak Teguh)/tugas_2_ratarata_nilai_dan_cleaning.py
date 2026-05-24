import pandas as pd
import numpy as np

df = pd.DataFrame({
    "nama": ["Adit", "Bima", "Cici", "Deni", "Adit"],
    "nilai": [80, np.nan, 70, 90, 80]
})

rata_sebelum = df["nilai"].mean()

df_bersih = df.drop_duplicates().copy()
df_bersih["nilai"] = df_bersih["nilai"].fillna(0)

rata_sesudah = df_bersih["nilai"].mean()

print("Nama: Alfian Nofriadi")
print("Kelas: X PPLG A\n")
print("Rata-rata sebelum cleaning: ", rata_sebelum)
print("Rata-rata sesudah cleaning: ", rata_sesudah)
print("\nData bersih:\n", df_bersih)