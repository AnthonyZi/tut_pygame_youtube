from Game import Game
import pygame as pg


if __name__ == "__main__":
    g = Game()
    g.show_start_screen()

    while g.running:
        g.newGame()
        g.show_go_screen()
        g.run()

    pg.quit()
