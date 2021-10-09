import pygame

pygame.init()

prozor = pygame.display.set_mode((400, 300))  # stvaramo prozor dimenzija 400x300

prozor.fill(color=pygame.Color('yellow'))  # bojimo ceo prozor zutom bojom

pygame.display.flip()  # promene u baferu saljemo na ekran
pygame.time.wait(3000)

pygame.quit()
