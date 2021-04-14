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
    # returns if the current positionis a valid space
    pass


def check_lost(positions):
    pass

def get_shape():
    return Piece(5, 0, random.choice(shapes))


def draw_text_middle(text, size, color, surface):
    pass

def draw_grid(surface,grid, row, col):
    # draw lines for grid
    sx = top_left_x
    sy = top_left_y
    for i in range(len(grid)):
        pygame.draw.line(surface, (128,128,128), (sx, sy+i*block_size),(sx+play_width, sy+ i*block_size))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128), (sx+ j * block_size, sy) ,(sx + j * block_size, sy+play_height))


def clear_rows(grid, locked):
    pass

def draw_next_shape(shape, surface):
    pass

def draw_window(surface, grid):
    surface.fill((0 , 0 , 0))
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 60)
    label = font.render("Tetris", 1, (255, 255, 255))
    surface.blit(label, (top_left_x + play_width/2- (label.get_width()/2), 30))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size,block_size),0)
    pygame.draw.rect(surface, (255,0 ,0 ), (top_left_x,top_left_y,play_width,play_height), 4)
    draw_grid(surface,grid)
    pygame.display.update()

def main(win):
    # set up variables
    locked_positions ={}
    grid = create_grid(locked_positions)
    change_piece = False
    run = True
    currrent_piece = get_shape()
    next_piece = get_shape()
    #clock object
    clock = pygame.time.Clock()
    fall_time = 0
#     main game loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                # all the different keys
                if event.key == pygame.K_LEFT:
                    #move block left  change x val left
                    currrent_piece.x -= 1
                    if not(valid_space(currrent_piece,grid)):
                        currrent_piece += 1
                if event.key == pygame.K_RIGHT:
                    currrent_piece.x += 1
                    if not(valid_space(currrent_piece,grid)):
                        currrent_piece -=1
                if event.key == pygame.K_DOWN:
                    currrent_piece.y += 1
                    if not(valid_space(currrent_piece,grid)):
                        currrent_piece.y -=1
                if event.key == pygame.K_UP:
                    # rotate block
                    currrent_piece.rotation += 1
                    if not(valid_space(currrent_piece,grid)):
                        currrent_piece.rotation -=1
        draw_window(win, grid)





def main_menu(win):
    main(win)


#draw game surface
win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Tetris")
main_menu(win)  # start game