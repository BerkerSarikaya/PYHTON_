print("""
**************************
Gelismis Kullanici Girisi
**************************
""")

sys_kullanici_adi = "berker"
sys_parola = "1234"
giris_hakki = 3

while True :
    kullanici_adi = input ("Kullanici Adi Giriniz : ")
    parola = input ("Parola Giriniz : ")
    if ( sys_kullanici_adi == kullanici_adi and sys_parola != parola ):
        print("parola hatali")
        giris_hakki -= 1
    elif( sys_kullanici_adi != kullanici_adi and sys_parola == parola ) :
        print ("kullanici adi hatali")
        giris_hakki -=1
    elif ( sys_kullanici_adi != kullanici_adi and sys_parola != parola ) :
        print ("kullanici adi ve parola hatali")
        giris_hakki -=1
    else:
        print ("giris_basarili")
        break
    if (giris_hakki == 0):
        print("giris hakkiniz kalmadi")
        break
