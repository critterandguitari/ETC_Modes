import os
import pygame

x = 0
y = 0
spacex = 61
xpos = 30

def setup(screen, etc):
    pass

def draw(screen, etc):
    global  x, y, xpos, spacex
    
    aberration = int(etc.knob1 * 15)
    ypos = int(etc.knob2 * 715)
    spread = int(etc.knob3*45)
    color = int(etc.knob4*254)+1
    
    #red
    for i in range(0,21):
        
        for j in range(0,21):
            x = i*spacex+(aberration*2)+xpos 
            y = j*spread+(aberration*2)+ypos 
            
            pygame.draw.line(screen, (color,0,0), (x, y),(x, y), int(abs(etc.audio_in[j]/140)))
    
    #green
    for i in range(0,21):
        
        for j in range(0,21):
            x = i*spacex-(aberration*3)+xpos 
            y = j*spread+(aberration)+ypos 
            
            pygame.draw.line(screen, (0,color,0), (x, y),(x, y), int(abs(etc.audio_in[j+25]/140)))
    
    #blue
    for i in range(0,21):
        
        for j in range(0,21):
            x = i*spacex+(aberration)+xpos 
            y = j*spread+ypos   
            
            pygame.draw.line(screen, (0,0,color), (x, y),(x, y), int(abs(etc.audio_in[j+50]/140)))
           
   
    
    
