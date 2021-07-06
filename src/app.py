import pygame
import createBlitz

def main():

    pygame.init()

    pygame.display.set_caption("Hello Game")

    global screen
    screen = pygame.display.set_mode((720,480))
    
    running = True
    #main loop
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()

        #pygame.draw.rect(screen, (0,255,0), (10,10,100,200))
        newRect = RectBlit(blue, (10,10,100,200))
        newRect.createBlit(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
