import os
import pygame
import time
import random


last_point = [320, 0]
last_point1 = [320, 0]




def setup(screen, etc):
    pass

def draw(screen, etc):
    
    global last_point, last_point1
    
    linewidth= int(etc.knob1*20)+1
    offset1 = etc.knob2*360
    offset2 = etc.knob3*360
    offset3 = etc.knob3*640
    
   
    pygame.gfxdraw.filled_polygon(screen, [(0,0+offset2),(offset1,360),(0,720-offset2)], (etc.bg_color[0]*.9,etc.bg_color[1]*.9,etc.bg_color[2]*.9))
    pygame.gfxdraw.filled_polygon(screen, [(640-offset3,0),(offset1,offset1),(1280-offset1,offset1),(640+offset3,0)], (etc.bg_color[0]*.8,etc.bg_color[1]*.8,etc.bg_color[2]*.8))
    pygame.gfxdraw.filled_polygon(screen, [(1280,0+offset2),(1280-offset1,360),(1280,720-offset2)], (etc.bg_color[0]*.7,etc.bg_color[1]*.7,etc.bg_color[2]*.7))
    pygame.gfxdraw.filled_polygon(screen, [(640+offset3,720),(1280-offset1,720-offset1),(offset1,720-offset1),(640-offset3,720)], (etc.bg_color[0]*.6,etc.bg_color[1]*.6,etc.bg_color[2]*.6))
    for i in range(0, 21) :
        x = 0
        y = 0
        xoffset = int(x + i*(361/20))
        yoffset = int(y + i*(361/20))
        auDio = etc.audio_in[i] / 35
        color = etc.color_picker()
        
        if i == 0 : last_point = [(x + auDio), (y + -auDio)]
        if i == 0 : auDio = 0
        if i == 20 : auDio = 0
        
        pygame.draw.line(screen, color, last_point, [xoffset + auDio, yoffset + -auDio], linewidth)
        last_point = [(xoffset + auDio),(yoffset + -auDio)]
        
    for j in range(20, 40) :
        x = 360
        y = 360
        xoffset = int(x - (j-20)*(361/19))
        yoffset = int(y + (j-20)*(361/19))
        auDio = etc.audio_in[j] / 35
        color = etc.color_picker()
        
        if j == 20 : last_point = [(x), (y)]
        if j == 20 : auDio = 0
        if j == 39 : auDio = 0
        
        pygame.draw.line(screen, color, last_point, [xoffset + -auDio, yoffset + -auDio], linewidth)
        last_point = [(xoffset + -auDio),(yoffset + -auDio)]
        
    for k in range(40,60) :
        x = 1280
        y = 0
        xoffset = int(x - (k-40)*(361/19))
        yoffset = int(y + (k-40)*(361/19))
        auDio = etc.audio_in[k] / 35
        color = etc.color_picker()
        
        if k == 40 : last_point = [(x), (y)]
        if k == 59 : auDio = 0
        if k == 40 : auDio = 0
        
        pygame.draw.line(screen, color, last_point, [xoffset + -auDio, yoffset + -auDio], linewidth)
        last_point = [(xoffset + -auDio),(yoffset + -auDio)]
        
    for l in range(60, 80) :
        x = 920
        y = 360
        xoffset = int(x + (l-60)*(361/19))
        yoffset = int(y + (l-60)*(361/19))
        auDio = etc.audio_in[l] / 35
        color = etc.color_picker()
        
        if l == 60 : last_point = [(x), (y)]
        if l == 79 : auDio = 0
        if l == 60 : auDio = 0
        
        pygame.draw.line(screen, color, last_point, [xoffset + auDio, yoffset + -auDio], linewidth)
        last_point = [(xoffset + auDio),(yoffset + -auDio)]
        
    for m in range(80, 100) :
        x = 360
        y = 360
        xoffset = x + (m-79)*(560/20)
        yoffset = int(y)
        auDio = etc.audio_in[m] / 35
        color = etc.color_picker()
        
        if m == 80 : last_point = [(x), (y)]
        if m == 99 : auDio = 0
        if m == 79 : auDio = 0
        
    
        
        pygame.draw.line(screen, color, last_point, [xoffset, yoffset + auDio], linewidth)
        last_point = [(xoffset),(yoffset + auDio)]

    
        
        
    
        
   
    
        
