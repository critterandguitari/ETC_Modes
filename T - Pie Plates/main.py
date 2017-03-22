import os
import pygame
import time
import random
import pygame.gfxdraw

count = 0
size = 0

def setup(screen, etc):
    pass

def draw(screen, etc):
    global count, size
    
    if etc.audio_trig or etc.midi_note_new :
        
        x=random.randrange(0,1300)
        y=random.randrange(0,800)
        pierad=random.randrange(10,100) 
        arcstart=random.randrange(0,360)
        arcend=random.randrange(0, 360-arcstart)
        
        fillrange = int(etc.knob2*100)+ 1
        diameter = int(etc.knob1 * 1000)+1
        nest = int(etc.knob3 * 10)
        color = etc.color_picker()
        
        
        
        for i in range(fillrange):
            size = diameter-(nest*i)
            if size < 0 : size = 5
            pygame.gfxdraw.pie(screen, x, y, size, arcstart + i*2, arcend - i*2, color)
