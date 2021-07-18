import pygame
from createBlitz import RectBlit,colours

screenHeight = 480
screenWidth = 720

def text_objects(text, font):
    textSurface = font.render(text, True, colours["white"])
    return textSurface, textSurface.get_rect()


def message_display(text, textSize, xPos, yPos):
    textFont = pygame.font.Font('freesansbold.ttf',textSize)
    TextSurf, TextRect = text_objects(text, textFont)
    TextRect.center = ((xPos),(yPos))
    screen.blit(TextSurf, TextRect)


def checkCollide(gameEvents):
    global pos
    pos = (-1000, -1000)

    for event in gameEvents:
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()


def checkFollowing():
    pass    


def createMenu(x, y1, y2):
    buttonGM1 = RectBlit(colours['white'], (x, y1, 200, 100))
    buttonGM2 = RectBlit(colours['white'], (x, y2, 200, 100))
    buttonGM1.createBlit(screen)
    buttonGM2.createBlit(screen)


    

def main():
    pygame.init()
    pygame.display.set_caption("Hello Game")
    
    display = pygame.display
    global screen 
    screen = display.set_mode((screenWidth,screenHeight), pygame.RESIZABLE)
    display.init()

    xChange = 30
    yChange = 20
    x = screenWidth * 0.45 #centered(in small window...)
    y = screenHeight * 0.8 #bottom page
    #^ these two var may need to change in the future. prob make local in functions. 

    btnXCoord = screenWidth/2 -100
    btn1YCoord = screenHeight/4*3
    btn2YCoord = screenHeight/4 + 50

    def pause(t):
        pygame.time.delay(t)

    #loop for catch the box
    running = True
    gameStarted = False
    gameOver = False
    gameMode = 0
    menuOpen = True
    
    while running:
        #game init stuff
        #------------------------#
        gameEvents = pygame.event.get()

        for event in gameEvents:
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()
        #------------------------#


        #menu 
        #------------------------#
        if menuOpen:
            createMenu(btnXCoord, btn1YCoord, btn2YCoord)

            checkCollide(gameEvents)
            if pos[0] > btnXCoord and pos[0] < btnXCoord + 200 and pos[1] > btn1YCoord and pos[1] < btn1YCoord + 200:
                gameMode = 1
                menuOpen = False
                gameStarted = True
            elif pos[0] > btnXCoord and pos[0] < btnXCoord + 200 and pos[1] > btn2YCoord and pos[1] < btn2YCoord + 200:
                gameMode = 2
                menuOpen = False
                gameStarted = True

            pygame.display.update()
        #------------------------#

        elif gameStarted:

            mvingSq = RectBlit(colours['green'], (x, y, 100, 100))
            mvingSq.createBlit(screen)

            #click the box game
            #------------------------#
            if gameMode == 1:
                if x < 10:
                    y -= yChange
                    if y < 10:
                        x += xChange
                elif y < 10:
                    x += xChange
                    if x > screenWidth - 120:
                        y += yChange
                elif x > screenWidth - 120:
                    y += yChange
                    if y > screenHeight - 110:
                        x -= xChange
                elif y > screenHeight - 110:
                    x -= xChange

                checkCollide(gameEvents)
                if pos[0] > x and pos[0] < x + 100 and pos[1] > y and pos[1] < y + 100:
                    xChange = 0
                    yChange = 0
                    message_display('Stopped!', 115, screenWidth/2, screenHeight/2)
                    gameOver = True
            #------------------------#

            #help the box game
            #------------------------#
            elif gameMode == 2:
                pass
                message_display('Soon', 115, screenWidth/2, screenHeight/2)
                gameOver = True
            #------------------------#
            
            #refesh display
            #------------------------#
            pygame.display.update()
            pause(50)

            if gameOver == False:
                screen.fill(colours["black"])

            pygame.display.update()
            #------------------------#
        

if __name__ == "__main__":
    main()
