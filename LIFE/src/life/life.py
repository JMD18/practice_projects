import time
import pygame
import numpy as np

BG_COLOR = (10,10,10)
GRID_COLOR = (40,40,40)
DYING_COLOR = (170,170,170)
ALIVE_COLOR = (255,255,255)


# update screen with or without progress (new generation)
def update(screen, cells, size, with_progress = False):

    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row,col]
        color = BG_COLOR if cells[row,col] == 0 else ALIVE_COLOR

        if cells[row,col] == 1:
            if alive < 2 or alive > 3:
                if with_progress: color = DYING_COLOR

            elif 2 <= alive <= 3 : 
                updated_cells[row,col] = 1 
                if with_progress: color = ALIVE_COLOR

        else:
            if alive == 3:
                updated_cells[row,col] = 1
                if with_progress: color = ALIVE_COLOR

        pygame.draw.rect(screen, color, (col*size, row*size, size-1, size-1))

    return updated_cells


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    pygame.display.set_caption("Conway's Game of Life - JMD18")
    try: icon = pygame.image.load("glider_icon.jpg")
    except UnicodeEncodeError:
        pass
    pygame.display.set_icon(icon)

    cells = np.zeros((72,128))
    screen.fill(GRID_COLOR)
    update(screen,cells,10)


    pygame.display.flip()
    pygame.display.update()

    running = False

    # main game loop
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: 
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                try:
                    cells[pos[1] // 10, pos[0] // 10] = 1
                except Exception as e:
                    print(e)
                update(screen, cells, 10)
                pygame.display.update()
            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                try:
                    cells[pos[1] // 10, pos[0] // 10] = 0
                except Exception as e:
                    print(e)
                update(screen, cells, 10)
                pygame.display.update()

        screen.fill(GRID_COLOR)

        if running:
            cells = update(screen,cells,10,with_progress=True)
            pygame.display.update()

        time.sleep(0.001)

if __name__ == "__main__":
    main()