import os
import pygame


def setup(screen, etc) :
    pass

def draw(screen, etc) :
    for i in range(0, 100) :
        seg(screen, etc, i)    

def seg(screen, etc, i) :
    
    x0 = 0
    x1 = (etc.audio_in[i] / 90)
    y = int(i * 19 * etc.knob1 * 5)
  
    color = etc.color_picker()
   
   
    offx = int(etc.knob2 * 720)
    offy = int(etc.knob3 * 1280) 
    
    pygame.draw.circle(screen,color,(y+offy, x1+offx),5, 0)
    pygame.draw.line(screen, color, [y+offy, x0+offx], [y+offy, x1+offx], 2)

