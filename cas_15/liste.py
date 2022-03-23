"""
Neka je zmija lista delova zmije u matrici, gde je (a, b)
deo zmije u polju reda a i kolone b

Prvi element je rep zmije, a poslednji - njena glava
. . . . . .
. r * . . .
. . * . . .
. . G . . .
. . . . . .
"""

zmija = [(1,1), (1,2), (2,2), (3,2)]
#          r      *      *      G
#          0      1      2      3     indeksi sleva udesno
#         -4     -3     -2     -1     indeksi zdesna ulevo

print("Glava je", zmija[-1])

stara_glava = zmija[-1]         # dohvatamo poslednji element liste
red, kolona = stara_glava       # delimo par na red i kolonu [ zapis a, b = (x, y) je isto sto i a = x, b = y ]
nova_glava = (red + 1, kolona)  # ako se zmija krece dole, glava se pomeri dole, to jest red se poveca za 1

print("Nova glava je", nova_glava)

zmija.append(nova_glava)  # kako je glava poslednji elemnt liste, dodajemo novu glavu na kraj
zmija.pop(0)  # kako duzina zmije ne sme da se promeni, brisemo stari rep (elemnt na pozicji 0). Novi rep je (1,2)

"""
. . . . . .
. . r . . .
. . * . . .
. . * . . .
. . G . . .
"""

print(zmija)

