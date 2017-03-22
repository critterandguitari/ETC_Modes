import os
import pygame
import time
import random



def setup(screen, etc) :
    pass

def draw(screen, etc) :
    color = etc.color_picker() #on knob4
    
    steppy = int(etc.knob1 * 16)
    leftpoint = int(etc.knob2 * 720)
    linewidth = int(etc.knob3*42+1)
    
    for i in range (0,30) :
        ay0 = 240 + leftpoint - (steppy * i)
        ay1 = 240 + leftpoint - (steppy * i) + (etc.audio_in[i] / 128)
        ax = i * 21.3 
    
        pygame.draw.line(screen, color, [ax, ay1], [ax, ay0], linewidth)
    
    for i in range (30,60) :
        ay0 = 480 - leftpoint + (steppy * (i-30))
        ay1 = 480 - leftpoint + (steppy * (i-30))+ (etc.audio_in[i] / 128)
        ax = (i-30) * 21.3 
    
        pygame.draw.line(screen, color, [ax, ay1], [ax, ay0], linewidth)
    
    for i in range (60,94) :
        ay0 = 360
        ay1 = 360 + (etc.audio_in[i] / 80)
        ax = (i-30) * 21.3
    
        pygame.draw.line(screen, color, [ax, ay1], [ax, ay0], linewidth)
    
    
    
    #pygame.draw.line(screen, (0,0,0), [640, 0], [640, 720], 10)
        
    
