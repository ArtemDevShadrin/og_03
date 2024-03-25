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
#################################################################

running = True
while running:
    pass

pygame.quit()
