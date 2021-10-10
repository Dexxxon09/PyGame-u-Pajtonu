import pygame
pygame.init()  # olaksava zivot
prozor = pygame.display.set_mode((400, 300))  # pravim prozor dimenzija 400x300

""" DALJE SLEDI VAS KOD ⬇ """

# bojene pozadine nekom bojom
prozor.fill(pygame.Color('yellow'))

# Kada crtate, na prvom mestu ide povrsina na kojoj crtate (prozor), a
# na drugom boja. Boja moze biti u formatu `pygame.Color("boja")` ili
# `(r, g, b)`. Alat za RGB boje: https://g.co/kgs/ZmPsJM

# rect = rectangle = cetvorougao
# 1. prozor
# 2. boja
# 3. (x, y, sirina, visina)
pygame.draw.rect(prozor, (157, 255, 71), (50, 150, 100, 50))

# circle = krug/kruznica
# 1. prozor
# 2. boja
# 3. centar (x, y)
# 4. poluprecnik R
pygame.draw.circle(prozor, pygame.Color("red"), (200, 150), 50)

# line = duz
# 1. prozor
# 2. boja
# 3. prva tacka (x1, y1)
# 4. druga tacka (x2, y2)
pygame.draw.line(prozor, pygame.Color("pink"), (0, 0), (400, 300), 5)

""" KRAJ VASEG KODA """

pygame.display.flip()  # okrece tablu / refreshuje ekran
pygame.time.wait(4000)
