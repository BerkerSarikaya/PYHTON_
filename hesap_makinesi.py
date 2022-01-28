
print("""****************
Hesap Makinesi

1.  Toplama Islemi
2.  Cikarma Islemi
3.  Carpma Islemi
4.  Bolme Islemi 
*****************
""")

a = int(input("birinci sayi:"))
b = int(input("ikinci sayi:"))

islem=input("islemi seciniz:")

if islem == "1" :
    print("{} ile {} toplami {}'dir.".format(a,b,a+b))
elif islem == "2" :
    print("{} ile {} farki {}'dir.".format(a, b, a - b))
elif islem == "3" :
    print("{} ile {} carpimi {}'dir.".format(a, b, a * b))
elif islem == "4" :
    print("{} ile {} bolumu {}'dir.".format(a, b, a / b))
else:
    print("hatali sonuc")


