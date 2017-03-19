import os
import pygame
import random

trigger = False
pos = [(random.randrange(640,642),random.randrange(360,362)) for i in range(0,12)]
def setup(screen, etc):
    pass

def draw(screen, etc):
    global trigger, pos
   
    balls = int(etc.knob2*10)+1
    
    xdensity = int(etc.knob3*640)
    ydensity = int(etc.knob3*360)
    size = int(etc.knob1*250)+1
    
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
    
    if trigger == True :
        pos = [(random.randrange(640-xdensity,642+xdensity+10),random.randrange(360-ydensity,362+ydensity+10)) for i in range(0,12)]
    
    
    for i in range (0, balls):
        color = etc.color_picker()
        #colorChange = (color[0]*(i*0.09), color[1]*(i*0.09), color[2]*(i*0.09))
        pygame.draw.circle(screen,color,pos[i],size, 0)
    
    
    
    trigger = False

