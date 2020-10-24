import pygame
from pygame.draw import *
from random import randint
import math
import pygame.freetype
pygame.init()

FPS = 30 # Кол-во кадров в секунду
SCREEN_WIDTH = 1200 # Ширина экрана
SCREEN_HEIGHT = 900 # Высота экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

''' Значения цветов '''
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

MAX_BALLS = 5 # Максимальное кол-во шариков на экране

def display_score(score):
    FONT = pygame.freetype.Font("Calibri.ttf", 50)
    FONT.render_to(screen, (50, 50), "Score: " + str(score), (70, 70, 0))
def draw_ball(x, y, r, color):
    '''рисует шарик '''
    circle(screen, color, (x, y), r)

def check_ball_click(ball_x, ball_y, ball_r, mouse_pos):
    '''Функция принимает координаты и радиус шарика, координаты мыши. Если мышь нажала на шарик,
    то возращает True, в противном случае False'''

    #print("Checking ball click", ball_x, ball_y, ball_r, mouse_pos)
    distance = math.sqrt(abs(ball_x - mouse_pos[0]) ** 2 + abs(ball_y - mouse_pos[1]) ** 2)
    if distance <= ball_r:
        return True
    return False

def check_balls_click(balls, mouse_pos):
    ''' Функция возвращает номера всех нажатых шариков '''
    ans = []
    for i in range(len(balls) - 1, -1, -1):
        if check_ball_click(balls[i][3], balls[i][4], balls[i][5], mouse_pos):
            ans.append(i)
    #print(ans)
    return ans


pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = 0 # Счет игрока
balls = [] # Этот массив содержит данные всех шариков

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in check_balls_click(balls, event.pos):
                #print(i, len(balls))
                balls.pop(i)
                score += 1
                #print(score)
    for i in range(len(balls), MAX_BALLS): # Заполнить масив шариков
        ball_frames = 1
        ball_speed_x = randint(-8, 8)
        ball_speed_y = randint(-8, 8)
        ball_r = randint(40, 100)
        ball_x = randint(ball_r + 50, SCREEN_WIDTH - ball_r - 50)
        ball_y = randint(ball_r + 50, SCREEN_HEIGHT - ball_r - 50)
        color = COLORS[randint(0, 5)]
        balls.append([ball_frames, ball_speed_x, ball_speed_y, ball_x, ball_y, ball_r, color])
        #print("Ball added", len(balls))
    for i in range(len(balls)):
        #print("Ball scanned")
        ball = balls[i]
        ball_frames = ball[0]
        ball_speed_x = ball[1]
        ball_speed_y = ball[2]
        ball_x = ball[3]
        ball_y = ball[4]
        ball_r = ball[5]
        color = ball[6]

        ball_frames += 1

        # Если шарик врезается в стену, его скорость нужно перевернуть
        if ball_x <= ball_r or ball_x >= SCREEN_WIDTH - ball_r:
            ball_speed_x *= -1
        elif ball_y <= ball_r or ball_y >= SCREEN_HEIGHT - ball_r:
            ball_speed_y *= -1

        # Перемещение шарика
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Отрисовка шарика
        draw_ball(ball_x, ball_y, ball_r, color)

        balls[i] = [ball_frames, ball_speed_x, ball_speed_y, ball_x, ball_y, ball_r, color]

    display_score(score)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()