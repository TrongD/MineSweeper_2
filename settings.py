import pygame
import os

# colors rgb format
WHITE = (255, 255, 255)
BLACK =(0 , 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100,100, 100)
GREEN = (0, 255, 0)
DARKGREEN = (0, 200, 0)
BLUE = (0,0,255)
RED = (266,0,0)
YELLOW = (255,255, 0)
BGCOLOR = DARKGREY

#game settings
TILESIZE =32
ROWS =15
COLS =15
AMOUNT_MINES =5
WIDTH = TILESIZE*ROWS
HEIGHT = TILESIZE *COLS
FPS = 60
TITLE = "Minesweeper Game"

#add all the tiles in assets folder to a list
tile_numbers = []
for i in range(1,9):
    tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", f"Tile{i}.png")),(TILESIZE,TILESIZE)))

tile_empty = pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileEmpty.png")),(TILESIZE,TILESIZE))
tile_exploded = pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileExploded.png")),(TILESIZE,TILESIZE))
tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileFlag.png")),(TILESIZE,TILESIZE))
tile_mine = pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileMine.png")),(TILESIZE,TILESIZE))
tile_not_mine = pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileNotMine.png")),(TILESIZE,TILESIZE))
tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileUnknown.png")),(TILESIZE,TILESIZE))