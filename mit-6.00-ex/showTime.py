import turtle
import time

def drawNumber0(p, startPoint, width, height):
    p.penup()
    p.setheading(0)
    p.goto(startPoint[0], startPoint[1])
    p.pendown()
    p.forward(width)
    p.left(90)
    p.forward(height)
    p.left(90)
    p.forward(width)
    p.left(90)
    p.forward(height)

def drawNumber1(p, startPoint, width, height):
    p.penup()
    p.setheading(90)
    p.goto(startPoint[0]+width, startPoint[1])
    p.pendown()
    p.forward(height)

def drawNumber2(p, startPoint, width, height):
    p.penup()
    p.setheading(180)
    p.goto(startPoint[0]+width, startPoint[1])
    p.pendown()
    p.forward(width)
    p.right(90)
    p.forward(int(0.5*height))
    p.right(90)
    p.forward(width)
    p.left(90)
    p.forward(int(0.5*(height)))
    p.left(90)
    p.forward(width)

def drawNumber3(p, startPoint, width, height):
    p.penup()
    p.setheading(0)
    p.goto(startPoint[0], startPoint[1])
    p.pendown()
    p.forward(width)
    p.left(90)
    p.forward(height)
    p.left(90)
    p.forward(width)
    p.penup()
    p.goto(startPoint[0]+width, startPoint[1]+int(0.5*height))
    p.forward(width)

def drawNumber4(p, startPoint, width, height):
    p.penup()
    p.setheading(90)
    p.goto(startPoint[0]+width, startPoint[1])
    p.pendown()
    p.forward(height)
    p.penup()
    p.goto(startPoint[0], startPoint[1]+height)

def drawNumber5(p, startPoint, width, height):
    p.penup()
    p.setheading(0)
    p.goto(startPoint[0], startPoint[1])
    p.pendown()
    p.forward(width)
    p.left(90)
    p.forward(int(0.5*height))
    p.left(90)
    p.forward(width)
    p.right(90)
    p.forward(int(0.5*height))
    p.right(90)
    p.forward(width)

def drawNumber6(p, startPoint, width, height):
    p.penup()
    p.setheading(0)
    p.goto(startPoint[0], startPoint[1])
    p.pendown()
    p.forward(width)
    p.left(90)
    p.forward(int(0.5*height))
    p.left(90)
    p.forward(width)
    p.penup()
    p.goto(startPoint[0], startPoint[1])
    p.pendown()
    p.right(90)
    p.forward(height)
    p.right(90)
    p.forward(width)

def drawNumber7(p, startPoint, width, height):
    p.penup()
    p.setheading(90)
    p.goto(startPoint[0]+width, startPoint[1])
    p.pendown()
    p.forward(height)
    p.left(90)
    p.forward(width)

def drawNumber8(p, startPoint, width, height):
    p.penup()
    p.setheading(0)
    p.goto(startPoint[0], startPoint[1])
    p.pendown()
    p.forward(width)
    p.left(90)
    p.forward(height)
    p.left(90)
    p.forward(width)
    p.left(90)
    p.forward(height)
    p.penup()
    p.goto(startPoint[0], startPoint[1]+int(0.5*height))
    p.pendown()
    p.setheading(0)
    p.forward(width)

def drawNumber9(p, startPoint, width, height):
    p.penup()
    p.setheading(0)
    p.goto(startPoint[0], startPoint[1])
    p.pendown()
    p.forward(width)
    p.left(90)
    p.forward(height)
    p.left(90)
    p.forward(width)
    p.left(90)
    p.forward(int(0.5*height))
    p.left(90)
    p.forward(width)

def drawTime(p, startPoint, width, height, gap):
    t = time.localtime(time.time())
    year = time.strftime("%Y", t)
    month = time.strftime("%m", t)
    day = time.strftime("%d", t)
    #print(year + "-" + month + "-" + day)
    date = year + month + day
    dx = 0
    for num in date:
        newStartPoint = (startPoint[0] + dx, startPoint[1])
        if num == str(0):
            drawNumber0(p, newStartPoint, width, height)
        if num == str(1):
            drawNumber1(p, newStartPoint, width, height)
        if num == str(2):
            drawNumber2(p, newStartPoint, width, height)
        if num == str(3):
            drawNumber3(p, newStartPoint, width, height)
        if num == str(4):
            drawNumber4(p, newStartPoint, width, height)
        if num == str(5):
            drawNumber5(p, newStartPoint, width, height)
        if num == str(6):
            drawNumber6(p, newStartPoint, width, height)
        if num == str(7):
            drawNumber7(p, newStartPoint, width, height)
        if num == str(8):
            drawNumber8(p, newStartPoint, width, height)
        if num == str(9):
            drawNumber9(p, newStartPoint, width, height)
        dx = dx + gap + width

def main():
    p = turtle.Turtle()
    p.color("red")
    p.pensize(5)
    p.speed(10)
    p.hideturtle()

    startPoint = (-240, -50)
    width = 50
    height = 100
    gap = 10

    drawTime(p, startPoint, width, height, gap)

main()
    
        



