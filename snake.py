import pygame
import random
import sys

pygame.init()

# Определение цветов
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Определение размеров экрана
WIDTH = 400
HEIGHT = 600

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

# Загрузка изображений
BACKGROUND = pygame.image.load("C:/Users/SystemX/Desktop/lab7/images/road.png")
bad_screen = pygame.image.load("C:/Users/SystemX/Desktop/lab7/images/dd.png")
bad_screen = pygame.transform.scale(bad_screen, (WIDTH, HEIGHT))

# Установка шрифта и размера текста
font = pygame.font.Font(None, 36)

# Определение класса Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/SystemX/Desktop/lab7/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH and pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

# Определение класса Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/SystemX/Desktop/lab7/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, WIDTH - 30), 0)

    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(30, WIDTH - 30), 0)

# Определение класса COIN
class COIN(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/SystemX/Desktop/lab7/images/coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, WIDTH - 30), 35)

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > HEIGHT:
            self.rect.center = (random.randint(30, WIDTH - 30), 0)

# Создание экземпляров классов
P1 = Player()
E1 = Enemy()
C1 = COIN()

# Создание групп спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# Основной игровой цикл
done = False
cnt = 0
FPS = 60
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Движение игрока
    P1.move()

    # Движение спрайтов
    for entity in all_sprites:
        entity.move()

    # Проверка столкновений
    if pygame.sprite.spritecollide(P1, coins, True):
        cnt += 1
        C1 = COIN()
        coins.add(C1)
        all_sprites.add(C1)

    if pygame.sprite.spritecollideany(P1, enemies):
        screen.blit(bad_screen, (0, 0))
        pygame.display.flip()
        pygame.time.wait(1000)
        done = True

 
    screen.blit(BACKGROUND, (0, 0))
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    
    text_surface = font.render(f'POINTS: {cnt}', True, RED)
    screen.blit(text_surface, (250, 10))

   
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
