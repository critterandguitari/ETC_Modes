import os
import pygame
import random

trigger = False
myRect = pygame.Rect(640-25,360-25,50,50)

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    global trigger, myRect
    
    color = etc.color_picker() 
    myRect = pygame.Rect(myRect.topleft, (int(etc.knob1*200)-100, int(etc.knob2*200)-100))
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
    if trigger == True :
        
        set = random.randrange(0,7)
        
        if set == 0 :
            #up
            myRect.bottom = myRect.top             
        
        if set == 1 :
            #upright
            myRect.bottomleft = myRect.topright    
        
        if set == 2 :
            #upleft
            myRect.bottomright = myRect.topleft    
        
        if set == 3 :
            #left
            myRect.right = myRect.left             
        
        if set == 4 :
            #right
            myRect.left = myRect.right             
        
        if set == 5 :
            #downright
            myRect.topleft = myRect.bottomright    
        
        if set == 6 :
            #down
            myRect.top = myRect.bottom             
        
        if set == 7 :
            #downleft
            myRect.topright = myRect.bottomleft  
        
    trigger = False    
    
    if myRect.center[0] <= 0 : myRect.center = (640,360)
    if myRect.center[0] >= 1280 : myRect.center = (640,360)
    if myRect.center[1] <= 0 : myRect.center = (640,360)
    if myRect.center[1] >= 720 : myRect.center = (640,360)
    
    pygame.draw.rect(screen, color, myRect, int(etc.knob3 * 100))
    
    

    
    
        
   
     

    
  