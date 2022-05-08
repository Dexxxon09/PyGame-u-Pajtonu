import pygame
from pygame import Vector2
from random import randint

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Times New Roman", 20)

ball_pos = Vector2(300, 300)
ball_vel = Vector2(10, 5)

paddle_size = Vector2(10, 60)
left_paddle = Vector2(0, 300-paddle_size.y//2)
right_paddle = Vector2(590, 300-paddle_size.y//2)

score_levo = 0
score_desno = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    ball_pos += ball_vel

    """ KONTROLE """
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle.y -= 10
    if keys[pygame.K_s]:
        left_paddle.y += 10
    if keys[pygame.K_UP]:
        right_paddle.y -= 10
    if keys[pygame.K_DOWN]:
        right_paddle.y += 10

    """ ODBIJANJE OD LOPATICA """
    if ball_pos.x >= 590 and right_paddle.y <= ball_pos.y <= right_paddle.y + paddle_size.y:
        ball_vel.x = -ball_vel.x
        ball_vel.y += randint(-10, 10)  # kad se odbije y komponenta se promeni (da nam malo zabiberi zivot)
    if ball_pos.x <= 10 and left_paddle.y <= ball_pos.y <= left_paddle.y + paddle_size.y:
        ball_vel.x = -ball_vel.x
        ball_vel.y += randint(-10, 10)  # kad se odbije y komponenta se promeni (da nam malo zabiberi zivot)

    """ Kontrlismeo da y komponenta ne pstane prevelika (moze da bude izmedju -10 i 10) """
    if ball_vel.y > 10:
        ball_vel.y = 10
    if ball_vel.y < -10:
        ball_vel.y = -10

    """ Vertikalni zidovi (kad se slupi protivnik dobije poen, a loptica se vrati u centar) """
    if ball_pos.x >= 610:
        ball_pos = Vector2(300, 300)
        ball_vel = Vector2(10, 5)
        score_levo += 1
    if ball_pos.x <= -10:
        ball_pos = Vector2(300, 300)
        ball_vel = Vector2(10, 5)
        score_desno += 1

    """ Horizontalni zidovi (krov i dno prozora) """
    if ball_pos.y >= 610 or ball_pos.y <= -10:
        ball_vel.y = -ball_vel.y

    """ RENDIRANJE SLIKE """
    window.fill(pygame.Color("black"))
    pygame.draw.circle(window, pygame.Color("red"), ball_pos, 5)
    pygame.draw.rect(window, pygame.Color("white"), pygame.Rect(left_paddle, paddle_size))
    pygame.draw.rect(window, pygame.Color("white"), pygame.Rect(right_paddle, paddle_size))

    """ Prikaz piena """
    score_levo_tekst = font.render(f"{score_levo}", True, pygame.Color("white"))
    window.blit(score_levo_tekst, (5, 5))
    score_desno_tekst = font.render(f"{score_desno}", True, pygame.Color("white"))
    window.blit(score_desno_tekst, (595-score_desno_tekst.get_rect().width, 5))

    pygame.display.flip()
    clock.tick(30)
