import pandas as pd
import matplotlib.pyplot as plt

ringkas = pd.Series({"Latte":17, "Cappuccino":8, "Espresso":12})
ax = ringkas.plot(kind="bar", title="Total Penjualan per Rasa")
ax.set_xlabel("Rasa Kopi")
ax.set_ylabel("Jumlah Terjual")
plt.show()