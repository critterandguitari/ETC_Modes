import os
import pygame
import random
import pygame.gfxdraw

pointNumber = 20
pOints = [(random.randrange(0,1200), random.randrange(0,600)) for i in range(1, pointNumber)]
trigger = False
pOints.append(pOints[0])
pOints1 = [(640,640), (45,760), (90,90)]



def setup(screen, etc):
    pass

def draw(screen, etc):
    
    global pOints, trigger, pointNumber, pOints1
    
    number = int(etc.knob2*5)
    smooth = 6
    place = int(etc.knob3*150) +10
    
    pOints1 = [(pOints[i][0] - place, pOints[i][1] - place) for i in range(1,pointNumber)]
    pOints1.append(pOints1[0])
    
    pOints2 = [(pOints1[i][0] + place+(place/4), pOints1[i][1] + place+(place/4)) for i in range(1,pointNumber)]
    pOints2.append(pOints2[0])
    
    pOints3 = [(pOints2[i][0] + place+(place/2), pOints2[i][1] - place+(place/2)) for i in range(1,pointNumber)]
    pOints3.append(pOints3[0])
    
    pOints4 = [(pOints3[i][0] - place+(place/1), pOints3[i][1] + place+(place/1)) for i in range(1,pointNumber)]
    pOints4.append(pOints4[0])
    
    
    color = etc.color_picker()
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
        
    if trigger == True :
        pointNumber = int(etc.knob1*20)+4
        pOints = [(random.randrange(20,1240), random.randrange(20,680)) for i in range(1,pointNumber)]
        pOints.append(pOints[0])
        pOints1 = [(pOints[i][0] + place, pOints[i][1] + place) for i in range(1,pointNumber)]
        pOints1.append(pOints1[0])
        
    trigger = False
    
    pygame.gfxdraw.bezier(screen, pOints, smooth, color)
    if number>1 : 
        pygame.gfxdraw.bezier(screen, pOints1, smooth, color)
    if number>2 : 
        pygame.gfxdraw.bezier(screen, pOints2, smooth, color)
    if number>3 :
        pygame.gfxdraw.bezier(screen, pOints3, smooth, color)
    if number>4 :
        pygame.gfxdraw.bezier(screen, pOints4, smooth, color)
    
    
   
    
    
    
