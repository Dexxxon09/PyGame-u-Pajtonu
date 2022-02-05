import pygame

pygame.init()
prozor = pygame.display.set_mode((400, 300))

"""
Mnogougao se crta funkcijom pygame.draw.polygon()
Njeni parametri su:
    - surface: povrsina na kojoj se duz crta
    - color: boja
    - points: lista koordinata temena mnogougla
Ova funkcija iscrtava mnogougao i popunjava ga izabranom bojom.

Postoji mogucnost da se doda i ctvrti argument:
    - width: debljina stranice u pikselima
U ovom slucaju bice nacrtana samo kontura odgovrajuce boje, a 
unutrasnjost nece biti obojena.
"""

# obojen zeleni trougao
pygame.draw.polygon(surface=prozor,
                    color=pygame.Color('green'),
                    points=[(50, 50), (350, 50), (50, 250)])

# neobojena crvena kontura
pygame.draw.polygon(surface=prozor,
                    color=pygame.Color('red'),
                    points=[(350, 250), (350, 50), (50, 250)],
                    width=5)


pygame.display.flip()

pygame.time.wait(3000)
pygame.quit()
