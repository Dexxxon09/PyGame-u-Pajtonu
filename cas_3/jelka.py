import pygame
pygame.init()
prozor = pygame.display.set_mode((400, 300))

x = 200
y = 0
H = 280

# Crtamo jelku ciji je vrh u (x, y), a ima visinu H

# Najpre crtamo stablo dimenzija 20x20, nalazi se H pikslea ispod vrha (y+H),
# a njegovo gornje levo teme ima x koordinatu x-10 (pomereno je ulevo
# u odnosu na simetralu za pola svoje sirine)
pygame.draw.rect(prozor, pygame.Color("brown"), (x-10, y+H, 20, 20))

# Crtamo trougao, jedno teme (vrh) ima koordinate (x, y), a druga dva su
# spustena za H nadole (y+H). Jedno je levo, a drugo je desno od simetrale,
# to jest imaju koordinate (x-50, y+H) i (x+50, y+H)
pygame.draw.polygon(prozor, pygame.Color("green"), [(x, y),
                                                    (x-50, y+H),
                                                    (x+50, y+H)])

# Ovim dobijamo sliku koja moze da se lako pomera
# x i y odredjuju poziciju jelke, a promenom H menjam njenu visinu

pygame.display.flip()
pygame.time.wait(4000)

