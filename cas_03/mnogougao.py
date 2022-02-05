import pygame
pygame.init()
prozor = pygame.display.set_mode((400, 300))

# petougao definisan sa pet tacaka datih u listi (nizu)
pygame.draw.polygon(prozor, pygame.Color("red"), [(50, 50),
                                                  (200, 150),
                                                  (350, 50),
                                                  (350, 250),
                                                  (50, 250)])

pygame.display.flip()
pygame.time.wait(4000)