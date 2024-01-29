import pygame
from constants import *
from snake import Snake


def main():
    pygame.init()

    snake = Snake(200, 200)
    running = True

    while running:
        CLOCK.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # LOGIC
        keys = pygame.key.get_pressed()
        
        # Allow snake to move if alive
        if snake.alive:
            if keys[pygame.K_RIGHT] and snake.right == False:
                snake.right, snake.left, snake.up, snake.down = True, False, False, False
            elif keys[pygame. K_LEFT] and snake.left == False:
                snake.right, snake.left, snake.up, snake.down = False, True, False, False
            elif keys[pygame.K_UP] and snake.up == False:
                snake.right, snake.left, snake.up, snake.down = False, False, True, False
            elif keys[pygame.K_DOWN] and snake.down == False:
                snake.right, snake.left, snake.up, snake.down = False, False, False, True

        # COLLISION
        if snake.x >= HORIZONTAL - snake.length or snake.x <= 0 or snake.y <= 0 or snake.y >= VERTICAL - snake.length:
            snake.alive = False
        
        # DISPLAY
        SCREEN.fill('black')
        snake.update(SCREEN)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
