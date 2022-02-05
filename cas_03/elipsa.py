import pygame
pygame.init() 
prozor = pygame.display.set_mode((400, 300)) 

# plavi pravougaonik i crvena elipsa upisana u njega
pygame.draw.rect(prozor, pygame.Color("blue"), (50, 50, 300, 150))
pygame.draw.ellipse(prozor, pygame.Color("red"), (50, 50, 300, 150))

pygame.display.flip()
pygame.time.wait(4000)