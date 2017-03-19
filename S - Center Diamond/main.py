import os
import pygame
import time
import random
import math


last_point = [320, 0]
last_point1 = [320, 0]

def setup(screen, etc):
    pass

def draw(screen, etc):
    
    global last_point, last_point1
    
    linewidth= int(etc.knob1*140)+1
    shadow = int(etc.knob2*120)
    xshadow = math.cos((etc.knob3)*6.28)*shadow
    yshadow = math.sin((etc.knob3)*6.28)*shadow
    shadowColor = ((etc.bg_color[0]*etc.knob2)/1.25, (etc.bg_color[1]*etc.knob2)/1.25, (etc.bg_color[2]*etc.knob2)/1.25)
   
        
    for i in range(0, 25) : #shadow
    
        xoffset = int(640+(615/24*i))+xshadow
        yoffset = int(180+(615/24*i))+yshadow
        auDio = etc.audio_in[i] / 35
        color = shadowColor#(0,0,0)#etc.color_picker()
        
        if i == 0 : last_point = [(640+ -auDio)+xshadow, (180+auDio)+yshadow]
        
        pygame.draw.line(screen, color, last_point, [xoffset + -auDio, yoffset + auDio], linewidth)
        last_point = [(xoffset + -auDio),(yoffset + auDio)]
    
    for j in range(25, 50) : #shadow
    
        xoffset = int(820 - (615/24)*(j-25))+xshadow
        yoffset = int(360 + (615/24)*(j-25))+yshadow
        auDio = etc.audio_in[j] / 35
   
        color = shadowColor#(0,0,0)#etc.color_picker()
        if j == 25 : last_point1 = [(820+ -auDio)+xshadow, (360+ -auDio)+yshadow]
   
        pygame.draw.line(screen, color, last_point1, [xoffset + -auDio, yoffset + -auDio], linewidth)
        last_point1 = [(xoffset + -auDio),(yoffset + -auDio)]

    
    for k in range(75, 100) : #shadow
    
        xoffset = int(460 + (615/24)*(k-75))+xshadow
        yoffset = int(360 - (615/24)*(k-75))+yshadow 
        auDio = etc.audio_in[k] / 35
   
        color = shadowColor#(0,0,0)#etc.color_picker()
        if k == 75 : last_point1 = [(460+ -auDio)+xshadow, (360+ -auDio)+yshadow]
   
        pygame.draw.line(screen, color, last_point1, [xoffset + -auDio, yoffset + -auDio], linewidth)
        last_point1 = [(xoffset + -auDio),(yoffset + -auDio)]
        
    
    for l in range(50, 75) : #shadow
    
        xoffset = int(640 - (615/24)*(l-50))+xshadow
        yoffset = int(540 - (615/24)*(l-50))+yshadow 
        auDio = etc.audio_in[l] / 35
   
        color = shadowColor#(0,0,0)#etc.color_picker()
        if l == 50 : last_point1 = [(640+ -auDio)+xshadow, (540+ auDio)+yshadow]
   
        pygame.draw.line(screen, color, last_point1, [xoffset + -auDio, yoffset + auDio], linewidth)
        last_point1 = [(xoffset + -auDio),(yoffset + auDio)]    
    
    
    for i in range(0, 25) :
    
        xoffset = int(640+(615/24*i))
        yoffset = int(180+(615/24*i))
        auDio = etc.audio_in[i] / 35
        color = etc.color_picker()
        
        if i == 0 : last_point = [(640+ -auDio), (180+auDio)]
        
        pygame.draw.line(screen, color, last_point, [xoffset + -auDio, yoffset + auDio], linewidth)
        last_point = [(xoffset + -auDio),(yoffset + auDio)]
    
    
    for j in range(25, 50) :
    
        xoffset = int(820 - (615/24)*(j-25))
        yoffset = int(360 + (615/24)*(j-25)) 
        auDio = etc.audio_in[j] / 35
   
        color = etc.color_picker()
        if j == 25 : last_point1 = [(820+ -auDio), (360+ -auDio)]
   
        pygame.draw.line(screen, color, last_point1, [xoffset + -auDio, yoffset + -auDio], linewidth)
        last_point1 = [(xoffset + -auDio),(yoffset + -auDio)]
    
    
    for l in range(50, 75) :
    
        xoffset = int(640 - (615/24)*(l-50))
        yoffset = int(540 - (615/24)*(l-50)) 
        auDio = etc.audio_in[l] / 35
   
        color = etc.color_picker()
        if l == 50 : last_point1 = [(640+ -auDio), (540+ auDio)]
   
        pygame.draw.line(screen, color, last_point1, [xoffset + -auDio, yoffset + auDio], linewidth)
        last_point1 = [(xoffset + -auDio),(yoffset + auDio)]
    
    
    
    for k in range(75, 100) :
    
        xoffset = int(460 + (615/24)*(k-75))
        yoffset = int(360 - (615/24)*(k-75)) 
        auDio = etc.audio_in[k] / 35
   
        color = etc.color_picker()
        if k == 75 : last_point1 = [(460+ -auDio), (360+ -auDio)]
   
        pygame.draw.line(screen, color, last_point1, [xoffset + -auDio, yoffset + -auDio], linewidth)
        last_point1 = [(xoffset + -auDio),(yoffset + -auDio)]
        
   
        
