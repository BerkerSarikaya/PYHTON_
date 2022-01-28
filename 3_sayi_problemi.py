print("""
**********************
Buyuk Deger Uygulamasi
**********************
""")

a = input("Birinci Sayiyi Giriniz:")
b = input("Ikinci Sayiyi Giriniz:")
c = input("Ucuncu Sayiyi Giriniz")

if (a >= b and a>= c):
    print("En Buyuk Deger {}:".format(a))
elif (a <= b and b >= c):
    print("En Buyuk Deger {}:".format(b))
elif ( a<=b and b<=c):
    print("En Buyuk Deger {}:".format(c))
