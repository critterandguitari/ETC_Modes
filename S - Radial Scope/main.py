import os
import pygame
import time
import random
import math

def setup(screen, etc):
    pass

def draw(screen, etc):
    for i in range(0, 100) :
        seg(screen, etc, i)    

def seg(screen, etc, i) :
    
    color = etc.color_picker()
    R = int(etc.knob2*1000)
    R = R + (etc.audio_in[i] / 100)
    x = R * math.cos((i /  100.) * 6.28) + 640
    y = R * math.sin((i /  100.) * 6.28) + 360
    
    pygame.draw.line(screen, color, [640, 360], [x, y], int(etc.knob1*20)+1)
    pygame.draw.circle(screen,color,(int(x),int(y)),int(etc.knob3*20), 0)

