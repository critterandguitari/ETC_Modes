import os
import pygame
import pygame.gfxdraw

circles = 10

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    color = etc.color_picker() #on knob4
    
    circles = int(etc.knob1*25)+1
    space = (1280/circles)
    offset = int(etc.knob2*30)
    y = int(etc.knob3*720)
    
    for i in range (0, circles) :
        auDio = abs(etc.audio_in[i] / 194)
        r = auDio + offset
        ax = (i*space)+(space/2)
    
        pygame.gfxdraw.filled_circle(screen, ax, y, r, color)
    
    
    #cool audio scaler thing#
    ### auDio = ((etc.audio_in[i] * 0.00003052)*0.5)+0.5
    #    r = int(auDio * offset)+1
    #    ax = (i*space)+(space/2)


        
    