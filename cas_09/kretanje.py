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
mis.brzina = Vector2(20, 0)  # mis ce se pomerati desno brzinom 20 pixela po frejmu
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

    mis.pozicija = mis.pozicija + mis.brzina  # menjamo poziciju za vrednost brzine (krecemo se za 20 desno)
    prozor.blit(mis.slike[mis.id_slike], mis.pozicija)  # iscrtava trenutnu sliku na poziciji misa

    mis.id_slike = mis.id_slike + 1  # uvecavamo brojac slike
    if mis.id_slike >= len(mis.slike):
        mis.id_slike = 0  # ukoliko dodje do prekoracenja (u nasem slucako ako id_slike postane 2) vracamo ga na 0

    pygame.display.flip()
    sat.tick(10)  # kod u petlji se izvrsava 10 puta u sekundi

pygame.quit()
