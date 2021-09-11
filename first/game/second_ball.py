import pygame
import random
from settings import *



class Ball:
    def __init__(self, x, y, x_step, y_step, color, radius, screen):
        self.x = x
        self.y = y
        self.x_step = x_step
        self.y_step = y_step
        self.color = color
        self.radius = radius
        self.screen = screen

    def move(self):
        self.x += self.x_step
        self.y += self.y_step

        if not self.radius <= self.x <= SCREEN_WIDTH - self.radius:
            self.x_step *= -1

        if not self.radius <= self.y <= SCREEN_HEIGHT - self.radius:
            self.y_step *= -1


        box_left = 350
        box_right = 450
        box_top = 250
        box_bottom = 350

        if box_left <= self.x <= box_right:
            if box_top <= self.y <= box_bottom:
                #we got a hit

                #left side?

                if box_left <= self.x <= box_left+ self.radius:
                    self.x_step *= -1

                # right side?

                if box_right <= self.x <= box_right - self.radius:
                    self.y_step *= -1

                # bottom side?

                if box_bottom <= self.y <= box_bottom + self.radius:
                    self.y_step *= -1

                # upper side?

                if box_top <= self.y <= box_top - self.radius:
                    self.y_step *= -1

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def collide(self, paddle):
        pass

    def show_next_hit(self):
        shadow_x = self.x
        shadow_y = self.y

        no_hit = True
        while no_hit:
            shadow_x += self.x_step
            shadow_y += self.y_step

            if not self.radius <= shadow_x <= SCREEN_WIDTH - self.radius:
                no_hit = False

            if not self.radius <= shadow_y <= SCREEN_HEIGHT - self.radius:
                no_hit = False

        pygame.draw.circle(self.screen, self.color, (shadow_x, shadow_y), self.radius, 5)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ball = Ball(300, 600, -1, 1, random.choice(COLORS), random.randint(10,20), screen)

    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(Thistle)
        ball.draw()
        ball.move()
        pygame.draw.rect(screen, Gold,(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50, 100, 100))
        #ball.show_next_hit()
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
