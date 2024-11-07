import math
import random

def kalkulator():
    while True:
        print("\n===========================================")
        print("========== PROGRAM CALCULATOR =============")
        print("===========================================")

        print("PILIH OPERASI YANG KAMU INGINKAN:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Akar Kuadrat")
        print("6. Pangkat")
        print("7. Generate Random Number")
        print("8. Keluar")

        pilihan = int(input("Masukkan pilihanmu: "))

        if pilihan == 1:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
            hasil = angka1 + angka2
            print(f"\nHasil dari {angka1} + {angka2} = {hasil}")

        elif pilihan == 2:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
            hasil = angka1 - angka2
            print(f"\nHasil dari {angka1} - {angka2} = {hasil}")

        elif pilihan == 3:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
            hasil = angka1 * angka2
            print(f"\nHasil dari {angka1} * {angka2} = {hasil}")

        elif pilihan == 4:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
            if angka2 != 0:
                hasil = angka1 / angka2
                print(f"\nHasil dari {angka1} / {angka2} = {hasil}")
            else:
                print("\nError: Pembagian dengan nol tidak diperbolehkan.")

        elif pilihan == 5:
            angka = float(input("Masukkan angka: "))
            hasil = math.sqrt(angka)
            print(f"\nHasil akar kuadrat dari {angka} = {hasil}")

        elif pilihan == 6:
            angka1 = float(input("Masukkan angka pertama (basis): "))
            angka2 = float(input("Masukkan angka kedua (pangkat): "))
            hasil = math.pow(angka1, angka2)
            print(f"\nHasil dari {angka1} ^ {angka2} = {hasil}")

        elif pilihan == 7:
            random1 = int(input("Masukkan batas bawah: "))
            random2 = int(input("Masukkan batas atas: "))
            hasil = random.randint(random1, random2)
            print(f"\nAngka random yang kamu generate dari {random1} sampai {random2} adalah {hasil}")

        elif pilihan == 8:
            print("Terima kasih telah menggunakan kalkulator. Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")
            
kalkulator()
