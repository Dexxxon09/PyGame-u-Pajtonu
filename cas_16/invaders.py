import pygame
from pygame import Vector2

pygame.init()
prozor = pygame.display.set_mode((600,600))
sat = pygame.time.Clock()

# stvari vezane za igraca / letelicu
letelica = pygame.image.load("letelica.png")
letelica = pygame.transform.scale(letelica, (60,60))
brzina_letelice = 10
x = 300

# stvari vezane za metak
metak = None
brzina_metka = 20

# stvari vezane za vanzemaljce
vanzemaljac = pygame.image.load("vanzemaljac.png")
vanzemaljac = pygame.transform.scale(vanzemaljac, (36,48))
lista = []
for red in range(6):            # imamo 6 redova i 8 kolona vanzemaljaca
    for kolona in range(8):
        # svaki red je spusten za 60 u odnosu na rethodni, a svaka sledeca kolona pomerena za 50 udesno
        lista.append(Vector2(20+kolona*60, 20+red*50))
smer = "DESNO"  # pocetni smer kretanja flote vanzemaljaca

program_radi = True
while program_radi:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            program_radi = False
    """
    Interakcija sa korisnikom
    """
    tasteri = pygame.key.get_pressed()
    if tasteri[pygame.K_LEFT] and x > 50:    # pomeranje letelice ulevo
        x -= brzina_letelice
    if tasteri[pygame.K_RIGHT] and x < 550:  # pomeranje letelice udesno
        x += brzina_letelice
    if tasteri[pygame.K_SPACE] and (metak is None):  # ako trenutno nije ispaljen metak pucamo
        metak = Vector2(x, 500)

    """
    Crtanje i pomeranje
    """
    prozor.fill((0, 0, 0))

    # ako metak postoji, pomeramo ga i crtamo (ako ne postoji preskacemo if to jest ne radimo nista)
    if metak:
        metak.y -= brzina_metka
        pygame.draw.line(prozor, pygame.Color("red"), metak, metak + Vector2(0, 15), 5)

        # provera da li smo pogodili nekog vanzemaljca
        for vanzemaljac_poz in lista:
            hitbox = pygame.Rect(vanzemaljac_poz, (36,48))  # hitbox - pravougaonik u kojem se nalazi vanzemaljac
            if hitbox.collidepoint(metak.x, metak.y):  # ako je metak unutar hitbox-a znaci da smo pogodili
                lista.remove(vanzemaljac_poz)  # sklanjamo mrtvog vanzemaljca
                metak = None  # iskoriscen metak nestaje
                break  # prekidamo petlju jer odjednom ne mozemo ubiit vise vanzemaljaca

        # ako je metak izasao van ekrana, brisemo ga
        if metak and metak.y < 0:
            metak = None

    # ako je duzina liste nule, to znaci da nije ostalo vanzemaljca - pobeda!
    if len(lista) == 0:
        font = pygame.font.SysFont("Arial", 50)
        text = font.render("You have won!", True, pygame.Color("white"), pygame.Color("blue"))
        prozor.blit(text, (120, 220))
        pygame.display.flip()
        pygame.time.wait(5000)
        pygame.quit()
        exit(0)

    # ako su vanzemaljci stigli do dna ekrana, izgubili smo
    if max(i.y for i in lista) >= 480:
        font = pygame.font.SysFont("Arial", 50)
        text = font.render("GAME OVER!", True, pygame.Color("white"), pygame.Color("blue"))
        prozor.blit(text, (120, 220))
        pygame.display.flip()
        pygame.time.wait(5000)
        pygame.quit()
        exit(0)

    # pomeramo vanzemaljce levo/desno (u zavisnosti od trenutnog smera kretanja)
    for vanzemaljac_poz in lista:
        if smer == "DESNO":
            vanzemaljac_poz.x += 2
        elif smer == "LEVO":
            vanzemaljac_poz.x -= 2

    # kada stignemo do desne granice menjamo smer i spustamo nadole
    if max(i.x for i in lista) > 550:  # max(i.x for i in lista) je najveca X-koordinata vanzemaljaca
        smer = "LEVO"
        for vanzemaljac_poz in lista:
            vanzemaljac_poz.y += 20

    # kada stignemo do leve granice menjamo smer i spustamo nadole
    if min(i.x for i in lista) < 10:  # max(i.x for i in lista) je najmanja X-koordinata vanzemaljaca
        smer = "DESNO"
        for vanzemaljac_poz in lista:
            vanzemaljac_poz.y += 20

    # crtamo vanzemaljce i letelicu
    for vanzemaljac_poz in lista:
        prozor.blit(vanzemaljac, vanzemaljac_poz)
    prozor.blit(letelica, (x-30, 530))

    pygame.display.flip()
    sat.tick(30)

pygame.quit()
