import pandas as pd
from scipy.optimize import linear_sum_assignment

# Baca file CSV
df = pd.read_csv('dataset_assigment_10_10.csv', header=0)

cost_matrix = df.to_numpy()

# Mendapatkan hasil penugasan
row_ind, col_ind = linear_sum_assignment(cost_matrix)


# Inisialisasi total biaya
total_biaya: int = 0  # Total biaya

# Cetak hasil penugasan yang diurutkan berdasarkan pekerjaan (kolom)
for col, row in zip(col_ind, row_ind):
    biaya = cost_matrix[row, col]  
    print(f"Pekerja {row + 1} mengerjakan Tugas {col + 1} dengan biaya {biaya}")

    # Menambahkan biaya untuk perhitungan total biaya
    total_biaya += biaya

# Menampilkan total biaya yang diperlukan
print(f"Total biaya yang diperlukan: {total_biaya}")
