from email.mime import audio
import imp
import sys
from turtle import position
import pygame
import enemy
import time
from gtts import gTTS

from pygame.locals import *
from random import *
from test import *

import speech_recognition as sr
destory_index = 0
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
def button(screen, position, text, color):
    font = pygame.font.Font("./font/font.ttf", 80)
    text_render = font.render(text, 1, color)
    x, y, w, h = text_render.get_rect()
    x, y = position
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

def input_key(key_pressed, me):
    if key_pressed[K_w] or key_pressed[K_UP]:
        me.moveUp()
    if key_pressed[K_s] or key_pressed[K_DOWN]:
        me.moveDown()
    if key_pressed[K_a] or key_pressed[K_LEFT]:
        me.moveLeft()
    if key_pressed[K_d] or key_pressed[K_RIGHT]:
        me.moveRight()

def input_key2(key_pressed):
    if key_pressed[K_l]:
        return True
    else:
        return False

def magic_speech(state):
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ('Say Something!')
        audio = r.listen(source)
    
    magic_spell = "fire"
    data = ""
    try:
        data = r.recognize_google(audio)
        data = data.lower()
        print("word: ", data)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        pass

    if data == magic_spell:
        state = True
    else:
        state = False
    time.sleep(1)
    return state