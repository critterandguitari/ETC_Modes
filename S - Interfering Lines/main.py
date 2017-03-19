import os
import pygame
import time
import random

def setup(screen, etc):
    pass

def draw(screen, etc):
    
    lines = int(etc.knob1*59)+1
    color = etc.color_picker() #knob4
  
    R = etc.audio_in[1]*0.01 + 360
    L = etc.audio_in[11]*0.01 + 360
    T = etc.audio_in[21]*0.01 + 360
    E = etc.audio_in[45]*0.01 + 360
    F = etc.audio_in[75]*0.01 + 360
    #x = int(etc.knob1*1280)
    #y = int(etc.knob2*720)
    #z = etc.knob3*9
    fan=100*etc.knob3/8
    point=100*etc.knob2/8
    
    for i in range (0,lines) :
        
        modi = i%2
        if modi == 1 :
            pygame.draw.aalines(screen, color, True, [[0, R-i*point], [640, L-i*fan], [1280, T-i*point], [960, E-i*fan], [340, F-i]], 1)
        if modi == 0 :
            pygame.draw.aalines(screen, color, True, [[0, R+i*point], [640, L+i*fan], [1280, T+i*point], [960, E+i*fan], [340, F+i]], 1)

    


    
        
