import os
import pygame
import random


speedList = [random.randrange(-1,1)+.1 for i in range(0,20)]
yList = [random.randrange(-50,770) for i in range(0,20)]
widthList = [random.randrange(20,200) for i in range(0,20)]
countList = [i for i in range(0,20)]
xden = 1
yden = 1
trigger = False

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    global trigger, yList, widthList, countList, speedList, xden, yden
    
    color = etc.color_picker() #on knob4
    
    if yden != (int(etc.knob1 * 19) + 1) :
        yden = (int(etc.knob1 * 19) + 1)
        speedList = [random.randrange(-2,2)+.1 for i in range(0,20)]
        yList = [random.randrange(-50,770) for i in range(0,20)]
        widthList = [random.randrange(20,200) for i in range(0,20)]
    
    if xden != (int(etc.knob2 * 19) + 1) :
        xden = (int(etc.knob2 * 19) + 1)
        speedList = [random.randrange(-2,2)+.1 for i in range(0,20)]
        yList = [random.randrange(-50,770) for i in range(0,20)]
        widthList = [random.randrange(20,200) for i in range(0,20)]
    
    for i in range (0,yden) :
        
        y0 = yList[i]
        for j in range (0,xden) :
            
            width = widthList[i]
            y1 = y0 + (etc.audio_in[j+i] / 500)
            countList[i] = countList[i] + speedList[i]
            modSpeed = countList[i]%(1280+width*2)
            x = (j * (width/5)) + (modSpeed-width)
            pygame.draw.line(screen, color, [x, y1], [x, y0], int(etc.knob3*100+1))
    
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
    
    #if trigger == True :

   
    trigger = False
    
    
   
        
    
