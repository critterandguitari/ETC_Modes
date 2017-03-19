import os
import pygame
import time
import random

note_down = False

def draw(screen, etc):
    for i in range(0, 100) :
        seg(screen, etc, i)    

def seg(screen, etc, i) :
    
    x0 = 640#random.randrange(0,1920)
    x1 = 640 + (etc.audio_in[i] / 35)#random.randrange(0,1920)
    y = i * 11#random.randrange(0,1080)
    bw = random.randrange(0,255)
    color = etc.color_picker()
    
    pygame.draw.circle(screen,color,(y, x1),5, 0)
    pygame.draw.line(screen, color, [y, x0], [x1, y], 2)

