import os
import pygame
import random

trigger = False
pList = [(random.randrange(-100,1380),random.randrange(-100,820)) for i in range(0,100)]

def setup(screen, etc):
    pass

def draw(screen, etc):
    global trigger, pList
    
    fill = int(etc.knob3*4)
    size = int(etc.knob1*200)+1
    xdensity = int(etc.knob2*740)
    ydensity = int(etc.knob2*460)
    
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
    
    if trigger == True :
        pList = [(random.randrange(-100+xdensity,1380-xdensity+10),random.randrange(-100+ydensity,820-ydensity+10)) for i in range(0,100)]
    
    for j in range(0, 100) :     
        color = etc.color_picker()
        pygame.draw.rect(screen, color, [pList[j][0]-(size/2),pList[j][1]-(size/2),size,size], fill)
        
    trigger = False  
