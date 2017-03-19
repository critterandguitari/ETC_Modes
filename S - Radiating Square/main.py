import os
import pygame
import time
import random

#MAKE KNOB1 CONTROL ALPHA


note_down = False

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    
    for i in range(0, 100) :
        seg(screen, etc, i)    

def seg(screen, etc, i) : 
    global counter
    
    if i <= 25:  
        angle = int(etc.knob3*200)
        x0 = 490  
        x1 = x0 - abs(etc.audio_in[i] / 35)
        y = 210 + i * 12
        color = etc.color_picker() #on knob4
        pygame.draw.line(screen, color, [x0, y], [x1, y - angle], int(etc.knob2*250))
    

    if i >= 25 and i <= 50:
        angle = int(etc.knob3*200)
        x = 190 + i * 12 
        y0 = 510
        y1 = y0 + abs(etc.audio_in[i] / 35)
        color = etc.color_picker() #on knob4
        pygame.draw.line(screen, color, [x, y0], [x + angle, y1], int(etc.knob2*250))        
                
    
    if i >= 50 and i <= 75:
        angle = int(etc.knob3*200)
        x0 = 790
        x1 = x0 + abs(etc.audio_in[i] / 35)
        y = 1110 - i * 12
        color = etc.color_picker() #on knob4
        pygame.draw.line(screen, color, [x0, y], [x1, y + angle], int(etc.knob2*250))
                        
    
    if i >= 75 and i <= 99:
        angle = int(etc.knob3*200)
        x = 1690 - i * 12 
        y0 = 210
        y1 = y0 - abs(etc.audio_in[i] / 35)
        color = etc.color_picker() #on knob4
        pygame.draw.line(screen, color, [x, y0], [x - angle, y1], int(etc.knob2*250))
        
    if i == 1:
        angle = int(etc.knob3*200)
        x = 490 
        y0 = 210
        y1 = y0 - abs(etc.audio_in[i] / 35)
        color = etc.color_picker() #on knob4
        pygame.draw.line(screen, color, [x, y0], [x - angle, y1], int(etc.knob2*250))

    
    