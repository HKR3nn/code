buku_perpustakaan = {
    "Buku A": {"volume": 5, "status": ["available"] * 5},
    "Buku B": {"volume": 3, "status": ["available"] * 3},
    "Buku C": {"volume": 2, "status": ["available", "available"]},
    "Buku D": {"volume": 4, "status": ["available"] * 4},
}

def tampilkan_buku():
    print("\nDaftar Buku Perpustakaan:")
    for buku, info in buku_perpustakaan.items():
        print(f"{buku} - Volume: {info['volume']}, Status: {info['status']}")
def pinjam_buku():
    buku = input("\nMasukkan nama buku yang ingin dipinjam: ")
    
    if buku in buku_perpustakaan:
        info_buku = buku_perpustakaan[buku]
        if "available" in info_buku["status"]:
            for i in range(info_buku["volume"]):
                if info_buku["status"][i] == "available":
                    info_buku["status"][i] = "not available"
                    print(f"Anda telah meminjam {buku} - Volume {i+1}")
                    break
        else:
            print(f"Maaf, semua volume dari {buku} telah dipinjam.")
    else:
        print(f"Buku {buku} tidak ditemukan di perpustakaan.")
def kembalikan_buku():
    buku = input("\nMasukkan nama buku yang ingin dikembalikan: ")
    if buku in buku_perpustakaan:
        info_buku = buku_perpustakaan[buku]
        if "not available" in info_buku["status"]:
            for i in range(info_buku["volume"]):
                if info_buku["status"][i] == "not available":
                    info_buku["status"][i] = "available"
                    print(f"Anda telah mengembalikan {buku} - Volume {i+1}")
                    break
        else:
            print(f"Semua volume dari {buku} sudah tersedia di perpustakaan.")
    else:
        print(f"Buku {buku} tidak ditemukan di perpustakaan.")
while True:
    print("\n1. Tampilkan Buku")
    print("2. Pinjam Buku")
    print("3. Kembalikan Buku")
    print("4. Keluar")
    
    pilihan = input("Pilih opsi: ")
    
    if pilihan == "1":
        tampilkan_buku()
    elif pilihan == "2":
        pinjam_buku()
    elif pilihan == "3":
        kembalikan_buku()
    elif pilihan == "4":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
