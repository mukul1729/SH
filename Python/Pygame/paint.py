import pygame
pygame.init()
window = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
run = True
window.fill((255,255,255))
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            tmp1,tmp2 = pygame.mouse.get_pos()
            while pygame.MOUSEBUTTONDOWN:
                print(event) 
        if event.type == pygame.MOUSEBUTTONUP:
            tmp3,tmp4 = pygame.mouse.get_pos()
            pygame.draw.line(window,(0,0,0),(tmp1,tmp2),(tmp3,tmp4))
        pygame.display.update()
