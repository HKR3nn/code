import random
nama_list = [
    "nelson", "Fia", "Ribka Lemagang", "Naomi", "Albert", "Diva", "Dimas", "Thanya", 
    "Yoan", "Adi", "Joy", "Mabe", "Verena", "Putri", "Geo", "Gorga", "Ilens", "William", 
    "Sania", "Rut", "Nicky", "Christin", "Novi", "Aswan", "Angel", "Mario", 
    "Merry", "Raflin", "Arifin", "Christy", "Ribka Lewian", "Daniel", "Chintya"
]

def bagi_kelompok_dengan_aturan(nama_list, jumlah_kelompok=4):
    elton = "Elton"
    vita = "Vita"
    orince = "Orince"
    liston = "Liston"
    nobel = "nelson" 
    ina = "Ina"
    maya = "Maya"
    riann = "Riann double N"  

    nama_khusus = [elton, vita, orince, liston, nobel, ina, maya, riann]
    for nama in nama_khusus:
        if nama in nama_list:
            nama_list.remove(nama)

    random.shuffle(nama_list)

    kelompok = [[] for _ in range(jumlah_kelompok)]
    for i, nama in enumerate(nama_list):
        kelompok[i % jumlah_kelompok].append(nama)
    
    kelompok[0].append(riann)  # Riann double N di kelompok 1
    kelompok[0].append(elton)  # Elton di kelompok 1
    kelompok[0].append(maya)   # Maya di kelompok 1
    kelompok[1].append(vita)   # Vita di kelompok 2
    kelompok[1].append(nobel)  # Nobel (Nelson) di kelompok 2
    kelompok[2].append(orince) # Orince di kelompok 3
    kelompok[2].append(liston) # Liston di kelompok 3
    kelompok[3].append(ina)    # Ina di kelompok 4
    
    return kelompok

kelompok = bagi_kelompok_dengan_aturan(nama_list, jumlah_kelompok=4)
for i, k in enumerate(kelompok, start=1):
    print(f"Kelompok {i}:")
    for nama in k:
        print(nama)
    print()  #

