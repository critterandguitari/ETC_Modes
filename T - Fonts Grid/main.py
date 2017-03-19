import os
import pygame
import time
import random

count = 0
hlines = 8 
hwidth = 720 / hlines
hoffset = hwidth / 2
vlines = 8
vwidth = 1280 / vlines
voffset = hoffset#vwidth / 2


def setup(screen, etc):
    pass

def draw(screen, etc):
    global count
    
    size = int(etc.knob1 * 200) + 5    
    font = pygame.font.Font(etc.mode_root + "/font.ttf", size)
    
    linewidth = int(etc.knob2*20)
        
    unistr = get_unicode_character(int(etc.knob3 * 10)+1)
    textpos = (0,0)
    color = etc.color_picker()
    text = font.render(unistr, True, (color))     
    y = 0
    hlength = 0
    vlength = 0
    gridColor = (etc.bg_color[0]*0.8,etc.bg_color[1]*0.8,etc.bg_color[2]*0.8)
    
    for i in range(0, hlines) :
        pygame.draw.line(screen,gridColor, [hlength, (i * hwidth) -1], [1280 - hlength, (i * hwidth) - 1 ], linewidth)
        pygame.draw.line(screen, gridColor, [0,720],[1280,720], linewidth)
    for i in range(0, vlines) :
        pygame.draw.line(screen, gridColor, [(i * vwidth) - 1,vlength], [(i * vwidth) - 1,720 - vlength ], linewidth)
        pygame.draw.line(screen, gridColor, [1280,0],[1280,720], linewidth)
    if etc.audio_trig or etc.midi_note_new :
        count += 1 % 32
        for i in range(0,32) :
            x = (count % 8) * 160 + 80 
            y = (int(count / 8) % 8) * 90 + 45  
            textpos = text.get_rect(center = (x,y))
            screen.blit(text, textpos)
            
        
       

def get_unicode_character(set) :
    
    if set == 0 :
        # all of them (or a lot of them...)
        return unichr(random.choice((0x0000, 0xFF00)) + random.randint(0, 0xff))
        
    if set == 1 :
        # ogham
        return unichr(random.randint(0x1680, 0x169C))
        
    if set == 2 :
        # arrows
        return unichr(random.randint(0x2190, 0x21FF))
        
    if set == 3 :
        # math
        return unichr(random.randint(0x2200, 0x22ff))
        
    if set == 4 :
        # geometric shapes
        return unichr(random.randint(0x25a0, 0x25ff))
        
    if set == 5 :
        # box drawing
        return unichr(random.randint(0x2500, 0x257f))
        
    if set == 6 :
        # Brail
        return unichr(random.randint(0x2800, 0x28FF))
        
    if set == 7 :
        # More math
        return unichr(random.randint(0x2A00, 0x2ADF))
        
    if set == 8 :
        # from math -- sharp symbols
        return unichr(random.randint(0x2A80, 0x2ABC))

    if set == 9 :
        # more arrows
        return unichr(random.randint(0x2900, 0x297F))
    
    if set == 10 :
        #chess
        return unichr(random.randint(0xE010, 0xE04F))
        
    if set == 11 :
        #Genji-mon Symbols
        return unichr(random.randint(0xF500, 0xF535))
        

