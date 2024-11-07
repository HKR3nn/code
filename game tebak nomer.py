kemenangan = 9
count = 0
batas_mencoba = 3
while count < batas_mencoba:
    tebak = int(input('Tebak : '))
    count += 1
    if tebak == kemenangan:
        print("EZ")
        break
else:
    print("TETOT!!")