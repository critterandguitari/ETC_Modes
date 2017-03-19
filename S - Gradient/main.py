import os
import pygame
import time
import random

def setup(screen, etc):
    pass

def draw(screen, etc):
    for i in range(0, 100) :
        seg(screen, etc, i)    

def seg(screen, etc, i) :
    
    x0 = 640
    x1 = 640 + (etc.audio_in[i] / 64)
    y = i * 11
    bw = abs((etc.audio_in[i] / 128))
    color = (bw, bw, bw)
    
    bw2 = 255 - abs((etc.audio_in[i] / 128))
    color2 = (bw2, bw2, bw2)
    
    circlesize = int(etc.knob1*55)
    circlesize2 = int(etc.knob3*55)
    circlelinewidth = int(etc.knob2*circlesize) 
    circlelinewidth2 = int(etc.knob4*circlesize2)
    
    #pygame.draw.circle(screen,color,(x1, y),circlesize, circlelinewidth)
    pygame.draw.circle(screen,color,(x1, y),circlesize, circlelinewidth)
    pygame.draw.circle(screen,color2,(x1, y),circlesize2, circlelinewidth2)

