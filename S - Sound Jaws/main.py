import os
import pygame

num = 25
clench = 0
teeth = 1
toff = 1

def setup(screen, etc) :
    pass

def draw(screen, etc) : 
  
    color = etc.color_picker() #on knob4
    teeth = int(etc.knob2 * 10)
    teethwidth = int(1280-128*teeth)
    if teethwidth == 0 : teethwidth = 128#1280-(teeth*51)
    clench = int(etc.knob1 * 200) - teethwidth/2
    if teethwidth > 640 : clench = int(etc.knob1)-320
    shape = int(etc.knob3*3)
    
    for i in range(0, 10) :
        
        x = (i * teethwidth)+teethwidth/2
        y0 = 0
        y1 = y0 + abs(etc.audio_in[i] / 85) + clench
        pygame.draw.line(screen, color, [x, y0], [x, y1], teethwidth)
        if shape == 1 :
            pygame.gfxdraw.filled_trigon(screen, x-teethwidth/2, y1, x, y1+teethwidth/2, x+teethwidth/2, y1, color)
        if shape >= 2 :
            pygame.gfxdraw.filled_circle(screen, x, y1, teethwidth/2, color)    
 
    for i in range(10, 20) :
        x = ((i-10) * teethwidth) + teethwidth/2
        y0 = 720
        y1 = y0 - abs(etc.audio_in[i] / 85) - clench
        pygame.draw.line(screen, color, [x, y0], [x, y1], teethwidth)
        if shape == 1 :
            pygame.gfxdraw.filled_trigon(screen, x-teethwidth/2, y1, x, y1-teethwidth/2, x+teethwidth/2, y1, color)
        if shape >= 2 :
            pygame.gfxdraw.filled_circle(screen, x, y1, teethwidth/2, color)

    
    