import pygame
import sys

pygame.init()


w = 800
h = 600

screen_color = (255, 255, 255)
ball_color = (255, 0, 0)

ball_radius = 25
ball_x = (w - ball_radius) // 2
ball_y = (h - ball_radius) // 2
ball_speed = 20

screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Red Ball")


while True:
    screen.fill(screen_color)

    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    pygame.display.flip()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - ball_speed >= 0:
                    ball_y -= ball_speed
            elif event.key == pygame.K_DOWN:
                if ball_y + ball_speed <= h - ball_radius:
                    ball_y += ball_speed
            elif event.key == pygame.K_LEFT:
                if ball_x - ball_speed >= 0:
                    ball_x -= ball_speed
            elif event.key == pygame.K_RIGHT:
                if ball_x + ball_speed <= w - ball_radius:
                    ball_x += ball_speed

    pygame.time.Clock().tick(30)
