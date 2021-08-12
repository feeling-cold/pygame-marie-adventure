import pygame
import random
from pygame.locals import *
import sys
import os
FPS = 30
from itertools import cycle

class MyMap():

    def __init__(self, x, y,path):

        self.bg = pygame.image.load(path).convert_alpha()
        self.x = x
        self.y = y

    def map_rolling(self,point):
        if self.x < point:
            self.x = -(point)+1
        else:
            self.x -= 3

    def map_update(self):
        SCREEN.blit(self.bg, (self.x, self.y))


class Stop_Button():
    is_start = True
    def __init__(self):
        self.start_img = pygame.image.load('image/stopbutton.png').convert_alpha()
        #self.stop_img = pygame.image.load('image/stop.png').convert_alpha()

    def is_select(self):
        point_x, point_y = pygame.mouse.get_pos()
        w, h = self.start_img.get_size()
        in_x = point_x > 60 and point_x < 60 + w
        in_y = point_y > 20 and point_y < 20 + h
        return in_x and in_y


class Music_Button():
    is_open = True
    def __init__(self):
        self.open_img = pygame.image.load('image/btn_open.png').convert_alpha()
        self.close_img = pygame.image.load('image/btn_close.png').convert_alpha()
        self.bg_music = pygame.mixer.Sound('audio/bg_music.wav')
    def is_select(self):

        point_x, point_y = pygame.mouse.get_pos()
        w, h = self.open_img.get_size()

        in_x = point_x > 20 and point_x < 20 + w
        in_y = point_y > 20 and point_y < 20 + h
        return in_x and in_y



class Marie():
    def __init__(self,lowest_y):
        # 初始化小玛丽矩形
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.jumpState = False
        self.jumpHeight = 130
        self.lowest_y = lowest_y
        self.jumpValue = 0

        self.marieIndex = 0
        self.marieIndexGen = cycle([0, 1, 2])
        # 加载小玛丽图片
        self.adventure_img = (
            pygame.image.load("image/adventure1.png").convert_alpha(),
            pygame.image.load("image/adventure2.png").convert_alpha(),
            pygame.image.load("image/adventure3.png").convert_alpha(),
        )
        self.jump_audio = pygame.mixer.Sound('audio/jump.wav')
        self.rect.size = self.adventure_img[0].get_size()
        self.x = 50
        self.y = lowest_y
        self.rect.topleft = (self.x, self.y)
        self.mrect = self.adventure_img[0].get_rect()


    def jump(self):
        self.jumpState = True



    def move(self):
        if self.jumpState:
            if self.rect.y >= self.lowest_y:
                self.jumpValue = -5
            if self.rect.y <= self.lowest_y - self.jumpHeight:
                self.jumpValue = 5
            self.rect.y += self.jumpValue
            if self.rect.y >= self.lowest_y:
                self.jumpState = False

    def draw_marie(self):
        marieIndex = next(self.marieIndexGen)
        SCREEN.blit(self.adventure_img[marieIndex],
                    (self.x, self.rect.y))

class Marie2():
    def __init__(self,lowest_y):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.jumpState = False
        self.jumpHeight = 130
        self.lowest_y = lowest_y
        self.jumpValue = 0
        self.marieIndex = 0
        self.marieIndexGen = cycle([0, 1, 2, 3])
        self.adventure_img = (
            pygame.image.load("image/bros1.png").convert_alpha(),
            pygame.image.load("image/bros3.png").convert_alpha(),
            pygame.image.load("image/bros3.png").convert_alpha(),
            pygame.image.load("image/bros4.png").convert_alpha(),
        )
        self.jump_audio = pygame.mixer.Sound('audio/jump.wav')
        self.rect.size = self.adventure_img[0].get_size()
        self.x = 80;
        self.y = lowest_y;
        self.rect.topleft = (self.x, self.y)

    def jump(self):
        self.jumpState = True

    def move(self):
        if self.jumpState:
            if self.rect.y >= self.lowest_y:
                self.jumpValue = -5
            if self.rect.y <= self.lowest_y - self.jumpHeight:
                self.jumpValue = 5
            self.rect.y += self.jumpValue
            if self.rect.y >= self.lowest_y:
                self.jumpState = False

    def draw_marie(self):
        marieIndex = next(self.marieIndexGen)
        SCREEN.blit(self.adventure_img[marieIndex],
                    (self.x, self.rect.y))

class Marie3():
    def __init__(self,lowest_y):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.jumpState = False
        self.jumpHeight = 130
        self.lowest_y = lowest_y
        self.jumpValue = 0
        self.marieIndex = 0
        self.marieIndexGen = cycle([0, 1, 2, 3])
        self.adventure_img = (
            pygame.image.load("image/p1.png").convert_alpha(),
            pygame.image.load("image/p2.png").convert_alpha(),
            pygame.image.load("image/p3.png").convert_alpha(),
            pygame.image.load("image/p4.png").convert_alpha(),
        )
        self.jump_audio = pygame.mixer.Sound('audio/jump.wav')
        self.rect.size = self.adventure_img[0].get_size()
        self.x = 80;
        self.y = lowest_y;
        self.rect.topleft = (self.x, self.y)

    def jump(self):
        self.jumpState = True


    def move(self):
        if self.jumpState:
            if self.rect.y >= self.lowest_y:
                self.jumpValue = -8
            if self.rect.y <= self.lowest_y - self.jumpHeight:
                self.jumpValue = 8
            self.rect.y += self.jumpValue
            if self.rect.y >= self.lowest_y:
                self.jumpState = False

    def draw_marie(self):
        marieIndex = next(self.marieIndexGen)
        SCREEN.blit(self.adventure_img[marieIndex],
                    (self.x, self.rect.y))

class Marie4():
    def __init__(self,lowest_y):
        self.jumpState = False
        self.runState = False
        self.image = (pygame.image.load("image/adventure1.png").convert_alpha(),
                      pygame.image.load("image/adventure2.png").convert_alpha(),
                      pygame.image.load("image/adventure3.png").convert_alpha())
        self.mrect = self.image[0].get_rect()
        self.jumpHeight = 130
        self.mrect.y = lowest_y
        self.lowest_y = lowest_y
        self.jumpValue = 0
        self.jump_audio = pygame.mixer.Sound('audio/jump.wav')
        self.index = 0
        self.list = cycle([0,1,2])

    def jump(self):
            self.jumpState = True

    def move(self):
        if self.jumpState:
            if self.mrect.y >= self.lowest_y:
                self.jumpValue = -8
            if self.mrect.y <= self.lowest_y - self.jumpHeight:
                self.jumpValue = 8
            self.mrect.y += self.jumpValue
            if self.mrect.y >= self.lowest_y:
                self.jumpState = False

    def draw_marie(self):
        index = next(self.list)
        SCREEN.blit(self.image[index],self.mrect)


class Bullet():
    def __init__(self):
        self.x = 80
        self.y = 150
        self.bullet_img = pygame.image.load("image/s.png")
        self.brect = self.bullet_img.get_rect()

    def move(self,x,y):
        self.brect.x = x
        self.brect.y = y

    def draw_Bullet(self):
        SCREEN.blit(self.bullet_img,self.brect)


class Obstacle():
    score = 1
    move = 3
    obstacle_y = 150
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)

        self.missile = pygame.image.load("image/missile.png").convert_alpha()
        self.pipe = pygame.image.load("image/pipe.png").convert_alpha()

        self.numbers = (pygame.image.load('image/0.png').convert_alpha(),
                        pygame.image.load('image/1.png').convert_alpha(),
                        pygame.image.load('image/2.png').convert_alpha(),
                        pygame.image.load('image/3.png').convert_alpha(),
                        pygame.image.load('image/4.png').convert_alpha(),
                        pygame.image.load('image/5.png').convert_alpha(),
                        pygame.image.load('image/6.png').convert_alpha(),
                        pygame.image.load('image/7.png').convert_alpha(),
                        pygame.image.load('image/8.png').convert_alpha(),
                        pygame.image.load('image/9.png').convert_alpha())

        self.score_audio = pygame.mixer.Sound('audio/score.wav')

        r = random.randint(0, 1)
        if r == 0:
            self.image = self.missile
            self.move = 15
            self.obstacle_y = 100
        else:
            self.image = self.pipe

        self.rect.size = self.image.get_size()
        self.width, self.height = self.rect.size
        self.x = 800
        self.y = self.obstacle_y
        self.rect.center = (self.x, self.y)


    def obstacle_move(self):
        self.rect.x -= self.move


    def draw_obstacle(self):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))


    def getScore(self):
        self.score
        tmp = self.score;
        if tmp == 1:
            self.score_audio.play()
        self.score = 0;
        return tmp;


    def showScore(self, score,SCREENWIDTH,SCREENHEIGHT):

        self.scoreDigits = [int(x) for x in list(str(score))]
        totalWidth = 0  # 要显示的所有数字的总宽度
        for digit in self.scoreDigits:
            # 获取积分图片的宽度
            totalWidth += self.numbers[digit].get_width()
        # 分数横向位置
        Xoffset = (SCREENWIDTH - (totalWidth+30))
        for digit in self.scoreDigits:
            # 绘制分数
            SCREEN.blit(self.numbers[digit], (Xoffset, SCREENHEIGHT * 0.1))
            # 随着数字增加改变位置
            Xoffset += self.numbers[digit].get_width()

class twoObstacle():
    score = 1
    move = 3
    obstacle_y = 180
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.missile = pygame.image.load("image/missile.png").convert_alpha()
        self.pipe = pygame.image.load("image/pipe.png").convert_alpha()
        self.numbers = (pygame.image.load('image/0.png').convert_alpha(),
                        pygame.image.load('image/1.png').convert_alpha(),
                        pygame.image.load('image/2.png').convert_alpha(),
                        pygame.image.load('image/3.png').convert_alpha(),
                        pygame.image.load('image/4.png').convert_alpha(),
                        pygame.image.load('image/5.png').convert_alpha(),
                        pygame.image.load('image/6.png').convert_alpha(),
                        pygame.image.load('image/7.png').convert_alpha(),
                        pygame.image.load('image/8.png').convert_alpha(),
                        pygame.image.load('image/9.png').convert_alpha())
        self.score_audio = pygame.mixer.Sound('audio/score.wav')
        r = random.randint(0, 1)
        if r == 0:
            self.image = self.missile
            self.move = 15
            self.obstacle_y = 125
        else:
            self.image = self.pipe
        self.rect.size = self.image.get_size()
        self.width, self.height = self.rect.size
        self.x = 800
        self.y = self.obstacle_y
        self.rect.center = (self.x, self.y)

    def obstacle_move(self):
        self.rect.x -= self.move

    def draw_obstacle(self):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

    def getScore(self):
        self.score
        tmp = self.score;
        if tmp == 1:
            self.score_audio.play()
        self.score = 0;
        return tmp;

    def showScore(self, score,SCREENWIDTH,SCREENHEIGHT):
        self.scoreDigits = [int(x) for x in list(str(score))]
        totalWidth = 0  # 要显示的所有数字的总宽度
        for digit in self.scoreDigits:
            totalWidth += self.numbers[digit].get_width()
        Xoffset = (SCREENWIDTH - (totalWidth+150))
        for digit in self.scoreDigits:
            SCREEN.blit(self.numbers[digit], (Xoffset, SCREENHEIGHT * 0.1))
            Xoffset += self.numbers[digit].get_width()

class enemy():
    score = 1
    move = 10
    obstacle_y = 195
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.enemy1 = pygame.image.load("image/e1.png").convert_alpha()
        self.enemy2 = pygame.image.load("image/e2.png").convert_alpha()
        self.numbers = (pygame.image.load('image/0.png').convert_alpha(),
                        pygame.image.load('image/1.png').convert_alpha(),
                        pygame.image.load('image/2.png').convert_alpha(),
                        pygame.image.load('image/3.png').convert_alpha(),
                        pygame.image.load('image/4.png').convert_alpha(),
                        pygame.image.load('image/5.png').convert_alpha(),
                        pygame.image.load('image/6.png').convert_alpha(),
                        pygame.image.load('image/7.png').convert_alpha(),
                        pygame.image.load('image/8.png').convert_alpha(),
                        pygame.image.load('image/9.png').convert_alpha())
        self.score_audio = pygame.mixer.Sound('audio/score.wav')
        r = random.randint(0, 1)
        if r > 0.5:
            self.image = self.enemy1
            self.move = 15
            self.obstacle_y = 120
        else:
            self.image = self.enemy2
        self.rect.size = self.image.get_size()
        self.width, self.height = self.rect.size
        self.x = 800
        self.y = self.obstacle_y
        self.rect.center = (self.x, self.y)

    def enemy_move(self):
        self.rect.x -= self.move

    def draw_enemy(self):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

    def getScore(self):
        self.score
        tmp = self.score;
        if tmp == 1:
            self.score_audio.play()
        self.score = 0;
        return tmp;

    def showScore(self, score, SCREENWIDTH, SCREENHEIGHT):
        self.scoreDigits = [int(x) for x in list(str(score))]
        totalWidth = 0
        for digit in self.scoreDigits:
            totalWidth += self.numbers[digit].get_width()
        Xoffset = (SCREENWIDTH - (totalWidth + 60))
        for digit in self.scoreDigits:
            SCREEN.blit(self.numbers[digit], (Xoffset, SCREENHEIGHT * 0.1))
            Xoffset += self.numbers[digit].get_width()


def game_over():
    bump_audio = pygame.mixer.Sound('audio/bump.wav')
    bump_audio.play()
    screen_w = pygame.display.Info().current_w
    screen_h = pygame.display.Info().current_h
    over_img = pygame.image.load('image/gameover.png').convert_alpha()
    SCREEN.blit(over_img, ((screen_w - over_img.get_width()) / 2,
                                       (screen_h - over_img.get_height()) / 2))


def goon():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.display.set_caption('玛丽冒险')
    myfont = pygame.font.SysFont('comicsansms', 20)
    screen = pygame.display.set_mode((355, 250))
    background = pygame.image.load("image/main2.png")
    black = (0, 0, 0)
    textImage = myfont.render('GO ON ( Y / N ) ?', True, black)
    while True:
        screen.blit(background, (0, 0))
        screen.blit(textImage, (100, 100))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYDOWN and event.key == K_y:
                pygame.quit()
                mainGame()
            if event.type == KEYDOWN and event.key == K_n:
                pygame.quit()
                sys.exit(0)

def twogoon():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.display.set_caption('玛丽冒险')
    myfont = pygame.font.SysFont('comicsansms', 20)
    screen = pygame.display.set_mode((355, 250))
    background = pygame.image.load("image/main2.png")
    black = (0, 0, 0)
    textImage = myfont.render('GO ON ( Y / N ) ?', True, black)
    while True:
        screen.blit(background, (0, 0))
        screen.blit(textImage, (100, 100))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYDOWN and event.key == K_y:
                pygame.quit()
                twopmainGame()
            if event.type == KEYDOWN and event.key == K_n:
                pygame.quit()
                sys.exit(0)

def win():
    pygame.init()
    pygame.display.set_caption('玛丽冒险')
    pygame.image.load("image/main2.png")
    myfont = pygame.font.SysFont('comicsansms', 40)
    screen = pygame.display.set_mode((355, 250))
    background = pygame.image.load("E:/main2.png")
    black = (0, 0, 0)
    textImage = myfont.render('you win !!!', True, black)
    while True:
        screen.blit(background, (0, 0))
        screen.blit(textImage, (100, 70))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)


def mainGame():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    SCREENWIDTH = 822
    SCREENHEIGHT = 199
    score = 0
    runtmp = 50
    runstate = False
    over = False
    global SCREEN, FPSCLOCK
    pygame.init()

    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('玛丽冒险')


    bg1 = MyMap(0, 0,"image/bg.png")
    bg2 = MyMap(800, 0,"image/bg.png")


    marie = Marie(140)
    marie.mrect.y = 140


    addObstacleTimer = 0
    list = []

    music_button = Music_Button()
    btn_img  = music_button.open_img
    music_button.bg_music.play(-1)

    stop_Button = Stop_Button()
    start_img = stop_Button.start_img

    run = True
    current = True

    while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if music_button.is_select():
                        if music_button.is_open:
                            btn_img = music_button.close_img
                            music_button.is_open = False
                            music_button.bg_music.stop()
                        else:
                            btn_img = music_button.open_img
                            music_button.is_open = True
                            music_button.bg_music.play(-1)

                    if stop_Button.is_select():
                        if  stop_Button.is_start:
                            stop_Button.is_start = False
                            current = False
                            run = False
                        else :
                            stop_Button.is_start = True
                            current = True
                            run = True

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN and event.key == K_a:
                    current = False
                    run = False
                if event.type == KEYDOWN and event.key == K_b:
                    run = True
                    current = True




                if event.type == KEYDOWN and event.key == K_w:
                    if marie.rect.y >= marie.lowest_y:
                        marie.jump_audio.play()
                        marie.jump()

                    if over == True:
                        mainGame()

                if event.type == KEYDOWN and event.key == K_s:
                    if marie.jumpState == False:
                        runstate = True
                        marie.rect.x == runtmp


            if run:
                if current:
                    if over == False:

                        bg1.map_update()
                        bg1.map_rolling(-790)
                        bg2.map_update()
                        bg2.map_rolling(-790)


                        marie.move()
                        marie.draw_marie()

                        if runstate == True:
                            runtmp += 10


                        if addObstacleTimer >= 1300:
                            r = random.randint(0, 100)
                            if r > 40:

                                obstacle = Obstacle()
                                list.append(obstacle)

                            addObstacleTimer = 0


                        for i in range(len(list)):

                            list[i].obstacle_move()
                            list[i].draw_obstacle()


                            if pygame.sprite.collide_rect(marie, list[i]):
                                over = True
                                game_over()
                                music_button.bg_music.stop()
                                pygame.quit()
                                goon()
                            else:
                                if (list[i].rect.x + list[i].rect.width) < marie.rect.x:
                                    # 加分
                                    score += list[i].getScore()

                            list[i].showScore(score,SCREENWIDTH,SCREENHEIGHT)
                            if score > 1:
                                pygame.quit()
                                hardGame()


                    addObstacleTimer += 20
                    SCREEN.blit(btn_img, (20, 20))
                    SCREEN.blit(start_img, (60, 20))
                    pygame.display.update()
                    FPSCLOCK.tick(FPS)  # 循环应该多长时间运行一次



def twopmainGame():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    score1 = 0
    score2 = 0
    SCREENWIDTH = 715
    SCREENHEIGHT = 224
    over = False
    global SCREEN, FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('玛丽冒险')

    bg1 = MyMap(0, 0, "image/bg2.png")
    bg2 = MyMap(715, 0, "image/bg2.png")

    player1 = Marie(170)
    player2 = Marie2(170)
    addObstacleTimer = 0
    list = []
    list2 = []

    music_button = Music_Button()
    btn_img = music_button.open_img
    music_button.bg_music.play(-1)

    stop_Button = Stop_Button()
    start_img = stop_Button.start_img

    run = True
    current = True

    p1c = True
    p2c = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if music_button.is_select():
                    if music_button.is_open:
                        btn_img = music_button.close_img
                        music_button.is_open = False
                        music_button.bg_music.stop()
                    else:
                        btn_img = music_button.open_img
                        music_button.is_open = True
                        music_button.bg_music.play(-1)

                if stop_Button.is_select():
                    if  stop_Button.is_start:
                        stop_Button.is_start = False
                        current = False
                        run = False
                    else :
                        stop_Button.is_start = True
                        current = True
                        run = True

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN and event.key == K_a:
                current = False
                run = False
            if event.type == KEYDOWN and event.key == K_b:
                run = True
                current = True

            if event.type == KEYDOWN and event.key == K_SPACE:
                if player1.rect.y >= player1.lowest_y:
                    player1.jump_audio.play()
                    player1.jump()


            if event.type == KEYDOWN and event.key == K_UP:
                if player2.rect.y >= player2.lowest_y:
                    player2.jump_audio.play()
                    player2.jump()

                if over == True:
                    twopmainGame()

        if run:
            if current:
                if over == False:
                    bg1.map_update()
                    bg1.map_rolling(-715)
                    bg2.map_update()
                    bg2.map_rolling(-715)

                    player1.move()
                    player2.move()

                    player1.draw_marie()
                    player2.draw_marie()


                    if addObstacleTimer >= 1300:
                        r = random.randint(0, 100)
                        if r > 40:
                            obstacle1 = Obstacle()
                            obstacle2 = twoObstacle()
                            list.append(obstacle1)
                            list2.append(obstacle2)

                        addObstacleTimer = 0


                    for i in range(len(list)):

                        list2[i].obstacle_move()

                        list2[i].draw_obstacle()



                        if pygame.sprite.collide_rect(player1, list2[i]) and pygame.sprite.collide_rect(player2, list2[i]):
                            over = True
                            game_over()
                            music_button.bg_music.stop()
                            pygame.quit()
                            twogoon()
                        else:
                            if pygame.sprite.collide_rect(player1, list2[i]):
                                player1.rect.x = -10000000
                                player1.rect.y = -10000000
                                p1c = False
                            if pygame.sprite.collide_rect(player2, list2[i]):
                                player2.rect.x = -10000000
                                player2.rect.y = -10000000
                                p2c = False

                            if p1c == False and p2c == False:
                                over = True
                                game_over()
                                music_button.bg_music.stop()
                                pygame.quit()
                                twogoon()


                        if not pygame.sprite.collide_rect(player1, list2[i]) and  not pygame.sprite.collide_rect(player2, list2[i]):
                            if (list2[i].rect.x + list2[i].rect.width) < player1.rect.x :
                                score1 += list[i].getScore()

                            if (list2[i].rect.x + list2[i].rect.width) < player2.rect.x:
                                score2 += list2[i].getScore()

                            list[i].showScore(score1, SCREENWIDTH, SCREENHEIGHT)
                            list2[i].showScore(score2,SCREENWIDTH, SCREENHEIGHT)

                addObstacleTimer += 20
                SCREEN.blit(start_img,(60,20))
                SCREEN.blit(btn_img, (20, 20))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

    if score2 > score1:
        print("player2 is win")
    elif score2 < score1:
        print("player1 is win")


def hardGame():
    tmp = 100
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    SCREENWIDTH = 731
    SCREENHEIGHT = 244
    list = []
    score = 0
    over = False
    addObstacleTimer = 0
    global SCREEN, FPSCLOCK
    pygame.init()

    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('玛丽冒险')
    bg1 = MyMap(0, 0, "image/bg3.png")
    bg2 = MyMap(730, 0, "image/bg3.png")

    marie = Marie3(170)

    music_button = Music_Button()
    btn_img = music_button.open_img
    music_button.bg_music.play(-1)

    stop_Button = Stop_Button()
    start_img = stop_Button.start_img

    run = True
    current = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if music_button.is_select():
                    if music_button.is_open:
                        btn_img = music_button.close_img
                        music_button.is_open = False
                        music_button.bg_music.stop()
                    else:
                        btn_img = music_button.open_img
                        music_button.is_open = True
                        music_button.bg_music.play(-1)

                if stop_Button.is_select():
                    if stop_Button.is_start:
                        stop_Button.is_start = False
                        current = False
                        run = False
                    else:
                        stop_Button.is_start = True
                        current = True
                        run = True

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN and event.key == K_SPACE:
                if marie.rect.y >= marie.lowest_y:
                    marie.jump_audio.play()
                    marie.jump()

        if run:
            if current:
                if over == False:
                    bg1.map_update()
                    bg1.map_rolling(-730)
                    bg2.map_update()
                    bg2.map_rolling(-730)

                    marie.move()
                    marie.draw_marie()

                    bullet = Bullet()
                    #bullet2 = Bullet()

                    tmp += 10
                    bullet.brect.x = tmp
                    bullet.brect.y = marie.rect.y+10


                    if tmp >= 800:
                        tmp = 100

                    pygame.display.update()
                    bullet.draw_Bullet()
                    #bullet2.draw_Bullet()


                    if addObstacleTimer >= 1300:
                        r = random.randint(0, 100)
                        if r > 40:
                            e1 = enemy()
                            list.append(e1)
                        addObstacleTimer = 0

                    for i in range(len(list)):
                        list[i].enemy_move()
                        list[i].draw_enemy()

                        if bullet.brect.colliderect(list[i].rect):
                            tmp = 100

                            list[i].rect.x = -10000
                            #score += 1
                            score += list[i].getScore()             

                        if pygame.sprite.collide_rect(marie,list[i]):
                            over = True
                            game_over()
                            music_button.bg_music.stop()
                            pygame.quit()
                            goon()

                        list[i].showScore(score,SCREENWIDTH,SCREENHEIGHT)

                    if score >= 50:
                        pygame.quit()
                        win()

                    addObstacleTimer += 100
                    SCREEN.blit(start_img,(60,20))
                    SCREEN.blit(btn_img, (20, 20))
                    pygame.display.update()
                    FPSCLOCK.tick(FPS)


def mainGame2():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    SCREENWIDTH = 822
    SCREENHEIGHT = 199
    score = 0
    runtmp = 50
    runstate = False
    over = False
    global SCREEN, FPSCLOCK
    pygame.init()

    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('玛丽冒险')


    bg1 = MyMap(0, 0,"image/bg.png")
    bg2 = MyMap(800, 0,"image/bg.png")


    marie = Marie4(140)
    rect = marie.mrect


    addObstacleTimer = 0
    list = []

    music_button = Music_Button()
    btn_img  = music_button.open_img
    music_button.bg_music.play(-1)

    stop_Button = Stop_Button()
    start_img = stop_Button.start_img

    run = True
    current = True

    while True:
            rect.x = runtmp
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONUP:
                    if music_button.is_select():
                        if music_button.is_open:
                            btn_img = music_button.close_img
                            music_button.is_open = False
                            music_button.bg_music.stop()
                        else:
                            btn_img = music_button.open_img
                            music_button.is_open = True
                            music_button.bg_music.play(-1)

                    if stop_Button.is_select():
                        if  stop_Button.is_start:
                            stop_Button.is_start = False
                            current = False
                            run = False
                        else :
                            stop_Button.is_start = True
                            current = True
                            run = True

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
               
                if event.type == KEYDOWN and event.key == K_z:
                    current = False
                    run = False
                if event.type == KEYDOWN and event.key == K_x:
                    run = True
                    current = True

                if event.type == KEYDOWN and event.key == K_d:
                        runtmp += 10



                if event.type == KEYDOWN and event.key == K_w:
                    if marie.mrect.y >= marie.lowest_y:
                        marie.jump_audio.play()
                        marie.jump()

                    if over == True:
                        mainGame()



            if run:
                if current:
                    if over == False:

                        bg1.map_update()
                        bg1.map_rolling(-790)
                        bg2.map_update()
                        bg2.map_rolling(-790)


                        marie.draw_marie()



                        if addObstacleTimer >= 1300:
                            r = random.randint(0, 100)
                            if r > 40:

                                obstacle = Obstacle()
                                list.append(obstacle)

                            addObstacleTimer = 0


                        for i in range(len(list)):

                            list[i].obstacle_move()
                            list[i].draw_obstacle()

                            if marie.mrect.colliderect(list[i]):
                                over = True
                                game_over()
                                music_button.bg_music.stop()
                                pygame.quit()
                                goon()
                            else:
                                if (list[i].rect.x + list[i].rect.width) < marie.mrect.x:
                                    # 加分
                                    score += list[i].getScore()

                            list[i].showScore(score, SCREENWIDTH, SCREENHEIGHT)
                            if score > 1:
                                pygame.quit()
                                hardGame()


                        addObstacleTimer += 20
                        SCREEN.blit(btn_img, (20, 20))
                        SCREEN.blit(start_img, (60, 20))
                        pygame.display.update()
                        FPSCLOCK.tick(FPS)  # 循环应该多长时间运行一次


if __name__ == '__main__':

    pygame.init()
    myfont = pygame.font.SysFont('comicsansms', 40)
    screen = pygame.display.set_mode((1002, 749))
    background = pygame.image.load("image/main.png")

    black = (0, 0, 0)
    textImage = myfont.render('press space start game', True, black)
    textImage2 = myfont.render('press t start 2player game',True,black)
    while True:
            screen.blit(background, (0, 0))
            screen.blit(textImage, (275, 420))
            screen.blit(textImage2,(250,500))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == KEYDOWN and event.key == K_SPACE:
                    pygame.quit()
                    mainGame()
                if event.type == KEYDOWN and event.key == K_t:
                    pygame.quit()
                    twopmainGame()
                if event.type == KEYDOWN and event.key == K_q:
                    pygame.quit()
                    hardGame()
