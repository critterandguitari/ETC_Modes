import os
import pygame
import time
import random
import math


lx = 0
ly = 0

def setup(screen,etc):
    pass


def draw(screen, etc):
    for i in range(0, 100) :
        lineseg(screen, etc, i) 
    for i in range(0, 100) :
        ballseg(screen, etc, i)  

def lineseg(screen, etc, i) :
    global lx, ly
    x0 = 960
    x1 = 960 + (etc.audio_in[i] / 35)
    eccentric = etc.knob3 * 100
    
    if eccentric <= 0.24 :
        eccentric = 0.25
    
    color = etc.color_picker()
    R = 100
    R = R + (etc.audio_in[i] / 100)
    x = R * math.cos((i /  eccentric) * 6.28) + 640
    
    y = R * math.sin((i /  100.) * 6.28) + 360
    
    pygame.draw.line(screen, color, [lx, ly], [x, y], int(etc.knob2*20)+1)
    ly = y
    lx = x

def ballseg(screen, etc, i) :
    global lx, ly
    x0 = 960
    x1 = 960 + (etc.audio_in[i] / 35)

    color = etc.color_picker()
    R = etc.knob2
    R = R + (etc.audio_in[i] / 100)
    x = R * math.cos((i /  100.) * 6.28) + 640
    y = R * math.sin((i /  100.) * 6.28) + 360
    

    pygame.draw.circle(screen,color,[int(x), int(y)], int(etc.knob1 *20), 0)

