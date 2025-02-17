import pygame
import os
import sys
import sqlite3
pygame.font.init()

con = sqlite3.connect('wins1.db')
cur = con.cursor()
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Tank(pygame.sprite.Sprite):
    image1 = load_image('tank_team1.png')
    imaged = load_image('tank_team1d.png')
    images = load_image('tank_team1s.png')
    imagea = load_image('tank_team1a.png')
    image2 = load_image('tank_team2.png')
    image2d = load_image('tank_team2d.png')
    image2s = load_image('tank_team2s.png')
    image2a = load_image('tank_team2a.png')
    explosion = load_image('explosion.jpeg')
    explosion2 = load_image('explosion_real.jpg')
    explosion3 = load_image('exp.jpg')
    image1 = pygame.transform.scale(image1, (100, 100))
    imaged = pygame.transform.scale(imaged, (100, 100))
    images = pygame.transform.scale(images, (100, 100))
    imagea = pygame.transform.scale(imagea, (100, 100))
    image2 = pygame.transform.scale(image2, (100, 100))
    image2a = pygame.transform.scale(image2a, (100, 100))
    image2s = pygame.transform.scale(image2s, (100, 100))
    image2d = pygame.transform.scale(image2d, (100, 100))
    explosion = pygame.transform.scale(explosion, (100, 100))
    explosion3 = pygame.transform.scale(explosion3, (250, 150))

    def __init__(self, group, k):
        super().__init__(group)
        if k == 1:
            self.image = Tank.image1
            self.rect = self.image.get_rect()
            self.rect.x = 850
            self.rect.y = 900
        else:
            self.image = Tank.image2s
            self.rect = self.image.get_rect()
            self.rect.x = 850
            self.rect.y = 0

    def update(self, s, k):
        if s == 1:
            if k == 1:
                self.image = Tank.image1
                self.rect = self.rect.move(0, -50)
            elif k == 2:
                self.image = Tank.images
                self.rect = self.rect.move(0, 50)
            elif k == 3:
                self.image = Tank.imagea
                self.rect = self.rect.move(-50, 0)
            elif k == 4:
                self.image = Tank.imaged
                self.rect = self.rect.move(50, 0)
        if s == 2:
            if k == 5:
                self.image = Tank.image2
                self.rect = self.rect.move(0, -50)
            elif k == 6:
                self.image = Tank.image2s
                self.rect = self.rect.move(0, 50)
            elif k == 7:
                self.image = Tank.image2d
                self.rect = self.rect.move(50, 0)
            elif k == 8:
                self.image = Tank.image2a
                self.rect = self.rect.move(-50, 0)

    def is_collide(self):
        self.image = Tank.explosion3

class Tank_Shell(pygame.sprite.Sprite):
    shell = load_image('TankShell1.png')
    shells = load_image('TankShells.png')
    shella = load_image('TankShella.png')
    shelld = load_image('TankShelld.png')
    shell = pygame.transform.scale(shell, (15, 25))
    shells = pygame.transform.scale(shells, (15, 25))
    shella = pygame.transform.scale(shella, (25, 15))
    shelld = pygame.transform.scale(shelld, (25, 15))

    def __init__(self, group, x, y, k):
        super().__init__(group)
        self.image = Tank_Shell.shell
        self.rect = self.image.get_rect()
        self.k = k
        if self.k == 'w':
            self.rect.x = x + 44
            self.rect.y = y - 40
        elif self.k == 's':
            self.rect.x = x + 44
            self.rect.y = y + 100
        elif self.k == 'a':
            self.rect.x = x - 47
            self.rect.y = y + 42
        elif self.k == 'd':
            self.rect.x = x + 120
            self.rect.y = y + 42
        elif self.k == 'up':
            self.rect.x = x + 44
            self.rect.y = y - 40
        elif self.k == 'down':
            self.rect.x = x + 44
            self.rect.y = y + 100
        elif self.k == 'right':
            self.rect.x = x + 120
            self.rect.y = y + 42
        elif self.k == 'left':
            self.rect.x = x - 47
            self.rect.y = y + 42

    def update(self):
        if self.k == 'w':
            self.image = Tank_Shell.shell
            self.rect = self.rect.move(0, -4)
        if self.k == 's':
            self.image = Tank_Shell.shells
            self.rect = self.rect.move(0, 4)
        if self.k == 'a':
            self.image = Tank_Shell.shella
            self.rect = self.rect.move(-4, 0)
        if self.k == 'd':
            self.image = Tank_Shell.shelld
            self.rect = self.rect.move(4, 0)
        if self.k == 'up':
            self.image = Tank_Shell.shell
            self.rect = self.rect.move(0, -4)
        if self.k == 'down':
            self.image = Tank_Shell.shells
            self.rect = self.rect.move(0, 4)
        if self.k == 'left':
            self.image = Tank_Shell.shella
            self.rect = self.rect.move(-4, 0)
        if self.k == 'right':
            self.image = Tank_Shell.shelld
            self.rect = self.rect.move(4, 0)


class Tiles(pygame.sprite.Sprite):
    tile = load_image('plitka.jpeg')
    tile = pygame.transform.scale(tile, (50, 50))

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Tiles.tile
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Kirpichi(pygame.sprite.Sprite):
    kirpich = load_image('kirpich_stena.png')
    kirpich = pygame.transform.scale(kirpich, (50, 50))

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Kirpichi.kirpich
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Bushes(pygame.sprite.Sprite):
    bush = load_image('bush.png')
    bush = pygame.transform.scale(bush, (50, 50))

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Bushes.bush
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Start_Screen(pygame.sprite.Sprite):
    start = load_image('zastavka.jpeg')
    start = pygame.transform.scale(start, (1800, 1000))

    def __init__(self, group):
        super().__init__(group)
        self.image = Start_Screen.start
        self.rect = self.image.get_rect()

size = width, height = 1800, 1000
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
running = True
key = ''
key1 = ''
flag1 = False

all_sprites2 = pygame.sprite.Group()

all_tiles = pygame.sprite.Group()
Tiles(all_tiles, 0, 0)
Tiles(all_tiles, 100, 50)
Tiles(all_tiles, 0, 950)
Tiles(all_tiles, 250, 500)
Tiles(all_tiles, 300, 450)
Tiles(all_tiles, 800, 550)
Tiles(all_tiles, 1000, 450)
Tiles(all_tiles, 900, 600)
Tiles(all_tiles, 1200, 500)
Tiles(all_tiles, 1250, 550)
Tiles(all_tiles, 1750, 0)
Tiles(all_tiles, 1750, 950)
#
Tiles(all_tiles, 1000, 800)
Tiles(all_tiles, 750, 800)
#
Tiles(all_tiles, 1000, 150)
Tiles(all_tiles, 750, 150)

all_kirpichi = pygame.sprite.Group()
Kirpichi(all_kirpichi, 0, 900)
Kirpichi(all_kirpichi, 50, 950)
Kirpichi(all_kirpichi, 400, 500)
Kirpichi(all_kirpichi, 350, 500)
Kirpichi(all_kirpichi, 550, 500)
Kirpichi(all_kirpichi, 500, 500)
Kirpichi(all_kirpichi, 300, 500)
Kirpichi(all_kirpichi, 300, 550)
Kirpichi(all_kirpichi, 550, 550)
Kirpichi(all_kirpichi, 850, 600)
Kirpichi(all_kirpichi, 900, 450)
#
Kirpichi(all_kirpichi, 1400, 500)
Kirpichi(all_kirpichi, 1300, 500)
Kirpichi(all_kirpichi, 1250, 500)
Kirpichi(all_kirpichi, 1350, 500)
Kirpichi(all_kirpichi, 1450, 500)
Kirpichi(all_kirpichi, 1500, 500)
Kirpichi(all_kirpichi, 1250, 450)
Kirpichi(all_kirpichi, 1500, 450)
#
Kirpichi(all_kirpichi, 850, 800)
Kirpichi(all_kirpichi, 900, 800)
Kirpichi(all_kirpichi, 800, 800)
Kirpichi(all_kirpichi, 950, 800)
Kirpichi(all_kirpichi, 1000, 850)
Kirpichi(all_kirpichi, 750, 850)
#
Kirpichi(all_kirpichi, 850, 150)
Kirpichi(all_kirpichi, 900, 150)
Kirpichi(all_kirpichi, 800, 150)
Kirpichi(all_kirpichi, 950, 150)
Kirpichi(all_kirpichi, 1000, 100)
Kirpichi(all_kirpichi, 750, 100)


all_bushes = pygame.sprite.Group()
Bushes(all_bushes, 50, 50)
Bushes(all_bushes, 50, 0)
Bushes(all_bushes, 0, 50)
Bushes(all_bushes, 100, 0)
Bushes(all_bushes, 0, 150)
Bushes(all_bushes, 0, 100)
Bushes(all_bushes, 50, 100)
Bushes(all_bushes, 1000, 500)
Bushes(all_bushes, 1000, 550)
Bushes(all_bushes, 950, 550)
Bushes(all_bushes, 950, 500)
Bushes(all_bushes, 950, 600)
Bushes(all_bushes, 950, 450)
Bushes(all_bushes, 800, 500)
Bushes(all_bushes, 850, 500)
Bushes(all_bushes, 900, 500)
Bushes(all_bushes, 900, 550)
Bushes(all_bushes, 850, 550)
Bushes(all_bushes, 1450, 550)
Bushes(all_bushes, 1500, 550)
Bushes(all_bushes, 1550, 500)
Bushes(all_bushes, 1700, 950)
Bushes(all_bushes, 1650, 950)
Bushes(all_bushes, 1750, 900)
Bushes(all_bushes, 1700, 900)
Bushes(all_bushes, 1750, 850)
for i in range(200, 900, 50):
    Bushes(all_bushes, -50, i)
for i in range(50, 950, 50):
    Bushes(all_bushes, 1800, i)
for i in range(150, 1800, 50):
    Bushes(all_bushes, i, -50)
for i in range(150, 1800, 50):
    Bushes(all_bushes, i, 1000)

starting_screen = pygame.sprite.Group()
Start_Screen(starting_screen)

flag = False
win_loss = False
flag2 = True
start_ticks = pygame.time.get_ticks()
pygame.font.init()
while running:
    if flag2:
        all_sprites = pygame.sprite.Group()
        all_sprites1 = pygame.sprite.Group()
        Tank(all_sprites, 1)
        Tank(all_sprites1, 2)
        flag2 = False
    if flag and not win_loss:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                collide_tiles_tank1 = pygame.sprite.groupcollide(all_sprites, all_tiles, False, False)
                collide_kirpichi_tank1 = pygame.sprite.groupcollide(all_sprites, all_kirpichi, False, False)
                collide_bushes_tank1 = pygame.sprite.groupcollide(all_sprites, all_bushes, False, False)
                collide_tiles_tank2 = pygame.sprite.groupcollide(all_sprites1, all_tiles, False, False)
                collide_kirpichi_tank2 = pygame.sprite.groupcollide(all_sprites1, all_kirpichi, False, False)
                collide_bushes_tank2 = pygame.sprite.groupcollide(all_sprites1, all_bushes, False, False)
                collide_tanks = pygame.sprite.groupcollide(all_sprites, all_sprites1, False, False)
                if not collide_tiles_tank1 and not collide_kirpichi_tank1 and not collide_bushes_tank1 and not collide_tanks:
                    if event.key == pygame.K_w:
                        for tank in all_sprites:
                            tank.update(1, 1)
                            key = 'w'
                    elif event.key == pygame.K_s:
                        for tank in all_sprites:
                            tank.update(1, 2)
                            key = 's'
                    elif event.key == pygame.K_a:
                        for tank in all_sprites:
                            tank.update(1, 3)
                            key = 'a'
                    elif event.key == pygame.K_d:
                        for tank in all_sprites:
                            tank.update(1, 4)
                            key = 'd'
                else:
                    if key == 'w':
                        if event.key == pygame.K_s:
                            for tank in all_sprites:
                                tank.update(1, 2)
                                key = 's'
                                collide_tiles_tank1 = False
                                collide_kirpichi_tank1 = False
                                collide_bushes_tank1 = False
                                print(1111)
                        elif event.key == pygame.K_a:
                            for tank in all_sprites:
                                tank.update(1, 3)
                                key = 'a'
                                collide_tiles_tank1 = False
                                collide_kirpichi_tank1 = False
                                collide_bushes_tank1 = False
                        elif event.key == pygame.K_d:
                            for tank in all_sprites:
                                tank.update(1, 4)
                                key = 'd'
                                collide_tiles_tank1 = False
                                collide_kirpichi_tank1 = False
                                collide_bushes_tank1 = False
                    if key == 's':
                        if event.key == pygame.K_a:
                            for tank in all_sprites:
                                tank.update(1, 3)
                                key = 'a'
                                collide_tiles_tank1 = False
                                collide_kirpichi_tank1 = False
                                collide_bushes_tank1 = False
                        elif event.key == pygame.K_d:
                            for tank in all_sprites:
                                tank.update(1, 4)
                                key = 'd'
                                collide_tiles_tank1 = False
                                collide_kirpichi_tank1 = False
                                collide_bushes_tank1 = False
                        elif event.key == pygame.K_w:
                            for tank in all_sprites:
                                tank.update(1, 1)
                                key = 'w'
                                collide_tiles_tank1 = False
                                collide_kirpichi_tank1 = False
                                collide_bushes_tank1 = False
                    if key == 'a':
                        if event.key == pygame.K_d:
                            for tank in all_sprites:
                                tank.update(1, 4)
                                key = 'd'
                                collide_tiles_tank1 = False
                                collide_kirpichi_tank1 = False
                                collide_bushes_tank1 = False
                        elif event.key == pygame.K_w:
                            for tank in all_sprites:
                                tank.update(1, 1)
                                key = 'w'
                                collide_tiles_tank1 = False
                                collide_kirpichi_tank1 = False
                                collide_bushes_tank1 = False
                        elif event.key == pygame.K_s:
                            for tank in all_sprites:
                                tank.update(1, 2)
                                key = 's'
                                collide_tiles_tank1 = False
                                collide_kirpichi_tank1 = False
                                collide_bushes_tank1 = False
                    if key == 'd':
                        if event.key == pygame.K_w:
                            for tank in all_sprites:
                                tank.update(1, 1)
                                key = 'w'
                                collide_tiles_tank1 = False
                                collide_kirpichi_tank1 = False
                                collide_bushes_tank1 = False
                        elif event.key == pygame.K_s:
                            for tank in all_sprites:
                                tank.update(1, 2)
                                key = 's'
                                collide_tiles_tank1 = False
                                collide_kirpichi_tank1 = False
                                collide_bushes_tank1 = False
                        elif event.key == pygame.K_a:
                            for tank in all_sprites:
                                tank.update(1, 3)
                                key = 'a'
                                collide_tiles_tank1 = False
                                collide_kirpichi_tank1 = False
                                collide_bushes_tank1 = False
                if not collide_tiles_tank2 and not collide_kirpichi_tank2 and not collide_bushes_tank2 and not collide_tanks:
                    if event.key == pygame.K_UP:
                        for tank in all_sprites1:
                            tank.update(2, 5)
                            key1 = 'up'
                    elif event.key == pygame.K_DOWN:
                        for tank in all_sprites1:
                            tank.update(2, 6)
                            key1 = 'down'
                    elif event.key == pygame.K_RIGHT:
                        for tank in all_sprites1:
                            tank.update(2, 7)
                            key1 = 'right'
                    elif event.key == pygame.K_LEFT:
                        for tank in all_sprites1:
                            tank.update(2, 8)
                            key1 = 'left'
                    elif event.key == pygame.K_e:
                        x, y = (0, 0)
                        for i in all_sprites:
                            x, y = i.rect.x, i.rect.y
                        Tank_Shell(all_sprites2, x, y, key)
                    elif event.key == pygame.K_RETURN:
                        x, y = (0, 0)
                        for i in all_sprites1:
                            x, y = i.rect.x, i.rect.y
                        Tank_Shell(all_sprites2, x, y, key1)
                else:
                    if key1 == 'up':
                        if event.key == pygame.K_DOWN:
                            for tank in all_sprites1:
                                tank.update(2, 6)
                                key1 = 'down'
                                collide_tiles_tank2 = False
                                collide_kirpichi_tank2 = False
                                collide_bushes_tank2 = False
                        elif event.key == pygame.K_RIGHT:
                            for tank in all_sprites1:
                                tank.update(2, 7)
                                key1 = 'right'
                                collide_tiles_tank2 = False
                                collide_kirpichi_tank2 = False
                                collide_bushes_tank2 = False
                        elif event.key == pygame.K_LEFT:
                            for tank in all_sprites1:
                                tank.update(2, 8)
                                key1 = 'left'
                                collide_tiles_tank2 = False
                                collide_kirpichi_tank2 = False
                                collide_bushes_tank2 = False
                    if key1 == 'down':
                        if event.key == pygame.K_UP:
                            for tank in all_sprites1:
                                tank.update(2, 5)
                                key1 = 'up'
                                collide_tiles_tank2 = False
                                collide_kirpichi_tank2 = False
                                collide_bushes_tank2 = False
                        elif event.key == pygame.K_RIGHT:
                            for tank in all_sprites1:
                                tank.update(2, 7)
                                key1 = 'right'
                                collide_tiles_tank2 = False
                                collide_kirpichi_tank2 = False
                                collide_bushes_tank2 = False
                        elif event.key == pygame.K_LEFT:
                            for tank in all_sprites1:
                                tank.update(2, 8)
                                key1 = 'left'
                                collide_tiles_tank2 = False
                                collide_kirpichi_tank2 = False
                                collide_bushes_tank2 = False
                    if key1 == 'right':
                        if event.key == pygame.K_UP:
                            for tank in all_sprites1:
                                tank.update(2, 5)
                                key1 = 'up'
                                collide_tiles_tank2 = False
                                collide_kirpichi_tank2 = False
                                collide_bushes_tank2 = False
                        elif event.key == pygame.K_DOWN:
                            for tank in all_sprites1:
                                tank.update(2, 6)
                                key1 = 'down'
                                collide_tiles_tank2 = False
                                collide_kirpichi_tank2 = False
                                collide_bushes_tank2 = False
                        elif event.key == pygame.K_LEFT:
                            for tank in all_sprites1:
                                tank.update(2, 8)
                                key1 = 'left'
                                collide_tiles_tank2 = False
                                collide_kirpichi_tank2 = False
                                collide_bushes_tank2 = False
                    if key1 == 'left':
                        if event.key == pygame.K_UP:
                            for tank in all_sprites1:
                                tank.update(2, 5)
                                key1 = 'up'
                                collide_tiles_tank2 = False
                                collide_kirpichi_tank2 = False
                                collide_bushes_tank2 = False
                        elif event.key == pygame.K_DOWN:
                            for tank in all_sprites1:
                                tank.update(2, 6)
                                key1 = 'down'
                                collide_tiles_tank2 = False
                                collide_kirpichi_tank2 = False
                                collide_bushes_tank2 = False
                        elif event.key == pygame.K_RIGHT:
                            for tank in all_sprites1:
                                tank.update(2, 7)
                                key1 = 'right'
                                collide_tiles_tank2 = False
                                collide_kirpichi_tank2 = False
                                collide_bushes_tank2 = False
        screen.fill((0, 0, 0))
        for tankshell in all_sprites2:
            tankshell.update()
        collide_tanks1 = pygame.sprite.groupcollide(all_sprites, all_sprites2, False, True)
        collide_tanks2 = pygame.sprite.groupcollide(all_sprites1, all_sprites2, False, True)
        collide_kircpichi_shells = pygame.sprite.groupcollide(all_sprites2, all_kirpichi, True, False)
        collide_bushes_shells = pygame.sprite.groupcollide(all_sprites2, all_bushes, True, False)
        collide_tiles_shells = pygame.sprite.groupcollide(all_sprites2, all_tiles, True, False)
        if collide_tanks1:
            for i in all_sprites:
                i.is_collide()
                font = pygame.font.SysFont(None, 50)
                texsurf = font.render('PLAYER 1 WON THE GAME', False, (255, 255, 255))
                screen.blit(texsurf, (680, 50))
                wins2 = cur.execute("SELECT Player2 from W").fetchone()
                wins1 = cur.execute("SELECT Player1 from W").fetchone()
                print(wins2[0])
                #cur.execute("""INSERT INTO W(PLAYER2) VALUES('{}')""".format(wins2[0] + 1))
                #cur.execute("""INSERT INTO W(PLAYER1) VALUES('{}')""".format(wins1[0] + 0))
                cur.execute("""UPDATE W SET PLAYER1 = '{}' WHERE PLAYER1 = '{}'""".format(int(wins1[0]) + 1, wins1[0]))
                con.commit()
                win_loss = True
        if collide_tanks2:
            for i in all_sprites1:
                i.is_collide()
                font = pygame.font.SysFont(None, 50)
                texsurf = font.render('PLAYER 2 WON THE GAME', False, (255, 255, 255))
                screen.blit(texsurf, (680, 50))
                wins1 = cur.execute("SELECT Player1 from W").fetchone()
                wins2 = cur.execute("SELECT Player2 from W").fetchone()
                #cur.execute("""INSERT INTO W(PLAYER1) VALUES('{}')""".format(wins1[0] + 1))
                #cur.execute("""INSERT INTO W(PLAYER2) VALUES('{}')""".format(wins2[0] + 0))
                cur.execute("""UPDATE W SET PLAYER2 = '{}' WHERE PLAYER2 = '{}'""".format(int(wins2[0]) + 1, wins2[0]))
                con.commit()
                win_loss = True
        all_sprites.draw(screen)
        all_sprites1.draw(screen)
        all_sprites2.draw(screen)
        all_tiles.draw(screen)
        all_kirpichi.draw(screen)
        all_bushes.draw(screen)
        pygame.display.flip()
        #
    elif not flag:
        screen.fill((0, 0, 0))
        starting_screen.draw(screen)
        #
        rectangle1 = pygame.draw.rect(screen, (255, 255, 255), (750, 450, 300, 100))
        my_font = pygame.font.SysFont(None, 50)
        text_surface = my_font.render('ИГРАТЬ', False, (0, 0, 0))
        screen.blit(text_surface, (830, 485))
        #
        rectangle78 = pygame.draw.rect(screen, (255, 255, 255), (725, 600, 350, 100))
        my_font = pygame.font.SysFont(None, 50)
        text_surface = my_font.render('ВЫЙТИ ИЗ ИГРЫ', False, (0, 0, 0))
        screen.blit(text_surface, (755, 635))
        #
        my_font = pygame.font.SysFont(None, 100)
        text_surface = my_font.render('ТАНКИ', False, (0, 0, 0))
        screen.blit(text_surface, (770, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if rectangle1.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONUP:
                    flag = True
            if rectangle78.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONUP:
                    running = False
        pygame.display.flip()
    elif win_loss:
        rectangle2 = pygame.draw.rect(screen, (255, 255, 255), (650, 450, 500, 100))
        rectangle3 = pygame.draw.rect(screen, (255, 255, 255), (650, 580, 500, 100))
        rectangle4 = pygame.draw.rect(screen, (0, 0, 0), (500, 300, 350, 100))
        rectangle5 = pygame.draw.rect(screen, (0, 0, 0), (900, 300, 350, 100))
        my_font1 = pygame.font.SysFont(None, 50)
        text_surface1 = my_font1.render('ИГРАТЬ ЕЩЕ РАЗ', False, (0, 0, 0))
        text_surface2 = my_font1.render('ВЫЙТИ В ГЛАВНОЕ МЕНЮ', False, (0, 0, 0))
        screen.blit(text_surface1, (750, 485))
        screen.blit(text_surface2, (670, 615))
        font78 = pygame.font.SysFont(None, 50)
        texsurf78 = font78.render('PLAYER 1 WINS:', False, (255, 255, 255))
        screen.blit(texsurf78, (570, 300))

        texsurf56 = font78.render('PLAYER 2 WINS:', False, (255, 255, 255))
        screen.blit(texsurf56, (1000, 300))
        wins1 = cur.execute("SELECT Player1 from W").fetchone()
        wins2 = cur.execute("SELECT Player2 from W").fetchone()
        texsurf1 = font78.render(str(wins1[0]), False, (255, 255, 255))
        texsurf2 = font78.render(str(wins2[0]), False, (255, 255, 255))
        screen.blit(texsurf1, (700, 350))
        screen.blit(texsurf2, (1150, 350))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if rectangle2.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONUP:
                    flag = True
                    win_loss = False
                    flag2 = True
            if rectangle3.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONUP:
                    flag = False
                    win_loss = False
                    flag2 = True
        pygame.display.flip()