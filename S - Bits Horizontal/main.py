import os
import pygame
import random
import math

trigger = False
xpos = []
x = 0
y = 0
height = 720 
width = 1300
linelength = 50
lineAmt = 20
xpos = [random.randrange(-200, 1280) for i in range(0, lineAmt+2)]

def setup(screen, etc):
    pass

def draw(screen, etc):
    global trigger, x, y, height, width, xpos, lineAmt, linelength
    
    linewidth = height / lineAmt
    linelength = int(etc.knob2*300 + 1)
    color = etc.color_picker()
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
        
    if trigger == True :
        
        lineAmt = int(etc.knob1*60 + 1)
        xpos = [random.randrange(-200, 1280) for i in range(0, lineAmt+2)]
    
    trigger = False           
            
    for i in range(0, lineAmt+2) :
        
        auDio = int(etc.audio_in[i] / 180)
       
        x = xpos[i] + linelength
        y = (i * linewidth) + int(linewidth/2)- 1
        pygame.draw.line(screen, color, (xpos[i]+(auDio / 4), y), (x+auDio, y), linewidth)
    
            
       
    
    
        
    
