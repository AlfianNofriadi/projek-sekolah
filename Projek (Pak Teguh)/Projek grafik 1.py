import matplotlib.pyplot as plt

bulan = ['Jan', 'Feb', 'Mar', 'Apr']
subs = [100, 200, 400, 600]

plt.plot(bulan, subs)
plt.title('Pertumbuhan Subscriber')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Subscriber')
plt.show()