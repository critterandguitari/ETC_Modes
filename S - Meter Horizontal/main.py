import os
import pygame
import time
import random
import math

lines = 20 
width = 720 / lines
offset = width / 2



def setup(screen, etc):
    pass

def draw(screen, etc):
    global lines, offset, width
    
    avg = 0
    
    avg = abs(etc.audio_in[0] / 30) 
    
    #if avg < 1 : avg = 1
    
    length = int(etc.knob2 * 639)
    
    for i in range(0, lines) :
        color = etc.color_picker()
        #pygame.draw.line(screen, color, [0, offset + (i * width)], [1280, offset + (i * width) ], width - int(etc.knob1 * 35)) #fullwidth
        pygame.draw.line(screen, color, [length, offset + (i * width)], [1280 - length, offset + (i * width) ], width - int(etc.knob1 * 35))

        
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
    
    pygame.draw.line(screen, (255,255,255), [0, offset + (i * width)], [1280, offset + (i * width) ], width - int(etc.knob1 * 35))
        
    
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

    

