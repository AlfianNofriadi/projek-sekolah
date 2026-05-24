import numpy as np
import matplotlib.pyplot as plt

nilai = np.random.randint(50, 100, 100)

plt.hist(nilai, bins=10, color='lightgreen', edgecolor='black')
plt.title('Sebarkan Nilai Ujian')
plt.xlabel('Nilai')
plt.show()