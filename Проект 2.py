import pygame
import random

pygame.init()
a, b = 370, 740
screen = pygame.display.set_mode([a, b])
pygame.display.set_caption("Swimming fish")
width = 25
height = 25
x, y = 70, b // 2 - height // 2 - 200
is_jump = False
jump_count = 6
del_pixels = []

first_stop = True
first_run = False

sand_pixels = 100
best_score = 0

enemies = [i * 10 for i in range(9, 34)] + [i * 10 for i in range(13, 26)] + [i * 10 for i in range(19, 31)]
enemy_count = 1
enemies_now = []
enemy_width = 80
enemy_distance = 100
how_enemies_back = 0
run = True
if_life = False

fps = 60
clock = pygame.time.Clock()
animCount = 0

Motions_picture = [pygame.image.load("1"),
                   pygame.image.load("2"),
                   pygame.image.load("3"),
                   pygame.image.load("4"),
                   pygame.image.load("5")]

Enemy_picture = [[pygame.image.load("h1"), pygame.image.load("d1"), "1"],
                 [pygame.image.load("h2"), pygame.image.load("d2"), "2"],
                 [pygame.image.load("h3"), pygame.image.load("d3"), "3"]]

bg = pygame.image.load("back_ground")

pygame.display.update()


class Enemies:
    def __init__(self, first_en, second_en, x_pos_en, y_pos_en):
        self.first_en = first_en
        self.second_en = second_en
        self.x_pos_en = x_pos_en
        self.y_pos_en = y_pos_en

    def draw(self, sc):
        sc.blit(self.first_en, (self.x_pos_en, 0))
        sc.blit(self.second_en, (self.x_pos_en, self.y_pos_en))


def draw_fish(x_pos_f, y_pos_f, sc):
    global animCount
    animCount += 1
    if animCount >= 60:
        animCount = 0
    sc.blit(Motions_picture[animCount // 10], (x_pos_f, y_pos_f))


while run:
    clock.tick(fps)

    if if_life:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        screen.blit(bg, (0, 0))
        enemy_count += 1

        if enemy_count % enemy_distance == 0:
            enemy_distance = 60
            enemy_count = 1
            enemy = random.choice(Enemy_picture)
            enemies_now.append(Enemies(enemy[0], enemy[1], a, enemy[2]))

        for en in enemies_now:
            if a > en.x_pos_en > 0 - enemy_width:
                en.x_pos_en -= 5

        # --------------------------------------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------

        for i in enemies_now:
            for j in range(i[1], i[1] + enemy_width + width):
                for r in range(13):
                    if (x == j - width and y == i[0] - r) or (x == j - width and y == i[0] + 200 + r - height):
                        if_life = False
                        first_stop = True
                        continue

            for j in range(i[0]):
                if (x == i[1] - width and y == j) or (x == i[1] - width and y == j + i[0] + 200):
                    if_life = False
                    first_stop = True
                    continue

        # --------------------------------------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------

        if y >= b - height or y <= 0:
            if_life = False
            first_stop = True
            continue

        # прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок

        if keys[pygame.K_SPACE]:
            is_jump = True
            jump_count = 6

        if jump_count < 0:
            if jump_count < -7:
                jump_count = -7
            y += (jump_count ** 2) // 4
        else:
            y -= (jump_count ** 2) // 4
        if jump_count <= 2 or jump_count >= -2:
            jump_count -= 0.5
        else:
            jump_count -= 0.5

        # прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок

        if x in [i.x_pos_en[1] + enemy_width for i in enemies_now]:
            how_enemies_back += 1

        # текст текст текст текст текст текст текст текст текст текст текст текст текст текст текст текст текст текст

        font3 = pygame.font.Font(None, 40)
        text3 = font3.render("Score: " + str(how_enemies_back), True, (50, 255, 50))
        text_x3, text_y3 = 5, 5
        text_w3 = text3.get_width()
        text_h3 = text3.get_height()
        screen.blit(text3, (text_x3, text_y3))
        pygame.draw.rect(screen, (100, 100, 100), (0, 0,
                                                   text_w3 + 10, text_h3 + 10))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0,
                                             text_w3 + 10, text_h3 + 10), 1)

        # текст текст текст текст текст текст текст текст текст текст текст текст текст текст текст текст текст текст

        draw_fish(x, y, screen)

        pygame.display.update()

    else:
        if first_stop:
            screen.fill((100, 100, 100))
            first_stop = False
            first_run = True

            if how_enemies_back > best_score:
                best_score = how_enemies_back

            font1 = pygame.font.Font(None, 100)
            text1 = font1.render("Play", True, (50, 255, 50))
            text_w = text1.get_width()
            text_h = text1.get_height()
            text_x, text_y = width // 2 + a // 2 - text_w // 2 - 15, height // 2 + b // 2
            screen.blit(text1, (text_x, text_y))
            pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                                   text_w + 20, text_h + 20), 3)

            font3 = pygame.font.Font(None, 40)
            text3 = font3.render("Score: " + str(how_enemies_back), True, (50, 255, 50))
            text_x3, text_y3 = 5, 5
            text_w3 = text3.get_width()
            text_h3 = text3.get_height()
            pygame.draw.rect(screen, (100, 100, 100), (0, 0,
                                                       text_w3 + 10, text_h3 + 10))
            screen.blit(text3, (text_x3, text_y3))

            font2 = pygame.font.Font(None, 40)
            text2 = font2.render("Best score: " + str(best_score), True, (50, 255, 50))
            text_x2, text_y2 = 5, text_h3 + 15
            screen.blit(text2, (text_x2, text_y2))

            how_enemies_back = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if pos[0] in [i for i in range(text_x - 10, text_x - 10 + text_w + 20)] and \
                        pos[1] in [i for i in range(text_y - 10, text_y - 10 + text_h + 20)]:
                    x, y = 70, b // 2 - height // 2 - 200
                    is_jump = False
                    jump_count = 6
                    del_pixels = []
                    enemies_now = []
                    if_life = True

        pygame.display.update()

pygame.quit()
