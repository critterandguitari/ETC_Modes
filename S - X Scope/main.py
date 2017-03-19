import os
import pygame
import math
import pygame.gfxdraw


last_point = [320, 0]
last_point1 = [320, 0]

def setup(screen, etc):
    pass

def draw(screen, etc):
    
    global last_point, last_point1
    
    linewidth= int(etc.knob1*20)+1
    linelength= 640
    
    
    shadow = int(etc.knob2*120)
    xshadow = math.cos((etc.knob3)*6.28)*shadow
    yshadow = math.sin((etc.knob3)*6.28)*shadow
    shadowColor = ((etc.bg_color[0]*etc.knob2)/1.1, (etc.bg_color[1]*etc.knob2)/1.1, (etc.bg_color[2]*etc.knob2)/1.1)

    for i in range(0, 50) : #shadow
    
        xoffset = int(320+(linelength/49*i))+xshadow
        yoffset = int(40+(linelength/49*i))+yshadow
        auDio = etc.audio_in[i] / 35
        color = shadowColor#etc.color_picker()
        
        if i == 0 : last_point = [(320+ -auDio)+xshadow, (40+ auDio)+yshadow]
        
        pygame.draw.line(screen, shadowColor, last_point, [xoffset + -auDio, yoffset + auDio], linewidth)
        last_point = [(xoffset + -auDio),(yoffset + auDio)]
        
        
    for j in range(50, 100) : #shadow
    
        xoffset = int(320 + (linelength/49)*(j-50))+xshadow
        yoffset = int(680 - (linelength/49)*(j-50))+yshadow
        auDio = etc.audio_in[j] / 35
        
        color = etc.color_picker()
        if j == 50 : last_point1 = [(320+ -auDio)+xshadow, (680 + -auDio)+yshadow]
   
        pygame.draw.line(screen, shadowColor, last_point1, [xoffset + -auDio, yoffset + -auDio], linewidth)
        last_point1 = [(xoffset + -auDio),(yoffset + -auDio)]
    
    
    
    for i in range(0, 50) :
    
        xoffset = int(320+(linelength/49*i))
        yoffset = int(40+(linelength/49*i))
        auDio = etc.audio_in[i] / 35
        color = etc.color_picker()
        
        if i == 0 : last_point = [(320+ -auDio), (40+ auDio)]
        
        pygame.draw.line(screen, color, last_point, [xoffset + -auDio, yoffset + auDio], linewidth)
        last_point = [(xoffset + -auDio),(yoffset + auDio)]
        
        
    for j in range(50, 100) :
    
        xoffset = int(320 + (linelength/49)*(j-50))
        yoffset = int(680 - (linelength/49)*(j-50)) 
        auDio = etc.audio_in[j] / 35
   
        color = etc.color_picker()
        if j == 50 : last_point1 = [(320+ -auDio), (680 + -auDio)]
   
        pygame.draw.line(screen, color, last_point1, [xoffset + -auDio, yoffset + -auDio], linewidth)
        last_point1 = [(xoffset + -auDio),(yoffset + -auDio)]
        
    