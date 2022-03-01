import pygame
import time
from pygame.locals import *
import numpy as np
SQUARE_SIZE=200
CROSS_COLOR=(241, 239, 246)
SPACE=55
CROSS_WIDTH=25
def draw_shapes():
    for row in range(3) :
        for col in range(3) :
            if playing_screen[row][col] == 1 :
                pygame.draw.circle(playscreen,(241, 239, 246),(int(col * 200 + 100),int (row*200+100)),60,15)
            elif playing_screen[row][col] == 2 :
                pygame.draw.line(playscreen, (241, 239, 246), (col * SQUARE_SIZE + 55, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(playscreen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)

def mark_square (row , coloum , player) :
        playing_screen[row][coloum] = player

def empty_square (row , coloum):
    if playing_screen[row][coloum]==0 :
        return True
    else:
        return False

def board_is_full () :
    for x in range(3) :
        for y in range (3) :
         if playing_screen[x][y]==0 :
             return False

    return True
CIRCLE_COLOR =(241, 239, 246)
WIDTH=600
HEIGHT = 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
SQUARE_SIZE = 200
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)


def draw_vertical_winning_line(col, player):
	posX = col * SQUARE_SIZE + SQUARE_SIZE//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( playscreen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH )

def draw_horizontal_winning_line(row, player):
	posY = row * SQUARE_SIZE + SQUARE_SIZE//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( playscreen, color, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH )



def draw_asc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( playscreen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH )

def draw_desc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( playscreen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH )
def check(player):
    for col in range(3) :
        if playing_screen[0][col]==playing_screen[1][col] and playing_screen[0][col]==playing_screen[2][col] and playing_screen[0][col] !=0 :
            draw_vertical_winning_line(col,player)

            return True
    for row in range(3) :
        if playing_screen[row][0]==playing_screen[row][1] and playing_screen[row][0]==playing_screen[row][2] and playing_screen[row][0] !=0  :
            draw_horizontal_winning_line(row,player)
            return True
    if playing_screen[2][0] == player and playing_screen[1][1] == player and playing_screen[0][2] == player and playing_screen[0][2] !=0 :
        draw_asc_diagonal(player)

        return True

        # desc diagonal win chek
    if playing_screen[0][0] == player and playing_screen[1][1] == player and playing_screen[2][2] == player and playing_screen[2][2] !=0 :
        draw_desc_diagonal(player)
        return True

    return False


    return
def printt():
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    # assigning values to X and Y variable
    X = 400
    Y = 400

    # create the display surface object
    # of specific dimension..e(X, Y).
    display_surface = pygame.display.set_mode((X, Y))

    # set the pygame window name
    pygame.display.set_caption('Show Text')

    # create a font object.
    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    font = pygame.font.Font('freesansbold.ttf', 32)

    # create a text surface object,
    # on which text is drawn on it.
    text = font.render('player 1  won', True, green, blue)

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (X // 2, Y // 2)

    # infinite loop
    while True:

        # completely fill the surface object
        # with white color
        display_surface.fill(white)

        # copying the text surface object
        # to the display surface object
        # at the center coordinate.
        display_surface.blit(text, textRect)

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():

            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()

                # quit the program.
                quit()

            # Draws the surface object to the screen.
            pygame.display.update()

def printt2():
                white = (255, 255, 255)
                green = (0, 255, 0)
                blue = (0, 0, 128)

                # assigning values to X and Y variable
                X = 400
                Y = 400

                # create the display surface object
                # of specific dimension..e(X, Y).
                display_surface = pygame.display.set_mode((X, Y))

                # set the pygame window name
                pygame.display.set_caption('Show Text')

                # create a font object.
                # 1st parameter is the font file
                # which is present in pygame.
                # 2nd parameter is size of the font
                font = pygame.font.Font('freesansbold.ttf', 32)

                # create a text surface object,
                # on which text is drawn on it.
                text = font.render('player 2  won', True, green, blue)

                # create a rectangular object for the
                # text surface object
                textRect = text.get_rect()

                # set the center of the rectangular object.
                textRect.center = (X // 2, Y // 2)

                # infinite loop
                while True:

                    # completely fill the surface object
                    # with white color
                    display_surface.fill(white)

                    # copying the text surface object
                    # to the display surface object
                    # at the center coordinate.
                    display_surface.blit(text, textRect)

                    # iterate over the list of Event objects
                    # that was returned by pygame.event.get() method.
                    for event in pygame.event.get():

                        # if event object type is QUIT
                        # then quitting the pygame
                        # and program both.
                        if event.type == pygame.QUIT:
                            # deactivates the pygame library
                            pygame.quit()

                            # quit the program.
                            quit()

                        # Draws the surface object to the screen.
                        pygame.display.update()


def printt22():
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    # assigning values to X and Y variable
    X = 400
    Y = 400

    # create the display surface object
    # of specific dimension..e(X, Y).
    display_surface = pygame.display.set_mode((X, Y))

    # set the pygame window name
    pygame.display.set_caption('Show Text')

    # create a font object.
    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    font = pygame.font.Font('freesansbold.ttf', 32)

    # create a text surface object,
    # on which text is drawn on it.
    text = font.render('DRAW', True, green, blue)

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (X // 2, Y // 2)

    # infinite loop
    while True:

        # completely fill the surface object
        # with white color
        display_surface.fill(white)

        # copying the text surface object
        # to the display surface object
        # at the center coordinate.
        display_surface.blit(text, textRect)

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():

            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()

                # quit the program.
                quit()

            # Draws the surface object to the screen.
            pygame.display.update()
def draw_shape():
    pygame.draw.line(playscreen,line_color,(600,200),(0,200),line_width)
    pygame.draw.line(playscreen, line_color, (600,400),(0,400),line_width)
    pygame.draw.line(playscreen, line_color, (200, 0), (200, 600),line_width)
    pygame.draw.line(playscreen, line_color, (400, 0), (400, 600),line_width)

# initialize the pygame libary
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
line_color = (77,40,226)
color =(14,1,67)
line_width=20
row=3
coloum = 3
player =1
# screen and the icon customization
playscreen = pygame.display.set_mode((600,600))
icon = pygame.image.load("3081789.png")
pygame.display.set_caption("X vs O ")
pygame.display.set_icon(icon)
playscreen.fill(color)
draw_shape()
#board
playing_screen = np.zeros((row,coloum))
print(playing_screen)
# RUUNING MODE OF THE SCREEN
running_mode = True
gameover=False
while running_mode and not gameover :
    for event in pygame.event.get():
          if event.type==pygame.QUIT :
              running_mode=False

          if event.type==pygame.MOUSEBUTTONDOWN :
              x_cord = event.pos[0]
              y_cord = event.pos[1]
              row_clicked = y_cord // 200
              colum_clicked = x_cord // 200
              if empty_square(row_clicked,colum_clicked) :
                  if player==1 :
                    mark_square(row_clicked,colum_clicked,1)
                    draw_shapes()

                    if check(player) :

                        printt()
                        gameover=True
                    player=2
                  elif player ==2 :
                    mark_square(row_clicked, colum_clicked,2)
                    draw_shapes()

                    if check(player):

                        printt2()
                        gameover =True
                    player =1

              if board_is_full() :

                  printt22()

              print(playing_screen)



    pygame.display.update()




