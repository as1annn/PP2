import pygame 
from datetime import datetime
 
pygame.init() 
screen = pygame.display.set_mode((1200, 800)) 
running = True 
clock = pygame.time.Clock() 
main_clock = pygame.image.load("C:/Users/SystemX/Desktop/lab7/images/mainclock.png")
right_hand = pygame.image.load("C:/Users/SystemX/Desktop/lab7/images/rightarm.png")
left_hand = pygame.image.load("C:/Users/SystemX/Desktop/lab7/images/leftarm.png")

done = False
clock_place = main_clock.get_rect(center=(1200/2, 800/2))
minute_place = right_hand.get_rect(center=(1200/2, 800/2))
second_place = left_hand.get_rect(center=(1200/2, 800/2))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    cur_time = datetime.now().time()


    seconds_angle = -(cur_time.second * 6)
    minutes_angle = -(cur_time.minute * 6) - (cur_time.second / 10) - 68*6
    
    leftarm_move = pygame.transform.rotate(left_hand, seconds_angle)
    rightarm_move = pygame.transform.rotate(right_hand, minutes_angle)
    
    leftarm_rect = leftarm_move.get_rect(center=clock_place.center)
    rightarm_rect = rightarm_move.get_rect(center=clock_place.center)
    
    screen.fill((255, 255, 255))
    screen.blit(main_clock, clock_place)
    screen.blit(leftarm_move, leftarm_rect)
    screen.blit(rightarm_move, rightarm_rect)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

