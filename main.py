import pygame
import random

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()

# GLOBALS VARS
# set up screen height and width
s_width = 800
s_height = 700
# the actual playing area
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

# SHAPE FORMATS - this represents the shapes in tetrus
# lists in lists to represent the different rotations of each shapes in tetrus
# 5 x 5 grid of periods, the 00 represent where the block actually is
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]
# list that holds shapes for easy access to shapes and shape_colors, doing this in lue of dictionaries
shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]


# index 0 - 6 represent shape

# the main data structure for game, this class will represent the x,y width ,height piece
class Piece(object):
    def __init__(self,x,y,shape):
        self.x =x
        self.y =y
        self.shape = shape
        self.colors = shape_colors[shapes.index(shape)]
        self.rotation = 0

def create_grid(locked_pos={}):
    grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(j, i) in locked_pos:
                c = locked_pos[(j, i)]
                grid[i][j] = c
    return grid

def convert_shape_format(shape):
    pass


def valid_space(shape, grid):
    pass


def check_lost(positions):
    pass

def get_shape():
    return random.choice(shapes)


def draw_text_middle(text, size, color, surface):
    pass

# we are going to be passed a surface
def draw_grid(surface,grid, row, col):
    # draw grid objects onto screen
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # loop through every color in grid - grid[i][j] draw on surface on at what position, and fill
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size,block_size),0)
    #draw red rectancle the represents play area
    pygame.draw.rect(surface, (255,0 ,0 ), (top_left_x,top_left_y,play_width,play_height), 4)

def clear_rows(grid, locked):
    pass

def draw_next_shape(shape, surface):
    pass

def draw_window(surface, grid):
    #fill surface with black
    surface.fill((0 , 0 , 0))
    # draw a title init font object in pygame
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 60)
    # color white
    label = font.render("Tetris", 1, (255, 255, 255))
    # draw label on the screen, in the middle
    surface.blit(label, (top_left_x + play_width/2- (label.get_width()/2), 30))
    # call draw grid function
    draw_grid(surface,grid)
    #update screen
    pygame.display.update()

def main():
    pass


def main_menu():
    pass


main_menu()  # start game