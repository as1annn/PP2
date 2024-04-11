import pygame
from random import randint

pygame.init()

WIDTH = 720
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))

colorWHITE = (255, 255, 255)
colorGRAY = (70, 70, 70)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

clock = pygame.time.Clock()

CELL = 60

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def generate():
        return Point(randint(0, WIDTH // CELL - 1) * CELL, randint(0, HEIGHT // CELL - 1) * CELL)

class Snake:
    def __init__(self):
        self.body = [Point.generate()]
        self.dx = 0
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        head = self.body[0]
        head.x += self.dx * CELL
        head.y += self.dy * CELL
        if head.x >= WIDTH or head.x < 0 or head.y >= HEIGHT or head.y < 0:
            return True  # Check for wall collision
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True  # Check for self-collision
        return False

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))
            return True

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x, head.y, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x, segment.y, CELL, CELL))

class Food:
    def __init__(self):
        self.pos = Point.generate()
        self.timer = 100

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x, self.pos.y, CELL, CELL))

    def regenerate(self):
        self.pos = Point.generate()
        self.timer = 100

    def update_timer(self):
        self.timer -= 1
        if self.timer <= 0:
            self.regenerate()

def draw_grid():
    for i in range(0, HEIGHT, CELL):
        for j in range(0, WIDTH, CELL):
            pygame.draw.rect(screen, colorGRAY, (i, j, CELL, CELL), 1)

snake = Snake()
food = Food()

score = 0
level = 1
foods_eaten = 0
speed = 5

font = pygame.font.SysFont(None, 36)

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.dy == 0:
                snake.dx = 0
                snake.dy = -1
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx = -1
                snake.dy = 0

    screen.fill(colorBLACK)

    if snake.move():
        game_over = True  # End game if snake hits the wall or itself

    if not game_over:
        if snake.check_collision(food):
            food.regenerate()
            score += 10
            foods_eaten += 1
            if foods_eaten >= 3:
                speed += 1
                foods_eaten = 0
            if score >= 50 * level:
                level += 1
                speed += 1
        
        food.update_timer()
        snake.draw()
        food.draw()
        draw_grid()

        score_text = font.render("Score: " + str(score), True, colorWHITE)
        level_text = font.render("Level: " + str(level), True, colorWHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 40))

        pygame.display.flip()
        clock.tick(speed)

pygame.quit()
