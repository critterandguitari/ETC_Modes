import os
import pygame
import time
import random

def setup(screen, etc):
    pass

def draw(screen, etc):

    R = 1 
    
    peak = 0
    for i in range(0,100) :
        if etc.audio_in[i] > peak:
            peak = etc.audio_in[i]
    R = (peak / 100) + (etc.knob3 * 100)

    x = int(etc.knob1*1280)
    y = int(etc.knob2*720)
    color = etc.color_picker()
    
    pygame.draw.circle(screen,color,(x,y),(int(R)+10))



    
        
