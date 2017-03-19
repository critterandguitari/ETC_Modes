import os
import pygame
import time
import random
import math

litList = []
color = [255,255,255]
counter = 1

def setup(screen, etc):
    pass

def draw(screen, etc):
    LFO = etc.knob1*6
    counter = 1
    counter = counter + LFO
    
    litList1 = [unichr( (11000 + i) - int(abs(etc.audio_in[i])*.001) ) for i in range(0,20)]
    litList2 = [unichr( (11000 + i) - int(abs(etc.audio_in[i])*.001) ) for i in range(21,40)]
    litList3 = [unichr( (11000 + i) - int(abs(etc.audio_in[i])*.001) ) for i in range(41,60)]

    string1 = ''.join(litList1)
    string2 = ''.join(litList2)
    string3 = ''.join(litList3)
    
    
    size = int(etc.knob2 * 100) + 5    
    font = pygame.font.Font(etc.mode_root + "/font.ttf", size)
    auDio = ( ( (etc.audio_in[i] * .00003125) * 0.5) + 0.5 ) 
    color[0] = ((auDio*auDio)*254) + 1
    color[1] = ((auDio*auDio)*150) + 50
    color[2] = ((auDio*auDio)*130) + 100
    text1 = font.render(string1, True, (color[0:4]))
    text2 = font.render(string2, True, (color[0:4]))
    text3 = font.render(string3, True, (color[0:4]))
    textpos1 =[40, 360-(text1.get_height()/2) ]
    
    
    
    screen.blit(text1, textpos1)
    screen.blit( text2, (textpos1[0], (textpos1[1]*2)))
    screen.blit( text3, (textpos1[0], (textpos1[1]* 0.025)))
    
    
    
    
    
    
    



   

