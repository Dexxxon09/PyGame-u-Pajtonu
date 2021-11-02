import pygame

pygame.init()

prozor = pygame.display.set_mode((400, 400))

for i in range(5):
    pygame.draw.circle(prozor, pygame.Color("white"), (100+i*50, 200), 15)

pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()


