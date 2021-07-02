import pygame


def main():

    pygame.init()

    pygame.display.set_caption("Hello Game")

    screen = pygame.display.set_mode((720,480))

    running = True

    #main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()


if __name__ == "__main__":
    main()