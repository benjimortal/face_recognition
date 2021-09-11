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
        if not self.radius <= self.x <= SCREEN_WIDTH - self.radius:
            self.x_step *= -1
        self.y += self.y_step
        if not self.radius <= self.y <= SCREEN_HEIGHT - self.radius:
            self.y_step *= -1


    def draw(self):
        pygame.draw.circle(self.screen, self.color,(self.x, self.y), self.radius)

    def collide(self, paddle):
        pass

    def show_next_hit(self):
        pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), )
    # ball = Ball(300, 400, -2, -2, random.choice(COLORS), random.randint(10,40), screen)

    balls = []
    for i in range(25):
        x = random.randrange(MAX_RADIUS, SCREEN_WIDTH - MAX_RADIUS)
        y = random.randrange(MAX_RADIUS, SCREEN_HEIGHT - MAX_RADIUS)
        x_step = random.choice([-3, -2, -1, 1, 2, 3])
        y_step = random.choice([-3,-2,-1,1,2,3])
        color = random.choice(COLORS)
        radius = random.randrange(5,MAX_RADIUS)
        ball = Ball(x, y, x_step, y_step,color, radius, screen)
        balls.append(ball)




    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(LightC)
        for ball in balls:
            ball.move()
            ball.draw()
        pygame.display.update()
        clock.tick(FPS)



if __name__ == '__main__':
    main()
