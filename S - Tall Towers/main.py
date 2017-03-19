import os
import pygame
import time
import random

last_point = [0, 360]

def setup(screen, etc):
    pass

def draw(screen, etc):
    global last_point

    for i in range(0, 100) :
        seg(screen, etc, i)   

def seg(screen, etc, i):
    global last_point
    xoffset = 0
    y0 = screen.get_height() // 2
    y1 = (screen.get_height() // int((etc.knob3) * 10 + 1)) + (etc.audio_in[i] / 35) 
    x = int(etc.knob2 *128) * 10
    colorr = etc.color_picker() #colorr=(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    color = (0,0,0)

    #pygame.draw.rect(screen, colorr, [random.randrange(0,1280),random.randrange(0,720),5,5], 0)
    pygame.draw.circle(screen,colorr,(x + xoffset, y1),int(etc.knob1 * 20), 0)
    pygame.draw.line(screen, colorr, last_point, [x + xoffset, y1], (etc.audio_in[i] / 200))
    last_point = [x + xoffset, y1]

