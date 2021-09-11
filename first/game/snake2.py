import pygame, sys, random
from pygame.math import Vector2




WHITE = (155, 205, 200)
BLACK = (0, 10, 200)
RED = (240, 100, 80)
GREEN = (10, 200, 10)
BLUE = (0, 100, 250)



class FRUIT:
    def __init__(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1 )
        self.pos = Vector2(self.x, self.y)

        # create an x and y position
        # draw a square

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x) * cell_size, int(self.pos.y) * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, RED, fruit_rect)
        # create a rectangle
        # draw the rectangle


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
        for block in self.body:
            x_pose = int(block.x * cell_size)
            y_pose = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pose, y_pose, cell_size, cell_size)
            pygame.draw.rect(screen, BLUE , block_rect )
            # create a rectangle
            # draw the rectangle

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy[:]

# def main():
pygame.init()
cell_size = 40
cell_number = 20
pygame.display.set_caption('SNAKE')
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

fruit = FRUIT()
snake = SNAKE()

S_UPDATE = pygame.USEREVENT
pygame.time.set_timer(S_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.S_UPDATE:
            snake.move_snake()


    screen.fill((170, 210, 50))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)


# if __name__ == '__main__':
#     main()
