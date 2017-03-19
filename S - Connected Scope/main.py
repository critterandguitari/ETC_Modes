import os
import pygame
import time
import random

last_point = [0, 360]
first_point = []

color = (255,0,255)
colorList = []

def setup(screen, etc):
    pass

def draw(screen, etc):
    global last_point, first_point, color, colorList
    for i in range(0, 100) :
        lineseg(screen, etc, i)
    for i in range(0, 100) :
        ballseg(screen, etc, i)
    

def lineseg(screen, etc, i):
    global last_point, first_point, color, colorList
    
    linewidth = int(etc.knob1*100)+1
    y1 = (screen.get_height() // 2) + (etc.audio_in[i] / 90)
    x = i * 10
    xoffset = (1280 - (99*10)) // 2
    color = etc.color_picker()
    colorList = ( color[0]*(i*.01), color[1]*(i*.01), color[2]*(i*.01) )
    first_point = [(0*10)+xoffset, (screen.get_height() // 2) + (etc.audio_in[0] / 35)]
    
    if i == 0 : 
        last_point = first_point
    else :
        last_point = last_point
    
    pygame.draw.line(screen, colorList, last_point, [x + xoffset, y1], linewidth)
    last_point = [x + xoffset, y1]

def ballseg(screen, etc, i):
    global color, colorList
    
    ballwidth = int(etc.knob2*100)+1
    y1 = (screen.get_height() // 2) + (etc.audio_in[i] / 90)
    x = i * 10
    xoffset = (1280 - (99*10)) // 2
    color = etc.color_picker()
    colorList = ( color[0]*((99-i)*.01), color[1], color[2] )
    
    pygame.draw.circle(screen,colorList,(x + xoffset, y1),ballwidth, 0)
    
    
