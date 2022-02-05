import pygame

pygame.init()
prozor = pygame.display.set_mode((730, 270))

for idx, boja in enumerate(pygame.color.THECOLORS):
    red = idx // 73
    kolona = idx % 73
    pygame.draw.rect(surface=prozor,
                     color=pygame.Color(boja),
                     rect=pygame.Rect(kolona*10, red*30, 10, 30))

pygame.display.flip()

pygame.time.wait(3000)
pygame.quit()