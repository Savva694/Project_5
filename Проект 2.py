import pygame
import random
import os

pygame.init()
a, b, c = 370, 740, 322
screen = pygame.display.set_mode([a, b])
pygame.display.set_caption("Flappy Bird")
width = 49
height = 35
x, y = 70, b // 2 - height // 2 - 200  # x = 70
is_jump = False
jump_count = 6

first_stop = True
first_run = False

sand_pixels = 100
best_score = 0

enemy_count = 1
enemies_now = []
enemy_width = 100
enemy_distance = 100
how_enemies_back = 0
run = True
if_life = False

fps = 60
clock = pygame.time.Clock()
animCount = 0


def load_image(name):
    fullname = os.path.join("data", name)
    image = pygame.image.load(fullname)
    image.set_colorkey(-1)
    return image


Motions_picture = [load_image("bird_1.png"),
                   load_image("bird_2.png"),
                   load_image("bird_1.png"),
                   load_image("bird_3.png")]

Enemy_picture = [[load_image("tube_1.1.jpg"), load_image("tube_1.2.jpg"), 440],
                 [load_image("tube_2.1.jpg"), load_image("tube_2.2.jpg"), 470],
                 [load_image("tube_3.1.jpg"), load_image("tube_3.2.jpg"), 500],
                 [load_image("tube_4.1.jpg"), load_image("tube_4.2.jpg"), 410],
                 [load_image("tube_5.1.jpg"), load_image("tube_5.2.jpg"), 530],
                 [load_image("tube_6.1.jpg"), load_image("tube_6.2.jpg"), 380],
                 [load_image("tube_7.1.jpg"), load_image("tube_7.2.jpg"), 560]]

bg = pygame.image.load("bg_3.jpg")
bg2 = pygame.image.load("bg_1.jpg")

pygame.display.update()

# музыка музыка музыка музыка музыка музыка музыка музыка музыка музыка музыка музыка музыка музыка музыка музыка музыка


sound1 = pygame.mixer.Sound("die.wav")
sound2 = pygame.mixer.Sound("point.wav")
sound3 = pygame.mixer.Sound("wing.wav")


# музыка музыка музыка музыка музыка музыка музыка музыка музыка музыка музыка музыка музыка музыка музыка музыка музыка


class Enemies:
    def __init__(self, first_en, second_en, x_pos_en, y_pos_en):
        self.first_en = first_en
        self.second_en = second_en
        self.x_pos_en = x_pos_en
        self.y_pos_en = y_pos_en

    def draw_en(self, sc):
        sc.blit(self.first_en, (self.x_pos_en, 0))
        sc.blit(self.second_en, (self.x_pos_en, self.y_pos_en))


def draw_fish(x_pos_f, y_pos_f, sc):
    global animCount
    animCount += 1
    if animCount >= 40:
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
            enemy_distance = 80
            enemy_count = 1
            enemy = random.choice(Enemy_picture)
            enemies_now.append(Enemies(enemy[0], enemy[1], a, enemy[2]))

        for en in enemies_now:
            if a >= en.x_pos_en >= 0 - enemy_width:
                en.x_pos_en -= 4
            else:
                del enemies_now[enemies_now.index(en)]

        if y >= b - height or y <= 0:
            sound1.play()
            if_life = False
            first_stop = True
            continue

        # прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок

        if keys[pygame.K_SPACE]:
            sound3.play()
            is_jump = True
            jump_count = 6

        if jump_count < 0:
            if jump_count < -7:
                jump_count = -7
            y += (jump_count ** 2) // 4
        else:
            y -= (jump_count ** 2) // 4
        jump_count -= 0.5

        # прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок прыжок

        if x in [i.x_pos_en + enemy_width for i in enemies_now]:
            sound2.play()
            how_enemies_back += 1

        # отрисовка отрисовка отрисовка отрисовка отрисовка отрисовка отрисовка отрисовка отрисовка отрисовка отрисовка

        for i in enemies_now:
            i.draw_en(screen)

        draw_fish(x, y, screen)

        # отрисовка отрисовка отрисовка отрисовка отрисовка отрисовка отрисовка отрисовка отрисовка отрисовка отрисовка

        # текст текст текст текст текст текст текст текст текст текст текст текст текст текст текст текст текст текст

        font3 = pygame.font.Font(None, 40)
        text3 = font3.render("Score: " + str(how_enemies_back), True, (50, 255, 50))
        text_x3, text_y3 = 5, 5
        text_w3 = text3.get_width()
        text_h3 = text3.get_height()
        pygame.draw.rect(screen, (100, 100, 100), (0, 0,
                                                   text_w3 + 10, text_h3 + 10))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0,
                                             text_w3 + 10, text_h3 + 10), 1)
        screen.blit(text3, (text_x3, text_y3))

        # текст текст текст текст текст текст текст текст текст текст текст текст текст текст текст текст текст текст

        # проверка на смерть проверка на смерть проверка на смерть проверка на смерть проверка на смерть

        for i in enemies_now:
            fake_jump_count = jump_count + 0.5
            if x in range(i.x_pos_en - width, i.x_pos_en + enemy_width) and \
                    ((y > i.y_pos_en > y - ((jump_count - 0.5) ** 2) // 4) or
                     (y < i.y_pos_en - 200 < y + ((jump_count + 0.5) ** 2) // 4)):
                sound1.play()
                if_life = False
                first_stop = True
                continue

            if x - 1 == i.x_pos_en - width and (y in range(0, i.y_pos_en - 200) or
                                                y in range(i.y_pos_en - height, b)):
                if_life = False
                first_stop = True
                sound1.play()
                continue

        # проверка на смерть проверка на смерть проверка на смерть проверка на смерть проверка на смерть

        pygame.display.update()

    else:
        if first_stop:
            screen.blit(bg, (0, 0))
            first_stop = False
            first_run = True

            if how_enemies_back > best_score:
                best_score = how_enemies_back

            font1 = pygame.font.Font(None, 100)
            text1 = font1.render("Play", True, (50, 255, 50))
            text_w = text1.get_width()
            text_h = text1.get_height()
            text_x, text_y = a // 2 - text_w // 2, height // 2 + b // 2 - 20
            screen.blit(text1, (text_x, text_y))
            pygame.draw.rect(screen, (50, 255, 50), (text_x - 10, text_y - 10,
                                                     text_w + 20, text_h + 20), 4)

            font3 = pygame.font.Font(None, 40)
            text3 = font3.render("Score: " + str(how_enemies_back), True, (50, 255, 50))
            text_x3, text_y3 = 5, 5
            text_w3 = text3.get_width()
            text_h3 = text3.get_height()
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
                    enemies_now = []
                    if_life = True

        pygame.display.update()

pygame.quit()
