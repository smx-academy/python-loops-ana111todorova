

#1.Da se napravi programa vo koja korisnikot ke vnese 2 broevi i da se proveri dali zbirot e pomal od 100

"""broj1 = int(input("vnesi eden broj ") )
broj2 = int(input("vnesi drug broj ") )
zbir = broj1 + broj2
if zbir < 100 :
    print("zbirot e pomal od 100")
else:
    print("zbirot e pogolem od 100")"""

#2.Da se napravi programa vo koja korisnikot ke vnese godina na ragjanje, ke se presmeta kolku godini e i da se odredi dali e maloleten 
# ili polnoleten

"""godini= int(input("vnesete godina na raganje "))
vozrast= 2023-godini
print("vie imate {} godini".format(vozrast))
if vozrast>18:
    print("liceto e polnoletno")
else:
    print("liceto ne e polnoletno")"""

#3.Da se napravi programa vo koja korisnikot ke vnese strani na dva pravoagolnici, da se presmeta plostinata i da se proveri koj 
# pravoagolnik e pogolem

"""print("venesete strani na prviot pravoagolnik")
x=int(input("strna 1: "))
y=int(input("strana 2: "))
print("vnesete stani za vtoriot pravoagoolnik")
z=int(input("strna 1: "))
d=int(input("strana 2: "))

P1=x*y
P2=z*d
if P1>P2:
    print("prviot pravoagolnik ima pogolema ploshtina")
else:
    print("vtoriot pravoagolnik ima pogolema ploshtina ")"""


#4. Da se napravi programa vo koja korisnikot ke vnese goleminite na aglite na triagolnici, i da se proveri dali so tie golemini moze da se
#  kreira triagolnik(zbirot treba da bide 180)

"""print("venesete tri agli ")
x=int(input("agol 1: "))
y=int(input("agol 2: "))
z=int(input("agol 3: "))

if x+y+z==180:
    print("aglite formiraat triagolnik")
else:
    print("dadenite agli ne moze da formiraat triagolnik ")"""


#5.Da se napravi programa vo koja korisnikot ke vnese nekoe ime i da se proveri sekoga samoglaska kolku pati se pojavuva vo ime i od 
# kolku karakteri e sostaveno toa ime

"""zbor=input("vnesete ime ")
a=zbor.count("a")
e=zbor.count("e")
i=zbor.count("i")
o=zbor.count("o")
u=zbor.count("u")
br=zbor.count("")
print("bukvata a se pojavuva{} pati, e {} pati, i {} pati, o {} i u{} pati, a ima vkupno {} karakteri". format(a,e,i,o,u,br))"""