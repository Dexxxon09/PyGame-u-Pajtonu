import pygame
import random

pygame.init()

dimenzija = 25  # velicina polja (to jest domenzije polja po kojem se krece zmija, 25x25)
vel_kvadrata = 20  # velicina jednog polj au pikselima
prozor = pygame.display.set_mode((dimenzija * vel_kvadrata, dimenzija * vel_kvadrata))

sat = pygame.time.Clock()
pygame.display.set_caption("Zmija")

"""
Neka je zmija lista delova zmije u matrici, gde je (a, b)
deo zmije u polju reda a i kolone b
Prvi element je rep zmije, a poslednji - njena glava
. . . . . .
. r * . . .
. . * . . .
. . G . . .
. . . . . .
"""
zmija = [(1, 1), (1, 2), (2, 2), (3, 2)]
pravac = "DOLE"

"""
Pocetna pozicija prve jabuke (centar ekrana)
"""
hrana = (12, 12)

program_radi = True
while program_radi:
    # u jednoj petlji mozemo samo jednom promeniti pravac
    promenili_pravac = False

    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            program_radi = False

        if dogadjaj.type == pygame.KEYDOWN and promenili_pravac == False:
            taster = dogadjaj.key

            """
            Ako se desilo da je igrac kliknuo strelicu i ta promena pravca je validna (zmija ne moze da se okrene
            u jednom potezu za 180 stepeni pa to nije validno), menjamo vrednost promenljive "pravac" i blokiramo 
            promene tako sto postavljamo "promenili_pravac" na True
            """
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

    """
    U zavisnosti od toga koji je pravac, nalazimu poziciju nove glave zmije
    """
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

    """
    Ukoliko je nova_glava izasla van granica mape (slupala se o zid) ili se vec nalazi u listi zmija
    (slupala se sama o sebe), igrac je izgubio pa igru prekidamo
    """
    if red < 0 or kolona < 0 or red >= dimenzija or kolona >= dimenzija or nova_glava in zmija:
        print("GAME OVER")
        print("Final score:", (len(zmija) - 4) * 100)
        pygame.quit()
        exit(0)

    """
    Dodajemo glavu na kraj liste (za detalje pogledajte liste.py)
    """
    zmija.append(nova_glava)

    """
    Ukoliko se nova_glava poklopila s hranom, znaci da je zmija naisla na hranu i pojela
    U tom slucaju zmija raste, pa ne moramo da skracujemo rep, a hranu moramo da pomerimo na novu poziciju
    """
    if nova_glava == hrana:
        print("SCORE:", (len(zmija) - 4) * 100)
        pygame.display.set_caption("Zmija | Score: " + str((len(zmija) - 4) * 100))

        # trazimo novu poziciju sve dok ne nadjemo slobodnu (ne smemo praviti hranu u (in) zmiji)
        while hrana in zmija:
            hrana = (random.randint(0, 24), random.randint(0, 24))
    else:
        # ako nije pojela hranu, standardno skracujemo zmiju jer nije porasla
        zmija.pop(0)

    """
    Crtamo hranu i zmiju
    """
    prozor.fill((0, 0, 0))

    pygame.draw.circle(prozor, (255, 0, 0),
                       (hrana[1] * vel_kvadrata + vel_kvadrata // 2, hrana[0] * vel_kvadrata + vel_kvadrata // 2),
                       vel_kvadrata // 2)

    for komad_zmije in zmija:
        red, kolona = komad_zmije
        pygame.draw.rect(prozor, (255, 255, 255),
                         (kolona * vel_kvadrata, red * vel_kvadrata, vel_kvadrata, vel_kvadrata))

    pygame.display.flip()
    sat.tick(8)

pygame.quit()
