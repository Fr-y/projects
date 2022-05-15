import pygame
pygame.init()

size = WIDTH, HEIGHT = 1500, 1500
WIN = pygame.display.set_mode(size)
pygame.display.set_caption("ulan")

FONT = pygame.font.SysFont("ariel", 100)

def prim(num):
    osztok = sum(num % i == 0 for i in range(1, num+1))
    return osztok == 2


def draw(step, x, y, px, py):

    # num = FONT.render(f'{step}', 1, (255, 255, 255))
    # WIN.blit(num, (x,y))
    if prim(step):
        pygame.draw.circle(WIN, (255, 255, 255), (x, y), 2)
    pygame.draw.lines(WIN, (255, 255, 255), False, [(x, y), (px, py)], 1)




def func():
    x, y  = size[0] / 2, size[1] / 2
    stepSize = 10
    numSteps = 1
    state = 0
    turnCounter = 0
    px, py = x, y

    for step in range(1, 20000):
        # print(px, py, x, y)
        draw(step, x, y, px, py)
        px, py = x, y
        if state == 0:
            x += stepSize
        elif state == 1:
            y -= stepSize
        elif state == 2:
            x -= stepSize
        elif state == 3:
            y += stepSize

        if step % numSteps == 0:
            state = (state + 1) % 4
            turnCounter += 1
            if turnCounter % 2 == 0:
                numSteps += 1






def main():
    run = True
    func()


    while run:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

main()












    # selfsize = FONT.size(str(step))
    # drawX, drawY = x - (selfsize[0] / 2.), y + (selfsize[1] / 2.)