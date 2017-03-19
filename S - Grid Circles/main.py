import os
import pygame

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    
    for i in range(0, 7) :
        xoffset = int(etc.knob1*(1280/8))
        yoffset = int(etc.knob2*(720/5))
         
        for j in range(0, 10) :
            x = (j*(1280/8))-(1280/8)
            y = (i*(720/5))-(720/5)
            
            rad = abs(etc.audio_in[j-i] / 100)
            width = int(etc.knob3*80)+1+rad
            color = etc.color_picker()
            if (i%2) == 1 : 
                x = j*(1280/8)-(1280/8)+xoffset
            if (j%2) == 1 : 
                y = i*(720/5)-(720/5)+yoffset
            
            
            points = [x, y]
            pygame.draw.circle(screen, color, points, width, 1) 
            
            
    
        
   
    
    