import os
import pygame
import time
import random

last_point = [320, 0]
last_point1 = [320, 0]


def setup(screen, etc):
    pass

def draw(screen, etc):
    
    global last_point, last_point1, speed
    
    linewidth = int(etc.knob1*10)+1
    #lines = int(etc.knob2*89)+10
    #lines2
    lines = 72#int(65-(etc.knob2*65))+7
    spacehoriz = 180*etc.knob2+18
    spacevert = spacehoriz
    recsize = 10*etc.knob3
    #if recsize <1 : recsize = 0
    
    
    
    
    for m in range(0, lines) :
        
        #space = int(1280/lines)
        x = m*spacehoriz
        y = 0
        auDio = etc.audio_in[m] / 35
        color = etc.color_picker()
        if auDio < 0 : auDio = 0
        pygame.draw.line(screen, color, [x,y], [x, y + auDio], linewidth)
        if recsize >= 1 :
            pygame.draw.rect(screen, color, [x-(recsize/2),y+auDio,recsize,recsize], 0)
    
    for i in range(0, lines) :
        
        #space = int(1280/lines)
        x = i*spacehoriz
        y = 720
        auDio = etc.audio_in[i] / 35
        color = etc.color_picker()
        if auDio > 0 : auDio = 0
        pygame.draw.line(screen, color, [x,y], [x, y - -auDio], linewidth)
        if recsize >= 1 :
            pygame.draw.rect(screen, color, [x-(recsize/2),y+auDio,recsize,recsize], 0)    
    
    for j in range(0, lines) :
        
        space = j*spacehoriz
        
        pygame.draw.line(screen, color, (0,space), (1280,space), linewidth)
        
        
        
        
        