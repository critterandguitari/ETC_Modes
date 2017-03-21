import os
import pygame
import time
import random

note_down = False

def setup(screen, etc):
    pass

def draw(screen, etc):
    for i in range(0, 100) :
        seg(screen, etc, i)    

def seg(screen, etc, i) :
    
    x0 = int(etc.knob2 * 720)#random.randrange(0,1920)
    x1 = (int(etc.knob1 * 1280) ) + (etc.audio_in[i] / 64)#random.randrange(0,1920)
    y = i * 12#random.randrange(0,1080)
    bw = random.randrange(0,255)
    color = etc.color_picker()
    
    #pygame.draw.circle(screen,color,(y + 40, x0),int(etc.knob3 * 10), 0)
    pygame.draw.circle(screen,color,(x1, y + 40),int(etc.knob3 * 10), 0)
    pygame.draw.line(screen, color, [y + 40, x0], [x1, y + 40], 2)

