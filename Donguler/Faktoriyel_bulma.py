print(""""
***************
Faktoriyel Bulma

cikmak icin q'ya basiniz.

""")

while True :
    sayi = input("Faktoriyelini bulmak istediginiz sayiyi giriniz : ")
    if (sayi == "q"):
        print("program sonlandirildi.")
        break
    else:
        sayi=int(sayi)
        faktoriyel = 1
        for i in range(2,sayi+1):
            faktoriyel *= i
        print ("Faktoriyel : ",faktoriyel)
