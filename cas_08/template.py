import pygame

pygame.init()
prozor = pygame.display.set_mode((600,600))
sat = pygame.time.Clock()

program_radi = True
while program_radi:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            program_radi = False

    prozor.fill((0,0,0))

    """
    vas kod
    """

    pygame.display.flip()
    sat.tick(30)

pygame.quit()
