import pygame
from pygame.locals import *
import random
import time


'''
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        self.images = []
        project_dir = r'/home/mukul/Documents/SH/Python/Pygame/Boxy/'
        self.images.append(pygame.image.load(project_dir+'images/walk1.png'))
        self.images.append(pygame.image.load(project_dir+'images/walk2.png'))
        self.images.append(pygame.image.load(project_dir+'images/walk3.png'))
        self.images.append(pygame.image.load(project_dir+'images/walk4.png'))
        self.images.append(pygame.image.load(project_dir+'images/walk5.png'))
        self.images.append(pygame.image.load(project_dir+'images/walk6.png'))
        self.images.append(pygame.image.load(project_dir+'images/walk7.png'))
        self.images.append(pygame.image.load(project_dir+'images/walk8.png'))
        self.images.append(pygame.image.load(project_dir+'images/walk9.png'))
        self.images.append(pygame.image.load(project_dir+'images/walk10.png'))


        self.index = 0

        self.image = self.images[self.index]

        self.rect = pygame.Rect(5, 5, 150, 198)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

def main():
    pygame.init()
    project_dir = r'/home/mukul/Documents/SH/Python/Pygame/Boxy/'
    screen = pygame.display.set_mode((800,800))
    my_sprite = MySprite()
    sysfont = pygame.font.get_default_font()

    font1 = pygame.font.SysFont(sysfont, 72)
    img1 = font1.render('Shaiza',True,(255,25,0))



    my_group = pygame.sprite.Group(my_sprite)

    boxy = pygame.image.load(project_dir + 'boxy.png').convert()
    rect = boxy.get_rect()

    pts = ('topleft')
    points = [(random.randint(100,400),random.randint(200,500)) for i in
        range(100)]

    clock = pygame.time.Clock()
    drawing = False
    copy_surf = None
    old_copy = None
    screen.fill((255, 255, 255))
    text = 'This is it'
    font = pygame.font.SysFont(None, 48)
    img = font.render(text, True, (255,255,0))

    rect = img.get_rect()
    rect.topleft = (20,20)
    cursor = Rect(rect.topleft, (3, rect.height))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

            screen.fill((255, 255, 255))
            img = font.render(text, True, (255,255,0))
            screen.blit(img,(20,20))
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(text)>0:
                        text = text[:-1]
                else:
                    text += event.unicode

            if event.type == MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    drawing = True
            if event.type == MOUSEMOTION and drawing == True:
                rect.move_ip(event.rel)
            if event.type == MOUSEBUTTONUP:
                drawing = False


            #my_group.update()
            #my_group.draw(screen)
            pygame.display.flip()
            clock.tick(120)

if __name__ == '__main__':
    main()
'''

class App:
    def __init__(self):
        pygame.init()
        flags = RESIZABLE
        App.screen = pygame.display.set_mode((840,720), flags)
        App.running = True
        App.t = Text('Shaiza my love', pos = (20,20))
        App.scenes = []
        App.scene = None

    def run(self):
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False
            App.screen.fill(Color('gray'))
            App.t.draw()
            pygame.display.update()
        pygame.quit()


class Text:
    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos
        self.fontname = None
        self.fontsize = 72
        self.fontcolor = Color('black')
        self.set_font()
        self.render()

    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        App.screen.blit(self.img, self.rect)

class Scene:
    id = 0
    bg = Color('gray')
    def __init__(self, *args, **kwargs):
        App().scenes.append(self)
        App().scene = self
        self.id = Scene.id
        Scene.id += 1
        self.nodes = []
        self.bg = Scene.bg
    def draw(self):
        App.sceen.fill(self.bg)
        for node in self.nodes:
            node.draw()
        pygame.display.flip()
    def __str__(self):
        return 'Scene {}'.format(self.id)

class Demo(App):
    def __init__(self):
        super().__init__()
        Scene(bg=Color('yellow'), caption='Options')
        App.scene = App.scenes[0]

if __name__ == '__main__':
    Demo().run()

