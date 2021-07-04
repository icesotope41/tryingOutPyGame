import pygame
import createBlitz

def main():

    pygame.init()

    pygame.display.set_caption("Hello Game")

    screen = pygame.display.set_mode((720,480))

    running = True

    createBlitz.drawShapes(createBlitz.simpleRect)
    
    #main loop
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()

        

        pygame.display.flip()


if __name__ == "__main__":
    main()