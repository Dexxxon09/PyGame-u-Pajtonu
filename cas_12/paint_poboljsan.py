"""
Ideja je da tacke spajamo duzima, pa da tako dobijam normalne (neisprekidane) linije
"""

import pygame
from boje import *

pygame.init()
prozor = pygame.display.set_mode((600,600))
sat = pygame.time.Clock()

prozor.fill(CRNA)

prethodna_tacka = None

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
        """
        Ukoliko tek krecemo da crtamo liniju, prethodna_tacka je None, pa ne crtamo duz nego samo kruzic.
        
        U suportnom, prethodna_tacka je stara pozicija kursora, pa mozemo da je spojimo sa trenutnom 
            cime dobijamo liniju.
        """
        if prethodna_tacka is None:
            pygame.draw.circle(prozor, boja, pozicijaKursora, 2)
        else:
            pygame.draw.line(prozor, boja, pozicijaKursora, prethodna_tacka, 5)
        """
        Postavljamo prethodnu tacku na poziciju kursora (u sledecem frejmu ta pozicija ce biti stara)
        """
        prethodna_tacka = pozicijaKursora

    elif pygame.mouse.get_pressed()[2]:
        """
        Sve isto ali za brisanje
        """
        if prethodna_tacka is None:
            pygame.draw.circle(prozor, CRNA, pozicijaKursora, 2)
        else:
            pygame.draw.line(prozor, CRNA, pozicijaKursora, prethodna_tacka, 5)
        prethodna_tacka = pozicijaKursora

    else:
        """
        Ako nije stisnut nijedan taster, ne crtamo nista, vec brisemo informaciju u prethodnoj tacki
        """
        prethodna_tacka = None

    pygame.display.flip()
    sat.tick(60)

pygame.quit()
