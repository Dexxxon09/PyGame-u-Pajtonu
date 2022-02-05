import pygame
prozor = pygame.display.set_mode((300, 300))

prozor.fill(pygame.Color("white"))
pygame.draw.polygon(prozor, pygame.Color("black"),
                    [
                        (60,60),
                        (120,60),
                        (120,240),
                        (60,240),
                        (60,180),
                        (240,180),
                        (240,240),
                        (180,240),
                        (180,60),
                        (240,60),
                        (240,120),
                        (60,120)
                    ], 4)

pygame.display.flip()
pygame.time.wait(3000)