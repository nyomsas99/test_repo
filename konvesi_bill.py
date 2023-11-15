while True:
    print("1.Hexa Decimal to Decimal\n2.Decimal to Hexadecimal\n3.Exit")
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
        print(f"Hasil konversi: {decimal_result}")
    elif(x == 2):
        def decimal_to_hex(decimal_number):
            try:
                hex_number = hex(decimal_number).upper()[2:]
                return hex_number
            except ValueError:
                print("Input tidak valid. Pastikan input merupakan bilangan desimal yang benar.")
        decimal_number = int(input("Masukkan bilangan desimal: "))
        hex_result = decimal_to_hex(decimal_number)
        print(f"Hasil konversi: {hex_result}")
    else:
        exit()
