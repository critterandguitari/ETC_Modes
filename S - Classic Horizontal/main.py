import os
import pygame

def setup(screen,etc) :
    pass

def draw(screen, etc):
    for i in range(0, 100) :
        seg(screen, etc, i)    

def seg(screen, etc, i) :
    
    y0 = 0
    y1 = (etc.audio_in[i] / 90)
    x = i * 13 - 10
    
    linewidth = int(etc.knob2*10)
    position = int(etc.knob1*720)
    ballSize = int(etc.knob3*50)
    color = etc.color_picker()
    
    pygame.draw.circle(screen,color,(x, y1+position),ballSize, 0)
    pygame.draw.line(screen, color, [x, y0+position], [x, y1+position], linewidth)

