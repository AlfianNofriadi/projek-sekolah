import pandas as pd

df = pd.DataFrame({
    "nama_jajanan": ["Roti Coklat", "Risol", "Donat"],
    "harga": [5000, 3000, 4000],
    "jumlah_terjual": [40, 70, 50] 
})

df["total"] = df["harga"] * df["jumlah_terjual"]
top = df.loc[df["total"].idxmax()]

print(df)
print("\nJajanan total terbesar:")
print(top.to_string(index=False))