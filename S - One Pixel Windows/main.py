import os
import pygame


trigger = False
x = 0
y = 0


def setup(screen, etc):
    pass

def draw(screen, etc):
    
    global  trigger, x, y
    
   
    spacex = 64
    spacey = 12
    
   
     
    for i in range(0,21):
        
        for j in range(0,21):
            x = i*spacex+2 
            y = j*spacey+182 
            
            pygame.draw.line(screen, (255,0,0), (x, y),(x, y), int(abs(etc.audio_in[j]/140)))
    for i in range(0,21):
        
        for j in range(0,21):
            x = i*spacex-3 
            y = j*spacey+181 
            
            pygame.draw.line(screen, (0,255,0), (x, y),(x, y), int(abs(etc.audio_in[j+25]/140)))
    for i in range(0,21):
        
        for j in range(0,21):
            x = i*spacex+1 
            y = j*spacey+180 
            
            pygame.draw.line(screen, (0,0,255), (x, y),(x, y), int(abs(etc.audio_in[j+50]/140)))
           
   
    
    
