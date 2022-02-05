import pygame

window = pygame.display.set_mode((600, 600))

x = 300
y = 300
r = 250

for i in range(7):
    pygame.draw.circle(window, pygame.Color("white"), (x, y), r, 3)
    r -= 35
    if i % 2 == 0:
        x -= 35
    else:
        x += 35

pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
