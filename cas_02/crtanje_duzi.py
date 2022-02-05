import pygame

pygame.init()
prozor = pygame.display.set_mode((400, 300))

"""
Duz se crta funkcijom pygame.draw.line()
Njeni parametri su:
    - surface: povrsina na kojoj se duz crta
    - color: boja duzi
    - start_pos: koordinate prve tacke
    - end_pos: koordinate druge tacke
    - width: sirina duzi u pikselima
"""

pygame.draw.line(surface=prozor,
                 color=pygame.Color('yellow'),
                 start_pos=(50, 50),
                 end_pos=(300, 150),
                 width=5)

pygame.draw.line(surface=prozor,
                 color=pygame.Color('red'),
                 start_pos=(150, 50),
                 end_pos=(150, 250),
                 width=5)

pygame.display.flip()

pygame.time.wait(3000)
pygame.quit()
