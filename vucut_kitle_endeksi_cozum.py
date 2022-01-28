print(""""
********************
Beden Kitle Endeksi
********************
""")

boy = float(input("lutfen boyunuzu giriniz:"))
kilo = int(input("lutfen kilonuzu giriniz:"))

beden_kitle_endeksi = kilo / (boy*boy)
print("beden_kitle_endeksi {}:".format(kilo / (boy*boy)))

if (beden_kitle_endeksi < 18.5 ):
    print("zayif")
elif (beden_kitle_endeksi <25):
    print("normal")
elif (beden_kitle_endeksi <30) :
    print ("fazla kilolu")
else:
    print("obez")