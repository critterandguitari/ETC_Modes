import os
import pygame
import time
import random
import math

count = 0

def setup(screen, etc):
    pass

def draw(screen, etc):
    global count
    speed = etc.knob1*20
    count = int(count + speed)
    thick = int(etc.knob3*100)+1
    color = etc.color_picker()
    
    peak = 0
    for i in range(0,100) :
        if etc.audio_in[i] > peak:
            peak = etc.audio_in[i]
        
    R = 4 * etc.knob2 * peak / 128
    x = R * math.cos((count /  1000.) * 6.28) + 640
    y = R * math.sin((count /  1000.) * 6.28) + 360
    pygame.draw.line(screen, color, [640, 360], [x, y], thick)
   
   
    

