import pygame
from pygame.math import Vector2

prozor = pygame.display.set_mode((400,400))
prozor.fill(pygame.Color("yellow"))

leviTocak = Vector2(-15, -15)
desniTocak = Vector2(15, -15)
auto = Vector2(-30, -45)
kapa = Vector2(-15, -75)

vektorPolozaja = Vector2(150, 150)

pygame.draw.circle(prozor, pygame.Color("black"), leviTocak+vektorPolozaja, 7)
pygame.draw.circle(prozor, pygame.Color("black"), desniTocak+vektorPolozaja, 7)
pygame.draw.rect(prozor, pygame.Color("gray"), tuple(auto+vektorPolozaja) + (60, 30))
pygame.draw.rect(prozor, pygame.Color("gray"), tuple(kapa+vektorPolozaja) + (30, 30))

pygame.display.flip()

pygame.time.wait(3000)














