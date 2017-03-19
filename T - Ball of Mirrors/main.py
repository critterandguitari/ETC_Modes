import os
import pygame
import glob
import random

image_index = 0
last_screen = pygame.Surface((1280,720))

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    global last_screen
    
    if etc.audio_trig or etc.midi_note_new :
        r = random.randrange(0,255)
        g = random.randrange(0,255)
        b = random.randrange(0,255)
        x = random.randrange(0,1280)
        y = random.randrange(0,720)
        pygame.draw.circle(screen,(r,g,b),[x,y],50)

    image = last_screen
    last_screen = screen.copy()
    thing = pygame.transform.scale(image, (int(etc.knob3 * 1280), int(etc.knob4 * 720) ) )
    screen.blit(thing, (int(etc.knob1 * 1280), int(etc.knob2 * 720)))