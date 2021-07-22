import pygame
import text

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (128,128,128)

# Options you can change if you want
refDelay = 3  # Delay the on screen reference (left and right keyboard) in seconds. 0 means it shows instantly
myFont = 'courier' # courier, monospace
darkMode = False # set to True for darkmode
scale = False    # Set scaling for larger resolutions or small screens (buggy) True = scaled
fpsLimit = 60 # FPS Limit (saves CPU from running full blast when not needed)

# Don't change (may break the app)
smallFontsize = 18
bigFontsize = 24
mouseDown = False
mouseWasDown = False
curCharacter = 0
curLine = 0
gameEnd = False
refTimer = 0   # Timer for the reference delay
gameText = ""   # text string used while playing a game. Added to through the main loop
logo = ('A', 'R', 'T', 'S', 'E', 'Y', 'I', 'O')
kbR = ('a', 'r', 't', 's', 'e', 'y', 'i', 'o') # Right Keyboard layout
kbL = ('s', 't', 'r', 'a', 'o', 'i', 'y', 'e') # Left Keyboard layout

# symbols that can be typed
symbols = {"!","@","#","$","%","^","&","*","(",")","_","+","-","=",";",":",",",".","/","?","[","]","{","}","\\","|","\"", "\'","`","~","<",">"}

if darkMode:
    BLACK = (100,100,100)
    WHITE = (0,0,0)
    RED = (128, 0, 0)

# Where to start
menu = 1
game = 0

# Menu Items, anything after 10 items goes off-screen.
# Must be 10 characters (monospace fonts) in order to keep the expected button size
menu_items = ['   ARTS   ', '   EYIO   ', ' Both Rows', '   CFJN   ', '   BWHKV  ', '   GUQP   ', '   DLMXZ  ', '   PUNCT  ', '  STORY 1 ', '  STORY 2 ']

pygame.init()
 
# Set the width and height of the screen [width, height] Fixed
size = (700, 500)

# Create screen and see if it's set to a scaled screen (I don't like the way scaling works)
if scale:
    screen = pygame.display.set_mode(size, pygame.SCALED | pygame.RESIZABLE)
else:
    screen = pygame.display.set_mode(size)

pygame.display.set_caption("ARTSEY.IO Trainer") # Screen caption/title

clock = pygame.time.Clock() # Start the clock to limit frames to save CPU

# Preload fonts instead of building them each time something needs to be printed
bBfont = pygame.font.SysFont(myFont, bigFontsize, True, False)
lBfont = pygame.font.SysFont(myFont, smallFontsize, True, False)
bRfont = pygame.font.SysFont(myFont, bigFontsize, True, False)
lRfont = pygame.font.SysFont(myFont, smallFontsize, True, False)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
fps = 0  # (this just initializes the variable, does not affect actual frame limit)
clock = pygame.time.Clock()

def drawFPS(x, y):
    # Display FPS for debugging
    drawText("fps: " + str(int(fps)), x, y, 2, False)

def drawMouseXY(x, y):
    # Show mouse coordinates... Used to debug UI/Hitbox
    mouseX, mouseY = pygame.mouse.get_pos()
    drawText("(" + str(mouseX)  + " " + str(mouseY) + ")", x, y, 2, False)

def mouseOver(x1, y1, x2, y2, mousex, mousey):
    # Check to see if the mouse is in a certain area
    if mousex > x1 and mousex < x2 and mousey > y1 and mousey < y2:
        return True
    else:
        return False

def drawText(text, x, y, type, cursor):
    # Draw Text to the screen at X,Y coords
    # ("text", x_pos, y_pos, text type, show cursor True/False)
    # Types: 1 = big Black, 2 = little Black, 3 = big Red, 4 = little Red
    if cursor == True:
        text += "_"
    if type == 1:
        dText = bBfont.render(text, True, BLACK)
    elif type == 2:
        dText = lBfont.render(text, True, BLACK)
    elif type == 3:
        dText = bRfont.render(text, True, RED)
    else:
        dText = lRfont.render(text, True, RED)
    screen.blit(dText, [x, y])

def drawGameText(x, y, gameText, inputText):
    # Draw the in game text (used to show when an error is made)
    printGT = ""
    for i in range(0, len(inputText)):
        curGT = gameText[i:i + 1]
        curIT = inputText[i:i + 1]
        if curGT == curIT:
            printGT = printGT + " "
        else:
            # if it is wrong, add it to the red overlay (if a space is wrong add a block)
            if curGT == " ":
                curGT = "█"
            printGT = printGT + curGT
    
    drawText(gameText, x, y, 1, False)
    drawText(printGT, x, y, 3, False)

def drawButton(text, x, y, invert):
    # Draw a UI Button at X,Y
    # ("text", x_pos, y_pos, invert/highlighted True/False)
    if invert == 0:
        pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, (len(text) * 14) + 21, 35), 2, 3)
        drawText(text, x +10, y+5, 1, False)
    else:
        pygame.draw.rect(screen, RED, pygame.Rect(x, y, (len(text) * 14) + 21, 35), 2, 3)
        drawText(text, x + 10, y + 5, 3, False)

def drawBackToMenu():
    # Draw in game UI including back to menu button
    mouseX, mouseY = pygame.mouse.get_pos() # Get mouse X and Y coords
    if mouseOver(5,5,82, 40, mouseX, mouseY):
        drawButton("MENU", 5,5, 1)
        if mouseWasDown:
            global menu, game
            menu = 1
            game = 99  # Set so it doesn't load a game before going back to the main menu (can be any number above the number of games)
            resetGameVars(0)
    else:
        drawButton("MENU", 5, 5, 0)

def drawMenu():
    # Draw the main Menu
    mx = 180
    my = 200
    mouseX, mouseY = pygame.mouse.get_pos() # Get mouse X and Y coords
    drawLogo(270,60)
    for i in range(0, len(menu_items)):
        if i == 5:
            # Start a new column of buttons if it's more than 5
            mx = 360
            my = my - (i * 50)
        if mouseOver(mx, my + (i * 50), mx + (len(menu_items[i]) * 14) + 21, my + (i * 50) + 35, mouseX, mouseY):
            drawButton(menu_items[i], mx, my + ( i * 50), 1)
            if mouseWasDown:
                # Mouse clicked inside the button. Set the game for the button selected
                global game, menu
                menu = 0
                game = i
                resetGameVars(0)
        else:
            drawButton(menu_items[i], mx, my + ( i * 50), 0)

def drawCombo(character):
    # Draws the combo of the current letter onscreen, LEFT and RIGHT
    i = 0
    cx = 140
    cy = 140
    rTime = ((pygame.time.get_ticks() - refTimer) / 1000)

    for ly in range(0, 2):
        for lx in range(0, 4):
            if text.chord[character].find(kbL[i]) != -1 and rTime >= refDelay:
                pygame.draw.rect(screen, GRAY, pygame.Rect(cx + (lx * 40), cy + (ly * 40), 40, 40), 0)
            pygame.draw.rect(screen, BLACK, pygame.Rect(cx + (lx * 40), cy + (ly * 40), 40, 40), 2, 3)
            i = i + 1
    drawText("LEFT", cx + 58, cy + 80, 2, False)

    i = 0
    cx = 390
    cy = 140
    for ly in range(0, 2):
        for lx in range(0, 4):
            if text.chord[character].find(kbR[i]) != -1 and rTime >= refDelay:
                pygame.draw.rect(screen, GRAY, pygame.Rect(cx + (lx * 40), cy + (ly * 40), 40, 40), 0)
            pygame.draw.rect(screen, BLACK, pygame.Rect(cx + (lx * 40), cy + (ly * 40), 40, 40), 2, 3)
            i = i + 1
    drawText("RIGHT", cx + 54, cy + 80, 2, False)

def drawLogo(x, y):
    # Draw the logo at X,Y
    i = 0
    for ly in range(0, 2):
        for lx in range(0, 4):
            pygame.draw.rect(screen, BLACK, pygame.Rect(x + (lx * 40), y + (ly * 40), 40, 40), 2, 3)
            drawText(logo[i], x + (lx * 40) + 13, y + (ly * 40) + 8, 1, False)
            i = i + 1
    drawText("Trainer", x + 43, y + 80, 2, False)

def resetGameVars(var):
    # Reset in game variables. Used just in case more are added you don't have to change every instance it needs to be called
    global curCharacter, curLine, gameText, gameEnd
    curCharacter = 0
    curLine = 0
    gameText = ""
    gameEnd = False

def inGame(inText, numLines):
        global curLine, gameText, gameEnd, curCharacter
        
        drawGameText(70, 300, inText, gameText)
        drawText(gameText, 70, 320, 1, True)
        
        # if it's at the end of a line move to the next, unless it's the last line in the game.
        if(len(inText) <= len(gameText) and curLine < numLines - 1):
            curLine += 1
            curCharacter = 0
            gameText = ""
        elif(len(inText) <= len(gameText) or curLine > numLines - 1):
            gameEnd = True
            gameText = gameText[0:len(gameText) - 1]
        
        # Draw the restart button at the end of the game
        if gameEnd == True:
            mouseX, mouseY = pygame.mouse.get_pos() # Get mouse X and Y coords
            if mouseOver(290, 360, 409, 394, mouseX, mouseY):
                drawButton("RESTART", 290, 360, 1)
                if mouseWasDown:
                    resetGameVars(0)
            else:
                drawButton("RESTART", 290, 360, 0)

        # Get the current character in order to show the visual combo
        curChar = inText[len(gameText):len(gameText) + 1]
        drawCombo(curChar)

def drawGame():
    # Game logic and drawing the selected game
    drawBackToMenu()
    if game == 0:
        inGame(text.topRow[curLine], len(text.topRow))
    elif game == 1:
        inGame(text.bottomRow[curLine], len(text.bottomRow))
    elif game == 2:
        inGame(text.bothRows[curLine], len(text.bothRows))
    elif game == 3:
        inGame(text.chords1[curLine], len(text.chords1))
    elif game == 4:
        inGame(text.chords2[curLine], len(text.chords2))
    elif game == 5:
        inGame(text.chords3[curLine], len(text.chords3))
    elif game == 6:
        inGame(text.chords4[curLine], len(text.chords4))
    elif game == 7:
        inGame(text.punctuation[curLine], len(text.punctuation))
    elif game == 8:
        inGame(text.story1[curLine], len(text.story1))
    elif game == 9:
        inGame(text.story2[curLine], len(text.story2))
    else:
        if menu == 0:
            drawText("Menu item " + str(game) + " Not yet implemented?", 200,200,3, False)
        else:
            print("Skip back to menu")  # Stops a new game from running while going back to the menu (might not be needed anymore)
        
def drawScreen():
    screen.fill(WHITE) # Clear the screen

    if menu > 0:
        drawMenu()
    else:
        drawGame()

    # Debugging for lag and hitbox issues
    #drawFPS(500, 10)
    #drawMouseXY(585, 10)

    pygame.display.flip()

# -------- Main Program Loop -----------
while not done:
    if mouseWasDown:
        mouseWasDown = False
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True # clicked
        if event.type == pygame.MOUSEBUTTONUP and mouseDown == True:
            mouseDown = False # mouse is now up, reset
            mouseWasDown = True #find where the mouse was after release of the mouse button
        if event.type == pygame.KEYDOWN and gameEnd != True:  # Add to the game text if a game is not over
            if event.unicode.isalpha() or event.unicode.isnumeric() or event.unicode in symbols:
                gameText += event.unicode
                curCharacter += 1
                refTimer = pygame.time.get_ticks()
                
            elif event.key == pygame.K_BACKSPACE:
                gameText = gameText[:-1]
                curCharacter -= 1
                refTimer = pygame.time.get_ticks()
            elif event.key == pygame.K_SPACE:
                gameText += " "
                curCharacter += 1
                refTimer = pygame.time.get_ticks()
            elif event.key == pygame.K_ESCAPE: # If escape is pressed go back to the menu screen
                menu = 1
                game = 99
                resetGameVars(0)

    drawScreen()
    clock.tick(fpsLimit) # This is where the game actually gets frame limited
    fps = clock.get_fps()
 
# Close the window and quit.
pygame.quit()