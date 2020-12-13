import pygame

Motions_picture = pygame.image.load("Fish_2.jpg")
bg = pygame.image.load("bg_2.jpg")

pygame.init()
a, b = 370, 740
screen = pygame.display.set_mode([a, b])
pygame.display.set_caption("Swimming fish")

screen.blit(bg, (0, 0))
screen.blit(Motions_picture, (100, 300))

pygame.display.update()

print(input())
