import pygame
from createBlitz import RectBlit,colours


def main():

    screenHeight = 480
    screenWidth = 720

    pygame.init()
    pygame.display.set_caption("Hello Game")

    display = pygame.display
    screen = display.set_mode((screenWidth,screenHeight), pygame.RESIZABLE)
    display.init()

    #main loop
    running = True
    while running:
        gameEvents = pygame.event.get()

        for event in gameEvents:
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()

        #----------------------------------#

        relativeX = screenWidth * 0.45 #centered
        relativeY = screenHeight * 0.8 #bottom page
        #^ these two var may need to change in the future. prob make local in functions. 

        newRect = RectBlit(colours['blue'], (relativeX,relativeY,100,200))
        newRect.createBlit(screen)

        attacked = False
        while attacked == False:

            mvingSq = RectBlit(colours['green'], (relativeX, relativeY, 100, 100))
            mvingSq.createBlit(screen)

            for event in gameEvents:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
            
                if mvingSq.rect.collidepoint(pos):
                    attacked == True


            if relativeX == 10:
                relativeY -= 10
                relativeX += 1

            elif relativeY == screenHeight - 10:
                relativeX += 5 
                relativeY -= 1
        
            elif relativeX == screenWidth - 10:
                relativeY += 10
                relativeX -= 1

            elif relativeY == 10:
                relativeX -= 5
                relativeY += 1

            else:
                relativeX -= 5


        pygame.display.update()


if __name__ == "__main__":
    main()
