import pygame
from settings import *
from sprites import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    def new(self): #create new game
        self.board = Board()
        self.board.display_board()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.board.draw(self.screen)
        pygame.display.flip() 

    def events(self):
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit(0)

            if event.type==pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                mx //= TILESIZE
                my //= TILESIZE

                if event.button == 1:
                    if not self.board.board_list[mx][my].flagged:
                        #dig and check if exploded
                        if not self.board.dig(mx, my):  #dig first
                            #explode, is a mine if code reaches here
                            for row in self.board.board_list:
                                for tile in row:
                                    if tile.flagged and tile.type != "X":       #clicked on mine, if flagged tile isnt bomb, reveal 'not bomb image'
                                        tile.flagged = False
                                        tile.revealed = True
# =======
#                         if not self.board.dig(mx, my):
#                             #explode
#                             for row in self.board.board_list:
#                                 for tile in row:
#                                     if tile.flagged and tile.type != "X":
#                                         tile.flagged = False
#                                         tile.revealed = True
# >>>>>>> 786acdbc302bbcd1fd652882618a19be66d97c96
                                        tile.image = tile_not_mine


                if event.button == 3:
                    if not self.board.board_list[mx][my].revealed:  
                        self.board.board_list[mx][my].flagged = not self.board.board_list[mx][my].flagged
                



#starts Game
game = Game()

while True:
    game.new()
    game.run()
