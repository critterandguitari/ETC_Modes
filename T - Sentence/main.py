import os
import pygame
import pygame.freetype

lines = []

string = unicode(" ")
word = 0
yourlines = None


def setup(screen, etc):
    global yourlines
    pygame.freetype.init()
    yourfile = open(etc.mode_root + "/text.txt", "rU")
    yourlines = yourfile.readlines()#.remove('no')
    pass

def draw(screen, etc):
    global string, word, yourlines

    lineNum = len(yourlines)
   
    color = etc.color_picker()
    size = etc.knob1 * 300 + 10
    x = etc.knob2 * 1000
    y = etc.knob3 * 720
    font = pygame.freetype.Font(etc.mode_root + "/font.ttf", size)
    (text, textpos1) = font.render(string, color)
    textpos1 = (100, 300)
    
    if etc.audio_trig or etc.midi_note_new :
        string = yourlines[word].rstrip()
        word = (word+1)%lineNum

    textpos1 =(x, y -10)
    screen.blit(text, textpos1)
    
    
    
    
    
    



   

