import math
import random
import pygame
from pygame.locals import *

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 617

BLACK = (0, 0, 0)
WHITE = (250, 250, 250)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('FISH GAME')
fps_clock = pygame.time.Clock()
FPS = 60
score = 0

default_font = pygame.font.Font('font.ttf', 28)
background_img = pygame.image.load('background.jpg')
pygame.mixer.music.load('music.mp3')
eat_sound = pygame.mixer.Sound('food.wav')
shark_sound = pygame.mixer.Sound('shark.wav')

class Fish(pygame.sprite.Sprite):
    def __init__(self):
        super(Fish, self). __init__()
        self.image = pygame.image.load('fish.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery

    def set_pos(self, x, y):
        self.rect.x = x - self.centerx
        self.rect.y = y - self.centery

    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_mask(self, sprite):
                return sprite

class Sharkright(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, hspeed, vspeed):
        super(Sharkright,self).__init__()
        self.image = pygame.image.load('shark-left.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.hspeed = hspeed
        self.vspeed = vspeed

    def update(self):
        self.rect.x += self.hspeed
        self.rect.y += self.vspeed
        if self.collide():
            self.kill()
    def collide(self):
        if self.rect.x < 0 - self.rect.height or self.rect.x > WINDOW_WIDTH:
            return True
        elif self.rect.y < 0 - self.rect.height or self.rect.y > WINDOW_HEIGHT:
            return True

def random_shark_right(speed):
    random_direction = random
    if random_direction == random:
        return Sharkright(WINDOW_WIDTH, random.randint(0, WINDOW_HEIGHT), -speed, 0)

class Sharkleft(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, hspeed, vspeed):
        super(Sharkleft,self).__init__()
        self.image = pygame.image.load('shark-right.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.hspeed = hspeed
        self.vspeed = vspeed

    def update(self):
        self.rect.x += self.hspeed
        self.rect.y += self.vspeed
        if self.collide():
            self.kill()
    def collide(self):
        if self.rect.x < 0 - self.rect.height or self.rect.x > WINDOW_WIDTH:
            return True
        elif self.rect.y < 0 - self.rect.height or self.rect.y > WINDOW_HEIGHT:
            return True

def random_shark_left(speed):
    random_direction = random
    if random_direction == random:
        return Sharkleft(0, random.randint(0, WINDOW_HEIGHT), speed, 0)

class Food(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, hspeed, vspeed):
        super(Food, self).__init__()
        self.image = pygame.image.load('food.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.hspeed = hspeed
        self.vspeed = vspeed

    def update(self):
        self.rect.x += self.hspeed
        self.rect.y += self.vspeed
        if self.collide():
            self.kill()
    def collide(self):
        if self.rect.x < 0 - self.rect.height or self.rect.x > WINDOW_WIDTH:
            return True
        elif self.rect.y < 0 - self.rect.height or self.rect.y > WINDOW_HEIGHT:
            return True

def random_food(speed):
    random_direction = random
    if random_direction == random:
        return Food(random.randint(0, WINDOW_WIDTH), 0, 0, speed)

def draw_repeating_background(background_img):
    background_rect = background_img.get_rect()
    for i in range(int(math.ceil(WINDOW_WIDTH / background_rect.width))):
        for j in range(int(math.ceil(WINDOW_HEIGHT / background_rect.height))):
            screen.blit(background_img, Rect(i * background_rect.width,
                                                 j * background_rect.height,
                                                 background_rect.width,
                                                 background_rect.height))
def draw_text(text, font, surface, x, y, main_color):
    text_obj = font.render(text, True, main_color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surface.blit(text_obj, text_rect)

def game_loop():
    global score

    pygame.mixer.music.play(-1)
    pygame.mouse.set_visible(False)

    fish = Fish()
    fish.set_pos(*pygame.mouse.get_pos())
    sharkright = pygame.sprite.Group()
    sharkleft = pygame.sprite.Group()
    foods = pygame.sprite.Group()
    occur_prob = 100
    occur_probs = 400
    score = 0
    paused = False


    while True:
        pygame.display.update()
        fps_clock.tick(FPS)

        if paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        paused = not paused
                        pygame.mouse.set_visible(False)
                if event.type == QUIT:
                    return 'quit'
        else:
            draw_repeating_background(background_img)

            occur_of_sharkright = 1
            occur_of_sharkleft = 1
            min_rock_speed = 1
            max_rock_speed = 1
            occur_of_foods = 1

            if random.randint(1, occur_probs) == 1:
                for i in range(occur_of_sharkright):
                    sharkright.add(random_shark_right(random.randint(min_rock_speed, max_rock_speed)))

            if random.randint(1, occur_probs) == 1:
                for i in range(occur_of_sharkleft):
                    sharkleft.add(random_shark_left(random.randint(min_rock_speed, max_rock_speed)))

            if random.randint(1, occur_prob) == 1:
                for i in range(occur_of_foods):
                    foods.add(random_food(random.randint(min_rock_speed, max_rock_speed)))

            draw_text('POINT : {}'.format(score), default_font, screen, 110, 40, WHITE)
            sharkright.update()
            foods.update()
            sharkleft.update()
            sharkright.draw(screen)
            foods.draw(screen)
            sharkleft.draw(screen)

            food = fish.collide(foods)

            if fish.collide(sharkright):
                shark_sound.play()
                pygame.mixer.music.stop()
                sharkright.empty()
                return 'game_screen'
            elif fish.collide(sharkleft):
                shark_sound.play()
                pygame.mixer.music.stop()
                sharkleft.empty()
                return 'game_screen'
            elif food:
                eat_sound.play()
                score += 10
                food.kill()

            screen.blit(fish.image, fish.rect)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[0] <= 10:
                        pygame.mouse.set_pos(WINDOW_WIDTH - 10, mouse_pos[1])
                    elif mouse_pos[0] >= WINDOW_WIDTH - 10:
                        pygame.mouse.set_pos(0 + 10, mouse_pos[1])
                    elif mouse_pos[1] <= 10:
                        pygame.mouse.set_pos(mouse_pos[0], WINDOW_HEIGHT - 10)
                    elif mouse_pos[1] >= WINDOW_HEIGHT - 10:
                        pygame.mouse.set_pos(mouse_pos[0], 0 + 10)
                    fish.set_pos(*mouse_pos)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        paused = not paused
                        if paused:
                            transp_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
                            transp_surf.set_alpha(150)
                            screen.blit(transp_surf, transp_surf.get_rect())
                            pygame.mouse.set_visible(True)
                            draw_text('PAUSED', pygame.font.Font('font.ttf', 60),
                                      screen, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, WHITE)
                if event.type == QUIT:
                    return 'quit'
    return 'game_screen'

def game_screen():
    global score
    pygame.mouse.set_visible(True)

    start_image = pygame.image.load('background.jpg')
    screen.blit(start_image,[0,0])

    draw_text('FISH GAME', pygame.font.Font('font.ttf', 100), screen,
                WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4, BLACK)
    draw_text('POINT : {}'.format(score),
                pygame.font.Font('font.ttf', 35), screen, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2.1, WHITE)
    draw_text('START : ENTER',
              pygame.font.Font('font.ttf', 50), screen, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 1.7, WHITE)
    draw_text('PLAY PAUSED : Q',
                pygame.font.Font('font.ttf', 25), screen, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 1.4, WHITE)
    draw_text('EXIT : Q',
              pygame.font.Font('font.ttf', 25), screen, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 1.2, WHITE)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                return 'quit'
            if event.key == pygame.K_RETURN:
                return 'play'
        if event.type == QUIT:
            return 'quit'
    return 'game_screen'

def main_loop():
    action = 'game_screen'
    while action != 'quit':
        if action == 'game_screen':
            action = game_screen()
        elif action == 'play':
            action = game_loop()
    pygame.quit()
main_loop()