import os
import pygame
import time
import random
import pygame.freetype


size = 1280
gs = 0
SentList = ["YES ","I'M ","LONELY ","WANNA ","DIE"]
x = 640
y = 360
yo = 255
speed = 1
string = unicode("YES ")
word=0

def setup(screen, etc):
    pygame.freetype.init()
    pass

def draw(screen, etc):
    global size, gs, charnum, x, y, charList, string, coloryo, yo, speed, word
    
    if etc.audio_trig or etc.midi_note_new :
        gs = 1
        size = 1280 * etc.knob2
        x = random.randrange(320,960)
        y = random.randrange(180,540)
        color = etc.color_picker()
        speed=int(etc.knob1*100+1)
        yo = speed
        string = unicode(SentList[word]) #+ unicode(SentList[word+1]) +unicode(SentList[word+2]) + unicode(SentList[word+3]) +unicode(SentList[word+4])
        word = (word+1)%5
        
    if gs == 1 and size > 0 :
        
        font = pygame.freetype.Font(etc.mode_root + "/font.ttf", size)
        color = etc.color_picker()
        coloryo = (int(color[0]*speed/yo),int(color[1]*speed/yo),color[2]*speed/yo)
        if coloryo == (1,1,1) : coloryo = (0,0,0)
        (text, textpos) = font.render(string, coloryo) #(abs(red-int(etc.knob1*255)),abs(green-int(etc.knob1*255)),abs(blue-int(etc.knob1*255))))
        textpos.centerx = x
        textpos.centery = y
    
        
        screen.blit(text, textpos)
        size = size - 5 * 50*etc.knob3
        yo = yo + 1
        if yo > 255 : yo = 255
        if size < 1 : size = 1
       


