
import pygame

pygame.init()
done = False
paused = False
screen = pygame.display.set_mode((700, 500))
player_sc = pygame.image.load("C:/Users/SystemX/Desktop/lab7/images/dota.png")
music_list = [
    pygame.mixer.Sound("C:/Users/SystemX/Desktop/lab7/music/a.mp3"),
    pygame.mixer.Sound("C:/Users/SystemX/Desktop/lab7/music/b.mp3"),
    pygame.mixer.Sound("C:/Users/SystemX/Desktop/lab7/music/c.mp3"),
    pygame.mixer.Sound("C:/Users/SystemX/Desktop/lab7/music/d.mp3")
]
play_place = player_sc.get_rect(center=(700/2, 500/2))
current_music_index = 0
music_list[current_music_index].play()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if not paused:
            music_list[current_music_index].stop()
            paused = True
        else:
            music_list[current_music_index].play()
            paused = False

    elif keys[pygame.K_RIGHT]:
        music_list[current_music_index].stop()
        current_music_index = (current_music_index + 1) % len(music_list)
        music_list[current_music_index].play()
        paused = False

    elif keys[pygame.K_LEFT]:
        music_list[current_music_index].stop()
        current_music_index = (current_music_index - 1) % len(music_list)
        music_list[current_music_index].play()
        paused = False

    screen.fill((255, 255, 255))
    screen.blit(player_sc, play_place)
    pygame.display.flip()

pygame.quit()
