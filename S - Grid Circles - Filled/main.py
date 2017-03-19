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
            
            rad = abs(etc.audio_in[j+i] / 200)
            restRad = int(etc.knob3*20)+1
            color = etc.color_picker()
            if (i%2) == 1 : 
                x = j*(1280/8)-(1280/8)+xoffset
            if (j%2) == 1 : 
                y = i*(720/5)-(720/5)+yoffset
            #else : x = j*(1280/8)
            #if (j%2) == 0 : y = y + yoffset
            
            
            pygame.draw.circle(screen, color, [x, y], rad+restRad) 