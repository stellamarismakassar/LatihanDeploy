import pandas as pd

# Data jumlah rumah tangga per kecamatan
kecamatan_rumah_tangga = {
    "Mariso": 18137,
    "Mamajang": 18057,
    "Tamalate": 26187,
    "Rappocini": 8019,
    "Makassar": 10358,
    "Ujung pandang": 17325,
    "Wajo": 44039,
    "Bontoala": 10884,
    "Ujung Tanah": 44143,
    "Tallo": 57708,
    "Panakukang": 63010,
    "Manggala": 44366,
    "Biring Kanaya": 45465,
    "Tamanlarea": 32184,
    "Kepulauan Sangkarrang": 4272
}

# Rata-rata persentase penggunaan bahan bakar dalam pecahan desimal
persentase_listrik = 0.01025
persentase_lpg = 0.48412
persentase_minyak_tanah = 0.09608
persentase_briket = 0.01504
persentase_kayu = 0.36794

# Inisialisasi list untuk menyimpan data
data = []

# Menghitung penggunaan bahan bakar per kecamatan
for kecamatan, rumah_tangga in kecamatan_rumah_tangga.items():
    penggunaan_listrik = persentase_listrik * rumah_tangga
    penggunaan_lpg = persentase_lpg * rumah_tangga
    penggunaan_minyak_tanah = persentase_minyak_tanah * rumah_tangga
    penggunaan_briket = persentase_briket * rumah_tangga
    penggunaan_kayu = persentase_kayu * rumah_tangga
    
    data.append([kecamatan, penggunaan_listrik, penggunaan_lpg, penggunaan_minyak_tanah, penggunaan_briket, penggunaan_kayu])

# Membuat DataFrame pandas
df = pd.DataFrame(data, columns=["Kecamatan", "Penggunaan Listrik", "Penggunaan LPG", "Penggunaan Minyak Tanah", "Penggunaan Briket", "Penggunaan Kayu"])

# Menampilkan DataFrame sebagai tabel
print(df)
