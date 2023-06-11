import sys
import pygame
import numpy as np


from constants import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(BG_COLOR)

class Board:
    def __init__(self):
        self.squares = np.zeros( (ROWS,COLS) )
        self.empty_sqrs = self.squares
        # self.marked_sqrs = 0


    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        # self.mark_sqr += 1


    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0
    
    def get_empty_sqrs(self):
        empty_sqrs = []
        pass


    def isfull(self):
        self.marked_sqrs == 9

    def isempty(self):
        self.marked_sqrs == 0


class Game:
    def __init__(self):
        self.show_lines()
        self.board = Board()
        self.player = 1

    def show_lines(self):
        #VERTICAL LINES
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE,0), (SQSIZE,HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH-SQSIZE,0), (WIDTH-SQSIZE,HEIGHT), LINE_WIDTH)

        #HORIZONTAL
        pygame.draw.line(screen, LINE_COLOR, (0,SQSIZE), (WIDTH,SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0,HEIGHT-SQSIZE), (600,HEIGHT-SQSIZE), LINE_WIDTH)

    def next_turn(self):
        self.player = self.player % 2 + 1
        #Player 1 -> X
        #Player 2 -> O


    def draw_fig(self, row, col):
        if self.player == 1:
            # draw cross
            # desc line
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
            # asc line
            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
        
        elif self.player == 2:
            # draw circle
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)


    def make_move(self, row, col):
        self.board.mark_sqr(row, col, self.player)
        self.draw_fig(row, col)
        self.next_turn()


def main():
        
    #object
    game = Game()
    board = game.board


    while True:

        # pygame events
        for event in pygame.event.get():

            # quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE

                if board.empty_sqr(row, col):
                    board.mark_sqr(row, col, game.player)
                    print(board.squares)
                    game.make_move(row, col)
                    


        pygame.display.update()


main()