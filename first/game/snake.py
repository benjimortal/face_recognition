import pygame, sys

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500

WHITE = (155, 205, 200)
BLACK = (0, 10, 200)
RED = (240, 100, 80)
GREEN = (10, 200, 10)
BLUE = (0, 100, 250)




def main():
    pygame.init()
    pygame.display.set_caption('SNAKE')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    test_surface = pygame.Surface((100,200))
    x_pose = 200
    y_pose = 250
    #test_rect = pygame.Rect(100, 200, 100, 100) # (x, y, width, height)
    test_rect = test_surface.get_rect(center = (200,250)) # den lägger en rectangle runt object test_surface


    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((170, 210, 50))
        test_surface.fill((0, 0, 255))
        test_rect.left += 1
        # y_pose -= 1
        # x_pose -= 1
        #pygame.draw.rect(screen, RED, test_rect) # (surface, color, rectangle)

        screen.blit(test_surface, test_rect)
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
