import pygame
from time import sleep
import random

# Ініціалізація Pygame
pygame.init()

# Розміри вікна
WIDTH = 800
HEIGHT = 600

# Створення вікна
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Ball Game")

# Кольори
white = (255, 255, 255)
black = (0, 0, 0)

# Швидкість м'яча
vx = 5
vy = -5

# Початкова позиція м'яча
x = WIDTH // 2
y = HEIGHT // 2
radius = 10

# Платформа
p_height = 10
p_width = 80
xp = (WIDTH - p_width) // 2
yp = HEIGHT - p_height - 10  # трохи вище краю
vp = 10  # швидкість руху платформи

# Очки
score = 0

# Функція виведення результату
def drawScore():
    win.fill(black)
    pygame.font.init()
    path = pygame.font.match_font("arial")
    Font = pygame.font.Font(path, 40)
    text = f"Your score: {score}"
    rendered = Font.render(text, True, white)
    win.blit(rendered, (WIDTH // 2 - rendered.get_width() // 2, HEIGHT // 3))
    pygame.display.update()

# Функція малювання
def drawWindow():
    win.fill(black)
    pygame.draw.circle(win, white, (x, y), radius)
    pygame.draw.rect(win, white, (xp, yp, p_width, p_height))
    pygame.display.update()

# Основний цикл
run = True
clock = pygame.time.Clock()

while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Рух платформи
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and xp > 0:
        xp -= vp
    if keys[pygame.K_RIGHT] and xp < WIDTH - p_width:
        xp += vp

    # Рух м'яча
    x += vx
    y += vy

    # Відбиття від боків
    if x - radius <= 0 or x + radius >= WIDTH:
        vx = -vx
    if y - radius <= 0:
        vy = -vy

    # Перевірка зіткнення з платформою або програш
    if y + radius >= yp:
        if xp <= x <= xp + p_width:
            vy = -vy
            score += 10  # Додаємо очки
        else:
            drawScore()
            sleep(10)
            run = False

    drawWindow()

pygame.quit()
