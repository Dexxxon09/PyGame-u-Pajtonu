import pygame

pygame.init()

prozor = pygame.display.set_mode((400, 400))

for i in range(1, 19):
    pygame.draw.line(prozor, pygame.Color("white"), (i*20, i*20), (i*20+20, i*20), 3)

pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()


