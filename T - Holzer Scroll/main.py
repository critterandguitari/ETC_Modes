import os
import pygame
import time
import random
import math
import time
import pygame.freetype

subjList = ["I ","You ","We ","They "]
verbList = ["split ","jump ","ride ","eat ","drink ", "play "]
artList = ["a ","the ","one ","no "]
adjList = ["funny ","smelly ","bad ","cool ","real "]
nounList = ["log.","dog.","bog.","fog.","frog.", "cog.", "jog."]
start_ticks=pygame.time.get_ticks() #starter tick
string = unicode("I split a real log.")
scrollX = 1280 
gs = 0

color = (0,0,0)



def setup(screen, etc):
    pygame.freetype.init()
    pass

def draw(screen, etc):
    global string, word, color, scrollX, gs, text, size
    
    size = int(etc.knob1*200)+1
    color = etc.color_picker()
    font = pygame.freetype.Font(etc.mode_root + "/font.ttf", size)
    (text, textpos1) = font.render(string, color)
    
    if etc.audio_trig or etc.midi_note_new : 
        string = unicode(subjList[random.randint(0,3)]) + unicode(verbList[random.randint(0,5)]) +unicode(artList[random.randint(0,3)]) + unicode(adjList[random.randint(0,4)]) +unicode(nounList[random.randint(0,6)])
        gs = 1
        scrollX = 1280 + text.get_width() 
        
        
    if gs == 1 and size > 0 :
        font = pygame.freetype.Font(etc.mode_root + "/font.ttf", size)
        #audio movement
        textpos1 =(scrollX - (text.get_width()+1), (int(600 * etc.knob2)) )
   
    screen.blit(text, textpos1)
    scrollX = scrollX - (etc.knob3*40) + 1
    if scrollX < 1 : scrollX = 1

    
    
    
    
    



   

