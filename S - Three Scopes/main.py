import os
import pygame
import time
import random



def setup(screen, etc) :
    pass

def draw(screen, etc) :
    color = etc.color_picker() #on knob4
    
    for i in range (0,30) :
        ay0 = 240
        ay1 = 240 + (etc.audio_in[i] / 128)
        ax = i * 21.3 
    
        pygame.draw.line(screen, color, [ax, ay1], [ax, ay0], int(etc.knob3*42+1))
    
    for i in range (31,60) :
        ay0 = 480
        ay1 = 480 + (etc.audio_in[i] / 128)
        ax = (i-30) * 21.3 
    
        pygame.draw.line(screen, color, [ax, ay1], [ax, ay0], int(etc.knob3*42+1))
    
    for i in range (61,90) :
        ay0 = 360
        ay1 = 360 + (etc.audio_in[i] / 80)
        ax = (i-30) * 21.3 
    
        pygame.draw.line(screen, color, [ax, ay1], [ax, ay0], int(etc.knob3*42+1))
    
    
    
    #pygame.draw.line(screen, (0,0,0), [640, 0], [640, 720], 10)
        
    
