import pygame
from pygame import Vector2

pygame.init()
prozor = pygame.display.set_mode((800, 800))
sat = pygame.time.Clock()

bullets = []
pravac = 0

program_radi = True
while program_radi:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            program_radi = False

    tasteri = pygame.key.get_pressed()
    if tasteri[pygame.K_LEFT]:
        pravac -= 6
    if tasteri[pygame.K_RIGHT]:
        pravac += 6
    if tasteri[pygame.K_SPACE]:
        # jedan metak je par vektora, prvi je pozicija, a drugi pravac kretanja
        bullets.append(
            [Vector2(400, 400) + Vector2(32, 0).rotate(pravac),
             Vector2(10, 0).rotate(pravac)]
        )

    # pomeram svaki metak (menjam poziciju za vektor brzine)
    for metak in bullets:
        metak[0] = metak[0] + metak[1]

    prozor.fill((0, 0, 0))
    for metak in bullets:
        pygame.draw.circle(prozor, pygame.Color("red"), metak[0], 4)
    pygame.draw.circle(prozor, pygame.Color("white"), (400, 400), 18)
    pygame.draw.line(prozor, pygame.Color("white"), (400, 400), Vector2(400, 400) + Vector2(32, 0).rotate(pravac), 10)
    pygame.display.flip()
    sat.tick(60)

pygame.quit()
