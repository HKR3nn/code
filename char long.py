name  = input("masukan nama anda : ")
if len(name) <3 :
    print("nama terlalu pendek")
elif len(name) >= 50:
    print("nama terlalu panjang")
else:
    print("nama anda sudah sesuai")