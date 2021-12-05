import pygame
from pygame.math import Vector2

# na prime rimamo igraca i protivnika
# svaki ima ime, poziciju, brzinu, skup slika

imeIgraca = "Macka koja puca"
pozicijaIgraca = Vector2(50,50)
brzinaIgraca = Vector2(10,10)
slikeIgrac = list()

imeProtivnika = "Pacov"
pozicijaProtivnika = Vector2(100,100)
# ...
# ...

imeProtivnika2 = "Pacov 2"
# ...

class Objekat:
    ime = None
    pozicija = None
    brzina = None
    slike = None

igrac = Objekat()
igrac.ime = "Macka koja puca"
igrac.pozicija = Vector2(50,50)

protivnik1 = Objekat()
protivnik1.ime = "Veliki Pacov"

protivnik2 = Objekat()
protivnik2.ime = "Mali pacov"