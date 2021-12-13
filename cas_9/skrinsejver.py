import pygame
from pygame.math import Vector2

pygame.init()
prozor = pygame.display.set_mode((600, 600))
sat = pygame.time.Clock()


class Mis:
    pozicija = None  # vektor koji odgovara poziciji mis ana ekranu
    brzina = None  # brzina, odnosno promena pozicije u svakom frejmu
    slike = None  # slike (sprajtovi) misa
    id_slike = None  # broj slike koja se trenutno prikazuje


mis = Mis()  # stvaramo konretnog misa
mis.pozicija = Vector2(50, 50)
mis.brzina = Vector2(19, 13)
mis.slike = []
mis.id_slike = 0

sl = pygame.image.load("mis1.png")           # uzimamo sliku mis1.png iz memorije i syavljamo je u promenljivu sl
sl = pygame.transform.scale(sl, (100, 100))  # sliku sl transformisemo tako da bude velicine 100x100
mis.slike.append(sl)                         # dodajemo transformisanu sliku u listu slika

sl = pygame.image.load("mis2.png")           # radimo sve isto za sliku mis2.png
sl = pygame.transform.scale(sl, (100, 100))
mis.slike.append(sl)

program_radi = True
while program_radi:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            program_radi = False

    prozor.fill((0, 0, 0))

    mis.pozicija = mis.pozicija + mis.brzina
    prozor.blit(mis.slike[mis.id_slike], mis.pozicija)  # iscrtava trenutnu sliku na poziciji misa

    """
    Ukoliko je mis stigao do desnog ili levog zida, potrebno je promeniti pravac brzine
    Znamo da je stigao do desnog zida ako mu je x koordinata >= 600 ILI ako je x <= 0
    Kako mis.pozicija odgovara gornjem levom uglu slike, uslov za desni zid menjamo sa x >= 500
    Pravac brzine menjamo tako sto negiramo x komponentu:
        mis.brzina.x = -mis.brzina.x
    """
    if mis.pozicija.x >= 500 or mis.pozicija.x <= 0:
        mis.brzina.x = -mis.brzina.x  # ako je isao levo, icicde desno, i obrnuto

    """
    Kako bi obezbedili odbijanje od sva cetiri zida, potrebno je da prosli korak ponovimo za gornji i donji zid
    Kkao je prozor kvadrat, promena se svodi na zamenu x sa y:
    """
    if mis.pozicija.y >= 500 or mis.pozicija.y <= 0:
        mis.brzina.y = -mis.brzina.y  # ako je isao gore, icice dole, i obrnuto

    mis.id_slike = mis.id_slike + 1  # uvecavamo brojac slike
    if mis.id_slike >= len(mis.slike):
        mis.id_slike = 0  # ukoliko dodje do prekoracenja (u nasem slucako ako id_slike postane 2) vracamo ga na 0

    pygame.display.flip()
    sat.tick(10)  # kod u petlji se izvrsava 10 puta u sekundi

pygame.quit()
