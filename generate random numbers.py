import random


def togel():
    gatau = str(input("Mau angka togel ga ? (mau/tidak) : "))
    if gatau.lower () == 'mau':
        angka = ''.join([str(random.randint (0,9)) for _ in range (4)])
        print(f"nih angka togel {angka}")
    else:
        print("jangan main togel ya dek yaa")
while True:
    togel()
    ulang = input("Lagi ? (mau/ndak) : ")
    if ulang.lower() == 'mau':
        break
        
    