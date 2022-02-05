import pygame

pygame.init()
prozor = pygame.display.set_mode((400, 300))

pygame.draw.polygon(surface=prozor,
                    color=pygame.Color('gold'),
                    points=[(50, 50), (350, 50), (350, 250), (200, 150), (50, 250)],
                    width=5)

pygame.display.flip()

pygame.time.wait(3000)
pygame.quit()
