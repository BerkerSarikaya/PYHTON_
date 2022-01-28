
toplam=0
#bilgilendirme: q ile cikis yapabilirsiniz.
while True:
    sayi = (input("sayi giriniz"))
    if( sayi == "q"):
        print("cikis yaptiniz")
        break
    else:
        sayi=int(sayi)
        toplam += sayi
        print(toplam,"toplam sonuc")


