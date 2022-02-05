import pygame

prozor = pygame.display.set_mode((600, 600))

slika = pygame.image.load("macka.png")
slika = pygame.transform.scale(slika, (600, 300)) # razvucemo sliku do dimenzija 600x300
slika = pygame.transform.rotate(slika, 45) # rotiramo sliku za 45 stepeni ulevo

prozor.blit(slika, (0, 0))

pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()

