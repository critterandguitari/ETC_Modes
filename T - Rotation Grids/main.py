import os
import pygame
import time
import random
import math

lines = 40
hwidth = 720 / lines
vwidth = 1280/lines
hoffset = hwidth / 2
voffset = vwidth / 2
x21=y21=x2=y2=x3=y3=x11=y11=x1=y1=x4=y4=sound=0

def setup(screen, etc):
    pass

def draw(screen, etc):
    global lines, hoffset, voffset, vwidth, hwidth, sound
    
    for i in range(0, 100) :
        if abs(etc.audio_in[i]) > 10000 :
            sound = (((2*etc.knob3-1)/2000 + sound))
            
    
    hlength = int(etc.knob2 * 639)
    vlength = int(etc.knob2 * 359)
    #blue = random.randrange(0,255)
    #red = abs(blue-50)
    #green = blue/2
    
    
    #drawing horizontal lines
    for i in range(0, lines) :
        color = etc.color_picker()
        a = (-.5)*sound*math.pi
        xc = 640
        yc = hoffset + (i * hwidth)
        linewidth = hwidth - int(etc.knob1 * 17.5)#*int(sound*1000+1)%100
        L = 8*hlength
        
        if etc.knob3 < .5 :
            x21 = (L/2)*math.cos(a)
            y21 = (L/2)*math.sin(a)
            x2 = int(xc+x21)
            y2 = int(yc-y21)
            x3 = int(xc-x21)
            y3 = int(yc+y21)
            pygame.draw.line(screen, (color), [x2,y2], [x3, y3], linewidth)
            
        if etc.knob3 > .5 :
            x11 = (L/2)*math.cos(a)
            y11 = (L/2)*math.sin(a)
            x1 = xc-x11
            y1 = yc+y11
            x4 = xc+x11
            y4 = yc-y11
            pygame.draw.line(screen, (color), [x1,y1], [x4, y4], linewidth) 


    #drawing vertical lines  
    for i in range(0, lines) :
        a = sound*math.pi
        xc = voffset + (i * vwidth)
        yc = 360
        linewidth = vwidth - int(etc.knob1 * 31)
        L = 4*vlength
        color = etc.color_picker()

        
        if etc.knob3 < .5 :
            x21 = (L/2)*math.cos(a)
            y21 = (L/2)*math.sin(a)
            x2 = int(xc+x21)
            y2 = int(yc-y21)
            x3 = int(xc-x21)
            y3 = int(yc+y21)
            pygame.draw.line(screen, (color), [x2,y2], [x3, y3], linewidth)
            
        if etc.knob3 > .5 :
            x11 = (L/2)*math.cos(a)
            y11 = (L/2)*math.sin(a)
            x1 = xc-x11
            y1 = yc+y11
            x4 = xc+x11
            y4 = yc-y11
            pygame.draw.line(screen, (color), [x1,y1], [x4, y4], linewidth)    #red,green,blue
        
    #drawing lines 3    
    for i in range(0, lines) :
        color = etc.color_picker()    
        a = sound*math.pi*.125
        xc = voffset + (i * vwidth)
        yc = 360
        linewidth = vwidth - int(etc.knob1 * 31)
        L = 4*vlength
        
        
        if etc.knob3 < .5 :
            x21 = (L/2)*math.cos(a)
            y21 = (L/2)*math.sin(a)
            x2 = int(xc+x21)
            y2 = int(yc-y21)
            x3 = int(xc-x21)
            y3 = int(yc+y21)
            pygame.draw.line(screen, (color), [x2,y2], [x3, y3], linewidth)
            
        if etc.knob3 > .5 :
            x11 = (L/2)*math.cos(a)
            y11 = (L/2)*math.sin(a)
            x1 = xc-x11
            y1 = yc+y11
            x4 = xc+x11
            y4 = yc-y11
            pygame.draw.line(screen, (color), [x1,y1], [x4, y4], linewidth)        
    

