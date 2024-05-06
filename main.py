import pygame
import sys

# Инициализация Pygame
pygame.init()

# Устанавливаем размеры окна
width, height = 1820, 920
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Игра с трактором")

# Установка начальных координат трактора и скорости
x, y = 50, 50
vel = 5
distanceTractorToBorder = 0

#масштабируем изображение трактора
new_width = 75
new_height = 75
image = pygame.image.load("pixil-trac-left.png")
image = pygame.transform.scale(image, (new_width, new_height))
tracLeft = pygame.image.load("pixil-trac-left.png")
tracRight = pygame.image.load("pixil-trac-right.png")
tracUp = pygame.image.load("trac_up.png")
tracDown = pygame.image.load("trac_down.png")
tracLeft = pygame.transform.scale(tracLeft, (new_width, new_height))
tracRight = pygame.transform.scale(tracRight, (new_width, new_height))
tracUp = pygame.transform.scale(tracUp, (new_width, new_height))
tracDown = pygame.transform.scale(tracDown, (new_width, new_height))

run = True
# Основной цикл игры
while run:

    pygame.time.delay(50)  # Задержка для плавности обновления экрана

    #заливка фона
    win.fill((255, 255, 255))

    # отрисовка дороги
    color = (0, 0, 0)
    style = 13
    pygame.draw.rect(win, color, (-10, 15, 2000, 15))
    pygame.draw.rect(win, color, (-10, 200, 2000, 15))
    pygame.draw.line(win, color, (-10, 107), (100, 107), style)
    pygame.draw.line(win, color, (210, 107), (320, 107), style)
    pygame.draw.line(win, color, (430, 107), (540, 107), style)
    pygame.draw.line(win, color, (650, 107), (770, 107), style)
    pygame.draw.line(win, color, (890, 107), (1000, 107), style)
    pygame.draw.line(win, color, (1110, 107), (1230, 107), style)
    pygame.draw.line(win, color, (1340, 107), (1450, 107), style)
    pygame.draw.line(win, color, (1560, 107), (1670, 107), style)
    pygame.draw.line(win, color, (1780, 107), (1890, 107), style)
    pygame.draw.line(win, color, (2000, 107), (2110, 107), style)

    # Отрисовка окна и трактора
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Управление трактором
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - vel > 25:
        image = tracLeft
        x -= vel
    elif keys[pygame.K_LEFT]:
        image = tracLeft
        distanceTractorToBorder = x - 25
        x = x - distanceTractorToBorder
    if keys[pygame.K_RIGHT] and x + vel < width - 25:
        image = tracRight
        x += vel
    elif keys[pygame.K_RIGHT] and x < width:
        image = tracRight
        distanceTractorToBorder = width - 25 - 1 - x
        x = x + distanceTractorToBorder
    if keys[pygame.K_UP] and y - vel > 25:
        y -= vel
        image = tracUp
    elif keys[pygame.K_UP]:
        image = tracUp
        distanceTractorToBorder = y - 25
        y = y - distanceTractorToBorder
    if keys[pygame.K_DOWN] and y + vel < height - 25:
        image = tracDown
        y += vel
    elif keys[pygame.K_DOWN]:
        image = tracDown
        distanceTractorToBorder = height - 25 - 1 - y
        y = y + distanceTractorToBorder

    win.blit(image, (x, y))



    pygame.display.update()

pygame.quit()
sys.exit()