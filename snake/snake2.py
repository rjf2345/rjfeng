# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 22:23:32 2019

@author: 饶佳峰
"""

import pygame
import random


white=(255,255,255)
black=(0,0,0)
cell=10
snake_init_pos=[[250,250],[240,250],[230,250],[220,250]]
head_pos=[250,250]
size=width,hight=600,500
grade=0

pygame.init()
clock=pygame.time.Clock()
pygame.display.set_caption('贪吃蛇')
caption=pygame.display.set_mode(size)
myfont = pygame.font.Font(None,35)
s_font= pygame.font.SysFont('SimHei',40)
textImage = myfont.render(str(grade),True,white)

def snake_init():
    global snake_init_pos
    global head_pos
    snake_init_pos=[[250,250],[240,250],[230,250],[220,250]]
    head_pos=[250,250]
    

def draw_rect(color,postion):
    pygame.draw.rect(caption,color,pygame.Rect(postion[0],postion[1],cell,cell))


def change_direction(head_pos,direction):
    global f_pos
    global grade
    global textImage
    if direction==1:
        head_pos[0]-=cell
    elif direction==2:
        head_pos[0]+=cell
    elif direction==3:
        head_pos[1]-=cell
    elif direction==4:
        head_pos[1]+=cell
    snake_init_pos.insert(0,list(head_pos))
    if hit_self() or hit_wall():
        gameover()
    if head_pos!=food_pos:
        snake_init_pos.pop()
    else:
        grade+=5
        textImage = myfont.render(str(grade),True,white)
        f_pos=draw_food()
        
    
def draw_food():
    global food_pos
    while 1:
        food_pos=[random.randint(0,49)*10,random.randint(0,49)*10]
        if food_pos not in snake_init_pos:
            break
    return food_pos    

def hit_self():
    if snake_init_pos[0] in snake_init_pos[1:]:
        return True
    else:
        return False

def hit_wall():
    global size
    if head_pos[0]>=500 or head_pos[0]<0 or head_pos[1]>=size[1] or head_pos[1]<0:
        return True
    else:
        return False
    
def start_game():
    text1=s_font.render('准备好了吗？',True,white)
    text2=s_font.render('是',True,white)
    text3=s_font.render('否',True,white)
    while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
         if event.type == pygame.MOUSEBUTTONDOWN:
            pressed_array = pygame.mouse.get_pressed()
            print(pressed_array)
            x, y = pygame.mouse.get_pos()
            print((x,y))
            if pressed_array[0]==1 and x>=200 and x<=240 and y>=300 and y<=340:
                snake_init()
                gamming()
            if pressed_array[0]==1 and x>=350 and x<=390 and y>=300 and y<=340:
                pygame.quit()
                exit()
            
      caption.fill(black)
      caption.blit(text1,(200,150))
      caption.blit(text2,(200,300))
      caption.blit(text3,(350,300))  
      pygame.display.update()
      clock.tick(10)

def gamming():
    global f_pos
    global size
    global direction
    for pos in snake_init_pos:
        draw_rect(white,pos)
    for i in range(500):
        pygame.draw.rect(caption,white,pygame.Rect(500,i,1,1))
    
    f_pos=draw_food()
    
    draw_rect(white,f_pos)
    pygame.display.update()
    direction=2

        
    while 1:
        for event in pygame.event.get():
           if event.type==pygame.QUIT:
               pygame.quit()
           if event.type==pygame.KEYDOWN:
             if event.key==pygame.K_LEFT and direction !=2:
                 direction=1
               
             elif event.key==pygame.K_RIGHT and direction !=1:
                 direction=2
                
             elif event.key==pygame.K_UP and direction !=4:
                 direction=3
                
             elif event.key==pygame.K_DOWN and direction !=3:
                 direction=4
                
        change_direction(head_pos,direction)
        caption.fill(black)
        caption.blit(textImage,(550,50))
        draw_rect(white,f_pos)
        for i in range(500):
            pygame.draw.rect(caption,white,pygame.Rect(500,i,1,1))
        for pos in snake_init_pos:
            draw_rect(white, pos)
 
        pygame.display.update()
        clock.tick(3)
    
def gameover():
    text1=s_font.render('你死了，再来？',True,white)
    text2=s_font.render('是',True,white)
    text3=s_font.render('否',True,white)
    while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
         if event.type == pygame.MOUSEBUTTONDOWN:
            pressed_array = pygame.mouse.get_pressed()
            print(pressed_array)
            x, y = pygame.mouse.get_pos()
            print((x,y))
            if pressed_array[0]==1 and x>=200 and x<=240 and y>=300 and y<=340:
                start_game()
            if pressed_array[0]==1 and x>=350 and x<=390 and y>=300 and y<=340:
                pygame.quit()
      caption.fill(black)
      caption.blit(text1,(200,150))
      caption.blit(text2,(200,300))
      caption.blit(text3,(350,300))
      pygame.display.update()
      clock.tick(10)
def main():
    start_game()

if __name__=='__main__':
    main()
    