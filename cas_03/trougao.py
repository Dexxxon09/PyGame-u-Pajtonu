import pygame
pygame.init()
prozor = pygame.display.set_mode((400, 300))

# zuti trougao koji izlazi izvan ekrana (teme (50, 350) je ispod donje ivice)
pygame.draw.polygon(prozor, pygame.Color("yellow"), [(50, 50), (350, 50), (50, 350)])

# crveni trougao
pygame.draw.polygon(prozor, pygame.Color("red"), [(100, 50), (300, 50), (100, 250)])

pygame.display.flip()
pygame.time.wait(4000)