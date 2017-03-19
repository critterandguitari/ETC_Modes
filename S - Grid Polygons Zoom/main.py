import os
import pygame
import random
pList = [[(random.randrange(-20,20),random.randrange(-20,20)) for i in range(0,6)] for i in range(0,70)]
trigger = False

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    global trigger, pList
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
    if trigger == True :
        pList = [[(random.randrange(-20,20),random.randrange(-20,20)) for i in range(0,6)] for i in range(0,70)]
    trigger = False
    
    for i in range(0, 7) :
        xoffset = int(etc.knob1*(1280/8))
        yoffset = int(etc.knob2*(720/5))
         
        for j in range(0, 10) :
            x = (j*(1280/8))-(1280/8)
            y = (i*(720/5))-(720/5)
            
            rad = abs(etc.audio_in[j+i]*0.00003052)*20
            w = (etc.knob3*2)
           
            color = etc.color_picker()
            if (i%2) == 1 : 
                x = j*(1280/8)-(1280/8)+xoffset
            if (j%2) == 1 : 
                y = i*(720/5)-(720/5)+yoffset
            
            points = [pList[i*10+j][0], pList[i*10+j][1], pList[i*10+j][2], pList[i*10+j][3], pList[i*10+j][4], pList[i*10+j][5]]
            placePoints = [((points[k][0]*w)+x,(points[k][1]*w)+y) for k in range(0,6)]
            finalPoints = [(placePoints[j][0]+(points[j][0]*rad),placePoints[j][1]+(points[j][1]*rad)) for j in range(0,6)]
            
            pygame.draw.polygon(screen, color, finalPoints, 0) 
            
            
    
        
   
    
    