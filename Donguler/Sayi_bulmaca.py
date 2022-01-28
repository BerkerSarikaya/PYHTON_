import random
sayi = (random.randint(1,100))
hak=5

while True:
    tahmin=int(input("tahmininizi giriniz"))
    hak -=1
    print("{}hakkiniz kaldi".format(hak))
    if( hak == 0):
        print("hakkiniz kalmamistir")
        break
    elif( tahmin > sayi):
        print("lutfen daha kucuk bir tahminde bulununuz")
    elif( tahmin < sayi):
        print("lutfen daha buyuk bir tahminde bulununuz")
    else:
        print("tahmininiz dogru")

