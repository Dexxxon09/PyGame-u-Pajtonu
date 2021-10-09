import pygame

pygame.init()
prozor = pygame.display.set_mode((400, 300))

"""
Duz se crta funkcijom pygame.draw.circle()
Njeni parametri su:
    - surface: povrsina na kojoj se duz crta
    - color: boja kruga
    - center: koordinate centra pravougaonika
    - radius: poluprecnik kruga
"""

pygame.draw.circle(surface=prozor,
                   color=pygame.Color('red'),
                   center=(200, 150),
                   radius=100)

pygame.draw.circle(surface=prozor,
                   color=pygame.Color('white'),
                   center=(200, 150),
                   radius=50)

pygame.display.flip()

pygame.time.wait(3000)
pygame.quit()
