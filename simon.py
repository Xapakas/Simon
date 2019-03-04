from graphics import *
from random import *
from time import *

def drawInitial():
    win = GraphWin("Simon Window",600,600)
    greenbox = Rectangle(Point(10,10), Point(280,280))
    greenbox.setFill("green")
    greenbox.draw(win)
    redbox = Rectangle(Point(320,10), Point(590,280))
    redbox.setFill("red")
    redbox.draw(win)
    yellowbox = Rectangle(Point(10,320), Point(280,590))
    yellowbox.setFill("gold")
    yellowbox.draw(win)
    bluebox = Rectangle(Point(320,320), Point(590,590))
    bluebox.setFill("blue")
    bluebox.draw(win)

    return win

def getStartClick(win):
    startbox = Rectangle(Point(200,260),Point(400,340))
    startbox.setFill("white")
    startbox.draw(win)
    starttext = Text(Point(300,300),"START")
    starttext.setSize(20)
    starttext.draw(win)
    click = win.getMouse()
    x = click.getX()
    y = click.getY()
    while x < 200 or x > 400 or y < 260 or y > 340: # input validation
        click = win.getMouse()
        x = click.getX()
        y = click.getY()
    startbox.undraw()
    starttext.undraw()

    return startbox,starttext

def generateRandom(l_ist):
    i_num = randint(1,4)
    l_ist.append(i_num)

def drawSequence(win,l_ist):
    for i_num in l_ist:
        if i_num == 1: # green box lights up
            lit = Rectangle(Point(10,10),Point(280,280))
            lit.setFill("lime")
            lit.draw(win)
        elif i_num == 2: # red box = lit
            lit = Rectangle(Point(320,10), Point(590,280))
            lit.setFill("tomato")
            lit.draw(win)
        elif i_num == 3: # yellow box = lit
            lit = Rectangle(Point(10,320), Point(280,590))
            lit.setFill("yellow")
            lit.draw(win)
        elif i_num == 4: # blue box = lit
            lit = Rectangle(Point(320,320), Point(590,590))
            lit.setFill("aqua")
            lit.draw(win)
        sleep(0.25)
        lit.undraw()
        sleep(0.25)

def getGuess(win,l_ist):
    b_valid_click = False
    b_lose = False
    for i_num in range(len(l_ist)):
        if b_lose == False:
            while b_valid_click == False:
                click = win.getMouse()
                x = click.getX()
                y = click.getY()
                if x >= 10 and x <= 280 and y >= 10 and y <= 280: # clicks green box
                    i_guess = 1
                    b_valid_click = True
                elif x >= 320 and x <= 590 and y >= 10 and y <= 280: # clicks red box
                    i_guess = 2
                    b_valid_click = True
                elif x >= 10 and x <= 280 and y >= 320 and y <= 590: # clicks yellow box
                    i_guess = 3
                    b_valid_click = True
                elif x >= 320 and x <= 590 and y >= 320 and y <= 590: # cicks blue box
                    i_guess = 4
                    b_valid_click = True
                else:
                    i_guess = -1
            if i_guess != l_ist[i_num]:
                b_lose = True
            b_valid_click = False
        else:
            b_lose = True

    return b_lose

def drawLose(win,i_score):
    lose_box = Rectangle(Point(100,200),Point(500,400))
    lose_box.setFill("white")
    lose_box.draw(win)
    lose_text = Text(Point(300,250),"GAME OVER")
    lose_text.setFill("red")
    lose_text.setSize(36)
    lose_text.draw(win)
    score_text = Text(Point(300,300),"SCORE: " + str(i_score))
    score_text.setFill("blue")
    score_text.setSize(25)
    score_text.draw(win)
    play_again_text = Text(Point(300,350),"Click to Play Again")
    play_again_text.setFill("green")
    play_again_text.setSize(25)
    play_again_text.draw(win)
    win.getMouse()
    lose_box.undraw()
    lose_text.undraw()
    score_text.undraw()
    play_again_text.undraw()

def main():
    win = drawInitial()
    startbox,starttext = getStartClick(win)
    l_ist = []
    i_score = 0
    while True: # game start
        generateRandom(l_ist)
        drawSequence(win,l_ist)
##        print(l_ist)
        b_lose = getGuess(win,l_ist)
        if b_lose == True:
            drawLose(win,i_score)
            l_ist = []
            i_score = -1
        i_score += 1

main()
