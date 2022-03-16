import pygame


class MyWitch(pygame.sprite.Sprite):
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
        self.speed = 10
        self.active = True
        self.invincible = False

    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.rect.bottom < self.height - 60:
            self.rect.bottom += self.speed
        else:
            self.rect.bottom = self.height - 60

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.top = 0

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width

    def reset(self):
        self.active = True
        self.invincible = True
        self.rect.left = (self.width - self.rect.width) // 2
        self.rect.top = self.height - self.rect.height - 60
