import pygame
from random import *


class Enemy1(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("./images/ene_1.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("./images/ene_1d1.png").convert_alpha(),
            # pygame.image.load("./images/ene_1d2.png").convert_alpha()
        ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 2
        self.active = True
        self.rect.left = randint(0, self.width - self.rect.width)
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
        self.rect.top = randint(-3 * self.height, 0)


class Enemy2(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("./images/ene_2.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("./images/ene_2d1.png").convert_alpha()
        ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 3
        self.active = True
        self.rect.left = randint(0, self.width - self.rect.width)
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
        self.rect.top = randint(-3 * self.height, 0)
