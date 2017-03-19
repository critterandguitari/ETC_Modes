import os
import pygame
import time
import random

last_point = [320, 0]
last_point1 = [320, 0]
speed = 1
slide = 1

def setup(screen, etc):
    pass

def draw(screen, etc):
    
    global last_point, last_point1, speed, slide
    
    linewidth= int(10*etc.knob1)+1
    #speed = speed + 1
    #slide = speed % 12.8
    lines = 72#int(65-(etc.knob2*65))+7
    spacehoriz = 180*etc.knob2+18
    spacevert = spacehoriz
    recsize = 10*etc.knob3
    
    
    
    for m in range(0, lines) :
        x = m*spacehoriz
        y = 360
        auDio = etc.audio_in[m] / 35
        color = etc.color_picker()
        if auDio < 0 : auDio = 0
        pygame.draw.line(screen, color, [x,0], [x, y-auDio], linewidth)
        if recsize >= 1 and y-auDio < 360 :
            pygame.draw.rect(screen, color, [x-(recsize/2),y-auDio,recsize,recsize], 0)

    for i in range(0, lines) :
        x = i*spacehoriz
        y = 360
        color = etc.color_picker()
        auDio = etc.audio_in[i] / 35
        #color = etc.color_picker()
        if auDio > 0 : auDio = 0
        pygame.draw.line(screen, color, [x,720], [x, y-auDio], linewidth)
        if recsize >= 1 and y-auDio > 360:
            pygame.draw.rect(screen, color, [x-(recsize/2),y-auDio,recsize,recsize], 0)
        
    for j in range(0,lines) :
        
        pygame.draw.line(screen, color, (-1,j*spacevert), (1280,j*spacevert), linewidth)
    
    
    