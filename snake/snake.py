import pygame

pygame.init()
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
size = [400,400]
screen = pygame.display.set_mode(size)

clock= pygame.time.Clock()

def draw_block(screen, color, position):
    block = pygame.Rect((position[1] * 20, position[0] * 20), (20, 20))
    pygame.draw.rect(screen, color, block)


def runGame():
    pos_x = 1
    pos_y = 1
    done = False
    while not done:
        clock.tick(10)
        screen.fill(GREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                done = True
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pos_x = pos_x - 1
                elif event.key == pygame.K_DOWN:
                    pos_x = pos_x + 1
                elif event.key == pygame.K_LEFT:
                    pos_y = pos_y - 1
                elif event.key == pygame.K_RIGHT:
                    pos_y = pos_y + 1

                
        draw_block(screen, RED, (pos_x, pos_y))
        pygame.display.update()

runGame()
pygame.quit()
