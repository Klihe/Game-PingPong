import pygame

pygame.init()

# Settings
winWidth = 1920
winHeight = 1080

# Config
winMain = pygame.display.set_mode((winWidth, winHeight))
clock = pygame.time.Clock()

# Const variables

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Values
BLOCK = 60

# Player
class Player():
    def __init__(self, x, y, width, height, speed, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

    def movement(self, up, down):
        if keys[up] and self.y > 0:
            self.y -= self.speed
        if keys[down] and self.y < winHeight - self.height:
            self.y += self.speed

    def update(self, win):
        pygame.draw.rect(win, WHITE, (self.x, self.y, self.width, self.height))

# Update Frame
def winUpdate():
    winMain.fill(BLACK)
    player1.update(winMain)
    player2.update(winMain)
    pygame.display.update()

# Create objects
player1 = Player(BLOCK, winHeight / 2, BLOCK / 2, BLOCK * 2, 10, WHITE)
player2 = Player(winWidth - BLOCK - BLOCK / 2, winHeight / 2, BLOCK / 2, BLOCK * 2, 10, WHITE)

# Game
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
            game_display = pygame.display.set_mode((winWidth, winHeight))

    player1.movement(pygame.K_w, pygame.K_s)
    player2.movement(pygame.K_UP, pygame.K_DOWN)

    winUpdate()

pygame.quit()