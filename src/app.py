import pygame
from createBlitz import RectBlit,colours

def checkcollide():
    pass

def main():

    screenHeight = 480
    screenWidth = 720

    pygame.init()
    pygame.display.set_caption("Hello Game")

    display = pygame.display
    screen = display.set_mode((screenWidth,screenHeight), pygame.RESIZABLE)
    display.init()

    def pause(t):
        pygame.time.delay(t)

    x = screenWidth * 0.45 #centered
    y = screenHeight * 0.8 #bottom page
    #^ these two var may need to change in the future. prob make local in functions. 

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

        #moving the box
        #---------------------------------#
        xChange = 30
        yChange = 20

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
        #---------------------------------#
        
        pygame.display.update()
        pause(50)
        screen.fill(colours["black"])
        print("({},{})".format(x,y))
        pygame.display.update()
        

if __name__ == "__main__":
    main()
