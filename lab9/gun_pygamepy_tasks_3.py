import pygame
from pygame.draw import *
from random import randint
import math

FPS = 30 # Кол-во кадров в секунду
SCREEN_WIDTH = 800 # Ширина экрана
SCREEN_HEIGHT = 600 # Высота экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (100, 255, 100)][randint(0, 4)]
        self.type = randint(1, 2)
        #self.id = canv.create_oval(
        #        self.x - self.r,
        #        self.y - self.r,
        #        self.x + self.r,
        #        self.y + self.r,
        #        fill=self.color
        #)
        self.live = 30

        self.gravity = 1

    def set_coords(self):
        #canv.coords(
        #        self.id,
        #        self.x - self.r,
        #        self.y - self.r,
        #        self.x + self.r,
        #        self.y + self.r
        #)
        if self.type == 1:
            circle(screen, self.color, (int(self.x), int(self.y)), self.r)
        else:
            polygon(screen, self.color, [(int(self.x), int(self.y - self.r)),
                                        (int(self.x + self.r), int(self.y + self.r)),
                                        (int(self.x - self.r), int(self.y + self.r))])

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        if self.type == 1:
            self.vy -= self.gravity
        #print(self.vx, self.vy)
        if self.x <= self.r or self.x >= (800 - self.r):
            self.vx *= -1
        if self.y <= self.r :
            self.vy *= -1
            self.y = self.r + 1
        if self.y <= self.r or (self.y >= (600 - self.r) and self.vy < 0):
            self.vy *= -1
            self.vy -= self.gravity * 2
            if self.vy <= 0 and self.y < 600 - self.r:
                self.vy = 0
                self.y = 599 - self.r
                self.vx *= 0.9

        self.set_coords()
    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if math.sqrt((obj.x - self.x) ** 2 + (obj.y - self.y) ** 2) <= obj.r + self.r:
            return True
        return False


class gun():
    def __init__(self):
        self.f2_power = 20
        self.f2_on = 0
        self.an = 1
        self.x = 20
        self.y = 450
        self.speed = 7
        #self.id = canv.create_line(20,450,50,420,width=7)

    def fire2_start(self, pos):
        self.f2_on = 1

    def fire2_end(self, pos, balls_old):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        #print("Boom!")
        new_ball = ball(self.x, self.y)
        new_ball.r += 5
        self.an = math.atan((pos[1]-new_ball.y) / (pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls_old += [new_ball]
        self.f2_on = 0
        self.f2_power = 10
        return balls_old

    def targetting(self, pos=0):
        """Прицеливание. Зависит от положения мыши."""
        if pos:
            self.an = math.atan((pos[1] - self.y) / (pos[0] - self.x))
        #if self.f2_on:
        #    canv.itemconfig(self.id, fill='orange')
        #else:
        #    canv.itemconfig(self.id, fill='black')
        #canv.coords(self.id, 20, 450,
        #            20 + max(self.f2_power, 20) * math.cos(self.an),
        #            450 + max(self.f2_power, 20) * math.sin(self.an)
        #            )
        line(screen, (255, 0, 0), [self.x, self.y], [int(self.x + max(self.f2_power, self.x) * math.cos(self.an)), int(self.y + max(self.f2_power, self.x) * math.sin(self.an))], 5)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            #canv.itemconfig(self.id, fill='orange')
        #else:
        #    canv.itemconfig(self.id, fill='black')
    def move_right(self):
        if self.x >= SCREEN_WIDTH :
            return
        self.x += self.speed

    def move_left(self):
        if self.x <= 0 :
            return
        self.x -= self.speed
    def move_up(self):
        if self.y <= 0 :
            return
        self.y -= self.speed
    def move_down(self):
        if self.y >= SCREEN_HEIGHT :
            return
        self.y += self.speed





class target():
    def __init__(self):
        self.points = 0
        self.live = 1    
        #self.id = canv.create_oval(0,0,0,0)
        #self.id_points = canv.create_text(30,30,text = self.points,font = '28')
        self.new_target()
    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = randint(300, 600)
        y = self.y = randint(300, 550)
        r = self.r = randint(20, 80)
        
        self.type = randint(1, 2)
        self.vx = randint(-5, 5)
        self.vy = randint(-5, 5)
        color = self.color = (0, 255, 255)
        if self.type == 1 :
            self.vx *= 3
            self.vy *= 3
        else:
            self.color = (151, 247, 106)

        
        #canv.coords(self.id, x-r, y-r, x+r, y+r)
        #circle(screen, color, (x, y), r)
        #canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        #canv.coords(self.id, -10, -10, -10, -10)
        #circle(screen, (100, 100, 0), (-10, -10), 0)
        self.x = self.r * -1
        self.live = 0
        self.points += points
        #canv.itemconfig(self.id_points, text=self.points)
    def draw(self):
        if self.live:
            if self.type == 1 :
                circle(screen, self.color, (self.x, self.y), self.r)
            else:
                polygon(screen, self.color, [(self.x - self.r, self.y - self.r), 
                                            (self.x + self.r, self.y - self.r),
                                            (self.x + self.r, self.y + self.r),
                                            (self.x - self.r, self.y + self.r)])
    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x <= self.r or self.x >= SCREEN_WIDTH - self.r :
            self.vx *= -1
        if self.y <= self.r or self.y >= SCREEN_HEIGHT - self.r :
            self.vy *= -1

#screen1 = canv.create_text(400, 300, text='', font='28')




def start_game():
    finished = False
    pygame.display.update()
    clock = pygame.time.Clock()
    FPS = 30
    t1 = target()
    t1.new_target()

    t2 = target()
    t2.new_target()
    balls = []
    g1 = gun()
    key_right_down = False
    key_left_down = False
    key_up_down = False
    key_down_down = False
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                g1.fire2_start(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                balls = g1.fire2_end(event.pos, balls)
            elif event.type == pygame.MOUSEMOTION:
                g1.targetting(event.pos)
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    key_up_down = True
                if event.key == pygame.K_DOWN:
                    key_down_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    key_up_down = False
                if event.key == pygame.K_DOWN:
                    key_down_down = False



        for b in balls:
            b.move()
            b.set_coords()
            if b.hittest(t1) and t1.live:
                t1.hit()
            if b.hittest(t2) and t2.live:
                t2.hit()

        if key_up_down:
            g1.move_up()
        if key_down_down:
            g1.move_down()
        t1.move()
        t2.move()
        #print("Moving")
        if not (t1.live or t2.live):
            start_game()
            finished = True
        g1.targetting()
        g1.power_up()
        t1.draw()
        t2.draw()
        pygame.display.update()
        screen.fill((0, 0, 0))


#new_game()
start_game()
pygame.quit()
