import pygame

pygame.init()

BACKGROUND = (175, 175, 175)
SNAKE_COLOR = (0, 255, 0)
APPLE_COLOR = (255, 0, 0)

size = [400, 400]

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

POS = []


def draw_snake(position):
    block = pygame.Rect((position[1] * 20, position[0] * 20), (20, 20))
    pygame.draw.rect(screen, SNAKE_COLOR, block)


def draw_apple(position):
    pygame.draw.circle(screen, APPLE_COLOR, (position[1] * 20 + 10, position[0] * 20 + 10), 10)


def runGame():
    pos_snake = [5, 5]
    pos_apple = [3, 3]
    done = False
    while not done:
        screen.fill(BACKGROUND)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pos_snake[0] = pos_snake[0] - 1
                    if pos_snake[0] < 0:
                        pos_snake[0] = 0
                elif event.key == pygame.K_DOWN:
                    pos_snake[0] = pos_snake[0] + 1
                    if pos_snake[0] > 19:
                        pos_snake[0] = 19
                elif event.key == pygame.K_LEFT:
                    pos_snake[1] = pos_snake[1] - 1
                    if pos_snake[1] < 0:
                        pos_snake[1] = 0
                elif event.key == pygame.K_RIGHT:
                    pos_snake[1] = pos_snake[1] + 1
                    if pos_snake[1] > 19:
                        pos_snake[1] = 19

        draw_snake(pos_snake)
        draw_apple(pos_apple)
        pygame.display.update()


runGame()
pygame.quit()
