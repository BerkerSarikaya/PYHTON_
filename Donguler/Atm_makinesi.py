print("""
****************
ATM MAKINESI

ISLEMLER

1. Bakiye Sorgulama

2. Para Cekme

3. Para Yatirma

Programdan cikis yapmak icin q'ya basiniz

****************
""")

bakiye = 1000

while True:
    islem = input("islem seciniz:")
    if( islem == "q"):
        print("yine bekleriz")
        break
    elif( islem == "1" ):
        print("bakiyeniz {} tl'dir.".format(bakiye))
    elif(islem == "2"):
        miktar = int(input("Yatirmak Istediginiz Miktari Giriniz :"))
        bakiye += miktar
    elif(islem == "3"):
        miktar = int(input("Cekmek Istediginiz Miktari Giriniz"))
        if( bakiye-miktar < 0):
            print("yetersiz bakiye")
            continue
        bakiye -= miktar
    else:
        print("gecersiz islem")
        continue














