def hitung_nilai_resistor(warna1, warna2, warna3, toleransi):
    nilai_warna = {
        'hitam': 0, 'coklat': 1, 'merah': 2, 'orange': 3, 'kuning': 4,
        'hijau': 5, 'biru': 6, 'ungu': 7, 'abu-abu': 8, 'putih': 9
    }

    nilai = (nilai_warna[warna1] * 10 + nilai_warna[warna2]) * 10 ** nilai_warna[warna3]
    toleransi_percent = {'emas': 5, 'perak': 10, 'tanpa warna': 20}

    toleransi_value = nilai * toleransi_percent[toleransi] / 100

    return nilai, toleransi_value

warna1 = input("Masukkan warna pertama: ").lower()
warna2 = input("Masukkan warna kedua: ").lower()
warna3 = input("Masukkan warna ketiga: ").lower()
toleransi = input("Masukkan toleransi (emas/perak/tanpa warna): ").lower()

nilai, toleransi_value = hitung_nilai_resistor(warna1, warna2, warna3, toleransi)

if(toleransi_value >= 1000 ):
   kiloOhm = toleransi_value / 1000
   print(f"Nilai Total Resistor: {kiloOhm} Kilo Ohm")
else:
   print(f"Nilai Total Resistor: {toleransi_value} ohm")
