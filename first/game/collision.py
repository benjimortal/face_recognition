import pygame
from settings import *

class Rect:
    def __init__(self, x, y, width, height, color, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen


    def top(self):
        return self.y

    def bottom(self):
        return self.y + self.height

    def left(self):
        return self.x

    def right(self):
        return self.x + self.width


    def draw(self):
        pygame.draw.rect(self.screen, self.color,(self.x ,self.y, self.width ,self.height),3)

    def collied(self, other):
        pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    red_rect = Rect(200, 200, 50, 50, RED, screen)
    white_rect = Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50, 100, 100 , WHITE, screen)

    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    red_rect.x -= 20
                elif event.key == pygame.K_RIGHT:
                    red_rect.x += 20
                elif event.key == pygame.K_UP:
                    red_rect.y -= 20
                elif event.key == pygame.K_DOWN:
                    red_rect.y += 20




        screen.fill(Thistle)
        red_rect.draw()
        white_rect.draw()
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
