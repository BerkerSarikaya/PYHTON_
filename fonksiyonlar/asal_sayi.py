#asal sayi decision

def asal_mi(sayi):
   if(sayi==1):
       return False
   elif(sayi==2):
       return True
   else:
       for i in range(2,sayi):
           if (sayi % i == 0):
               return False
       return True

while True:
    sayi = input("bir sayi giriniz")
    if( sayi=="q" ):
        print("cikis basarili")
        break
    else:
        sayi = int(sayi)
        if(asal_mi(sayi)):
            print(sayi,"asal bir sayidir")
        else:
            print(sayi,"asal bir sayi degildir")


