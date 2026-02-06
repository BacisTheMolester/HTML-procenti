import pygame
import time
import random

snake_speed = 20
window_x = 1080
window_y = 920
game = False
sakums = True

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(106, 159, 181)
yellow = pygame.Color(255, 255, 0)
orange = pygame.Color(255, 165, 0)

pygame.init()
pygame.display.set_caption('Čūska')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

snake_position = [100, 50]
snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50],
    [60, 50]
]

fruit_skaits = 67 
fruits = [
    [random.randrange(1, (window_x // 10)) * 10,
     random.randrange(1, (window_y // 10)) * 10]
    for _ in range(fruit_skaits)
]

direction = 'RIGHT'
change_to = direction
score = 0

def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Punkti ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (window_x / 2 , window_y / 120)
    game_window.blit(score_surface, score_rect)

def check_fruit_collision(snake_position, fruits):
    global score
    for i, fruit_pos in enumerate(fruits):
        if snake_position[0] == fruit_pos[0] and snake_position[1] == fruit_pos[1]:
            score += 1
            fruits[i] = [random.randrange(1, (window_x // 10)) * 10,
                         random.randrange(1, (window_y // 10)) * 10]
            return True
    return False

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Spēle beidzās.', True, white)
    game_over_score = my_font.render('Tavs Punktu skaits ir : ' + str(score), True, white)
    game_over_rect_1 = game_over_surface.get_rect()
    game_over_rect_2 = game_over_score.get_rect()
    game_over_rect_1.midtop = (window_x / 2, window_y / 4)
    game_over_rect_2.midtop = (window_x / 2, window_y / 3)
    game_window.blit(game_over_surface, game_over_rect_1)
    game_window.blit(game_over_score, game_over_rect_2)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    quit()

while sakums:
     game_window.fill(white)
     my_font = pygame.font.SysFont('times new roman', 50)
     sakums_kontroles = my_font.render('Kontroles ir w,a,s,d vai bultiņas', True, black)
     sakuma_nosacijumi = my_font.render('(Lai beigtu spēli jebkurā laikā nospied esc)', True, black)
     start_surface = my_font.render('Nospied esc, lai sāktu', True, black)
     start_surface_1 = my_font.render('Primatīva čūska', True, black)
     image = pygame.image.load("snake_1.jpeg")
     start_rect_1 = start_surface.get_rect()
     start_rect_2 = start_surface_1.get_rect()
     start_rect_3 = sakums_kontroles.get_rect()
     start_rect_4 = sakuma_nosacijumi.get_rect()
     start_rect_1.midtop = (window_x / 2, window_y / 3)
     start_rect_2.midtop = (window_x / 2, window_y / 5)
     start_rect_3.midtop = (window_x / 2, window_y / 2)
     start_rect_4.midtop = (window_x / 2, window_y / 2.4)
     game_window.blit(image, (window_x / 3.5, window_y / 2.5))
     game_window.blit(start_surface, start_rect_1)
     game_window.blit(start_surface_1, start_rect_2)
     game_window.blit(sakums_kontroles, start_rect_3)
     game_window.blit(sakuma_nosacijumi, start_rect_4)
     pygame.display.flip()
     for event in pygame.event.get():
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_ESCAPE:
                 game = True
                 sakums = False
     pygame.display.update()

while game:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))

    ate_fruit = check_fruit_collision(snake_position, fruits)
    if not ate_fruit:
        snake_body.pop()

    game_window.fill(black)

    for i, pos in enumerate(snake_body):
        if i % 2 == 0:
            color = green
        else:
            color = blue
        pygame.draw.rect(game_window,color , pygame.Rect(pos[0], pos[1], 10, 10))

    for i, fruit_pos in enumerate(fruits):
        if i % 2 == 0:
            color_1 = red
        elif i % 3 == 0:
            color_1 = green
        else:
            color_1 = orange
        pygame.draw.rect(game_window, color_1, pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(yellow, 'Courier', 20)

    pygame.display.update()
    fps.tick(snake_speed)