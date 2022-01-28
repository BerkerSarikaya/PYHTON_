#1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)

def pisagor():
    pisagor_listesi=list()
    for a in range(1,101):
        for b in range(1,101):

            c = (a**2 + b**2) ** 0.5

            if(c == int(c)):
                pisagor_listesi.append((a,b,int(c)))
    return pisagor_listesi

for a in pisagor():
    print(a)




