import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        super().__init__(self.groups)

        self.game = game
        self.image = pg.Surface((TILESIZE,TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.vx = 0
        self.vy = 0
        self.step_counter = 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE

    def get_keys(self):
        if self.step_counter == 0:
            self.vx, self.vy = 0, 0
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                self.vx = -PLAYER_SPEED
            if keys[pg.K_RIGHT]:
                self.vx = +PLAYER_SPEED
            if keys[pg.K_UP]:
                self.vy = -PLAYER_SPEED
            if keys[pg.K_DOWN]:
                self.vy = +PLAYER_SPEED

            if self.vx != 0 and self.vy != 0:
                self.vx *= 0.7071067811865475
                self.vy *= 0.7071067811865475

            if self.vx != 0 or self.vy != 0:
                self.step_counter = PLAYER_STEPS_PER_TILE

    def collide_with_walls(self, direction):
        if direction == "x":
            if pg.sprite.spritecollideany(self, self.game.walls):
                self.x -= self.vx * TILESIZE / PLAYER_STEPS_PER_TILE
                self.rect.x = self.x
        if direction == "y":
            if pg.sprite.spritecollideany(self, self.game.walls):
                self.y -= self.vy * TILESIZE / PLAYER_STEPS_PER_TILE
                self.rect.y = self.y


    def move(self):
        self.get_keys()
        if self.step_counter > 0:
            self.x += self.vx * TILESIZE / PLAYER_STEPS_PER_TILE
            self.y += self.vy * TILESIZE / PLAYER_STEPS_PER_TILE

            self.step_counter -= 1

            if self.step_counter == 0:
                self.x = round(self.x/TILESIZE)*TILESIZE
                self.y = round(self.y/TILESIZE)*TILESIZE

        self.rect.x = self.x
        self.collide_with_walls("x")
        self.rect.y = self.y
        self.collide_with_walls("y")


    def update(self):
        self.move()

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        super().__init__(self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE,TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
