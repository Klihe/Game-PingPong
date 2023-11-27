import pygame
import random
import math

pygame.init()

# Settings
winWidth = 1920
winHeight = 1080

# Config
pygame.display.set_caption("Ping Pong")
winMain = pygame.display.set_mode((winWidth, winHeight))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Const variables

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (204, 49, 61)
BLUE = (64, 142, 198)
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
        self.score = 0
        self.lastUse1 = 0

    def movement(self, up, down):
        if keys[up] and self.y > 0:
            self.y -= self.speed
        if keys[down] and self.y < winHeight - self.height:
            self.y += self.speed

    def ability(self, slot, cooldownTime, currentTime):
        if keys[slot] and currentTime - self.lastUse1 > cooldownTime:
            self.score += 10
            self.lastUse1 = currentTime

    def update(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

# Ball
class Ball():
    def __init__(self, x, y, radius, speed, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.color = color
        self.direction = random.choice([-45, -225, 45, 225])
    
    def movement(self):
        self.x += int(self.speed * math.cos(math.radians(self.direction)))
        self.y += int(self.speed * math.sin(math.radians(self.direction)))

        if self.y - self.radius <= 0 or self.y + self.radius >= winHeight:
            self.direction = -self.direction
        
        if self.x - self.radius <= 0:
            player2.score += 1
            self.speed = 10
            self.reset([-45, 45])
        
        elif self.x + self.radius >= winWidth:
            player1.score += 1
            self.speed = 10
            self.reset([-225, 225])
    
    def checkCollision(self, player):
        if (
            self.x + self.radius >= player.x
            and self.x - self.radius <= player.x + player.width
            and self.y + self.radius >= player.y
            and self.y - self.radius <= player.y + player.height
        ):
            self.direction = 180 - self.direction
            self.speed += 1
    
    def reset(self, direction):
        self.x = winWidth // 2
        self.y = winHeight // 2
        self.direction = random.choice(direction)

    def update(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

# Update Frame
def winUpdate():
    winMain.fill(BLACK)
    # class
    player1.update(winMain)
    player2.update(winMain)
    ball.update(winMain)
    # text
    score_text1 = font.render("Score: " + str(player1.score), True, WHITE)
    score_text2 = font.render("Score: " + str(player2.score), True, WHITE)
    winMain.blit(score_text1, (20, 20))
    winMain.blit(score_text2, (winWidth - 150, 20))

    pygame.display.update()

# Create objects
player1 = Player(BLOCK / 2, winHeight / 2, BLOCK / 2, BLOCK * 2, 10, RED)
player2 = Player(winWidth - BLOCK / 2 - BLOCK / 2, winHeight / 2, BLOCK / 2, BLOCK * 2, 10, BLUE)
ball = Ball(winWidth / 2, winHeight / 2, BLOCK / 4, 10, WHITE)

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

    currentTime = pygame.time.get_ticks()

    player1.movement(pygame.K_w, pygame.K_s)
    player2.movement(pygame.K_UP, pygame.K_DOWN)
    ball.movement()

    player1.ability(pygame.K_SPACE, 5000, currentTime)

    ball.checkCollision(player1)
    ball.checkCollision(player2)

    winUpdate()

pygame.quit()