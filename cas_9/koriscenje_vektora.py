from pygame.math import Vector2

"""
    Vektor kreiramo tako sto promenljivoj dodelimo vrednost Vektor2(x, y), gde su x i y koordinate
    Vektor mozemo ispisati ceo odjendom (da vidimo sta nas program radi)
    Mozemo ispisivati i pojedinacno komponente (delove) nekog vektora, a i menjati ih
"""
a = Vector2(100, 50)  # dodela
print("a =", a)  # ispisivanje
print("a.x =", a.x)  # ispisivanje x komponente
print("a.y =", a.y)  # ispisivanje y komponente
a.x = 75  # promena x komponente
print("Nakon promene, a.x =", a.x, "i a =", a)

print()  # prazan red

"""
    Vektore mozemo sabirati i oduzimati
    Na ovaj nacin mozemo simulirati brzine i kretanje, na primer dodavanjem konstantog vektora na pozicju
    slepog misa deluje kao da se mis krece!
"""
b = Vector2(20, 40)
print("b =", b)
c = Vector2(30, -10)
print("c =", c)
zbir = b + c
print("b+c =", zbir)
razlika = b - c
print("b-c =", razlika)

print()  # prazan red

"""
    Vektore mozemo mnoziti brojem, cime se menja intenzitet
    Intenzitet mozete smatrati duzinom strelice vektora
    Na primer, sto je brzina veca, to je intenzitet veci
"""
brzina = Vector2(10, 0)
print("brzina pre promene je", brzina)
brzina = brzina * 2
print("brzina kad je pomnozimo sa dva:", brzina)
# bitno je razumeti da mozemo mnoziti i razlomcima, na primer sa 0.5, cime se vektor prepolovi

print()  # prazan red

"""
    Veoma bitna osobina vektora za nas (i prednost u odnosu na zapis koordinata uz pomoc promenljivih) 
    je to da ih mozemo lako da rotiramo
    
    Na primer, neka covek stoji na poziciji (10, 0) i krece se u krug sa centrom u koordinatnom pocetku (0, 0)
    i smeru suprotnom od kretanaj kazaljke na satu
    
    Zadatak je da odredimo njegovu poziciju nakon sto predje 70 stepeni. Zadatak cemo uraditi na dva nacina:
    - prvo bez vektora
    - pa sa vektorima
"""

# 1. NACIN
from math import sqrt, sin, cos, radians
x = 10
y = 0
rastojanje_od_centra = sqrt(x*x + y*y)
novo_x = rastojanje_od_centra * cos(radians(70))  # 70 stepeni pretvaramo u radijane jer sin() radi sa radijanima
novo_y = rastojanje_od_centra * sin(radians(70))  # isto za kosinus
print("Nova pozicija je (", novo_x, ",", novo_y, ")")

# 2. NACIN
pozicija = Vector2(10, 0)
pozicija = pozicija.rotate(70)
print("Nova pozicija je (", pozicija.x, ",", pozicija.y, ")")

"""
    Na vama je da odlucite koji vam se nacin vise dopada :)
    Bitan dodatak je da prvi nacin nece da radi ako y nije 0, nego ce biti potreba izmena, dok drugi nacin uvek radi
    
    Primer kada mozemo da rotiramo vektor je igra u kojoj se trkamo, skretanjem se "okrece" pravac kretanja
"""