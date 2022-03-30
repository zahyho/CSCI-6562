import imp
import sys
from turtle import position
import pygame
import enemy

from pygame.locals import *
from random import *
from test import *

def add_enemies1(group1, group2, num, bg_size):
    for i in range(num):
        e1 = enemy.Enemy1(bg_size)
        group1.add(e1)
        group2.add(e1)


def add_enemies2(group1, group2, num, bg_size):
    for i in range(num):
        e1 = enemy.Enemy2(bg_size)
        group1.add(e1)
        group2.add(e1)


def inc_speed(target, inc):
    for each in target:
        each.speed += inc

# create button
def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w , h))
    return screen.blit(text_render, (x, y))

def start():
    print("Ok, let's go")

def draw_enemies(enemies, screen, delay, destory_index, enemy_down_sound, score):
    for each in enemies:
        if each.active:
            each.move()
            screen.blit(each.image, each.rect)
        else:
            # 毁灭
            if not (delay % 3):
                if destory_index == 0:
                    enemy_down_sound.play()
                print(len(each.destroy_images))
                print("e1d: ", str(destory_index))
                screen.blit(each.destroy_images[destory_index], each.rect)
                destory_index = (destory_index + 1) % 1
                if destory_index == 0:
                    score += 100
                    each.reset()
    
    return score

def input_key(key_pressed, state, me):
    if key_pressed[K_w] or key_pressed[K_UP]:
        me.moveUp()
    if key_pressed[K_s] or key_pressed[K_DOWN]:
        me.moveDown()
    if key_pressed[K_a] or key_pressed[K_LEFT]:
        me.moveLeft()
    if key_pressed[K_d] or key_pressed[K_RIGHT]:
        me.moveRight()
    if key_pressed[K_l]:
        if state == False:
            state = True
        else:
            state = False
    return state
