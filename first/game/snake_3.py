import pygame, sys
from pygame.locals import *
def main():
    pygame.init()
    surface = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('SNAKE')
    block = pygame.image.load('game/resources/block.jpg').convert()
    surface.blit(block, (0,0))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
    #             sys.exit()



        #pygame.display.flip()
        pygame.display.update() # is same as flip()
        surface.fill((161,215,226)) # fill background with a color



if __name__ == '__main__':
    main()
