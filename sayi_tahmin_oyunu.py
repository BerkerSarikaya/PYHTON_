import random
import time

print("""
*********************
sayi tahmin oyunu

1 ile 100 arasinda
*********************
""")

rastgele_sayi = random.randint(1,100)
tahmin_hakki=5
while True:

    tahmin=int(input("tahmininiz:"))

    if(tahmin > rastgele_sayi):
        print("tahmininizi kuculterek yeniden yapin")
        tahmin_hakki -=1
    elif(tahmin < rastgele_sayi):
        print("tahmininizi buyulterek yeniden yapin")
        tahmin_hakki -=1
    else:
        print("dogru tahmin yaptiniz")
        break
    if( tahmin_hakki == 0 ):
        print("tahmin hakkiniz bitmistir")
        print("sayimiz",rastgele_sayi)
        break