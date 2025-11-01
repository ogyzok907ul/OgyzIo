import pygame

active = True

window = pygame.display.set_mode((1200, 700))
fon = pygame.image.load("fon.png")
fon = pygame.transform.scale(fon, (1200, 700))
plane = pygame.image.load("samalet_neutral.png")

x = 500
y = 250

while active:
    window.blit(fon, (0, 0))
    window.blit(plane, (x, y))

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            active = False
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_a:
                x -= 25
            if ev.key == pygame.K_d:
                x += 25
            if ev.key == pygame.K_w:
                y -= 25
            if ev.key == pygame.K_s:
                y += 25

    pygame.display.update()