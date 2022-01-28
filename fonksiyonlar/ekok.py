def isEkok(sayi1,sayi2):
    ekok=1
    i=2
    while( sayi1!=1 or sayi2!=1 ):
        sayi1Check = False
        sayi2Check = False
        if (sayi1 % i == 0):
            sayi1 /= i
            sayi1Check = True
        if (sayi2 % i ==0):
            sayi2 /= i
            sayi2Check = True
        if(sayi1Check or sayi2Check):
            ekok *= i
        else:
            i += 1

    return ekok

sayi1=int(input("birinci sayi"))
sayi2=int(input("ikinci sayi"))
print("ekok",isEkok(sayi1,sayi2))
