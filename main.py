import pygame

active = True

up = False
down = False
right = False
left = False

fps = pygame.time.Clock()

count = 0

window = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("AviatIo")

fon = pygame.image.load("fon.png")
fon = pygame.transform.scale(fon, (1200, 700))

test = pygame.image.load("test.png")

frames = [
    pygame.image.load("plane0l.png"),
    pygame.image.load("plane1l.png"),
    pygame.image.load("plane2l.png"),
    pygame.image.load("plane0r.png"),
    pygame.image.load("plane1r.png"),
    pygame.image.load("plane2r.png"),
    pygame.image.load("plane0d.png"),
    pygame.image.load("plane1d.png"),
    pygame.image.load("plane2d.png"),
    pygame.image.load("plane0u.png"),
    pygame.image.load("plane1u.png"),
    pygame.image.load("plane2u.png")
]

class Sprite():
    def __init__(self, img, x, y, w, h):
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
test = Sprite("test.png", 100, 100, 351, 214)

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)


x = 500
y = 250

while active:
    
    window.blit(fon, (0, 0))
    test.draw()

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            active = False
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_a:
                left = True
            if ev.key == pygame.K_d:
                right = True
            if ev.key == pygame.K_w:
                up = True
            if ev.key == pygame.K_s:
                down = True
        if ev.type == pygame.KEYUP:
            if ev.key == pygame.K_a:
                left = False
            if ev.key == pygame.K_d:
                right = False
            if ev.key == pygame.K_w:
                up = False
            if ev.key == pygame.K_s:
                down = False
        if left == True:
            window.blit(frames[count], (test.rect.x, test.rect.y))
            test.rect.x -= 5
        if right == True:
            window.blit(frames[count], (test.rect.x, test.rect.y))
            test.rect.x += 5
        if down == True:
            window.blit(frames[count], (test.rect.x, test.rect.y))
            test.rect.y -= 5
        if up == True:
            window.blit(frames[count], (test.rect.x, test.rect.y))
            test.rect.y += 5
        if count == 3:
            count = 0

    pygame.display.update()
    fps.tick(40)
