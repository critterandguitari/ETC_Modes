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
    audio_lev = float(abs((etc.audio_in[i] / 128))) / 256
    color = etc.bg_color
    color_inverse = (255 - color[0], 255 - color [1], 255 - color[2])
    
    deltaR = color[0] - color_inverse[0]
    deltaG = color[1] - color_inverse[1]
    deltaB = color[2] - color_inverse[2]
    
    color = (int(color[0] + audio_lev * deltaR) & 0xFF, int(color[1] + audio_lev * deltaG) & 0xFF, int(color[2] + audio_lev * deltaB) & 0xFF)
    
    circlesize = int(etc.knob1*55)

    circlelinewidth = int(etc.knob2*circlesize) 
    
    pygame.draw.circle(screen,color,(x1, y),circlesize, 0)


