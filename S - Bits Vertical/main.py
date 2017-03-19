import os
import pygame
import random
import math

trigger = False
ypos = []
x = 0
y = 0
height = 800 
width = 1280
linelength = 50
lineAmt = 20
ypos = [random.randrange(-100, height) for i in range(0, lineAmt + 2)]

def setup(screen, etc):
     pass

def draw(screen, etc):
    global trigger, x, y, height, width, ypos, lineAmt, linelength
    
    linewidth = width / lineAmt
    linelength = int(etc.knob2*600 + 1)
    color = etc.color_picker()
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
        
    if trigger == True :
        lineAmt = int(etc.knob1*69 + 1)
        ypos = [random.randrange(-100, height) for i in range(0, lineAmt + 2)]
    
    trigger = False           
            
    for j in range(0, lineAmt + 2) :
        
        auDio = int(etc.audio_in[j] / 180)
        y = ypos[j] + linelength
        x = (j * linewidth) + (linewidth/2)- 1
        pygame.draw.line(screen, color, (x, ypos[j]+(auDio / 4)), (x, y+auDio), linewidth)
    
    #pygame.draw.line(screen, (255,0,0), (320, 40), (960, 40), 1)
