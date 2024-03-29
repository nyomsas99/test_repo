while True:
    print("1.Hexa Decimal to Decimal\n2.Decimal to Hexadecimal\n3.Calculate Resistor\n4.konversi fahrenheit to Celcius\n5.Konversi Celcius to Fahrenheit\n6.exit")
    x = int(input("What want you to do?: "))
    if(x == 1):
        def hex_to_decimal(hex_number):
            try:
                decimal_number = int(hex_number, 16)
                return decimal_number
            except ValueError:
                print("Input tidak valid. Pastikan input merupakan bilangan heksadesimal yang benar.")

        hex_number = input("Masukkan bilangan heksadesimal: ")
        decimal_result = hex_to_decimal(hex_number)
        print('-----------------------------------')
        print(f"Hasil konversi: {decimal_result}")
        print('-----------------------------------')
    elif(x == 2):
        def decimal_to_hex(decimal_number):
            try:
                hex_number = hex(decimal_number).upper()[2:]
                return hex_number
            except ValueError:
                print("Input tidak valid. Pastikan input merupakan bilangan desimal yang benar.")
        decimal_number = int(input("Masukkan bilangan desimal: "))
        hex_result = decimal_to_hex(decimal_number)
        print('------------------------------')
        print(f"Hasil konversi: {hex_result}")
        print('------------------------------')
    elif(x == 3):
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
            print('-----------------------------------------')
            print(f"Nilai Total Resistor: {kiloOhm} kOhm")
            print('-----------------------------------------')
        else:
            print('--------------------------------------------')
            print(f"Nilai Total Resistor: {toleransi_value} ohm")
            print('--------------------------------------------')
    elif(x == 4):
        def fahrenheit_ke_celsius(fahrenheit):
            celsius = (fahrenheit - 32) * 5.0/9.0
            return celsius
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        celsius = fahrenheit_ke_celsius(fahrenheit)
        print('--------------------------------------------------------------------------')
        print(f"{fahrenheit} derajat Fahrenheit sama dengan {celsius:.2f} derajat Celsius")
        print('--------------------------------------------------------------------------')
    elif(x == 5):
        def celsius_ke_fahrenheit(celsius):
            fahrenheit = (celsius * 9.0/5.0) + 32
            return fahrenheit
        celsius = float(input("Masukkan suhu dalam Celsius: "))
        fahrenheit = celsius_ke_fahrenheit(celsius)
        print('--------------------------------------------------------------------------')
        print(f"{celsius} derajat Celsius sama dengan {fahrenheit:.2f} derajat Fahrenheit")
        print('--------------------------------------------------------------------------')
    else:
        break