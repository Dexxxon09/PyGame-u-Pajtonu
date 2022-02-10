import pygame

# pogledajte fajl boje.py
from boje import *

pygame.init()
prozor = pygame.display.set_mode((600, 600))
sat = pygame.time.Clock()

# Posto se u ovom programu nista ne krece, ne moramo da iznova crtamo celu sliku u svakom frejmu,
# vec cemo samo dodavati 'iks' i 'oks' kad ih budu postavljali igraci.
# Krenemo od toga sto cemo nacrtati tablu:

prozor.fill(BELA)
pygame.draw.line(prozor, CRNA, (200, 0), (200, 600), 5)  # leva vertikalna
pygame.draw.line(prozor, CRNA, (400, 0), (400, 600), 5)  # desna vertikalna
pygame.draw.line(prozor, CRNA, (0, 200), (600, 200), 5)  # gornja horizontalna
pygame.draw.line(prozor, CRNA, (0, 400), (600, 400), 5)  # donja horizontalna
pygame.display.flip()

# pravimo 3x3 matricu koja predstavlja tablu
tabla = [
    # 0.    1.    2. kolone
    [None, None, None],  # 0. red
    [None, None, None],  # 1. red
    [None, None, None],  # 2. red
]

# igrac na potezu
na_potezu = 'X'

program_radi = True
while program_radi:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            program_radi = False

        # hvatamo levi klik misa (levo dugme ima kod 1)
        if dogadjaj.type == pygame.MOUSEBUTTONDOWN and dogadjaj.button == 1:
            x, y = dogadjaj.pos  # ovo mozemo postici i sa:  x, y = pygame.mouse.get_pos()

            """
            Sada treba da odredimo koju kolonu smo stisnuli... Imamo tri slucaja:
                1.   0 <= x < 200  kolona sa indkesom 0
                2. 200 <= x < 400  kolona sa indeksom 1
                3. 400 <= x < 600  kolona sa indeksom 2
                
            Mozemo napisati nesto poput:
                kolona = 0
                if x < 200:
                    kolona = 0
                elif x < 400:
                    kolona = 1
                else:
                    kolona = 2    

            Znatno je krace da napisemo ('//' je celobrojno deljenje):
                kolona = x // 200
            Zaista, u prvom slucaju x//200 bude nula, u drugom je 1, a u trecem 2
            """

            kolona = x // 200
            red = y // 200

            # menjamo nesto samo ako je stisnuto prazno polje! (tj ako je polje None)
            if tabla[kolona][red] is None:

                if na_potezu == 'X':
                    # crtamo X i upisujemo u tablu
                    tabla[kolona][red] = 'X'
                    pygame.draw.line(surface=prozor, color=CRVENA, width=10,
                                     start_pos=(kolona * 200, red * 200),
                                     end_pos=(kolona * 200 + 200, red * 200 + 200))
                    pygame.draw.line(surface=prozor, color=CRVENA, width=10,
                                     start_pos=(kolona * 200 + 200, red * 200),
                                     end_pos=(kolona * 200, red * 200 + 200))
                    na_potezu = 'O'
                else:
                    # crtamo O i upisujemo u tablu
                    tabla[kolona][red] = 'O'
                    pygame.draw.circle(surface=prozor, color=PLAVA, center=(kolona * 200 + 100, red * 200 + 100),
                                       radius=100, width=10)
                    na_potezu = 'X'

                pygame.display.flip()

    # Kako se nista ne krece, ne moramo da stvaramo iluziju glatkog kretanja, pa je FPS relativno mali
    sat.tick(10)

pygame.quit()
