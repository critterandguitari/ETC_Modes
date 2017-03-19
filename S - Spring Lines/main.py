import os
import pygame
import random



trigger = False
x1 = [random.randrange(-200,1400) for i in range(0, 20)]
y1 = [random.randrange(-100,800) for i in range(0, 20)]
xslope = [random.randrange(-5,5) for i in range(0,20)]
yslope = [random.randrange(-5,5) for i in range(0,20)]
x2 = []
y2 = []



   


def setup(screen, etc):
    pass

def draw(screen, etc):
    global trigger, x1, y1, x2, y2, xslope, yslope
    
    
    linewidth = int(etc.knob2*5) + 1
    color = etc.color_picker()
    
   
    x2 = [x1[j]+ xslope[j]*etc.audio_in[1] * .008 for j in range(0, 20)]
    y2 = [y1[j]+ yslope[j]*etc.audio_in[1] * .008 for j in range(0, 20)]
    
    for k in range(0, 20) :
        
        pygame.draw.line(screen, color, (x1[k], y1[k]), (x2[k], y2[k]), linewidth)
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
        
    if trigger == True :
        
        x1 = [random.randrange(-200,1400) for i in range(0, 20)]
        y1 = [random.randrange(-100,800) for i in range(0, 20)]

        y2 = [x1[i]+(etc.audio_in[1] / 80) for i in range(0, 20)]
        x2 = [x1[i]+(etc.audio_in[1] / 80) for i in range(0, 20)]
            
    trigger = False   
    
    
        
    
