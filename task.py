def hitung_vokal(kalimat):
    # Mengonversi kalimat menjadi huruf kecil untuk menghindari perbedaan antara huruf besar dan kecil
    kalimat = kalimat.lower()
    
    # Menginisialisasi variabel untuk menyimpan jumlah vokal
    jumlah_vokal = 0
    
    # Menggunakan loop untuk menghitung jumlah vokal
    for huruf in kalimat:
        if huruf in 'aeiou':
            jumlah_vokal += 1
    
    # Mengembalikan hasil jumlah vokal
    return jumlah_vokal

# Meminta pengguna untuk memasukkan kalimat
kalimat_input = input("Masukkan kalimat: ")

# Memanggil fungsi hitung_vokal dan menampilkan hasil
hasil = hitung_vokal(kalimat_input)
print("Jumlah huruf vokal dalam kalimat adalah:", hasil)
