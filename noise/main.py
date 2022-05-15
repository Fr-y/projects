import random
import pygame
# for blur
from PIL import Image, ImageFilter
pygame.init()

size = WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode(size)
pygame.display.set_caption("Noise")

noise = pygame.Surface(size, pygame.SRCALPHA)


# def blurSurf(surface, amt):
#     if amt < 1.0:
#         raise ValueError("Arg 'amt' must be greater than 1.0, passed in value is %s"%amt)
#     scale = 1.0/float(amt)
#     surf_size = surface.get_size()
#     scale_size = (int(surf_size[0]*scale), int(surf_size[1]*scale))
#     surf = pygame.transform.smoothscale(surface, scale_size)
#     surf = pygame.transform.smoothscale(surf, surf_size)
#     return surf

def generate():
    pxarray = pygame.PixelArray(noise)
    for i, px in enumerate(pxarray):
        print(i)





def generate_points():
    noise.fill((0,0,0,255))
    pxarray = pygame.PixelArray(noise)
    for i, px in enumerate(pxarray):
        for n in range(len(pxarray[i])):
            r = random.randint(0, (WIDTH * HEIGHT) / 1000)
            if r == 0:
                pxarray[i][n] = (255, 255, 255, random.randint(0,255))
    print(255 - i/len(pxarray))
    del pxarray



def main():
    run = True
    clock = pygame.time.Clock()
    generate_points()
    generate()
    WIN.blit(noise, (0, 0))



    while run:
        clock.tick(1)
        # surf = blurSurf(WIN, 10)
        # WIN.blit(surf, (0, 0))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

main()