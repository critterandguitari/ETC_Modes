import os
import pygame
import time
import random

note_down = False

def draw(screen, etc):
    #screen.fill( (0, 0, 0))
    for i in range(0, 25) :
        seg(screen, etc, i)    

def seg(screen, etc, i) :

    
    #x = 640 + (etc.audio_in[i] / 35)#random.randrange(0,1920)
    x = int(etc.knob2*1280) + (etc.audio_in[i * 4] / 35)
    y = i * 10 * 4#random.randrange(0,1080)
    
    squaresize = int(etc.knob1*125)
    

    #Shadow Squares
    #color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    color = (0,0,0)
    pygame.draw.line(screen, color, [x + (25-int(etc.knob3*50)), y+(25-int(etc.knob3*50))], [x + (25-int(etc.knob3*50)), y+squaresize], squaresize)
    
    
    #color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    color = etc.color_picker() #on knob4
    pygame.draw.line(screen, color, [x, y], [x, y+squaresize], squaresize)

