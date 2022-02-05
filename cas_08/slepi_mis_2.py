import pygame
from pygame.math import Vector2

pygame.init()
prozor = pygame.display.set_mode((600, 600))
sat = pygame.time.Clock()


slike = []

nova_slika = pygame.image.load("mis1.png")
transformisana_slika = pygame.transform.scale(nova_slika, (100, 100))
slike.append( transformisana_slika )

nova_slika = pygame.image.load("mis2.png")
transformisana_slika = pygame.transform.scale(nova_slika, (100, 100))
slike.append( transformisana_slika )

class Mis:
    broj_slike = 0
    pozicija = None
    brzina = None

m = Mis()
m.pozicija = Vector2(50,50)
m.brzina = Vector2(5,0)

program_radi = True
while program_radi:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            program_radi = False

    prozor.fill((0, 0, 0))

    prozor.blit(slike[m.broj_slike], m.pozicija)
    m.pozicija += m.brzina

    m.broj_slike = (m.broj_slike + 1) % 2

    pygame.display.flip()
    sat.tick(10)

pygame.quit()
