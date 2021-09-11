import pygame,sys

screen_width = 800
screen_height = 700


class Bouncing_rect:
    def __init__(self, x, y, width, height, color, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen





        # self.moving_rect = pygame.Rect(350, 350, 100, 100)
        # self.x_speed = 5
        # self.y_speed = 5
        #
        # self.other_rect = pygame.Rect(300, 600, 200, 100)
        # self.other_x_speed = 2
        # self.other_y_speed = 3
        #
        # pygame.draw.rect(self.screen, (36, 37, 37), self.moving_rect)
        # pygame.draw.rect(self.screen, (36, 37, 37), self.other_rect)


def main():
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((screen_width, screen_height))
    moving_rect = pygame.Rect(350, 350, 100, 100, (200,200,200), screen)
    bouncing_rect = Bouncing_rect()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        screen.fill((170, 210, 50))
        bouncing_rect(screen)

        clock.tick(60)


if __name__ == '__main__':
    main()
