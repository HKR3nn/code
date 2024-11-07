berat = int(input("Masukan Berat anda : "))
unit = input("(L)bs or (K)g : ")

if unit.lower() == 'l':
    berat_lbs = berat / 0.45
    print(f"Berat anda dalam Lbs adalah {berat_lbs} pounds")
elif  unit.lower() == 'k':
    berat_kg = berat * 0.45
    print(f"Berat anda dalam Kg adalah {berat_kg}")
