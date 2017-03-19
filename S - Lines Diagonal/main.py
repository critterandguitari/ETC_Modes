import os
import pygame
import time
import math


last_point = [320, 0]
last_point1 = [320, 0]

def setup(screen, etc):
    pass

def draw(screen, etc):
    
    global last_point, last_point1
    
    shadow = int(etc.knob2*60)
    linewidth= int(etc.knob1*20)+1
    linelength= 540
    xshadow = math.cos((etc.knob3)*6.28)*shadow
    yshadow = math.sin((etc.knob3)*6.28)*shadow
    shadowColor = ((etc.bg_color[0]*etc.knob2)/1.1, (etc.bg_color[1]*etc.knob2)/1.1, (etc.bg_color[2]*etc.knob2)/1.1)
    
    for i in range(0, 25) :
    
        xoffset = int(90+(linelength/24*i))-xshadow
        yoffset = int(90+(linelength/24*i))+yshadow
        auDio = etc.audio_in[i] / 35
        color = shadowColor#etc.color_picker()
        
        if i == 0 : last_point = [(90+ -auDio)-xshadow, (90+ auDio)+yshadow]
        
        pygame.draw.line(screen, color, last_point, [xoffset + -auDio, yoffset + auDio], linewidth)
        last_point = [(xoffset + -auDio),(yoffset + auDio)]

    for j in range(25, 50) :
    
        xoffset = int(360 + (linelength/24)*(j-25))-xshadow
        yoffset = int(90 + (linelength/24)*(j-25))+yshadow
        auDio = etc.audio_in[j] / 35
   
        
        if j == 25 : last_point1 = [(360+ -auDio)-xshadow, (90+ auDio)+yshadow]
   
        pygame.draw.line(screen, color, last_point1, [xoffset + -auDio, yoffset + auDio], linewidth)
        last_point1 = [(xoffset + -auDio),(yoffset + auDio)]
        
    for k in range(50, 75) :
    
        xoffset = int(650 + (linelength/24)*(k-50))-xshadow
        yoffset = int(90+ (linelength/24)*(k-50))+ yshadow
        auDio = etc.audio_in[k] / 35
   
       
        if k == 50 : last_point1 = [(650+ -auDio)-xshadow, (90+ auDio)+yshadow]
   
        pygame.draw.line(screen, color, last_point1, [xoffset + -auDio, yoffset + auDio], linewidth)
        last_point1 = [(xoffset + -auDio),(yoffset + auDio)]
    
   
    
    
    for i in range(0, 25) :
    
        xoffset = int(90+(linelength/24*i))
        yoffset = int(90+(linelength/24*i))
        auDio = etc.audio_in[i] / 35
        color = etc.color_picker()
        
        if i == 0 : last_point = [(90+ -auDio), (90+ auDio)]
        
        pygame.draw.line(screen, color, last_point, [xoffset + -auDio, yoffset + auDio], linewidth)
        last_point = [(xoffset + -auDio),(yoffset + auDio)]

    for j in range(25, 50) :
    
        xoffset = int(360 + (linelength/24)*(j-25))
        yoffset = int(90 + (linelength/24)*(j-25)) 
        auDio = etc.audio_in[j] / 35
   
        color = etc.color_picker()
        if j == 25 : last_point1 = [(360+ -auDio), (90+ auDio)]
   
        pygame.draw.line(screen, color, last_point1, [xoffset + -auDio, yoffset + auDio], linewidth)
        last_point1 = [(xoffset + -auDio),(yoffset + auDio)]
        
    for k in range(50, 75) :
    
        xoffset = int(650 + (linelength/24)*(k-50))
        yoffset = int(90+ (linelength/24)*(k-50)) 
        auDio = etc.audio_in[k] / 35
   
        color = etc.color_picker()
        if k == 50 : last_point1 = [(650+ -auDio), (90+ auDio)]
   
        pygame.draw.line(screen, color, last_point1, [xoffset + -auDio, yoffset + auDio], linewidth)
        last_point1 = [(xoffset + -auDio),(yoffset + auDio)]
    
   