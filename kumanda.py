import time
import random


class Kumanda():

    def __init__(self, tv_durum="kapali", tv_ses=0, kanal_listesi=["trt"], kanal="trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if self.tv_durum == "kapali":
            print("tv acildi")
            self.tv_durum = "acik"
        else:
            print("tv zaten acik")

    def tv_kapa(self):
        if self.tv_durum == "acik":
            print("tv kapandi")
            self.tv_durum = "kapali"
        else:
            print("tv zaten kapali")

    def ses(self):
        while True:
            ses = input("yukseltmek icin :  >, dusurmek icin :< ")
            if ses == ">":
                print("ses yukseltiliyor")
                self.tv_ses += 1
                print("ses:", self.tv_ses)
            elif ses == "<":
                print("ses yukseltiliyor")
                self.tv_ses += 1
                print("ses:", self.tv_ses)
            else:
                print("hatali giris yaptiniz")
                break

    def kanal_ekleme(self):
        eklenecek_kanallar = input("eklemek istediginiz kanallari giriniz")
        print("kanal ekleniyor")
        time.sleep(1)
        self.kanal_listesi.append(eklenecek_kanallar)
        print("kanal eklendi")

    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi)-1)

        self.kanal = self.kanal_listesi[rastgele]

        print("su anki kanal:",self.kanal)

    def bilgilerigoster(self):
        print("tv_durum:{}\nses:{}\nkanal_listesi:{}\nkanal:{}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal))

Kumanda = Kumanda()

print("""
*********************
        KUMANDA
        
    Islem Listes        
1.AC
2.KAPA
3.SES
4.KANAL EKLEME
5.RASTGELE KANAL ACMA 
6.BILGILERI GOSTER       
        
**********************     
        
        """)

while True:
    islem = input("gerceklestirmek istediginiz islemi giriniz:")
    if islem == "1":
        Kumanda.tv_ac()
    elif islem == "2":
        Kumanda.tv_kapa()
    elif islem == "3":
        Kumanda.ses()
    elif islem == "4":
        Kumanda.kanal_ekleme()
    elif islem == "5":
        Kumanda.rastgele_kanal()
    elif islem == "6" :
        Kumanda.bilgilerigoster()
    else:
        print("Hatali giris yaptiniz")
