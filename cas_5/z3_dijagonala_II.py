import pygame

pygame.init()

prozor = pygame.display.set_mode((400, 400))

for i in range(20):
    pygame.draw.rect(prozor, pygame.Color("white"), (i*20, 380-i*20, 20, 20))

pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()


