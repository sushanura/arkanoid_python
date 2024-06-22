import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Арканоид")

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Настройки платформы
paddle_width = 100
paddle_height = 10
paddle_speed = 10
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - paddle_height - 10, paddle_width, paddle_height)

# Настройки мяча
ball_radius = 10
ball_speed = [random.choice([-4, 4]), -4]
ball = pygame.Rect(screen_width // 2, screen_height // 2, ball_radius, ball_radius)

# Настройки блоков
block_width = 60
block_height = 20
blocks = []
for row in range(5):
    for col in range(screen_width // (block_width + 10)):
        block = pygame.Rect(col * (block_width + 10) + 35, row * (block_height + 10) + 35, block_width, block_height)
        blocks.append(block)

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление платформой
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:
        paddle.right += paddle_speed

    # Движение мяча
    ball.left += ball_speed[0]
    ball.top += ball_speed[1]

    # Проверка столкновений мяча с краями экрана
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.bottom >= screen_height:
        print("Game Over")
        pygame.quit()
        sys.exit()

    # Проверка столкновений мяча с платформой
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # Проверка столкновений мяча с блоками
    for block in blocks[:]:
        if ball.colliderect(block):
            ball_speed[1] = -ball_speed[1]
            blocks.remove(block)
            break

    # Рендеринг
    screen.fill(black)
    pygame.draw.rect(screen, white, paddle)
    pygame.draw.ellipse(screen, red, ball)
    for block in blocks:
        pygame.draw.rect(screen, green, block)

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()