import pygame


SCREEN_WIDTH =800
SCREEN_HEIGHT = 600
FPS = 100
BALL_SIZE = 20
WHITE = (155, 205, 200)
BLACK = (0, 10, 200)
RED = (240, 100, 80)
GREEN = (0, 200, 0)
BLUE = (0, 100, 250)

class Ball:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def move(self):
        pass

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    x = 400
    x_step = 2 # vi vill ha den förändringar att x ska ha om den slår på kanterna


    y = 300
    y_step = 2 # detta gör att bollen ändrar riktningen antingen i x led eller i y led

    x1 = 100
    x_step1 = 2  # vi vill ha den förändringar att x ska ha om den slår på kanterna

    y1 = 300
    y_step1 = 2  # detta gör att bollen ändrar riktningen antingen i x led eller i y led



    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        screen.fill(BLUE)
        pygame.draw.circle(screen, GREEN, (x, y),BALL_SIZE)
        pygame.draw.circle(screen,RED, (x1,y1), BALL_SIZE, 2)
        pygame.display.update()
        x += x_step
        if not 20 <= x <= SCREEN_WIDTH - 20:
            x_step *= -1

        y += y_step
        if not 20 <= y <= SCREEN_HEIGHT - 20:
            y_step *= -1

        x1 += x_step1
        if not 20 <= x1 <= SCREEN_WIDTH - 20:
            x_step1 *= -1

        y1 += y_step1
        if not 20 <= y1 <= SCREEN_HEIGHT - 20:
            y_step1 *= -1

        clock.tick(FPS)



if __name__ == '__main__':
    main()
