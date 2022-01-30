import pygame
from pygame import Vector2

pygame.init()
prozor = pygame.display.set_mode((600,600))
sat = pygame.time.Clock()

pozicija = Vector2(300, 300)

program_radi = True
while program_radi:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            program_radi = False

    prozor.fill((0,0,0))

    # pygame.key
    # pygame.mouse

    stisnutiDugmici = pygame.key.get_pressed()
    if stisnutiDugmici[pygame.K_UP]:
        pozicija.y -= 10
    if stisnutiDugmici[pygame.K_DOWN]:
        pozicija.y += 10
    if stisnutiDugmici[pygame.K_LEFT]:
        pozicija.x -= 10
    if stisnutiDugmici[pygame.K_RIGHT]:
        pozicija.x += 10

    # pygame.mouse.get_pos()
    # mis = pygame.mouse.get_pressed()
    # print(mis)

    pygame.draw.circle(prozor, pygame.Color("red"), pozicija, 10)

    """
    vas kod
    """

    pygame.display.flip()
    sat.tick(30)

pygame.quit()
