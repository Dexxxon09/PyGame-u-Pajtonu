import pygame
from boje import *

pygame.init()
prozor = pygame.display.set_mode((600,600))
sat = pygame.time.Clock()

prozor.fill(CRNA)

boja = "white"  # trenutna boja crtanja

program_radi = True
while program_radi:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            pygame.image.save(prozor, "slika.png")
            program_radi = False

        """
        Klikom na tastere 'w', 'r', 'g' i 'b' menjamo boju cetkice
           w - white
           r - red
           g - green
           b - blue
        """
        if dogadjaj.type == pygame.KEYDOWN:
            if dogadjaj.key == pygame.K_w:
                boja = BELA
            if dogadjaj.key == pygame.K_r:
                boja = CRVENA
            if dogadjaj.key == pygame.K_g:
                boja = ZELENA
            if dogadjaj.key == pygame.K_b:
                boja = PLAVA

    """
    Gledamo gde se nalazi kursor misa, pa onda da li je stisnuto neko dugmo
    - Ako je stisnuto levo dugmo, crtamo trenutnom bojom
    - Ako je stisnuto desno dugme - brisemo (to jest crtamo crnom bojom)
    """
    pozicijaKursora = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        pygame.draw.circle(prozor, boja, pozicijaKursora, 5)
    if pygame.mouse.get_pressed()[2]:
        pygame.draw.circle(prozor, CRNA, pozicijaKursora, 5)

    pygame.display.flip()
    sat.tick(60)

pygame.quit()
