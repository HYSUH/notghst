'''
Copyright(c) 2014 YSUV - MultiColour Square generator
MIT licence
'''

import turtle
import random


class MultiColoredSquares(turtle.Turtle):

    def __init__(self, startx=300, starty=50, squareSize=20,
                 length=30, width=5):
        '''
        (startx, startx)  - the x and y coordinates on the screen that the
        turtle starts drawing.
        squareSize  - the size of the square drawn.
        length  - the number of squares drawn horizontally
        width - number of quares drwan vertically.
        '''
        self.startx = startx
        self.starty = starty
        self.squareSize = squareSize
        self.length = length
        self.width = width
        super(MultiColoredSquares, self).__init__()

    def turnRight(self):
        ''' Turns the turtle right by rotating 90 degrees '''
        self.right(90)

    def setPosToDrawSquareLine(self, i):
        ''' This function moves the turtle to the position so that the set of
        squares can be drawn'''
        self.penup()
        self.setx(self.startx)
        self.sety(self.starty - self.squareSize * i)

    def moveBackASquare(self):
        ''' This function moves the turtle back so that the next square can be drawn
        again '''
        self.penup()  # dont want to draw while moving back
        self.backward(self.squareSize)

    def drawFilledSquare(self):
        ''' This function draws a square that is colored using a randomly
        selected color
        '''
        self.pendown()
        self.color(random.random(), random.random(), random.random())
        self.begin_fill()
        for _ in range(4):
            self.forward(self.squareSize)
            self.turnRight()
        self.end_fill()

    def drawMultiSquareLine(self):
        ''' draws `length` number of squares horizontally starting at (x,y) and
        moving backwards '''
        for _ in range(self.length):
            self.moveBackASquare()
            self.drawFilledSquare()

    def createSquareLogo(self):
        ''' This function draws a mulitcoloured line `width` number of times
        '''
        self.reset()
        for i in range(self.width):
            self.setPosToDrawSquareLine(i)
            self.drawMultiSquareLine()

if __name__ == '__main__':
    try:
        testturtle = MultiColoredSquares()
        testturtle.createSquareLogo()
    except Exception as e:
        print(e)
