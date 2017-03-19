import os
import pygame
import glob
import pygame.gfxdraw
import random
import math

bkgrnd = pygame.Surface((1280, 720))
trot = 0
trigger = False

def setup(screen, etc):
    pass
def draw(screen, etc) :
    global bkgrnd, shape, trot, trigger
    
    color = etc.color_picker()
    
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
    if trigger == True :
        trot = (trot + 1)
        
    trigger = False    
    
    
    shape = pygame.Surface((200,400))
    pygame.gfxdraw.filled_trigon(shape, 0,400,100,0,200,400, color)    
    shape = pygame.transform.scale(shape, (200, 400))
    
    shape.set_alpha (int(etc.knob3 * 255))
    shape.set_colorkey ((0,0,0))
    shape = shape.convert_alpha()
    
    shape = pygame.transform.rotate(shape, trot)
    new_width = shape.get_width()
    new_height = shape.get_height()
    x = (0 + new_width / 2)
    y = (0 + new_height / 2)
    
    
    screen.blit(shape, (int(etc.knob1 * 1280) - x, int(etc.knob2 * 720) - y))
    
    