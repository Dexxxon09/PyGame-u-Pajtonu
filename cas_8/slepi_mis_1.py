import pygame

prozor = pygame.display.set_mode((600, 600))

# slike je lista svih slicica macke
slike = []
slike.append( pygame.image.load("mis1.png") )
slike.append( pygame.image.load("mis2.png") )

redni_broj = 0

while True:
    prozor.fill((0,0,0))
    trentuna_slika = pygame.transform.scale(slike[redni_broj], (400, 400))

    # menjamo broj trenutne slike (kad izadjemo van granica vratimo se na nulu)
    redni_broj = (redni_broj + 1) % len(slike)

    prozor.blit(trentuna_slika, (50,50))

    pygame.display.flip()
    pygame.time.wait(200)
