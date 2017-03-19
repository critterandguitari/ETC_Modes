import os
import pygame
import pygame.gfxdraw

triangles = 10

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    color = etc.color_picker() #on knob4
    
    triangles = int(etc.knob1*70)+1
    space = (1280/triangles)
    offset = int(etc.knob2*space)-(space/2)
    y = int(etc.knob3*720)
    
    
    for i in range (0,triangles+1) :
        
       
        auDio = int(etc.audio_in[i] / 65)
        
        ax = i * space
    
        pygame.gfxdraw.filled_trigon(screen, ax, y, ax+int((space/2)+offset),auDio+y, ax + space, y, color)
    