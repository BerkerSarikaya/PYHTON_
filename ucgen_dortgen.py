print("""
*****************
Ucgen-Dortgen
*****************
""")

a=("dortgenin birinici kenari")
b=("dortgenin ikinci kenari")
c=("dortgenin ucuncu kenari")
d=("dortgenin dorduncu kenari")
dortgen=("dort kenarli geometrik sekil")
e=("ucgenin birinci kenari")
g=("ucgenin ikinci kenari")
f=("ucgenin ucuncu kenari")
ucgen=("uc kenarli geometrik sekil")
input("sekli giriniz")

if(dortgen):
    print("dortgen")
    a=input("a:")
    b=input("b:")
    c=input("c:")
    d=input("d:")

    if( a==b and b==c and c==d ):
         print("kare")
    elif(a==c and b==d and a!=d):
        print("dikdortgen")
    else:
        print("siradan dortgen")
        if(ucgen):
            print("ucgen")
            e=input("e")
            f=input("f")
            g=input("g")
        elif(abs(e-f) <= g <= e+f and abs(g-f) <= e <= g+f and abs(e-g <= f <= e+g)):
            print("ücgen degildir")
        elif(e==f and f==g):
            print("eskenar ucgen")
        elif(e==f and f!=g):
            print("ikizkenar ucgen")
        elif(e!=f and f==g):
            print("ikizkenar ucgen")
        elif(e==g and f!=g):
            print("ikizkenar ucgen")
        elif(e!=g and f!=g):
            print("normal ucgen")
