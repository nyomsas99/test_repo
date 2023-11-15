stop = False
while True:
    Nama = input("Masukan Nama anda: ")
    NPM = int(input("Masukan npm anda: "))
    A = int(input("Masukan nilai absen: "))
    B = int(input("Masukan nilai tugas: "))
    C = int(input("Masukan nilai quis: "))
    D = int(input("Masukan nilai mid: "))
    E = int(input("Masukan nilai uas: "))
    Indexs = ["A","B","C","D","E"]
    grade = ["Sangat Baik","Baik","Cukup","Kurang","Sangat Kurang"]

    total_nilai = (A * 0.15) + (B * 0.2) + (C * 0.15) + (0.2 * D) + (E * 0.3)
    print(f"Hallo {Nama} dengan NPM {NPM} Total nilai anda adalah: {total_nilai}")


    if(total_nilai >= 80):
        print(f"Dengan indexs {Indexs[0]} dan grade {grade[0]}")
    elif(total_nilai >= 70 and total_nilai >= 79.99):
        print(f"Dengan indexs {Indexs[1]} dan grade {grade[1]}")
    elif(total_nilai >= 55 and total_nilai >= 69.99):
        print(f"Dengan indexs {Indexs[2]} dan grade {grade[2]}")
    elif(total_nilai >= 40 and total_nilai >= 54.99):
        print(f"Dengan indexs {Indexs[3]} dan grade {grade[3]}")
    elif(total_nilai < 40):
        print(f"Dengan indexs {Indexs[4]} dan grade {grade[4]}")