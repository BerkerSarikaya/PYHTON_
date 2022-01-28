print("""
*********************
Harf Notu Hesaplama
*********************
""")

vize1 = int(input("Birinci Vize Notunu Giriniz:"))
vize2 = int(input("Ikinci Vize Notunu Giriniz:"))
final = int(input("Final Notunu Giriniz :"))


genel_not = (vize1* 0.3 + vize2 * 0.3 + final *0.4)
(print("genel_not:{}".format(vize1* 0.3 + vize2 * 0.3 + final *0.4)))

if(genel_not >= 90):
    print("AA")
elif(genel_not >=85):
    print("AB")
elif(genel_not >= 80):
    print("BB")
elif(genel_not >= 75):
    print("BC")
elif(genel_not >= 70):
    print("CC")
elif(genel_not >= 65):
    print("CD")
elif(genel_not >= 60):
    print("DC")
elif(genel_not >= 55):
    print("DD")
else:
    print("FF")
