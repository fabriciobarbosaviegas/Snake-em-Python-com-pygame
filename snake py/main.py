import pygame, random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0,390)
    y = random.randint (0,390)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGTH = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption('Snake py')

snake = [(200,200), (210,200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((0,255,0))

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

my_direction = LEFT

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0
game_over = False
while not game_over:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                my_direction = DOWN
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                my_direction = LEFT
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                my_direction = RIGTH

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        score += 1
    if snake[0][0] == 400 or snake[0][1] == 400 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        print('Game Over')
        print(f'total de pontos: {score}')
        break
    for i in range(len(snake) -1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] -10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] +10)
    if my_direction == RIGTH:
        snake[0] = (snake[0][0] +10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] -10, snake[0][1])

    for i in range(len(snake) -1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)   

    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (400 - 120, 10)
    screen.blit(score_font, score_rect)

    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()