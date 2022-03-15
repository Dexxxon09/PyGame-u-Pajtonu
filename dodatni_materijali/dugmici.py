import pygame
from pygame import Vector2

pygame.init()
prozor = pygame.display.set_mode((600,600))
sat = pygame.time.Clock()

mojFont = pygame.font.SysFont('Consolas', 30)


class Dugme:
    tekst = None  # tekst je renderovan tekst (sadrzaj + boja)
    rect = None   # pravougaonik u formatu (x, y, sirina, visina)
    boja = None   # RGB boja pozadine dugmeta


# funkcija crta dugme, pri cemo je tekst zalepljen za gornji levi cosak
def nacrtaj_dugme_bez_centiranja(dugme):
    pygame.draw.rect(prozor, dugme.boja, dugme.rect)
    prozor.blit(dugme.tekst, dugme.rect.topleft)  # lepsi nacin od linije dole, TOPLEFT je pozicija gornje leve tacke
    # prozor.blit(dugme.tekst, (dugme.rect.x, dugme.rect.y) )

# ova funkcija koristi slican pristup kao sto smo koristili za centrianje rotirane slike, tekst je zapravo i sam slika
# i mi ga crtamo tako da njegov centar poklopi sa centrom dugmeta
def nacrtaj_dugme(dugme):
    pygame.draw.rect(prozor, dugme.boja, dugme.rect)
    prozor.blit(dugme.tekst, Vector2(dugme.rect.center) - dugme.tekst.get_rect().center)

exit_dugme = Dugme()
exit_dugme.tekst = mojFont.render("EXIT", True, (255, 255, 255))  # ovde se zadaje tekst i boja
exit_dugme.rect = pygame.Rect(100, 100, 100, 50)  # x, y, sirina, visina (isto kao kad crtamo pravougaonik)
exit_dugme.boja = (128, 128, 128)

dugme2 = Dugme()
dugme2.tekst = mojFont.render("Drugo dugme", True, (0, 0, 0))
dugme2.rect = pygame.Rect(200, 200, 150, 150)
dugme2.boja = (255, 0, 0)

program_radi = True
while program_radi:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            program_radi = False

        if dogadjaj.type == pygame.MOUSEBUTTONDOWN:

            if exit_dugme.rect.collidepoint(dogadjaj.pos):
                print("Klik na EXIT dugme!")
                program_radi = False

            if dugme2.rect.collidepoint(dogadjaj.pos):
                print("Klik na dugme2!")


    prozor.fill((0,0,0))

    nacrtaj_dugme(exit_dugme)
    nacrtaj_dugme_bez_centiranja(dugme2)

    pygame.display.flip()
    sat.tick(30)

pygame.quit()
