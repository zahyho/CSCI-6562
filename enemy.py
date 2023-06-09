import pygame
from random import *


class Enemy1(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("./images/dragon_1.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("./images/images/1.png").convert_alpha(),
            # pygame.image.load("./images/images/2.png").convert_alpha(),
            # pygame.image.load("./images/images/3.png").convert_alpha(),
            # pygame.image.load("./images/images/4.png").convert_alpha(),
            # pygame.image.load("./images/images/5.png").convert_alpha()
        ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 2
        self.active = True
        self.invincible = False
        self.rect.left = randint(0, self.width - self.rect.width+80)
        self.rect.top = randint(-3 * self.height, 0)
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.top = randint(-4 * self.height, 0)


class Enemy2(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("./images/en_witch.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("./images/images/1.png").convert_alpha()
            # pygame.image.load("./images/images/fire_2.gif").convert_alpha(),
            # pygame.image.load("./images/images/fire_3.gif").convert_alpha(),
            # pygame.image.load("./images/images/fire_4.gif").convert_alpha(),
            # pygame.image.load("./images/images/fire_5.gif").convert_alpha(),
            # pygame.image.load("./images/images/fire_6.gif").convert_alpha(),
            # pygame.image.load("./images/images/fire_7.gif").convert_alpha(),
            # pygame.image.load("./images/images/fire_8.gif").convert_alpha(),
            # pygame.image.load("./images/images/fire_9.gif").convert_alpha(),
            # pygame.image.load("./images/images/fire_11.gif").convert_alpha(),
            # pygame.image.load("./images/images/fire_13.gif").convert_alpha()
        ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 3
        self.active = True
        self.rect.left = randint(0, self.width - self.rect.width+80)
        self.rect.top = randint(-9 * self.height, 0)
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.top = randint(-4 * self.height, 0)
        self.invincible = False