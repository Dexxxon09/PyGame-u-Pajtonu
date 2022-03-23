"""
Ovde prikazujemo kako se pise tekst u pygame-u
"""

import pygame

pygame.init()
prozor = pygame.display.set_mode((920, 300))
sat = pygame.time.Clock()

# pre nego sto mozemo da pisemo tekst, biramo font
# 1. prvi argument je naziv fonta: "Arial", "Times New Roman", "Consolas", ...
# 2. drugi argument je broj - velicina fonta
mojFont = pygame.font.SysFont("Times New Roman", 160)

program_radi = True
while program_radi:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            program_radi = False

    prozor.fill((0, 0, 0))

    # kada zelimo da ispisemo tekst, potrebno je prvo da ga rendiramo, to jest da napravimo sliku tog teksta
    # 1. prvi argument je string - tekst koji zelimo da prikazemo
    # 2. drugi argument je bool - da li zelimo da ukljucimo anti-aliasing (da tekst izgleda glatko)
    #    (pogledajte slike aliased.png i anti-aliased.png u folderu)
    # 3. treci argument je boja prikazanog teksta
    rendiranText = mojFont.render("primer teksta", True, (255, 255, 255))

    # ovako dobijen rendiranText crtamo isto kao sto crtali i slike: koriscenjem funkcije blit
    prozor.blit(rendiranText, (50, 50))

    pygame.display.flip()
    sat.tick(30)

pygame.quit()
