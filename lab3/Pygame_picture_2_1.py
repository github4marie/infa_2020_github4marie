def draw_human(x, y):
#	polygon(screen, (0, 0, 0), ([(x + 140, y - 250), (x + 140, y - 500),
#		(x - 140, y - 500), (x - 140, y -250)]) )
	hair(x, y)
	circle(screen, (255, 136, 0), (x, y + 240), 140)
	circle(screen, (255, 213, 176), (x, y + 5), 130)
	eye(x - 42, y - 25)
	eye(x + 42, y - 25)
	nose(x, y + 20)
	mouth(x, y + 65)
	larm(x - 130, y + 110)
	rarm(x + 130, y + 110)
	hand(x - 165, y - 180)
	hand(x + 165, y - 180)
	pentagon(x - 120, y + 110)
	pentagon(x + 96, y + 110)
	polygon(screen, (0, 255, 0), ([(x - 200, y - 180), (x + 200, y - 180),
		(x + 200, y - 230), (x - 200, y - 230)]) )
	FONT = pygame.freetype.Font("Calibri.ttf", 40)
	FONT.render_to(screen, (x - 165, y - 220), "PYTHON is AMAZING", (0, 51, 0))

def eye(x, y):
	circle(screen, (112, 203, 255), (x, y), 28)
	circle(screen, (0, 0, 0), (x, y), 28, 1)
	circle(screen, (0, 0, 0), (x, y), 7)

def nose(x, y):
	polygon(screen, (117, 79, 55), [(x - 15, y - 13),
	 (x + 15, y - 13), (x, y + 13)])
	polygon(screen, (0, 0, 0), [(x - 15, y - 13),
	 (x + 15, y - 13), (x, y + 13)], 1)

def mouth(x, y):
	polygon(screen, (255, 0, 0),
	[(x - 75, y - 25),
	 (x + 75, y - 25), (x, y + 25)])
	polygon(screen, (0, 0, 0),
	[(x - 75, y - 25),
	 (x + 75, y - 25), (x, y + 25)], 1)

def pentagon(x, y):
	polygon(screen, (255, 136, 0),
	[(x + 45, y),
	 (x + 30, y + 45), (x - 10, y + 45),
	 (x - 20, y), (x + 10, y - 25)])
	polygon(screen, (0, 0, 0),
	[(x + 45, y),
	 (x + 30, y + 45), (x - 10, y + 45),
	 (x - 20, y), (x + 10, y - 25)], 1)
def larm(x, y):
	polygon(screen, (222, 194, 164), 
	[(x + 10, y - 10), (x, y),
	 (x - 40, y - 300), (x - 25, y - 300)])
def rarm(x, y):
	polygon(screen, (222, 194, 164), 
	[(x - 10, y - 10), (x, y),
	 (x + 40, y - 300), (x + 25, y - 300)])
def hand(x, y):
	circle(screen, (255, 255, 255), (x, y), 21)
	circle(screen, (222, 194, 164), (x, y), 20)

def hair(x, y):
	for i in range(10):
		polygon(screen, (183, 0, 255), 
		[(x - 50, y), (x + 50, y), (x - i * 14, y - 140 + i * i * 0.5)])
		polygon(screen, (183, 0, 255), 
		[(x - 50, y), (x + 50, y), (x + i * 14, y - 140 + i * i * 0.5)])

import pygame
from pygame.draw import *
import pygame.freetype

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 500))

"""
rect(screen, (255, 0, 255), (100, 100, 200, 200))
rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
polygon(screen, (255, 255, 0), [(100,100), (200,50),
                               (300,100), (200, 100)])
polygon(screen, (0, 0, 255), [(100,100), (200,50),
                               (300,100)], 5)
circle(screen, (0, 255, 0), (200, 175), 50)
circle(screen, (255, 255, 255), (200, 175), 50, 5)
"""
draw_human(250, 250)
#draw_human(750, 250)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
