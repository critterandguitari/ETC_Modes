import os
import pygame
import time
import random
import glob

last_point = [0, 360]

images = []
image_index = 0


def setup(screen, etc):
    global images
    #for filepath in sorted(glob.glob('../patches/scope-image/*.png')):
    for filepath in sorted(glob.glob('../*.png')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath).convert()
        images.append(img)

def draw(screen, etc):
    global last_point, owen, image_index


    #owen = images[0]
    image_index += 1
    if image_index == len(images) : image_index = 0

    #screen.set_alpha(None)
    #owen.set_alpha(None)
    for i in range(0, 100) :
        seg(screen, etc, i)   

def seg(screen, etc, i):
    global last_point, images, owen
    xoffset = 40
    y0 = screen.get_height() // 2#random.randrange(0,1920)
    y1 = (screen.get_height() // 2) + (etc.audio_in[i] / 90)#random.randrange(0,1920)
    x = i * 12#random.randrange(0,1080)
    color = etc.color_picker() #on knob4

    last_point = [(int(etc.knob1*1280)), (int(etc.knob2*720))]
    pygame.draw.circle(screen,color,(x + xoffset, y1),int(etc.knob3 * 20) + 4, 0)
    pygame.draw.line(screen, color, last_point, [x + xoffset, y1], int(etc.knob3 * 20))

    
    
    #screen.blit(owen, (x + xoffset, y1))

