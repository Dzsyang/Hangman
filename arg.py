# This is main.py of Hangman game.
# Need to be added: Actually, this game should show Guesser which kind of the secret word.

import os
import sys
import random
import time
import getopt

if sys.platform == "win32":
    import msvcrt
    CLEAR = "cls"
    def press_any_key(msg):
        print(msg)
        msvcrt.getch()
else:
    import termios
    CLEAR = r"clear"
    def press_any_key(msg):
        fd = sys.stdin.fileno()
        old_ttyinfo = termios.tcgetattr(fd)
        new_ttyinfo = old_ttyinfo[:]
        new_ttyinfo[3] &= ~termios.ICANON
        new_ttyinfo[3] &= ~termios.ECHO
        sys.stdout.write(msg)
        sys.stdout.flush()
        termios.tcsetattr(fd, termios.TCSANOW, new_ttyinfo)
        os.read(fd, 7)
        termios.tcsetattr(fd, termios.TCSANOW, old_ttyinfo)

def Initialize():
    random.seed(time.time())
    os.system(CLEAR)
    drawlogo()
    drawauthor()
    return

def modechoose():
    print("*** MODE CHOOSE ***")
    mode = None
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "oth", ["one", "two", "help"])
    except:
        print("Error!")
    for opt, arg in opts:
        if opt in ["-o", "--one"]:
            mode = "o"
        elif opt in ["-t", "--two"]:
            mode = "t"
        elif opt in ["-h", "--help"]:
            mode = "h"
    os.system(CLEAR)
    return mode

def rolechoose():
    print("Please choose your role. Thinker or Guesser? [T/g]", end = " ")
    Thinker = ["T", "t", "Thinker", "thinker", "Think", "think"]
    if input() in Thinker:
        role = "t"
    else:
        role = "g"
    press_any_key("Press any key to continue...")
    return role

def mode1():
    os.system(CLEAR)
    print("***** T H I N K E R *****")
    print("You are Thinker, and your task is to think a word for Guesser to guess.")
    print("Notice: All letters should be different and in lower case.")
    while True:
        print("Please enter the word:", end = " ")
        word = input()
        if word.isalpha():
            break
        else:
            print("Invalid input! Please enter a word.")
    print("OK, the word you think is " + word + ".")
    press_any_key("Press any key to continue...")
    os.system(CLEAR)
    return word

def Is_end(cnt, x, word):
    if cnt == 6:
        drawman(cnt)
        print("***** L O S E *****")
        print("The secret word is " + word + ".")
        return True
    s = ""
    for i in range(len(word)):
        s += word[i] + " "
    if s == x:
        print("***** W I N *****")
        print("You really guess it out! " + word + ", that is!")
        return True
    return False

def drawlogo(): 
    print(" ##     ##    ###    ##    ##  ######   ##     ##    ###    ##    ##\n"
          " ##     ##   ## ##   ###   ## ##    ##  ###   ###   ## ##   ###   ##\n"
          " ##     ##  ##   ##  ####  ## ##        #### ####  ##   ##  ####  ##\n"
          " ######### ##     ## ## ## ## ##   #### ## ### ## ##     ## ## ## ##\n"
          " ##     ## ######### ##  #### ##    ##  ##     ## ######### ##  ####\n"
          " ##     ## ##     ## ##   ### ##    ##  ##     ## ##     ## ##   ###\n"
          " ##     ## ##     ## ##    ##  ######   ##     ## ##     ## ##    ##\n")     
    time.sleep(3)    
    os.system(CLEAR)
                          
def drawauthor(): 
    print(" ########   ########   ######   ##    ##     ###     ##    ##   ######   \n"
          " ##     ##       ##   ##    ##   ##  ##     ## ##    ###   ##  ##    ##  \n"
          " ##     ##      ##    ##          ####     ##   ##   ####  ##  ##        \n"
          " ##     ##     ##      ######      ##     ##     ##  ## ## ##  ##   #### \n"
          " ##     ##    ##            ##     ##     #########  ##  ####  ##    ##  \n"
          " ##     ##   ##       ##    ##     ##     ##     ##  ##   ###  ##    ##  \n"
          " ########   ########   ######      ##     ##     ##  ##    ##   ######   \n")
    time.sleep(3)      
    os.system(CLEAR)
                                                                     
def drawman(cnt):
    hangman = ["""
      +---+
          |
          |
          |
         ===""", """
      +---+
      O   |
          |
          |
         ===""", """
      +---+
      O   |
      |   |
          |
         ===""", """
      +---+
      O   |
      /|  |
          |
         ===""", """
      +---+
      O   |
     /|\  |
          |
         ===""", """
      +---+
      O   |
     /|\  |
     /    |
         ===""", """
      +---+
      O   |
     /|\  |
     / \  |
         ==="""]
    print(hangman[cnt])
    return

def mode2(word):
    cnt = 0
    x = ""
    for i in range(len(word)):
        x += "_ "
    os.system(CLEAR)
    print("***** G U E S S E R *****")
    print("You are Guesser, and your task is to guess the word out before the 'hangman' is drawn.")
    while not Is_end(cnt, x, word):
        drawman(cnt)
        print("Missed letters:")
        print(x)
        while True:
            print("Guess a letter:", end = " ")
            char = input()
            if char.isalpha():
                break
            else:
                print("Invalid input! Please enter a lower-case letter.")
        find = False
        for i in range(len(word)):
            if char == word[i]:
                x = x[: 2 * i] + char + x[2 * i + 1:]
                find = True
                break
        if not find:
            cnt += 1
    print("Do you want to play again? [Y/n]", end = " ")
    ans = input()
    yes = ["Y", "y", "yes", "Yes"]
    if ans in yes:
        print("Ok, let's play again!")
        press_any_key("Press any key to continue...")
        os.system(CLEAR)
        return 1
    else:
        exitgame()

def exitgame():
    os.system(CLEAR)
    print("Fine, see you next time!")
    press_any_key("Press any key to exit...")
    os.system(CLEAR)
    exit()

def getword():
    repo = ["cat", "cow", "act", "age", "aid", "arm", "bad", "ban", "bed", "beg", \
    "bow", "but", "cry", "cup", "day", "dog", "dry", "dot", "fan", "fly", "gay", "get", "god", "gum", \
    "gun", "guy", "fox", "fry", "fun", "fur", "hot", "hug", "ice", "ill", "ion", "jam", "job", "jog", \
    "key", "kin", "lab", "law", "lay", "leg", "let", "lie", "log", "low", "mad", "man", "map", "mat", \
    "may", "mix", "mob", "mud", "net", "nod", "new", "not", "now", "old", "out", "own", "owe", \
    "pay", "pet", "pen", "pea", "pie", "pig", "pin", "put", "rap", "rat", "ray", "red", "run", "row", \
    "sad", "saw", "say", "set", "sea", "sin", "sit", "sky", "skin", "spy", "sob", "sow", "sum", "sun", \
    "tag", "tax", "tie", "top", "try", "use", "wax", "way", "win", "zip"]
    i = random.randint(0, len(repo) + 1)
    word = repo[i]
    return word

def auto():
    playing = 1
    while playing:
        word = getword()
        playing = mode2(word)

def normal():
    playing = 1
    while playing:
        role = rolechoose()
        if role == "t":
            word = mode1()
        elif role == "g":
            playing = mode2(word)
        else:
            print("Error!")
            exit()

def help():
    print( "######### HELP #########\n"
           "-h|--help      print this help message\n"
           "-o|--one       one player mode\n"
           "-t|--two       two players mode\n")

# main
Initialize()
mode = modechoose()
if mode == "o":
    auto()
elif mode == "t":
    normal()
elif mode == "h":
    help()
