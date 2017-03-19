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
            
            rad = (etc.audio_in[j+i]*0.00003052)*200
            w = abs(etc.knob3*4)-2
            color = etc.color_picker()
            if (i%2) == 1 : 
                x = j*(1280/8)-(1280/8)+xoffset
            if (j%2) == 1 : 
                y = i*(720/5)-(720/5)+yoffset
            
            points = [pList[i*10+j][t] for t in range(0,6)]
            placePoints = [((points[k][0]*w)+x,(points[k][1]*w)+y) for k in range(0,6)]
            morphPoints = [(placePoints[0][0]-rad,placePoints[0][1]-rad),
                            (placePoints[1][0]+rad,placePoints[1][1]-rad),
                            (placePoints[2][0]+rad,placePoints[2][1]),
                            (placePoints[3][0]+rad,placePoints[3][1]+rad),
                            (placePoints[4][0],placePoints[4][1]-rad),
                            (placePoints[5][0]-rad,placePoints[5][1]+rad)]
            
            pygame.draw.polygon(screen, color, morphPoints, 0) 
            
            
    
        
   
    
    