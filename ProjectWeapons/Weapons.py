import pygame
pygame.init()

letsgo = True
screen = pygame.display.set_mode((1600, 700))
a = 800
b = 350


def on_mouse_motion(event):
    x, y = event.pos


while letsgo:
    pygame.draw.circle(screen, (255, 255, 0), (a, b), 50)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            letsgo = False
        elif event.type == pygame.MOUSEMOTION:
            on_mouse_motion(event)



