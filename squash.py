import pygame

# Variables

WIDTH = 1200
HEIGHT = 600
BORDER = 20
SPEED = 1
FRAMERATE = 800

# classes definitions


class Ball:

    RADIUS = 20

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def show(self, color):
        global screen
        pygame.draw.circle(screen, color, (self.x, self.y), self.RADIUS)

    def update(self):
        global bgColor, ballColor

        newx = self.x + self.vx
        newy = self.y + self.vy

        if newx < BORDER+self.RADIUS:
            self.vx = -self.vx
        elif newy < BORDER+self.RADIUS or newy > HEIGHT-BORDER-self.RADIUS:
            self.vy = -self.vy
        elif newx+self.RADIUS > WIDTH-Paddle.WIDTH and abs(newy-paddle.y) < Paddle.HEIGHT//2:
            self.vx = -self.vx
        else:
            self.show(bgColor)
            self.x += self.vx
            self.y += self.vy
            self.show(ballColor)


class Paddle:
    WIDTH = 20
    HEIGHT = 100

    def __init__(self, y):
        self.y = y

    def show(self, color):
        global screen
        pygame.draw.rect(screen, color, pygame.Rect(WIDTH-self.WIDTH, self.y-self.HEIGHT//2, self.WIDTH, self.HEIGHT))

    def update(self):
        global bgColor, padColor
        self.show(bgColor)
        self.y = pygame.mouse.get_pos()[1]
        self.show(padColor)


# create objects

ball = Ball(WIDTH-Ball.RADIUS-Paddle.WIDTH, HEIGHT//2, -SPEED, -SPEED)
paddle = Paddle(HEIGHT//2)

# Draw the game board

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

bgColor = pygame.Color('purple')
fgColor = pygame.Color('black')
ballColor = pygame.Color('black')
padColor = pygame.Color('black')

pygame.draw.rect(screen, fgColor, pygame.Rect(0, 0, WIDTH, BORDER))
pygame.draw.rect(screen, fgColor, pygame.Rect(0, 0, BORDER, HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0, HEIGHT-BORDER, WIDTH, BORDER))

paddle.show(padColor)
ball.show(ballColor)

clock = pygame.time.Clock()

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

    clock.tick(FRAMERATE)
    # visualize the changes
    pygame.display.flip()

    paddle.update()

    ball.update()

pygame.quit()
