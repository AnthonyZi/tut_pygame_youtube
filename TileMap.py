import pygame as pg
from settings import *

class TileMap(object):
    def __init__(self, mapfile):

        self.properties = dict()
        self.data = []

        with open(mapfile, "r") as mapf:
            mapfilelines = mapf.readlines()

        self.width = 0
        for line in mapfilelines:
            line = line.strip("\n\r")
            if not line.startswith("#"):
                self.data.append(line)
                self.width = max(self.width,len(line))
            else:
                prop_key,prop = line.strip("# \n\r").split("=")
                self.properties[prop_key] = prop

        self.height = len(self.data)


class Camera(object):
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH /2)
        y = -target.rect.y + int(HEIGHT / 2)
        self.camera = pg.Rect(x, y, self.width, self.height)
