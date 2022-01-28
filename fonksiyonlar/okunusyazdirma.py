def okunus(deger):
    birler = (" ", "bir", "iki", "uc", "dort", "bes", "alti", "yedi", "sekiz", "dokuz")
    onlar = (" ", "on", "yirmi", "otuz", "kirk", "elli", "altmis", "yetmis", "seksen", "doksan")
    while 10 <= deger < 100:
        if deger % 10 != 0:
            a = (deger % 10)
            birlerbas = birler[a]
        if deger // 10 != 0:
            b = (deger // 10)
            onlarbas = onlar[b]
        break
    return onlarbas + " " + birlerbas


sayi = int(input("bir sayi giriniz: "))
print("sayi: ", okunus(sayi))
