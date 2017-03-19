import os
import pygame
import time
import random
import math


lx = 0
ly = 0

def setup(screen,etc) :
    pass

def draw(screen, etc):
    for i in range(0, 100) :
        seg(screen, etc, i)    

def seg(screen, etc, i) :
    global lx, ly
    
   
    color = etc.color_picker()
    R = etc.knob2*400-200
    R = R + (etc.audio_in[i] / 100)
    x = R * math.cos((i /  100.) * 6.28) + 640
    y = R * math.sin((i /  100.) * 6.28) + 360
    
    pygame.draw.line(screen, color, [lx, ly], [x, y], int(etc.knob3*10)+1)
    ly = y
    lx = x
    pygame.draw.circle(screen,color,[int(x), int(y)], int(etc.knob1 *20), 0)

    
   

