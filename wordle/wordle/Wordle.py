import pygame
import time
import random

r = open("common6.txt", "r")
s = r.readlines()
sixes = []
for x in s:
    yes = True
    if len(x) == 6:
        for chart in x:
            if x.count(chart) > 1:
                yes = False
        if yes:
            sixes.append(x)
r.close()
dump = open('common7.txt', 'w')
dump.writelines(sixes)
dump.close()

f = open("common6.txt", "r")
f2 = open("common7.txt", "r")
possible_words = f.readlines()
guessing_words = f2.readlines()
for i in range(len(possible_words)):
    possible_words[i] = possible_words[i][:-1]
for i in range(len(guessing_words)):
    guessing_words[i] = guessing_words[i][:-1]


# Define global variables
black= (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0,120,255)
green = (0, 150, 0)
grey = (200, 200, 200)
dark_grey = (115, 115, 115)
yellow = (255, 219, 88)
pygame.init()
window_width = 700
window_height = 750
x_start = window_width/6+15
y_start = 60
increment = 75
rounds = 0

gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Wordle")
clock = pygame.time.Clock()


def setup():
    pygame.init()
    window_width = 700
    window_height = 750

    gameDisplay = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Wordle")
    clock = pygame.time.Clock()


class button():
    def __init__(self, x, y, width, length, letter):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.letter = letter
        self.colour = grey
        self.picked = False

    def draw(self, colour, size=25):
        pygame.draw.rect(gameDisplay, colour, (self.x, self.y, self.width, self.length), border_radius=4)
        draw_letter(self.letter, self.x + self.width / 2, self.y + self.length / 2, size)

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.length:
                return True
        return False


def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()


def draw_letter(string, x, y, size, colour=black):
    global rounds
    largeText = pygame.font.Font("freesansbold.ttf", size)
    TextSurf, TextRect, = text_objects(string, largeText, colour)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def makewordlist(zop):
    global possible_words
    global guessing_words
    zop += 1
    print("hello there" + str(zop))
    r = open("common6.txt", "r")
    s = r.readlines()
    sixes = []
    for x in s:
        yes = True
        if len(x) == zop:
            for chart in x:
                if x.count(chart) > 1:
                    yes = False
            if yes:
                sixes.append(x)
    r.close()
    dump = open('common7.txt', 'w')
    dump.writelines(sixes)
    dump.close()
    f = open("common6.txt", "r")
    f2 = open("common7.txt", "r")
    possible_words = f.readlines()
    guessing_words = f2.readlines()
    for i in range(len(possible_words)):
        possible_words[i] = possible_words[i][:-1]
    for i in range(len(guessing_words)):
        guessing_words[i] = guessing_words[i][:-1]

def draw_rectangles(k,size):
    for i in range(6):
        for j in range(k):
            pygame.draw.rect(gameDisplay, black, (x_start + increment * j, y_start + increment * i, size, size), width=2)


def wrong_guess(word, guess, num_guess,zop,size):
    global rounds
    global fsize
    upper_word = word.upper()
    for i in range(zop):
        colour = dark_grey
        drawn = False
        if upper_word[i] == guess[i]:
            drawn = True
            colour = green
        elif not drawn:
            for letter in upper_word:
                if guess[i] == letter and guess[:i].count(letter) == 0:
                    colour = yellow
        pygame.draw.rect(gameDisplay, colour, (x_start + increment * i, y_start + increment * num_guess, size, size))
        for letter in letters:
            if letter.letter == guess[i]:
                if letter.colour == grey:
                    letter.draw(colour)
                elif letter.colour == dark_grey and (colour == green or colour == yellow):
                    letter.draw(colour)
                elif letter.colour == yellow and colour == green:
                    letter.draw(colour)
                letter.picked = True
        for ind, letter in enumerate(guess):
            draw_letter(letter, x_start + increment * ind + 29-2.4*rounds,
                        y_start + increment * num_guess + 34-2.6*rounds, fsize)


def is_real_word(guess):
    for word in possible_words:
        if guess.lower() == word.lower():
            return True
    return False

def winner(word):
    pygame.draw.rect(gameDisplay, black, (250, 250, 200, 50), border_radius=5)
    draw_letter("You Win!", 350, 275, 37, white)
    play_again.draw(green)
    pygame.draw.rect(gameDisplay, black, (250, 350, 200, 50), 2)


def loser(word):
    pygame.draw.rect(gameDisplay, black, (275, 250, 150, 50), border_radius=5)
    draw_letter(word.upper(), 350, 275, 37, white)
    play_again.draw(green)
    pygame.draw.rect(gameDisplay, black, (250, 350, 200, 50), 2)

zop = 5
size = 60
fsize = 40
def game_loop():
    setup()
    global zop
    global rounds
    global size
    global fsize
    global increment
    gameDisplay.fill(white)
    gameExit = False
    draw_rectangles(zop,size)
    for letter in letters:
        letter.draw(blue)
    enter.draw(grey, 15)
    delete.draw(grey, 13)
    word = guessing_words[random.randint(0, len(guessing_words))]
    print(word)
    guesses = 0
    current_guess = ""
    gameOver = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if gameOver:
                if event.type == pygame.MOUSEMOTION:
                    position = pygame.mouse.get_pos()
                    if play_again.is_over(position):
                        play_again.draw(green, 30)
                        pygame.draw.rect(gameDisplay, black, (250, 350, 200, 50), 2)
                    else:
                        play_again.draw(green)
                        pygame.draw.rect(gameDisplay, black, (250, 350, 200, 50), 2)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    if play_again.is_over(position):
                        game_loop()
                if event.type == pygame.KEYDOWN:
                    pressed = event.key
                    if pressed == 27:
                        pygame.quit()
                        quit()
            if guesses == 6 and not gameOver:
                loser(word)
                gameOver = True
            if not gameOver:
                if event.type == pygame.KEYDOWN:
                    pressed = event.key
                    print(pressed)
                    if pressed == 27:
                        pygame.quit()
                        quit()
                    if 97 <= pressed <= 122:
                        if len(current_guess) < zop:
                            current_guess += chr(pressed - 32)
                            draw_letter(current_guess[-1], x_start + increment * (len(current_guess) - 1) + 29 - 2.35*rounds, y_start + increment*guesses + 34 - 2.65*rounds, fsize)
                    elif pressed == 13:
                        if len(current_guess) == zop:
                            if is_real_word(current_guess):
                                if current_guess == word.upper():
                                    wrong_guess(word, current_guess, guesses, zop,size)
                                    winner(word)
                                    zop+=1
                                    size -= 5
                                    fsize -= 4
                                    increment -= 5
                                    rounds += 1
                                    makewordlist(zop)
                                    game_loop()
                                else:
                                    wrong_guess(word, current_guess, guesses,zop,size)
                                    guesses += 1
                                    current_guess = ""

                    elif pressed == 8:
                        current_guess = current_guess[:-1]
                        pygame.draw.rect(gameDisplay, white, (x_start + increment * len(current_guess) + 2, y_start + increment * guesses + 2, size-3, size-3))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    for letter in letters:
                        if letter.is_over(position):
                            if len(current_guess) < zop:
                                current_guess += letter.letter
                                draw_letter(current_guess[-1], x_start + increment * (len(current_guess) - 1) + 29 - 2.45*rounds,
                                            y_start + increment * guesses + 34 - 2.5*rounds, 40)

                    if enter.is_over(position):
                        if len(current_guess) == zop:
                            if is_real_word(current_guess):
                                if current_guess == word.upper():
                                    wrong_guess(word, current_guess, guesses,zop,size)
                                    winner(word)
                                    zop+=1
                                    size -= 5
                                    fsize -= 4
                                    increment -= 5
                                    rounds +=1
                                    makewordlist(zop)
                                    game_loop()
                                else:
                                    wrong_guess(word, current_guess, guesses,zop,size)
                                    guesses += 1
                                    current_guess = ""
                    if delete.is_over(position):
                        current_guess = current_guess[:-1]
                        pygame.draw.rect(gameDisplay, white, (x_start + increment * len(current_guess) + 2, y_start + increment * guesses + 2, 57, 57))
        pygame.display.update()
        clock.tick(30)


button_length = 50
button_width = 40
q = button(100, 550, button_width, button_length, 'Q')
w = button(150, 550, button_width, button_length, 'W')
e = button(200, 550, button_width, button_length, 'E')
r = button(250, 550, button_width, button_length, 'R')
t = button(300, 550, button_width, button_length, 'T')
y = button(350, 550, button_width, button_length, 'Y')
u = button(400, 550, button_width, button_length, 'U')
i = button(450, 550, button_width, button_length, 'I')
o = button(500, 550, button_width, button_length, 'O')
p = button(550, 550, button_width, button_length, 'P')
a = button(125, 610, button_width, button_length, 'A')
s = button(175, 610, button_width, button_length, 'S')
d = button(225, 610, button_width, button_length, 'D')
f = button(275, 610, button_width, button_length, 'F')
g = button(325, 610, button_width, button_length, 'G')
h = button(375, 610, button_width, button_length, 'H')
j = button(425, 610, button_width, button_length, 'J')
k = button(475, 610, button_width, button_length, 'K')
l = button(525, 610, button_width, button_length, 'L')
z = button(175, 670, button_width, button_length, 'Z')
x = button(225, 670, button_width, button_length, 'X')
c = button(275, 670, button_width, button_length, 'C')
v = button(325, 670, button_width, button_length, 'V')
b = button(375, 670, button_width, button_length, 'B')
n = button(425, 670, button_width, button_length, 'N')
m = button(475, 670, button_width, button_length, 'M')
enter = button(100, 670, 65, button_length, "ENTER")
delete = button(525, 670, 65, button_length, "DELETE")
play_again = button(250, 350, 200, 50, "Play Again?")
letters = [q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m]


game_loop()
