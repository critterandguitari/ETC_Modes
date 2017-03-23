import os
import pygame
import time
import random

last_point = [0, 360]
first_point = []


def setup(screen, etc):
    pass

def draw(screen, etc):
    global last_point, first_point
    
    for i in range(0, 100) :
        lineseg(screen, etc, i)
    for i in range(0, 100) :
        ballseg(screen, etc, i)
    for i in range(0, int(etc.knob3 * 100)):
        pygame.draw.rect(screen, etc.color_picker(), [random.randrange(0,1280),random.randrange(0,720),5,5], 0)
    

def lineseg(screen, etc, i):
    global last_point, first_point
    
    linewidth = int(etc.knob1*75)+1
    y1 = (screen.get_height() // 2) + (etc.audio_in[i] / 50)
    x = i * 10
    xoffset = (1280 - (99*10)) // 2
    color = etc.color_picker()

    if i == 0 : 
        first_point = last_point
    else :
        last_point = last_point
    
    pygame.draw.line(screen, color, last_point, [x + xoffset, y1], linewidth)
    last_point = [x + xoffset, y1]

def ballseg(screen, etc, i):
    
    ballwidth = int(etc.knob2*75)+1
    y1 = (screen.get_height() // 2) + (etc.audio_in[i] / 50)
    x = i * 10
    xoffset = (1280 - (99*10)) // 2
    color = etc.color_picker()
    
    pygame.draw.circle(screen,color,(x + xoffset, y1),ballwidth, 0)
    
    
