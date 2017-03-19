import os
import pygame
import random

### 


trigger = False

x1 = 640
y1 = 360

xslope = random.randrange(0,5)
yslope = random.randrange(0,5)

x2 = 0
y2 = 0

def setup(screen, etc):
    pass

def draw(screen, etc):
    global trigger, x1, y1, x2, y2, xslope, yslope
    
    
    linewidth = int(etc.knob2*20) + 1
    color = etc.color_picker()
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
        
    if trigger == True :
        
        x1 = x2
        y1 = y2

        xslope = random.randrange(-5,5)
        yslope = random.randrange(-5,5)
    
    trigger = False 
    
    if x1 > 1000 : 
        xslope = random.randrange(-5,0)
        x1 = 1000
    if y1 > 600  : 
        yslope = random.randrange(-5,0)
        y1 = 600
    if x1 < 100 : 
        xslope = random.randrange(0,5)
        x1 = 100
    if y1 < 50 : 
        xslope = random.randrange(0,5)
        y1 = 50
    
    x2 = x1 + xslope*abs(etc.audio_in[1]* 0.008)
    y2 = y1 + yslope*abs(etc.audio_in[1]* 0.008)
    
    
    
    pygame.draw.line(screen, color, (x1, y1), (x2, y2), linewidth)
        
    
