import pygame

pygame.init()
# set screen size
screen = pygame.display.set_mode((800, 600))
# set title
pygame.display.set_caption("Pong")
class Paddle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.x_direction = 0.2
        self.y_direction = 0.2
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    def move(self):
        self.x += self.x_direction
        self.y += self.y_direction
paddle1 = Paddle(10, 10, 10, 100, (255, 255, 255))
paddle2 = Paddle(780, 10, 10, 100, (255, 255, 255))
ball = Ball(400, 300, 10, (100, 100, 100))
score1 = 0
score2 = 0
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    # if w is pressed
    if pygame.key.get_pressed()[pygame.K_w]:
        paddle1.y -= 1
    # if s is pressed
    if pygame.key.get_pressed()[pygame.K_s]:
        paddle1.y += 1
    # if up is pressed
    if pygame.key.get_pressed()[pygame.K_UP]:
        paddle2.y -= 1
    # if down is pressed
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        paddle2.y += 1
    # if paddle 1 is out of bounds (top) set it to 0
    if paddle1.y < 0:
        paddle1.y = 0
    # if paddle 1 is out of bounds (bottom) set it to 500
    if paddle1.y > 500:
        paddle1.y = 500
    # if paddle 2 is out of bounds (top) set it to 0
    if paddle2.y < 0:
        paddle2.y = 0
    # if paddle 2 is out of bounds (bottom) set it to 500
    if paddle2.y > 500:
        paddle2.y = 500
    # move ball
    ball.move()
    # if ball is out of bounds (left) increase score 2 and reset ball
    if ball.x < 0:
        score2 += 1
        ball.x = 400
        ball.y = 300
    # if ball is out of bounds (right) increase score 1 and reset ball
    if ball.x > 800:
        score1 += 1
        ball.x = 400
        ball.y = 300
    # if ball is out of bounds (top) change direction
    if ball.y < 0:
        ball.y_direction *= -1
    # if ball is out of bounds (bottom) change direction
    if ball.y > 600:
        ball.y_direction *= -1
    # if ball collides with paddle 1 change direction
    if ball.x - ball.radius < paddle1.x + paddle1.width and ball.y - ball.radius < paddle1.y + paddle1.height and ball.y + ball.radius > paddle1.y:
        ball.x_direction *= -1
    # if ball collides with paddle 2 change direction
    if ball.x + ball.radius > paddle2.x and ball.y - ball.radius < paddle2.y + paddle2.height and ball.y + ball.radius > paddle2.y:
        ball.x_direction *= -1
    ball.move()
    # if score1 or score2 excedes 10 end game and print winner on screen
    if score1 == 5 or score2 == 5:
        if (score1 > score2):
            font = pygame.font.SysFont("comicsansms", 72)
            text = font.render("Player 1 wins!", True, (255, 255, 255))
            screen.blit(text, (200, 200))
        else:
            font = pygame.font.SysFont("comicsansms", 72)
            text = font.render("Player 2 wins!", True, (255, 255, 255))
            screen.blit(text, (200, 200))
        pygame.display.update()
        pygame.time.wait(5000)
        pygame.quit()
        quit()
    # print ball
    screen.fill((0, 0, 0))
    #print score
    font = pygame.font.SysFont("comicsans", 30)
    text = font.render(str(score1), 1, (255, 255, 255))
    screen.blit(text, (350, 10))
    text = font.render(str(score2), 1, (255, 255, 255))
    screen.blit(text, (450, 10))

    ball.draw(screen)
    paddle1.draw(screen)
    paddle2.draw(screen)
    pygame.display.update()