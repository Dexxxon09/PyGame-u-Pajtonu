import pygame

pygame.init()
prozor = pygame.display.set_mode((600,600))
sat = pygame.time.Clock()

mojFont = pygame.font.SysFont("Consolas", 160)
text = mojFont.render("primer teksta", True, (255,255,255))

program_radi = True
while program_radi:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            program_radi = False

    prozor.fill((0,0,0))

    prozor.blit(text, (100,100))

    pygame.display.flip()
    sat.tick(30)

pygame.quit()
