import pygame

pygame.init()
prozor = pygame.display.set_mode((400, 300))

"""
Elipsa se crta funkcijom pygame.draw.ellipse()
Njeni parametri su:
    - surface: povrsina na kojoj se duz crta
    - color: boja kruga
    - rect: koordinate pravougaonika u koji je elipsa upisana
"""

pygame.draw.ellipse(surface=prozor,
                    color=pygame.Color('green'),
                    rect=pygame.Rect(100, 50, 250, 100))

pygame.draw.rect(surface=prozor,
                 color=pygame.Color('red'),
                 rect=pygame.Rect(100, 50, 250, 100),
                 width=2)

pygame.display.flip()

pygame.time.wait(3000)
pygame.quit()
