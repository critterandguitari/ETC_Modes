import os
import pygame

def setup(screen,etc) :
    pass

def draw(screen, etc):
    for i in range(0, 100) :
        seg(screen, etc, i)    

def seg(screen, etc, i) :
    
    x0 = 0
    x1 = 0 + (etc.audio_in[i] / 35)
    y = i * 8 - 40
    
    linewidth = int(etc.knob2*10)
    position = int(etc.knob1*1280)
    ballSize = int(etc.knob3*50)
    color = etc.color_picker()
    
    pygame.draw.circle(screen,color,(x1+position, y),ballSize, 0)
    pygame.draw.line(screen, color, [x0+position, y], [x1+position, y], linewidth)

