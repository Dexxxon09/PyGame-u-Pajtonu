import pygame

pygame.init()
prozor = pygame.display.set_mode((900, 300))
sat = pygame.time.Clock()

auto = pygame.image.load("auto.png")

y = 150    # y-koordinata auta, ne menja se
x = 450    # x-koordinata auta
v = 0      # brzina auta (na pocetku stoji)

a = 100    # ubrzanje auta u pikselima/s^2
dt = 1/30  # vremenski interval - trajanje jednog frejma

while True:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            pygame.quit()
            exit()

    tasteri = pygame.key.get_pressed()
    if tasteri[pygame.K_LEFT]:
        v = v - a * dt
    if tasteri[pygame.K_RIGHT]:
        v = v + a * dt
    x = x + v * dt

    # ukoliko je auto izvan granica ekrana, teleportujemo ga na drugu stranu
    if x < -100:
        x = 900
    elif x > 900:
        x = -100

    prozor.fill((255, 255, 255))
    prozor.blit(auto, (x-50, y))
    pygame.draw.rect(prozor, (0, 0, 0), (0, 250, 900, 100))
    pygame.display.flip()

    sat.tick(30)

pygame.quit()