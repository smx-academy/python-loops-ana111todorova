#1.Da se napravi programa vo koja ke se ispecatat site broevi do N. (N e broj koj go vnesuva korisnikot)

"""broj = int(input("Vnesi broj za iteracija: \n"))

for i in range(broj):
    print(i)"""

#2.Da se napravi programa vo koja korisnikot ke kaze kolku pati da se povtoruva ciklusot, da vnese suma vo denari i 
# da se napravi konverzija vo evra

"""pati=int(input("kolku pati da se izvrshi ciklusot"))
for i in range(pati):
    suma=int(input("koja suma da se konvertira vo evra"))
    evra= suma/61.5
    print("vrednosta vo evra e {}".format(evra))"""

#3.Da se napravi programa vo koja korisnikot kolku pati da se povtoruva ciklusot, da se ispecatat site parni broevi do brojot
#  koj go vnel korisnikot

"""n=int(input("do koj broj da se proverat parnite pbroevi "))
for i in range(n):
    if (i%2==0):
     print(i)"""

#4.Da se napravi programa vo koja korisnikot  ke moze da vnesuva broevi se dodeka ne izbere deka poveke ne saka da vnesuva, 
# da vnesuva licni podatoci na lica, da se prebroi kolku se bile vneseni polnoletni kolku maloletni

"""polnoleten = 0
maloleten = 0
while True:
    ime = input("Vnesi Ime: ")
    prezime = input("Vnesi Prezime: ")
    godina_ragjanje = int(input("Vnesi godina na ragjanje: "))
    godini = 2023 - godina_ragjanje
    
    if (godini >= 18):
        print("{} e polnoleten".format(ime))
        polnoleten += 1
    else:
        print("{} e maloleten".format(ime))
        maloleten += 1
    da_ne = input("Dali sakate da prodolzite da/ne: ")
    if (da_ne == 'ne'):
        break

print("Ima vkupno {} maloletni, a {} polnoletni".format(maloleten,polnoleten))"""


#5.Da se napravi programa za potrebite na nekoja prodavnica. Korisnikot da moze vnesuva produkti i cenite se dodeka ne izbere deka poveke 
# ne saka da vnesuva. Koga ke prestane da vnesuva produkti da se ispecati kolku vkupno ima za plakjanje, da plati i da se presmeta dali i 
# kolku treba da se vrati kusur.

vkupna_cena = 0
while True:
    produkt = input("Vnesi go produktot: ")
    cena = int(input("Vnesi ja cenata: "))
    vkupna_cena += cena
    da_ne = input("Dali sakate da prodolzite (da/ne): ")
    if (da_ne == 'ne'):
        break

print("Imate vkupno {} ".format(vkupna_cena))
plakanje = int(input("Vnesete ja uplatata: "))
while True:
    if (plakanje < vkupna_cena):
        plakanje = int(input("Ve molime uplatete poveke od {} ".format(vkupna_cena)))
    else:
        break
kusur = plakanje - vkupna_cena
print("Uplateni se {} den, vkupnata cena e {}, kusurot e {}".format(plakanje, vkupna_cena, kusur))


