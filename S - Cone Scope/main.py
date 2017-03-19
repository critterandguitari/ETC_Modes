import os
import pygame
import time
import random

def setup(screen, etc):
    pass

note_down = False

def draw(screen, etc):
    for i in range(0, 100) :
        seg(screen, etc, i)    

def seg(screen, etc, i) :
    
    #x0 = 640
    #x1 = 640 + (etc.audio_in[i] / 35)
    x0 = (int(etc.knob1*1280))
    x1 = x0 + (etc.audio_in[i] / 35)
    y = i * 7
    color = etc.color_picker()
    
    #pygame.draw.line(screen, color, [x0 + (640 - (int(etc.knob1*1280))), y + i], [x1 + (640 - (int(etc.knob2 *1280))), y+10], 10)
    pygame.draw.line(screen, color, [x0, y + i], [x1, y+i+(575-(int(etc.knob2*1150)))], 1+int(etc.knob3*20))
    

