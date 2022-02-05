import pygame
pygame.init()
prozor = pygame.display.set_mode((400, 300))

# zuta ivica oko celog prozora
pygame.draw.rect(prozor, pygame.Color("yellow"), (0, 0, 400, 300), 5)

# plavi kvadrat 200x200 i njegova crvena ivica
pygame.draw.rect(prozor, pygame.Color("blue"), (50, 50, 200, 200))
pygame.draw.rect(prozor, pygame.Color("red"), (50, 50, 200, 200), 3)

pygame.display.flip()
pygame.time.wait(4000)