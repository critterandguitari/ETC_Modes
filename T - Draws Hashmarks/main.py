import os
import pygame
import time
import random
import math

vertLines = 20
trigger = False
xpos = 0
x = 0
y = 0
height = 0
width = 0

def setup(screen, etc):
    pass

def draw(screen, etc):
    global vertLines, trigger, xpos, x, y, height, width
    
    linewidth = int(etc.knob2*5) + 1
    color = etc.color_picker()
    lines = int(9*etc.knob1+1)+90
    #linespace = int(720/lines)
    
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
        
    if trigger == True :
        
        vertLines = random.randrange(int(etc.knob3*50)+2,int(etc.knob3*70)+8)
        x = random.randrange(-200,1000)
        y = random.randrange(-200,700)
        width = random.randrange(-100,1000)
        height = random.randrange(-100,1000)
        
        for i in range(0, vertLines) :
            
            xpos = x + (i + 1)*(width/vertLines) 
            
    for k in range(0, vertLines) :
        ###maybe you can rotate them idk
        #rotx = math.cos((int(etc.knob3*1000) /  1000) * 6.28) + 640
        #roty = math.sin((int(etc.knob3*1000) /  1000) * 6.28) + 360
        xpos = x + (k + 1)*(width/vertLines)
        
        pygame.draw.line(screen, color, (xpos, y), (xpos, height), linewidth)
            
    trigger = False   
    
    
        
    for j in range(0, lines) :
        
        linespace = 720-(lines-1)*7.2
        
        pygame.draw.line(screen, color, (0,(j*linespace)+linespace/2), (1280,(j*linespace)+linespace/2), linewidth)
        #blit.screen
    
        #speed = (speed+1*etc.knob3/5)%80
