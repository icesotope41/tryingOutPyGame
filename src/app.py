import pygame
from createBlitz import RectBlit,colours

screenHeight = 480
screenWidth = 720

def text_objects(text, font):
    textSurface = font.render(text, True, colours["black"])
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((screenWidth/2),(screenHeight/2))
    screen.blit(TextSurf, TextRect)


def checkCollide(gameEvents, rightXCoord, topYCoord):
    global pos
    pos = (-1000, -1000)
    leftXCoord = rightXCoord + 100
    botYCoord = topYCoord + 100

    for event in gameEvents:
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

            print(pos[0] > rightXCoord and pos[0] < leftXCoord and pos[1] > topYCoord and pos[1] < botYCoord)
            

def main():
    pygame.init()
    pygame.display.set_caption("Hello Game")

    xChange = 30
    yChange = 20
    x = screenWidth * 0.45 #centered(in small window...)
    y = screenHeight * 0.8 #bottom page
    #^ these two var may need to change in the future. prob make local in functions. 
    
    display = pygame.display
    global screen 
    screen = display.set_mode((screenWidth,screenHeight), pygame.RESIZABLE)
    display.init()

    def pause(t):
        pygame.time.delay(t)

    #main loop
    running = True
    while running:
        gameEvents = pygame.event.get()

        for event in gameEvents:
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()

        mvingSq = RectBlit(colours['green'], (x, y, 100, 100))
        mvingSq.createBlit(screen)

        #------------------------#
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
        #------------------------#

        checkCollide(gameEvents, x, y)
        if pos[0] > x and pos[0] < x + 100 and pos[1] > y and pos[1] < y + 100:
                xChange = 0
                yChange = 0
        
        pygame.display.update()
        pause(50)
        screen.fill(colours["black"])
        #print("({},{})".format(x,y))
        pygame.display.update()
        

if __name__ == "__main__":
    main()
