import os
import pygame
import time
import random
import time
import pygame.freetype


xspeed = 3
yspeed = 2

#counters for direction
xdirection = 1
ydirection = 1

xpos = 640
ypos = 380
stringList = ["cool", "the", "engines", "slow", "this", "rocket", "down"]
unistr = unicode("cool")
size=100
rIght = 100
bOttom = 100
lEft = 0
tOp = 0
word = 0
avg = 0

coloryo = (0,0,0)

def setup(screen, etc) :
    pass

def draw(screen, etc) : 
    global xpos, ypos, xdirection, ydirection, rIght, bOttom, lEft, tOp, unistr, word, coloryo, avg
    
    color = etc.color_picker()
    auDio = etc.audio_peak / 128
    if auDio > 255 : auDio = 255
    
    coloryo = (auDio,color[1],color[2])
    
    size = int(100*etc.knob3)+1
    font = pygame.freetype.Font(etc.mode_root + "/font.ttf", size)
    
    unistr = unicode(stringList[word])
    
    (text, textpos) = font.render(unistr, (coloryo))
    
    xspeed = int(etc.knob1 * 50) + 1
    yspeed = int(etc.knob2 * 50) + 1
    
    xpos = xpos + (xspeed * xdirection)
    ypos = ypos + (yspeed * ydirection) 
    
    rIght = xpos + text.get_width()
    bOttom = ypos + text.get_height()
    lEft = xpos
    tOp = ypos
    
    screen.blit(text, (xpos,ypos))
    
    if rIght >= 1280 or lEft <= 0  : 
        xdirection *= -1
        word = (word+1)%7
    
    if bOttom >= 720 or tOp <= 0  : 
        ydirection *= -1
        word = (word+1)%7

       
    
    
    
   
    
    