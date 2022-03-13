import pygame
from pygame.math import Vector2

pygame.init()
prozor = pygame.display.set_mode((1280, 720))
sat = pygame.time.Clock()

raketa = pygame.image.load("raketa.png")

dt = 1/30

pozicija = Vector2(640, 360)
ubrzanje = Vector2(300, 0)
brzina = Vector2(0, 0)

rotacija = 0
brzina_rotacije = 0
ubrzanje_rotacije = 15

while True:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if dogadjaj.type == pygame.KEYDOWN:
            if dogadjaj.key == pygame.K_ESCAPE:
                pygame.quit()
                exit(0)

    tasteri = pygame.key.get_pressed()
    if tasteri[pygame.K_LEFT]:
        brzina_rotacije += ubrzanje_rotacije * dt
    if tasteri[pygame.K_RIGHT]:
        brzina_rotacije -= ubrzanje_rotacije * dt
    rotacija = rotacija + brzina_rotacije
    #print(rotacija)

    if tasteri[pygame.K_UP]:
        brzina = brzina + ubrzanje.rotate(rotacija) * dt
    pozicija = pozicija + Vector2(brzina.x, -brzina.y) * dt

    prozor.fill((0, 0, 0))
    rotirana_slika = pygame.transform.rotate(raketa, rotacija)
    prozor.blit(rotirana_slika, pozicija - rotirana_slika.get_rect().center)
    pygame.display.flip()
    sat.tick(30)