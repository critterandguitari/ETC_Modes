import os
import pygame
import time
import random
import pygame.gfxdraw

count = 0

def setup(screen, etc):
    pass

def draw(screen, etc):
    global count
    
    if etc.audio_trig or etc.midi_note_new :
        
        x=random.randrange(0,1300)
        y=random.randrange(0,800)
        pierad=random.randrange(10,100) 
        arcstart=random.randrange(0,360)
        arcend=random.randrange(0, 360-arcstart)
        size = int(etc.knob2 * 1000)
        color = etc.color_picker()
        fillrange=int(etc.knob1*100)
        
        for i in range(fillrange):
            pygame.gfxdraw.pie(screen, x, y, size, arcstart + i*2, arcend - i*2, color)

