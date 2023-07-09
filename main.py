import pygame
from settings import *
from sprites import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    def new(self): #create new game
        self.board =Board()
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

#starts Game
game = Game()

while True:
    game.new()
    game.run()