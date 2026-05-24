import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({
    "hari_ke": [1, 2, 3, 4, 5],
    "jumlah_terjual": [8, 10, 12, 14, 16]
})

x = df[["hari_ke"]]
y = df["jumlah_terjual"]

m = LinearRegression().fit(x, y)
pred_8 = m.predict(pd.DataFrame([[8]], columns=x.columns))[0]

print("Koefisien:", m.coef_[0], "| Intersep:", m.intercept_)
print("Prediksi jumlah_terjual saat hari_ke=8", round(pred_8))