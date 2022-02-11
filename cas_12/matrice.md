## Liste: podsetnik
Liste sluze za cuvanje vece kolicine podataka koji imaju neku **zajednicku
osobinu**. Na primer, lista namirnica, ili lista gradova, ili lista dana u nedelji.

Umesto da pravimo vise promenljivih za podatke istog tipa, smestamo ih u jednu 
listu i pristupamo uz pomoc **indeksa**. **Indeks** je redni broj elementa u listi.

**(!)** Mozda ste upoznati s pojmom niza iz jezika poput C++; lista u Pajtonu moze 
sve isto i cak vise!
```python
radni_dani = ["ponedeljak", "utorak", "sreda", "cetvrtak", "petak"]

print("Prvi dan u nedelji je", radni_dani[0])
```

Za dodavanje elemenata u listu koristimo `append`, a za ispitivanje duzine `len`:
```
>>> li = ['a', 'b', 'c']
>>> li
['a', 'b', 'c']
>>> li.append('d')
>>> li
['a', 'b', 'c', 'd']
>>> len(li)
4
```

Zapison `lista[i]` mozemo pristupati elemntima, ali ih i menjati:
```
>>> li[2]
'c'
>>> li[2] = 'e'
>>> li
['a', 'b', 'e', 'd']
```

### Ispisivanje elemenata liste
Za prolazak kroz listu koristimo `for` petlju, i svaki elem. ispisujemo u 
`print` naredbi:
```python
li = ['a', 'b', 'c']
for el in li:
    print(el)

ISPIS:
    a 
    b 
    c
```

## Matrice
**Matrica je lista listi.** Koriste se za predstavljana podataka
koji bi inace pisali u tabeli. U sledecem primeru matricom predstavljamo
telefonski imenik: svaki red je jedna osoba, a u svakom redu imamo 3 podatka -
prezime, ime i broj.
```python
imenik = [
    ["Petrovic"     , "Petar"     , "+381 62 123 1234"] ,
    ["Aleksandrovic", "Aleksandra", "+381 64 321 4321"] ,
    ["Nikolic"      , "Nikola"    , "+381 69 555 2233"]
]
```
Ovde je `imenik[i]` nista drugo nego lista koja predstavlja osobu broj `i`.
```
>>> imenik[0]
['Petrovic', 'Petar', '+381 62 123 1234']
>>> imenik[1]
['Aleksandrovic', 'Aleksandra', '+381 64 321 4321']
```
Kako bismo pristupili telefonu Nikole Nikolica, pisacemo:
```
>>> imenik[2][2]
'+381 69 555 2233'
```

### Ispisivanje matrice
```python
for osoba in imenik:
    print(osoba)

ISPIS:
    ["Petrovic", "Petar", "+381 62 123 1234"]
    ["Aleksandrovic", "Aleksandra", "+381 64 321 4321"]
    ["Nikolic", "Nikola", "+381 69 555 2233"]
```
Ovo mozemo ulepsati na sledeci nacin:
```python
for osoba in imenik:
    print(f"{osoba[1]} {osoba[0]} : {osoba[2]}")

ISPIS:
    Petar Petrovic : +381 62 123 1234
    Aleksandra Aleksandrovic : +381 64 321 4321
    Nikola Nikolic : +381 69 555 2233
```
**(!)** Zapis `f"nesto..."` predstavlja **formatiran** string. 
Prednost formatiranih stringova je u tome da mozemo lako u njih
ubaciti promenljive. Npr, umesto `print("a="+str(a)+"b="+str(b))` cemo pisati 
`print(f"a={a} b={b}")`, sto je krace i jednostavnije.

## Zadaci za vezbu
Dat je niz:
```python
niz = [1, 6, 2, 0, -3, 5, 6]
```
**Napisati kodove** koji rade sledece upite:
1. izracunati zbir prva tri elementa niza
2. koristeci `for` petlju, izracunati zbir svih elemenata
3. koristeci `for` petlju, odrediti broj parnih elemenata
4. ispisati sve elemente niza na parnim pozicijama

Data je matrica `mat`:
```python
mat = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
```
**Napisati kodove** koji rade sledece upite:
5. izracunati zbir elemenata iz srednje kolone
6. izracunati proizvod elemenata u poslednjoj vrsti (poslednjem redu)
7. izracunati zbir elemenata na dijagonali
8. koristeci `for` petlju, izracunati zbir elemenata u prvoj koloni
9. koristeci duplu `for` petlju, naci zbir svih elemenata matrice
```python
for red in mat:
    for el in red:
        ...
```
10. koristeci duplu `for` petlju, ispisati elemente matrice u ovom formatu:
```
10
20
30
40
50
60
70
80
90
```
