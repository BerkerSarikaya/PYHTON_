

def ebob_bulma(sayı1, sayı2):
    i = 1
    ebob = 1
    while (i <= sayı1 and i <= sayı2):

        if ((sayı1 % i==0) and (sayı2 % i==0)):
            ebob = i
        i += 1
    return ebob


sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ebob:", ebob_bulma(sayı1, sayı2))



