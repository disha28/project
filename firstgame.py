import pygame
import random
import sys
import time
from pygame.locals import *


pause=False
#boom=TRUE
pygame.init()
crash_sound=pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("bgnd.wav")

display_height=1000
display_width=1920
spaceshuttle_width=1024
spaceshuttle_height=1024
white=(255,255,255)
black=(0,0,0)
red=(200,0,0)
bright_red=(255,0,0)
bright_green=(0,255,0)
green=(0,200,0)


gamedisplay=pygame.display.set_mode((display_height,display_width))
pygame.display.set_caption('first game')
clock=pygame.time.Clock()

obsimg=pygame.image.load("a.png")




obsimg=pygame.transform.scale(obsimg,(70,60))

def things_score(count):
    font=pygame.font.SysFont(None,25)
    text=font.render("Score: "+str(count),True,white)
    gamedisplay.blit(text,(5,10))

def thingsnew(thing_x_new,thing_starty,thing_width,thing_height):
        
    #obsimg=pygame.image.load("a.png")
    #obsimg=pygame.transform.scale(obsimg,(70,60))
    #thing_x_new=random.randrange(0,display_width-thing_width)
    gamedisplay.blit(obsimg,(thing_x_new,thing_starty))
    
    
                                 

def things(thing_startx,thing_starty,thing_width,thing_height):
        gamedisplay.blit(obsimg,(thing_startx,thing_starty))
    


spaceimg=pygame.image.load("b.png")        #img_insertion

objimg=pygame.image.load("space-shuttle.png")          #img_insertion
objimg= pygame.transform.scale(objimg, (200, 100))

def spaceshuttle(x,y):
    gamedisplay.blit(objimg,(x,y))

def text_objects(text,font):
    textSurface=font.render(text,True,white)
    return textSurface,textSurface.get_rect()
def message_display(text):
    largetext=pygame.font.Font('freesansbold.ttf',115)
    textsurf,textRect=text_objects(text,largetext)
    textRect.center=(508,400)
    gamedisplay.blit(textsurf,textRect)

    pygame.display.update()

    time.sleep(2)
    game_loop()

def boom():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    largetext=pygame.font.Font('freesansbold.ttf',115)
        
    textsurf,textRect=text_objects("you collapsed",largetext)
    textRect.center=(508,400)
    gamedisplay.blit(textsurf,textRect)


    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        button("PLAY AGAIN",100,500,200,100,green,bright_green,game_loop)
        button("QUIT!",700,500,200,100,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)



def button(msg,u,v,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    print(click)
    if u+w> mouse[0]>u and v+h >mouse[1]>v:
        pygame.draw.rect(gamedisplay,ac,(u,v,w,h))
        if click[0]==1 and action!=None:
            action()

            
##            if action=="play":
##                game_loop()
##            elif action== "quit":
##                pygame.quit()
##                quit()
        
    else:
        pygame.draw.rect(gamedisplay,ic,(u,v,w,h))

    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textRect=text_objects(msg,smalltext)
    textRect.center=((u+(w/2)),(v+(h/2)))
    gamedisplay.blit(textsurf,textRect)


def quitgame():
    pygame.quit()
    quit()
def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause=False


def paused():
    pygame.mixer.music.pause()

    largetext=pygame.font.Font('freesansbold.ttf',115)
        
    textsurf,textRect=text_objects("pause",largetext)
    textRect.center=(508,400)
    gamedisplay.blit(textsurf,textRect)
   



    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        button("CONTINUE",100,500,200,100,green,bright_green,unpause)
        button("QUIT!",700,500,200,100,red,bright_red,quitgame)

        

        




                
        #spaceimg=pygame.image.load("b.png")
        #gamedisplay.blit(spaceimg,(0,0))
        
        #gamedisplay.fill(black)
        #largetext=pygame.font.Font('freesansbold.ttf',115)
        
        #textsurf,textRect=text_objects("pause",largetext)
        #textRect.center=(508,400)
        #gamedisplay.blit(textsurf,textRect)
        #button("CONTINUE",100,500,200,100,green,bright_green,unpause)
        #button("QUIT!",700,500,200,100,red,bright_red,quitgame)


       


       #pygame.draw.rect(gamedisplay,red,(700,500,200,100))
        pygame.display.update()
        clock.tick(15)


       




    
def game_intro():
    intro=True

    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        spaceimg=pygame.image.load("b.png")
        gamedisplay.blit(spaceimg,(0,0))
        
        #gamedisplay.fill(black)
        largetext=pygame.font.Font('freesansbold.ttf',115)
        
        textsurf,textRect=text_objects("space around",largetext)
        textRect.center=(508,400)
        gamedisplay.blit(textsurf,textRect)
        button("PLAY NOW",100,500,200,100,green,bright_green,game_loop)
        button("QUIT!",700,500,200,100,red,bright_red,quitgame)


       


       #pygame.draw.rect(gamedisplay,red,(700,500,200,100))
        pygame.display.update()
        clock.tick(15)
        
        

            



    


def game_loop():
    global pause
    pygame.mixer.music.play(-1)
    x=960
    y=900
    x_change=0
    y_change=0
    objimg_x=342
    objimg_y=612
    spaceshuttle_speed=0
    thing_width=100
    
    thing_startx=random.randrange(0,display_width-thing_width)
    thing_starty=-400
    thing_speed=3
    
    thing_height=100
    Score=0
    block_count=4
    thing_x_list=[]
    thing_x_new=random.randrange(0,display_width-thing_width)
    thing_x_three=random.randrange(0,display_width-thing_width)
    thing_x_four=random.randrange(0,display_width-thing_width)
    

    
    

    crashed=False
    while not crashed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                crashed =True
            
                
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT):
                    x_change=-9
                  
                
                elif (event.key == pygame.K_RIGHT):
                    x_change=9
                if event.key == pygame.K_p:
                    pause=True
                    paused()
                      
                   
                    
                elif (event.key ==pygame.K_UP):
                    y_change=-9
                elif (event.key ==pygame.K_DOWN):
                    y_change=9

        


            
            pygame.key.set_repeat(100,80)
            pygame.event.pump()
        key =pygame.key.get_pressed()
        pygame.event.pump()

        if key[K_LEFT]:
            if ((objimg_x+x_change)>0 and (objimg_x+x_change)>(display_width-2*spaceshuttle_width)):
               objimg_x-=9


        if key[K_RIGHT]:
            if ((objimg_x+x_change)>0 and (objimg_x+x_change)<(display_width-spaceshuttle_width)):
               objimg_x+=9


        if key[K_UP]:
            if ((objimg_y+y_change)>0 ):
              objimg_y-=9

        if key[K_DOWN]:
          if ((objimg_y+y_change)<(display_height-80) ):
            objimg_y+= 9   


        gamedisplay.fill(0)
        
        
        gamedisplay.blit(spaceimg,(0,0))
        spaceshuttle(960,900)
        
        things_score(Score)

        #thing_starty=-100
        for u in range (block_count):
        
            
            #thing_x_new=random.randrange(0,display_width-thing_width)
            thing_x_list.append(thing_x_new)
        thingsnew(thing_x_new,thing_starty,thing_width,thing_height)
        thing_starty += thing_speed
        thingsnew(thing_x_three,thing_starty,thing_width,thing_height)
        thing_starty+=thing_speed
        thingsnew(thing_x_four,thing_starty,thing_width,thing_height)
        thing_starty+=thing_speed
                
        
                
        if thing_x_new in range(objimg_x , objimg_x + 200):
            if thing_starty in range(objimg_y, objimg_y + 100):
                boom()

        if thing_x_three in range(objimg_x , objimg_x + 200):
            if thing_starty in range(objimg_y, objimg_y + 100):
                boom()

        if thing_x_four in range(objimg_x , objimg_x + 200):
            if thing_starty in range(objimg_y, objimg_y + 100):
                boom()


                

                
        if thing_starty>display_height:
            thing_starty=0-thing_height
            thing_startx=random.randrange(0,display_width)
            thing_x_new=random.randrange(0,display_width-thing_width)
            thing_x_three=random.randrange(0,display_width-thing_width)
            thing_x_four=random.randrange(0,display_width-thing_width)
            Score+=1
            #for u in range (block_count):
            thingsnew(thing_x_new,thing_starty,thing_width,thing_height)
            thing_starty += thing_speed
            thingsnew(thing_x_three,thing_starty,thing_width,thing_height)
            thing_starty=0-thing_height
            thingsnew(thing_x_four,thing_starty,thing_width,thing_height)
            thing_starty=0-thing_height
                
                
                  
        things(thing_startx,thing_starty,thing_width,thing_height)
        thing_starty += thing_speed
        
        

        #touched obstcale
        if thing_startx in range(objimg_x , objimg_x + 200):
            if thing_starty in range(objimg_y, objimg_y + 100):
                boom()
                                 
        
        
        gamedisplay.blit(objimg,(objimg_x,objimg_y))
       

        
        

        
        
        pygame.display.flip()
        clock.tick(200)
game_intro()
game_loop()
pygame.quit()
quit()
    
