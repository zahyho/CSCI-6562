import pygame
from random import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load().convert_alpha()
        self.destroy_image = []
        self.destroy_image.extend([
            pygame.image.load().convert_alpha()
        ])
        self.rect = self.image.get_rect()
        # 记得在main.py定义background的size
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 5
        self.active = True
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.top = randint(-3 * self.height, 0)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.top = randint(-3 * self.height, 0)