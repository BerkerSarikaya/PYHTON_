#kullanici girisi programi yazimi

print("""
********************
Kullanici Girisi
********************
""")

sys_kullanici_adi = "Berker Sarikaya"
sys_parola = "123456"

kullanici_adi = input("kullanici adini giriniz:")
parola = input("parola giriniz:")

if ( kullanici_adi == sys_kullanici_adi and parola != sys_parola  ):
    print("hatali giris yaptiniz.")
elif (kullanici_adi != sys_kullanici_adi and parola == sys_parola):
    print ("hatali giris yaptiniz.")
elif ( kullanici_adi != sys_kullanici_adi and parola != sys_parola):
    print ("hatali giris yaptiniz. ")
else :
    print ("giris basarili")


