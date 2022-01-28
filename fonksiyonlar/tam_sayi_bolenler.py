#tam sayi bolenlerini bulma programi


def tam_bolenler(sayi):
    tam_bolenler=[]
    for i in range(1,sayi+1):
        if (sayi % i == 0):
            tam_bolenler.append(i)
    return tam_bolenler

while True:
    sayi = input("sayi")
    if (sayi == "q"):
        print("basarili bir sekilde cikis yaptiniz")
        break
    else:
        sayi= int(sayi)
        print("tam sayi bolenleri:",tam_bolenler(sayi))
    break






