import time
import sys


class Player:
    def __init__(self, tag):
        self.name = tag


global gameStart
gameStart = False


def delayPrint(text, delay):
    for i in text:

        # I know I could have set the delay to be a constant but I had it this way before and I'm too lazy to change it

        time.sleep(delay)
        print(i, end='')
        sys.stdout.flush()
    print()


def startGame():
    x = input("Do you want to play? (y/n): ").lower()

    if x == "y":
        delayPrint("Splendid!", 0.05)
        return 1
    elif x == "n":
        delayPrint("Goodbye", 0.05)
        exit()
    else:
        delayPrint("\nInvalid Input.", 0.05)
        startGame()


def introSeq():
    x = input("Welcome! First, what is your name? ")

    player = Player(x)

    delayPrint("Hello " + player.name + "!  Let's begin", 0.05)


def firstChoice():
    delayPrint("You're taking a walk in the woods when you come along a fork in the road.", 0.05)
    choice = int(input("Do you 1. Go left or 2. Go right? "))

    if choice == 1:
        delayPrint("You go left down the path.", 0.05)
        return 1
    elif choice == 2:
        delayPrint("You go right down the path.", 0.05)
        return 2


def choiceOne():
    delayPrint("A rotting, half-eaten deer carcass is sitting in the middle of the road.", 0.05)
    cho = int(input("Do you: 1. Inspect the deer or 2. Go around? "))

    if cho == 1:
        delayPrint("You step closer to the deer carcass.", 0.05)
        return 1
    elif cho == 2:
        delayPrint("You swing around the carcass.", 0.05)
        return 2



def choiceTwo():
    delayPrint("A shadow with glaring red eyes stares at you from ahead before abruptly running off.", 0.05)
    chO = int(input("Do you: 1. Run after the shadow or 2. Keep walking normally? "))

    if chO == 1:
        delayPrint("You begin chasing after it as fast as you can", 0.05)
        return 1
    elif chO == 2:
        delayPrint("You begin whistling a merry tune as you continue your walk.", 0.05)
        return 2


def choiceOneOne():
    delayPrint("You tap the deer and begin to feel dizzy.  You wake up bound and gagged in a chair", 0.05)
    delayPrint("staring the down the barrel of a gun.  You're done for.", 0.05)
    delayPrint("Game Over!", 0.05)
    exit()


def choiceOneTwo():
    delayPrint("As you walk past the deer, shadows envelope you and begin to asphyxiate you.  You're dead.", 0.05)
    delayPrint("Game Over!", 0.05)
    exit()

def choiceTwoOne():
    delayPrint("While running after the shadow, it reappears and stares at you again.", 0.05)
    delayPrint("This time, the stare entrances you, leaving your body limp.  You're done for.", 0.05)
    delayPrint("Game Over!", 0.05)
    exit()

def choiceTwoTwo():
    delayPrint("You finish your walk as it begins to turn dark.  What a great day this has been!", 0.05)
    delayPrint("The good ending!", 0.05)
    exit()

gameChoice = startGame()

if gameChoice == 1:
    gameStart = True

if gameStart:
    introSeq()
    firstDec = firstChoice()

    if firstDec == 1:
        co = choiceOne()

        if co == 1:
            choiceOneOne()
        elif co == 2:
            choiceOneTwo()

    elif firstDec == 2:
        ct = choiceTwo()

        if ct == 1:
            choiceTwoOne()
        elif ct == 2:
            choiceTwoTwo()



