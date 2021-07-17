import pygame
from createBlitz import RectBlit,colours

def moveSquare(x,y,maxX,maxY):

    pygame.time.delay(1000)
            
    """
    for event in gameEvents:
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
    
        if mvingSq.rect.collidepoint(pos):
            attacked == True
    """

    if x == 10:
        y -= 10
        x += 1
        print("a")
        

    elif y == maxY - 10:
        x += 5 
        y -= 1
        print("b")
        
        
    elif x == maxX - 10:
        y += 10
        x -= 1
        print("c")
    

    elif y == 10:
        x -= 5
        y += 1
        print("d")
        

    else:
        x -= 5
        print('e')
        
    pygame.display.update()


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

        relativeX = screenWidth * 0.45 #centered
        relativeY = screenHeight * 0.8 #bottom page
        #^ these two var may need to change in the future. prob make local in functions. 

        mvingSq = RectBlit(colours['green'], (relativeX, relativeY, 100, 100))
        mvingSq.createBlit(screen)

        attacked = False
        while attacked is False:
            moveSquare(relativeX,relativeY,screenWidth,screenHeight)


        pygame.display.update()


if __name__ == "__main__":
    main()
