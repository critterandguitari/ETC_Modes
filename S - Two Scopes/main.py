import os
import pygame
import time
import random



note_down = False

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    
    for i in range (0,50) :
        #angle = int(etc.knob3*200)
        x0 = int(etc.knob1*1280) 
        x1 = x0 + (etc.audio_in[i] / 35)
        y = i * 14.4
        color = etc.color_picker() #on knob4
        pygame.draw.line(screen, color, [x0, y], [x1, y], int(etc.knob3*100+1))

    for i in range (51,100) :
        #angle = int(etc.knob3*200)
        x0 = int(etc.knob2*1280)
        x1 = x0 + (etc.audio_in[i] / 35)
        y = (i - 50) * 14.4
        color = etc.color_picker() #on knob4
        pygame.draw.line(screen, color, [x0, y], [x1, y], int(etc.knob3*100+1))
