import numpy as np
import matplotlib.pyplot as plt

# Data penduduk Indonesia tahun 2011-2021 (dalam jutaan)
tahun = np.array([2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])
penduduk = np.array([242.3, 245.8, 249.9, 254.5, 259.1, 263.5, 267.7, 271.1, 274.5, 277.7, 280.0])

# Fungsi pertumbuhan eksponensial
def eksponensial(t, A, r):
    return A * np.exp(r * (t - tahun[0]))

# Estimasi parameter pertumbuhan eksponensial
from scipy.optimize import curve_fit
params, covariance = curve_fit(eksponensial, tahun, penduduk, p0=[penduduk[0], 0.01])

A, r = params  # Parameter A adalah jumlah penduduk awal, r adalah tingkat pertumbuhan

# Prediksi penduduk untuk tahun-tahun berikutnya
tahun_prediksi = np.arange(2022, 2031)
penduduk_prediksi = eksponensial(tahun_prediksi, A, r)
print(penduduk_prediksi)
# Menampilkan hasil
# plt.figure(figsize=(10, 6))
# plt.plot(tahun, penduduk, 'o', label='Data Penduduk (2011-2021)')
# plt.plot(tahun_prediksi, penduduk_prediksi, 'r-', label='Prediksi Penduduk (2022-2030)')
# plt.xlabel('Tahun')
# plt.ylabel('Jumlah Penduduk (jutaan)')
# plt.title('Prediksi Jumlah Penduduk Indonesia')
# plt.legend()
# plt.grid(True)
# plt.show()
