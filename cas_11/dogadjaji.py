import pygame

pygame.init()
prozor = pygame.display.set_mode((600,600))
sat = pygame.time.Clock()

program_radi = True
while program_radi:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            program_radi = False
        if dogadjaj.type == pygame.KEYDOWN: # kada se stisne dugme
            if dogadjaj.key == pygame.K_LEFT:
                print("Left")
        if dogadjaj.type == pygame.KEYUP: # kada se dugme pusti
            pass
        if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
            print(dogadjaj.pos, dogadjaj.button)
        if dogadjaj.type == pygame.MOUSEWHEEL:
            print(dogadjaj.x, dogadjaj.y)
        if dogadjaj.type == pygame.MOUSEMOTION:
            print(dogadjaj.pos, dogadjaj.rel)

    prozor.fill((0,0,0))

    """
    vas kod
    """

    pygame.display.flip()
    sat.tick(30)

pygame.quit()
