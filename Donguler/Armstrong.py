print("""
**********
Armstrong
**********
""")

sayi= input("bir sayi giriniz:")
basamak_sayisi=len(sayi)
sayi=int(sayi)
toplam=0
x1=sayi
while(x1 > 0 ):
    (x1 % 10)**basamak_sayisi
    toplam += (x1 % 10)**basamak_sayisi
    x1 //= 10
if( sayi == toplam):
    print(sayi,"armstrongdur")
else:
    print(sayi,"degildir")