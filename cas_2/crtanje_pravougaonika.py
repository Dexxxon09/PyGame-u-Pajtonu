import pygame

pygame.init()
prozor = pygame.display.set_mode((400, 300))

"""
Pravougaonik se crta funkcijom pygame.draw.rectangle()
Njeni parametri su:
    - surface: povrsina na kojoj se duz crta
    - color: boja pravougaonika
    - rect: cetvorka gde prva dva broja predstavljaju koordinatu gornjeg levog ugla, a druga dva sirinu i visinu 
"""

# zeleni kvadrat dimenzija 150x150
pygame.draw.rect(surface=prozor,
                 color=pygame.Color('green'),
                 rect=pygame.Rect(50, 100, 150, 150))

# crveni pravougaonik dimenzija 200x100
pygame.draw.rect(surface=prozor,
                 color=pygame.Color('red'),
                 rect=pygame.Rect(100, 50, 200, 100))

pygame.display.flip()

pygame.time.wait(3000)
pygame.quit()
