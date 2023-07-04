import pygame
from settings import *

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

    def place_mines(self):
        for i in range (AMOUNT_MINES):
            while True:
                


    def draw(self, screen):
        for row in self.board_list:
            for tile in row:
                tile.draw(self.board_surface)
        screen.blit(self.board_surface, (0,0))

    def display_board(self):
        for row in self.board_list:
            print(row)


