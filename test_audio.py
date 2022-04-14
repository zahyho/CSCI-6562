#%%
#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import pygame
import sys
 
 
 
def speak(audioString):
    
    # print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    audio = pygame.mixer.Sound("audio.mp3")
    audio.play()
    #os.system("mpg321 audio.mp3")
 
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        data = r.recognize_google(audio)
 
 
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        pass
        # print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
 
 
pygame.init()
pygame.mixer.init()
font = pygame.font.Font("./font/font.TTF", 28)
def render(x):
    return font.render(x, 1, (255,255,255))
screen = pygame.display.set_mode((400, 400))
# pygame.display.set_caption("Say something")
clock = pygame.time.Clock()
loop = 1
say = font.render("Say something:", 1, (255,255,255))
while loop:
    screen.fill(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loop = 0
    data = recordAudio()
    text_surface = font.render(data, 1, (255,255,255))
    screen.blit(say, (0,0))
    screen.blit(text_surface, (0,50))
    # jarvis(data)
    pygame.display.update()
    clock.tick(2)
print("Game over")
pygame.quit()
sys.exit()