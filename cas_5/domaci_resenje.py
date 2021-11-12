import pygame

pygame.init()

prozor = pygame.display.set_mode((400, 400))

prozor.fill(pygame.Color("yellow"))

y = 40

for i in range(16):
    x = 80

    if i % 2 == 0:
        x = 160

    pygame.draw.line(prozor, pygame.Color("black"), (x, y), (x+160, y), 5)

    y = y + 20

pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()


