import pygame
import sys
import enemy
import mywitch
import magic
import traceback

from pygame.locals import *
from random import *

pygame.init()
pygame.mixer.init()

bg_size = width, height = 480, 700
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("WitchGame")

background = pygame.image.load("").convert()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.mixer.music.load("sound/menu_BGM.wav")
pygame.mixer.music.set_volume(0.2)
magic_sound = pygame.mixer.Sound("")
magic_sound.set_volume(0.2)
extramagic_sound = pygame.mixer.Sound("")
extramagic_sound.set_volume(0.2)
me_down_sound = pygame.mixer.Sound("")
me_down_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound("")
enemy2_down_sound.set_volume(0.2)


def add_enemies1(group1, group2, num):
    for i in range(num):
        e1 = enemy.Enemy1(bg_size)
        group1.add(e1)
        group2.add(e1)


def add_enemies2(group1, group2, num):
    for i in range(num):
        e1 = enemy.Enemy2(bg_size)
        group1.add(e1)
        group2.add(e1)


def inc_speed(target, inc):
    for each in target:
        each.speed += inc


def main():
    pygame.mixer.music.play(-1)

    me = mywitch.MyWitch(bg_size)
    enemies = pygame.sprite.Group()

    # 生成第一关敌人
    enemies1 = pygame.sprite.Group()
    add_enemies1(enemies1, enemies, 15)

    # 生成第二关敌人
    enemies2 = pygame.sprite.Group()
    add_enemies2(enemies2, enemies, 15)

    # 生成魔法
    magic1 = []
    magic1_index = 0
    magic1_num = 4
    for i in range(magic1_num):
        magic1.append(magic.Magic(me.rect.midtop))

    # 生成额外魔法
    extramagic = []
    extramagic_index = 0
    extramagic_num = 4
    for i in range(extramagic_num):
        extramagic.append(magic.ExtraMagic(me.rect.midtop))

    clock = pygame.time.Clock()
    e1_destroy_index = 0
    e2_destroy_index = 0
    me_destroy_index = 0

    # 统计得分
    score = 0
    score_font = pygame.font.Font("font/font.ttf", 36)

    # 游戏难度
    level = 1

    # extramagic
    extramagic_image = pygame.image.load("").convert_alpha()
    extramagic_rect = extramagic_image.get_rect()
    extramagic_font = pygame.font.Font("font/font.ttf", 48)
    bomb_num = 3

    # 检测是否使用extramagic
    is_extramagic = False
    # 解除无敌状态
    INVINCIBLE_TIME = USEREVENT + 2

    # 生命值
    life_image = pygame.image.load("").convert_alpha()
    life_rect = life_image.get_rect()
    life_num = 3

    # 用于阻止重复打开记录文件
    recorded = False

    # 游戏结束画面
    gameover_font = pygame.font.Font("font/font.TTF", 48)
    again_image = pygame.image.load("").convert_alpha()
    again_rect = again_image.get_rect()
    gameover_image = pygame.image.load("").convert_alpha()
    gameover_rect = gameover_image.get_rect()

    # 用于切换图片
    switch_image = True

    # 用于延迟
    delay = 100

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == INVINCIBLE_TIME:
                me.invincible = False
                pygame.time.set_timer(INVINCIBLE_TIME, 0)

        if level == 1 and score > 2000:
            level = 2
            # 增加3个初始怪物和2个邪恶巫师
            add_enemies1(enemies1, enemies, 3)
            add_enemies2(enemies2, enemies, 2)
            # 提升初始怪物的速度
            inc_speed(enemies1, 1)

        screen.blit(background, (0, 0))

        if life_num:
            # 检测用户的键盘操作
            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_w] or key_pressed[K_UP]:
                me.moveUp()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                me.moveDown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                me.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                me.moveRight()

            # 发射魔法
            if not (delay % 10):
                magic_sound.play()
                if is_extramagic:
                    magics = extramagic
                    magics[extramagic_index].reset(me.rect.midtop)
                    extramagic_index = (extramagic_index + 2) % extramagic_num
                else:
                    magics = magic1
                    magics[magic1_index].reset(me.rect.midtop)
                    magic1_index = (magic1_index + 1) % magic1_num

            # 检测是否击中敌人
            for m in magics:
                if m.active:
                    m.move()
                    screen.blit(m.image, m.rect)
                    enemy_hit = pygame.sprite.spritecollide(m, enemies, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        m.active = False
                        for e in enemy_hit:
                            e.hit = True
                            e.active = False

            # 绘制第一关敌人：
            for each in enemies1:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    # 毁灭
                    if not (delay % 3):
                        if e1_destroy_index == 0:
                            enemy1_down_sound.play()
                        screen.blit(each.destroy_images[e1_destroy_index], each.rect)
                        e1_destroy_index = (e1_destroy_index + 1) % 4
                        if e1_destroy_index == 0:
                            score += 100
                            each.reset()

            # 绘制第二关敌人：
            for each in enemies1:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    # 毁灭
                    if not (delay % 3):
                        if e2_destroy_index == 0:
                            enemy2_down_sound.play()
                        screen.blit(each.destroy_images[e2_destroy_index], each.rect)
                        e2_destroy_index = (e2_destroy_index + 1) % 4
                        if e2_destroy_index == 0:
                            score += 200
                            each.reset()

            # 检测我方巫师是否产生碰撞
            enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
            if enemies_down and not me.invincible:
                me.active = False
                for e in enemies_down:
                    e.active = False

            # 绘制我方巫师
            if me.active:
                if switch_image:
                    screen.blit(me.image1, me.rect)
                else:
                    screen.blit(me.image2, me.rect)
            else:
                # 毁灭
                if not (delay % 3):
                    if me_destroy_index == 0:
                        me_down_sound.play()
                    screen.blit(me.destroy_images[me_destroy_index], me.rect)
                    me_destroy_index = (me_destroy_index + 1) % 4
                    if me_destroy_index == 0:
                        life_num -= 1
                        me.reset()
                        pygame.time.set_timer(INVINCIBLE_TIME, 3 * 1000)

            # extramagic数量显示
            extramagic_text = extramagic_font.render("× %d" % bomb_num, True, WHITE)
            text_rect = extramagic_text.get_rect()
            screen.blit(extramagic_image, (10, height - 10 - extramagic_rect.height))
            screen.blit(extramagic_text, (20 + extramagic_rect.width, height - 5 - text_rect.height))

            # 绘制剩余生命数量
            if life_num:
                for i in range(life_num):
                    screen.blit(life_image, (width - 10 - (i + 1) * life_rect.width, height - 10 - life_rect.height))

            # 绘制得分
            score_text = score_font.render("Score : %s" % str(score), True, WHITE)
            screen.blit(score_text, (10, 5))

        # 游戏结束
        elif life_num == 0:
            # 背景音乐停止
            pygame.mixer.music.stop()
            # 停止全部音效
            pygame.mixer.stop()

            if not recorded:
                recorded = True
                # 读取历史最高得分
                with open("record.txt", "r") as f:
                    record_score = int(f.read())

                # 如果玩家得分高于历史最高得分，则存档
                if score > record_score:
                    with open("record.txt", "w") as f:
                        f.write(str(score))

            # 绘制结束画面
            record_score_text = score_font.render("Best : %d" % record_score, True, (255, 255, 255))
            screen.blit(record_score_text, (50, 50))

            gameover_text1 = gameover_font.render("Your Score", True, (255, 255, 255))
            gameover_text1_rect = gameover_text1.get_rect()
            gameover_text1_rect.left, gameover_text1_rect.top = (width - gameover_text1_rect.width) // 2, height // 3
            screen.blit(gameover_text1, gameover_text1_rect)

            gameover_text2 = gameover_font.render(str(score), True, (255, 255, 255))
            gameover_text2_rect = gameover_text2.get_rect()
            gameover_text2_rect.left, gameover_text2_rect.top = (width - gameover_text2_rect.width) // 2, gameover_text1_rect.bottom + 10
            screen.blit(gameover_text2, gameover_text2_rect)

            again_rect.left, again_rect.top = (width - again_rect.width) // 2, gameover_text2_rect.bottom + 50
            screen.blit(again_image, again_rect)

            gameover_rect.left, gameover_rect.top = (width - again_rect.width) // 2, again_rect.bottom + 10
            screen.blit(gameover_image, gameover_rect)

            # 检测用户的鼠标操作
            # 如果用户按下鼠标左键
            if pygame.mouse.get_pressed()[0]:
                # 获取鼠标坐标
                pos = pygame.mouse.get_pos()
                # 如果用户点击“重新开始”
                if again_rect.left < pos[0] < again_rect.right and \
                        again_rect.top < pos[1] < again_rect.bottom:
                    # 调用main函数，重新开始游戏
                    main()
                # 如果用户点击“结束游戏”
                elif gameover_rect.left < pos[0] < gameover_rect.right and \
                        gameover_rect.top < pos[1] < gameover_rect.bottom:
                    # 退出游戏
                    pygame.quit()
                    sys.exit()

        # 切换图片
        if not (delay % 5):
            switch_image = not switch_image

        delay -= 1
        if not delay:
            delay = 100

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
