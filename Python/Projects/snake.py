import pygame
from math import *
from pygame.locals import *
from collections import deque
import copy
from random import *

class Direction():
    right   = 1
    left    = 2
    down    = 3
    up      = 4

class Pos():
    x = 0
    y = 1
    dir = 2

class Snake:
    def __init__(self, x, y):
        pygame.init()
        self.height = 800
        self.width = 800
        self.x = x
        self.y = y
        self.snake = deque([[self.x, self.y, 1]])
        Snake.screen = pygame.display.set_mode((self.height, self.width))
        self.run = True
        self.size = 20
        self.speed = self.size
        self.has_sprite = False
        self.opposite = {1:2, 2:1, 3:4, 4:3}
        self.delta = {
                Direction.right:    [self.speed, 0], #right
                Direction.left:     [-self.speed, 0], #left
                Direction.down:     [0, self.speed],  #down
                Direction.up:       [0, -self.speed]  #up
                }
        self.clock = pygame.time.Clock()
        self.score = 0

    def draw_score_box(self, x, y):
        text = Text('Score: '+str(self.score), pos=(x,y), size=30)
        text.draw()

    def get_snake_head(self):
        x, y, _ = copy.deepcopy(self.snake[0])
        snake_head = pygame.Rect(x, y, self.size, self.size)
        return snake_head

    def snake_self_collision(self):
        snake_head = self.get_snake_head()
        for i in range(1,len(self.snake)):
            x, y, _ = self.snake[i]
            snake_tail = Rect(x, y, self.size, self.size)
            if snake_head.colliderect(snake_tail) == True:
                pos_head = self.snake[0][2]
                pos_tail = self.snake[-1][2]
                if self.opposite[pos_head] == pos_tail or \
                    self.opposite[pos_tail] == pos_head:
                        continue
                self.run = False
                print(snake_head,snake_tail)

    def make_sprite(self, sprite_rect):
        pygame.draw.rect(Snake.screen, Color('red'), sprite_rect)

    def get_sprite_rect(self):
        x = randint(self.size, self.height-self.size)
        y = randint(self.size, self.width-self.size)
        # Make x,y multiple of self.size
        x, y = self.size*(x//self.size), self.size*(y//self.size)
        # produce sprite rectangle
        sprite_rect = Rect(x, y, self.size, self.size)
        return sprite_rect

    def update_score(self, sprite_rect, snake_head):
        if sprite_rect.colliderect(snake_head):
            self.score += 10
            self.has_sprite = False
            self.increase_snake()

    def increase_snake(self):
        self.snake.append(self.snake[0])

    def move_forward(self):
        position = self.snake[0][2]
        deltax, deltay = self.delta[position]
        new_head = copy.deepcopy(self.snake[0])
        new_head[Pos.x] = new_head[Pos.x] + deltax
        new_head[Pos.y] = new_head[Pos.y] + deltay
        self.snake.appendleft(new_head)
        self.snake.pop()

    def draw_snake(self):
        # draw the snake
        for i in range(len(self.snake)):
            x, y, direction = self.snake[i]
            if x>800:
                self.snake[i][Pos.x] = -self.size
            if y>800:
                self.snake[i][Pos.y] = -self.size
            if x<0:
                self.snake[i][Pos.x] = self.width+self.size
            if y<0:
                self.snake[i][Pos.y] = self.height+self.size

            pygame.draw.rect(Snake.screen, Color('green'),
                            (x, y ,self.size, self.size))
        pygame.display.flip()
        self.move_forward()

    def main(self):
        while self.run:
            Snake.screen.fill(Color('black'))

            if self.has_sprite == False:
                sprite_rect = self.get_sprite_rect()
                self.has_sprite = True

            self.draw_score_box(600, 10)
            self.make_sprite(sprite_rect)
            self.draw_snake()
            #Check if Snake collided with itself



            for event in pygame.event.get():
                if self.snake_self_collision() == True or \
                    event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_RIGHT:
                        self.snake[0][2] = Direction.right
                    elif event.key == K_LEFT:
                        self.snake[0][2] = Direction.left
                    elif event.key == K_DOWN:
                        self.snake[0][2] = Direction.down
                    elif event.key == K_UP:
                        self.snake[0][2] = Direction.up
            self.clock.tick(30)
            self.snake_self_collision()
            self.update_score(sprite_rect, self.get_snake_head())

class Text:
    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos
        self.fontname = None
        self.fontsize = options["size"]
        self.fontcolor = Color('orange')
        self.set_font()
        self.render()

    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        Snake.screen.blit(self.img, self.rect)

if __name__ == '__main__':
    obj = Snake(60,60)
    obj.main()
