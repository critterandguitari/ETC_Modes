import os
import pygame
import time
import random
import math

hlines = 20 
hwidth = 720 / hlines
hoffset = hwidth / 2
vlines = 35
vwidth = 1280 / vlines
voffset = hoffset#vwidth / 2



def setup(screen, etc):
    pass

def draw(screen, etc):
    global lines, offset, width
    
    avg = 0
    
    for i in range(1, 99) :
        avg += (etc.audio_in[i] / 20) / i
    #if avg < 1 : avg = 1
    
    hlength = int(etc.knob2 * 639)
    vlength = int(etc.knob2 * 359)
    
    for i in range(0, hlines) :
        color = etc.color_picker()
        #pygame.draw.line(screen, color, [0, offset + (i * width)], [1280, offset + (i * width) ], width - int(etc.knob1 * 35)) #fullwidth
        pygame.draw.line(screen, color, [hlength, hoffset + (i * hwidth)], [1280 - hlength, hoffset + (i * hwidth) ], hwidth - int(etc.knob1 * 35))
     
    for i in range(0, vlines) :
        color = etc.color_picker()   
        pygame.draw.line(screen, color, [voffset + (i * vwidth),vlength], [voffset + (i * vwidth),720 - vlength ], hwidth - int(etc.knob1 * 35))
        
        #pygame.draw.line(screen, color, [0, int(etc.knob2*720)], [1280, offset + (i * width)], width - int(etc.knob1 * 35))
        
        #pygame.draw.line(screen, color, [0, offset + (i * width)], [1280, 720-int(etc.knob2*720) ], width - int(etc.knob1 * 35))
        #pygame.draw.line(screen, color, [0, int(etc.knob2*720)], [1280, offset + (i * width)], width - int(etc.knob1 * 35))
        
        #pygame.draw.line(screen, color, [0, offset + (i * width)], [1280, 720-avg ], width - int(etc.knob1 * 35))
        #pygame.draw.line(screen, color, [0, 720-avg], [1280, offset + (i * width)], width - int(etc.knob1 * 35))
        
        #pygame.draw.line(screen, color, [0, int(etc.knob2*720)], [1280, offset + (i * width)], avg)
        #pygame.draw.line(screen, color, [0, offset + (i * width)], [1280, 720-int(etc.knob2*720) ], avg)
        
    if avg > 1080 : i = 0
    if avg > 960 and avg < 1079 : i = 1
    if avg > 840 and avg < 959 : i = 2
    if avg > 720 and avg < 839 : i = 3
    if avg > 600 and avg < 719 : i = 4
    if avg > 480 and avg < 599 : i = 5
    if avg > 360 and avg < 479 : i = 6
    if avg > 240 and avg < 359 : i = 7
    if avg > 120 and avg < 239 : i = 8
    if avg > 0 and avg < 119 : i = 9
    
    if avg < 0 and avg > -119 : i = 10
    if avg < -120 and avg > -239 : i = 11
    if avg < -240 and avg > -359 : i = 12
    if avg < -360 and avg > -479 : i = 13
    if avg < -480 and avg > -599 : i = 14
    if avg < -600 and avg > -719 : i = 15
    if avg < -720 and avg > -839 : i = 16
    if avg < -840 and avg > -959 : i = 17
    if avg < -960 and avg > -1079 : i = 18
    if avg < -1080 : i = 19
    
    pygame.draw.line(screen, (255,255,255), [0, hoffset + (i * hwidth)], [1280, hoffset + (i * hwidth) ], hwidth - int(etc.knob1 * 35))
        
    
    #color = etc.color_picker()
    #R = int(etc.knob2*1000)
    #R = R + (etc.audio_in[i] / 100)
    #x = R * math.cos((i /  100.) * 6.28) + 640
    #y = R * math.sin((i /  100.) * 6.28) + 360
    
    pygame.draw.line(screen, (255,255,255), [0, 0], [1280, 0], 1) #top
    pygame.draw.line(screen, (255,255,255), [0, 360], [1280, 360], 1) #midline
    pygame.draw.line(screen, (255,255,255), [0, 718], [1280, 718], 1) #bottom
    
    pygame.draw.line(screen, (255,255,255), [0, 0], [0, 720], 1) #right
    pygame.draw.line(screen, (255,255,255), [640, 0], [640, 720], 1) #center
    pygame.draw.line(screen, (255,255,255), [1278, 0], [1278, 720], 1) #left
    
    #pygame.draw.line(screen, color, [0, 400], [1280, 400], int(etc.knob1*72))
    #pygame.draw.line(screen, color, [0, 200], [1280, 200], avg)

    

