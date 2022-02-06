import pygame

pygame.init()
prozor = pygame.display.set_mode((600,600))
sat = pygame.time.Clock()

prozor.fill((0,0,0))

boja = "white"

# na tastaturi
# w - white
# r - red
# g - green
# b - blue

program_radi = True
while program_radi:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            pygame.image.save(prozor, "slika.png")
            program_radi = False
        if dogadjaj.type == pygame.KEYDOWN:
            if dogadjaj.key == pygame.K_w:
                boja = "white"
            if dogadjaj.key == pygame.K_r:
                boja = "red"
            if dogadjaj.key == pygame.K_g:
                boja = "green"
            if dogadjaj.key == pygame.K_b:
                boja = "blue"

    pozicijaKursora = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        pygame.draw.circle(prozor, pygame.Color(boja), pozicijaKursora, 5)
    if pygame.mouse.get_pressed()[2]:
        pygame.draw.circle(prozor, pygame.Color("black"), pozicijaKursora, 5)

    pygame.display.flip()
    sat.tick(144)

pygame.quit()
