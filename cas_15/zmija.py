import pygame
import random

pygame.init()
prozor = pygame.display.set_mode((500,500))
sat = pygame.time.Clock()

dimenzija = 25  # velicina polja
vel_kvadrata = 20  # piksela


zmija = [(1,1), (1,2), (2,2), (3,2)]
pravac = "DESNO"

hrana = (12, 12)

program_radi = True
while program_radi:
    promenili_pravac = False
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            program_radi = False
        if dogadjaj.type == pygame.KEYDOWN and promenili_pravac == False:
            taster = dogadjaj.key
            if taster == pygame.K_LEFT and pravac != "DESNO":
                pravac = "LEVO"
                promenili_pravac = True
            if taster == pygame.K_RIGHT and pravac != "LEVO":
                pravac = "DESNO"
                promenili_pravac = True
            if taster == pygame.K_DOWN and pravac != "GORE":
                pravac = "DOLE"
                promenili_pravac = True
            if taster == pygame.K_UP and pravac != "DOLE":
                pravac = "GORE"
                promenili_pravac = True

    stara_glava = zmija[-1]
    red, kolona = stara_glava
    if pravac == "DOLE":
        red += 1
    if pravac == "GORE":
        red -= 1
    if pravac == "LEVO":
        kolona -= 1
    if pravac == "DESNO":
        kolona += 1
    nova_glava = (red, kolona)

    if red < 0 or kolona < 0 or red >= dimenzija or kolona >= dimenzija or nova_glava in zmija:
        pygame.quit()
        exit(0)

    zmija.append(nova_glava)

    if nova_glava == hrana:
        print("POJELI HRANU")
        while hrana in zmija:
            hrana = (random.randint(0,24), random.randint(0,24))
    else:
        zmija.pop(0)

    prozor.fill((0,0,0))

    pygame.draw.circle(prozor, (255,0,0),
                       (hrana[1] * vel_kvadrata + vel_kvadrata//2, hrana[0] * vel_kvadrata + vel_kvadrata//2),
                       vel_kvadrata//2)

    for komad_zmije in zmija:
        red, kolona = komad_zmije
        pygame.draw.rect(prozor, (255,255,255), (kolona * vel_kvadrata, red * vel_kvadrata, vel_kvadrata, vel_kvadrata))

    pygame.display.flip()
    sat.tick(10)

pygame.quit()
