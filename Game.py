import pygame as pg
import random
import os

from settings import *
from Sprites import *
from TileMap import *

class Game:
    def __init__(self):

        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500,100)
        self.load_data()

        self.running = True

    def load_data(self):
        game_folder = os.path.dirname(__file__)
        self.map = TileMap(os.path.join(game_folder,"map.txt"))

    def newGame(self):
        self.all_sprites    = pg.sprite.Group()
        self.walls          = pg.sprite.Group()

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == "W":
                    Wall(self, col, row)
                if tile == "P":
                    self.player = Player(self, col, row)

        self.camera = Camera(self.map.width*TILESIZE, self.map.height*TILESIZE)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, GRAY, (x,0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, GRAY, (0,y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
#        self.draw_grid()
#        self.all_sprites.draw(self.screen)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

    def quit(self):
        if self.playing:
            self.playing = False
        self.running = False

