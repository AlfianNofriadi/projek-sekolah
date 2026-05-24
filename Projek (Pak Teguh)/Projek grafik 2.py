import matplotlib.pyplot as plt

kategori = ['Makan', 'Transportasi', 'Game', 'Nabung']
pengeluaran = [40, 30, 20, 10]

plt.pie(pengeluaran, labels = kategori, autopct='%1.1f%%')
plt.title('Pengeluaran Uang Jajan')
plt.show()