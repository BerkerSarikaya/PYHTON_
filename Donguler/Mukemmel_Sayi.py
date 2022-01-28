print("""
*************
Mukemmel Sayi
*************
""")

sayi=int(input("sayiyi giriniz:"))
toplam = 0
a = 1

while (a < sayi):
    if(sayi % a == 0):
        toplam += a
    a +=1
if(toplam == sayi):
    print(sayi,"mukemmel sayi")
else:
    print(sayi,"mukemmel sayi degil")









