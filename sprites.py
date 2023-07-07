import pygame
from settings import *
import random

#types list:
# "." = uknown
# "X" = mine
# "C" = clue
# "/" = empty

class Tile:
    def __init__(self, x, y, image, type, revealed=False, flagged=False):
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.image =image
        self.type = type
        self.revealed = revealed
        self.flagged = flagged

    def draw(self, board_surface):
        board_surface.blit(self.image, (self.x, self.y))

    def __repr__(self):
        return self.type

class Board:
    def __init__(self):
        self.board_surface = pygame.Surface((WIDTH, HEIGHT))
        self.board_list =[[Tile(col, row, tile_empty, ".") for row in range(ROWS)] for col in range (COLS)]
        self.place_mines()

    #place landmines
    def place_mines(self):
        for i in range (AMOUNT_MINES):
            while True:
                x = random.randint(0, ROWS-1)
                y = random.randint(0, COLS-1)

                if self.board_list[x][y].type == ".":
                    self.board_list[x][y].image = tile_mine
                    self.board_list[x][y] = "X"
                    break

    def place_clues(self):
        pass

    @staticmethod
    def is_inside_board(x,y):
        return 0<= x < ROWS and 0 <= y < COLS


    def check_neighbors(self, x, y):
        total_mines = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                pass

    def draw(self, screen):
        for row in self.board_list:
            for tile in row:
                tile.draw(self.board_surface)
        screen.blit(self.board_surface, (0,0))

    def display_board(self):
        for row in self.board_list:
            print(row)


