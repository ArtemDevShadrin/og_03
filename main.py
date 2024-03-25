import random

import pygame

pygame.init()

#################################################################
# создаем экран
SCREEN_WIDTH = 800  # капс текст не изменяемая переменная
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# создаем заголовок
pygame.display.set_caption("Игра ТИР")

# создаем иконку
icon = pygame.image.load("icon/0c5be33281ae73c78d79fcc44d6ecfb5.jpg")
# устанавливаем иконку
pygame.display.set_icon(icon)
#################################################################

#################################################################
# создаем цели
target_img = pygame.image.load("icon/klipartz.com.png")

# задаем размер цели
target_width = 50
target_height = 50

# задаем случайные координаты цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# задаем случайный цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#################################################################

#################################################################
running = True
while running:
    # зальем экран цветом нашим случайным цветом
    screen.fill(color)
    # получаем все события в игре
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # задаем случайные координаты цели
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    # отрисовываем нашу мишень
    screen.blit(target_img, (target_x, target_y))
    # обновление экрана
    pygame.display.update()
#################################################################
pygame.quit()
