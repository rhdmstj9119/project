''' math, random , pygame 라이브러리를 작업하기위해서 가져옵니다.
 pygame의 기본 구조는 1. pygame을 선언합니다 2. pygame을 초기화시킵니다 3. pygame에서 사용할 전역 변수 선언합니다
 4. pygame 의 메인 루프를 작성합니다.'''
import math
import random
import pygame
from pygame.locals import *

# 윈도우크기를 정하고 작업에 필요한 색깔을 정해줍니다. (게임화면 설정)
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 617
BLACK = (0, 0, 0)
WHITE = (250, 250, 250)

# pygame을 초기화 시켜줍니다.
pygame.init()
# 게임스크린 크기를 지정합니다.
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
# 작업을 하는 프로젝트 이름을 정합니다.
pygame.display.set_caption('FISH GAME')
# 게임 루프를 작성하기전에 게임 루프의 주기를 결정하기위해 pygame.time.Clock 객체를 생성합니다.
fps_clock = pygame.time.Clock()
FPS = 60
# 게임스코어 전역변수를 선언합니다.
score = 0
# 게임에서의 폰트와 배경화면을 넣어주고 , 배경음악과 효과음을 넣어줍니다.
default_font = pygame.font.Font('font.ttf', 28)
background_img = pygame.image.load('background.jpg')
shark_sound = pygame.mixer.Sound('shark.wav')
eat_sound = pygame.mixer.Sound('food.wav')
pygame.mixer.music.load('music.mp3')

'''pygame 에서 제공하는 Sprite 라는 기본적인 클래스를 사용합니다.
   Class Fish와, Class Sharklift, Class Sharkright, Class Food를 만들어서 사용합니다.'''
class Fish(pygame.sprite.Sprite):
    def __init__(self):
        super(Fish, self). __init__() # super()로 기반 클래스의 __init__메서드를 호출합니다.
        self.image = pygame.image.load('fish.png').convert_alpha()# 물고기 이미지를 불러옵니다.
        self.mask = pygame.mask.from_surface(self.image)# 이미지 충돌을 위해서 mask를 사용합니다.
        self.rect = self.image.get_rect()# 이미지 위치를 가져옵니다.
        self.centerx = self.rect.centerx# rect에서 센터 x와 y를 정의해줍니다.
        self.centery = self.rect.centery

    def set_pos(self, x, y):
        self.rect.x = x - self.centerx
        self.rect.y = y - self.centery

    def collide(self, sprites): #충돌이 일어나는 부분입니다.
        for sprite in sprites:# sprites객체 마다 충돌이 일어났는지 확인을 합니다
            if pygame.sprite.collide_mask(self, sprite): # 만약에 충돌이 일어났으면 sprite로 리턴시켜줍니다.
                return sprite

class Sharkleft(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, hspeed, vspeed):
        super(Sharkleft,self).__init__()# super()로 기반 클래스의 __init__메서드를 호출합니다.
        self.image = pygame.image.load('shark-left.png').convert_alpha()# 상어 왼쪽 이미지를 불러옵니다.
        self.mask = pygame.mask.from_surface(self.image)# 이미지 충돌을 위해서 mask를 사용합니다.
        self.rect = self.image.get_rect()# 이미지 위치를 가져옵니다.
        self.rect.x = xpos #rect에서 x위치와 y위치를 정의해줍니다.
        self.rect.y = ypos
        self.hspeed = hspeed
        self.vspeed = vspeed

    def update(self):# 화면에 상어가 왼쪽으로 이동할때마다 이미지가 업데이트 되는 부분입니다.
        self.rect.x += self.hspeed
        self.rect.y += self.vspeed

    def collide(self):# 충돌이 일어나는 부분입니다.
        if self.rect.x < 0 - self.rect.height or self.rect.x > WINDOW_WIDTH:
            return True
        elif self.rect.y < 0 - self.rect.height or self.rect.y > WINDOW_HEIGHT:
            return True

# 랜덤으로 왼쪽에서 상어가 나오게끔 함수를 만들어줍니다.
def random_shark_left(speed):
    random_direction = random
    if random_direction == random: # random_direction이 랜덤이기 때문에 오른쪽에서 상어가 나오게끔 if문을 돌려줍니다.
        return Sharkleft(WINDOW_WIDTH, random.randint(0, WINDOW_HEIGHT), -speed, 0)

class Sharkright(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, hspeed, vspeed):
        super(Sharkright,self).__init__()# super()로 기반 클레스의 __init__ 메서드를 호출합니다.
        self.image = pygame.image.load('shark-right.png').convert_alpha()# 상어 오른쪽 이미지를 불러옵니다.
        self.mask = pygame.mask.from_surface(self.image)# 이미지 충돌을 위해서 mask를 사용합니다.
        self.rect = self.image.get_rect()# 이미지 위치를 가져옵니다.
        self.rect.x = xpos# rect에서 x위치와 y위치를 정의해줍니다.
        self.rect.y = ypos
        self.hspeed = hspeed
        self.vspeed = vspeed

    def update(self):# 화면에 상어가 오른쪽으로 이동할때마다 이미지가 업데이트 되는 부분입니다.
        self.rect.x += self.hspeed
        self.rect.y += self.vspeed
        if self.collide():
            self.kill()
    def collide(self):# 충돌이 일어나는 부분입니다.
        if self.rect.x < 0 - self.rect.height or self.rect.x > WINDOW_WIDTH:
            return True
        elif self.rect.y < 0 - self.rect.height or self.rect.y > WINDOW_HEIGHT:
            return True

# 랜덤으로 오른족에서 상어가 나오게끔 함수를 만들어줍니다.
def random_shark_right(speed):
    random_direction = random # random_direction이 랜덤이기 때문에 오른쪽에서 상어가 나오게끔 if문을 돌려줍니다.
    if random_direction == random:
        return Sharkright(0, random.randint(0, WINDOW_HEIGHT), speed, 0)

class Food(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, hspeed, vspeed):
        super(Food, self).__init__()# super()로 기반 클레스의 __init__ 메서드를 호출합니다.
        self.image = pygame.image.load('food.png').convert_alpha()# 먹이 이미지를 불러옵니다.
        self.mask = pygame.mask.from_surface(self.image)# 이미지 충돌(fish가 먹이를 먹을때)을 위해서 mask를 사용합니다.
        self.rect = self.image.get_rect()# 이미지 위치를 가져옵니다.
        self.rect.x = xpos# rect에서 x위치와 y위치를 정의해줍니다.
        self.rect.y = ypos
        self.hspeed = hspeed
        self.vspeed = vspeed

    def update(self):# 화면에 먹이가 위에서 내려오게끔 이미지가 업데이트 되는 부분입니다.
        self.rect.x += self.hspeed
        self.rect.y += self.vspeed

    def collide(self):# 충돌이 일어나는 부분입니다.
        if self.rect.x < 0 - self.rect.height or self.rect.x > WINDOW_WIDTH:
            return True
        elif self.rect.y < 0 - self.rect.height or self.rect.y > WINDOW_HEIGHT:
            return True

# 랜덤으로 위에서 먹이가 나오게끔 함수를 만들어줍니다.
def random_food(speed):
    random_direction = random# random_direction이 랜덤이기 때문에 위에서 먹이가가 나오게끔 if문을 돌려줍니다.
    if random_direction == random:
        return Food(random.randint(0, WINDOW_WIDTH), 0, 0, speed)

# 배경이미지를 반복해서 나오게끔 함수를 하나 만들어줍니다.
def draw_repeating_background(background_img):
    background_rect = background_img.get_rect()# 이미지 크기를 가져옵니다.
    for i in range(int(math.ceil(WINDOW_WIDTH / background_rect.width))):# 배경이미지를 계속 나오게끔 반복하기위해서 i, j를 for문을 돌려서 만듭니다.
        for j in range(int(math.ceil(WINDOW_HEIGHT / background_rect.height))):
            screen.blit(background_img, Rect(i * background_rect.width,
                                                 j * background_rect.height,
                                                 background_rect.width,
                                                 background_rect.height))
# text를 사용하기위해서 함수를 만들어 줍니다.
def draw_text(text, font, surface, x, y, main_color):
    text_obj = font.render(text, True, main_color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surface.blit(text_obj, text_rect)# surface.blit 메소드를 이용해서 text를 보여줍니다.

# 이제 작업에 필요한 게임루프를 처리하기위해서 함수를 만듭니다.
def game_loop():
    global score

    pygame.mixer.music.play(-1) # 게임의 배경음악을 실행합니다. -1 을넣어줘서 무한반복하게끔 바꿔줍니다.
    pygame.mouse.set_visible(False)# 게임내에서 마우스 포인트를 보여주지않게하기위해서 visible을 False합니다.

    fish = Fish()
    fish.set_pos(*pygame.mouse.get_pos()) # 마우스의 현재 위치를 fish.set_pos에 넣어줍니다.
    sharkright = pygame.sprite.Group()# sprite안에 그룹을(여러개를 처리할때 편리하기 때문에) 활용해서 사용합니다.
    sharkleft = pygame.sprite.Group()# sprite안에 그룹을 활용해서 사용합니다.
    foods = pygame.sprite.Group()# sprite안에 그룹을 활용해서 사용합니다.
    occur_prob = 100 # 발생되는 확률을 정해줍니다.
    occur_probs = 400 # 발생되는 확률을 정해줍니다.
    score = 0 # 먹이를 먹을때마다 점수를 늘리기위해서 score는 0으로 해줍니다.
    paused = False


    while True:
        # 화면에 업데이트를 지속해서 하고, FPS는 아까 정의한대로 60으로 진행합니다.
        pygame.display.update()
        fps_clock.tick(FPS)

        # q 버튼을 누르면 일시정지하기위해서 event키를 q버튼으로 바꾸고 mouse포인트를 보여줍니다. 일시정지상태에서 게임을 종료하기위해서 q버튼을 누르면 게임을 종료합니다.
        if paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        paused = not paused
                        pygame.mouse.set_visible(False)
                if event.type == QUIT:
                    return 'quit'
        # paused 가 아닐경우에
        else:
            # 배경화면을 계속 출력시켜줍니다.
            draw_repeating_background(background_img)
            # 상어와 먹이를 나오게 하기위해서 변수를 선언해줍니다.
            occur_of_sharkright = 1
            occur_of_sharkleft = 1
            min_rock_speed = 1
            max_rock_speed = 1
            occur_of_foods = 1

            # 1 부터 occur_probs 사이에서 1이 나올경우에 오른쪽에 상어를 나오게 설정해줍니다.
            if random.randint(1, occur_probs) == 1:
                for i in range(occur_of_sharkright):
                    sharkright.add(random_shark_right(random.randint(min_rock_speed, max_rock_speed)))
            # 1 부터 occur_probs 사이에서 1이 나올경우에 왼쪽에 상어를 나오게 설정해줍니다.
            if random.randint(1, occur_probs) == 1:
                for i in range(occur_of_sharkleft):
                    sharkleft.add(random_shark_left(random.randint(min_rock_speed, max_rock_speed)))
            # 1부터 occur_prob 사이에서 1이 나올경우에 위에서 먹이가 나오게 설정해줍니다.
            if random.randint(1, occur_prob) == 1:
                for i in range(occur_of_foods):
                    foods.add(random_food(random.randint(min_rock_speed, max_rock_speed)))

            # 작업 화면에서 점수를 표시 시켜줍니다.
            draw_text('POINT : {}'.format(score), default_font, screen, 110, 40, WHITE)
            # 상어와 먹이를 계속 업데이트 시켜주고 화면에 표시를 해줍니다.
            sharkright.update()
            foods.update()
            sharkleft.update()
            sharkright.draw(screen)
            foods.draw(screen)
            sharkleft.draw(screen)

            # 음식이 물고기와 충돌이 났을경우를 그려줍니다.
            food = fish.collide(foods)

            # 만약 상어와 물고기가 충돌을 했을경우에는 충돌 소리를 나오게하고 배경음악을 끄고 게임 대기화면으로 바꿔줍니다.
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
            # 만약 물고기가 먹이를 먹었을경우에는 먹는 효과음과 점수 +10점을 추가하고 그 충돌된 먹이는 없애줍니다.
            elif food:
                eat_sound.play()
                score += 10
                food.kill()

            # 화면에 물고기를 계속 보여줍니다.
            screen.blit(fish.image, fish.rect)

            # 마우스로 게임을 진행하기위해서 마우스 모션에 마우스 포지션을 넣어주고
            # 테마가 큰 바다이기 때문에 물고기가 화면 밖으로 나오면 반대쪽에서 나오게끔 설정해줍니다.
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
                # 위에와 마찬가지고 q를 누르면 게임 일시정지를 시킵니다.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        paused = not paused
                        # 만약에 일시정지이면 화면에 PAUSED 텍스트를 가운데에 보여주고 마우스 포인트를 보이게 해줍니다.
                        if paused:
                            transp_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
                            transp_surf.set_alpha(150)
                            screen.blit(transp_surf, transp_surf.get_rect())
                            pygame.mouse.set_visible(True)
                            draw_text('PAUSED', pygame.font.Font('font.ttf', 60),
                                      screen, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, WHITE)
                if event.type == QUIT:
                    return 'quit'
    # while 문의 반복이 끝났을경우에는 게임 대기화면으로 이동합니다.
    return 'game_screen'

# 게임 대기화면을 만들기위해 함수를 만듭니다.
def game_screen():
    # 점수를 표현하기위해 global에서 점수를 가져오고 마우스 포인트를 보여주기위해 visible(True로 해줍니다.)
    global score
    pygame.mouse.set_visible(True)

    # 배경이미지를 불러옵니다
    start_image = pygame.image.load('background.jpg')
    screen.blit(start_image,[0,0])

    # 게임의 이름과 점수, 시작, 일시정지, 게임종료 하는방법을 Text로 배경이미지 위에 보여줍니다.
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

    # 계속해서 화면에 업데이트를 해줍니다.
    pygame.display.update()

    # 위에서 마찬가지로 q을 누르면 게임종료하고, enter을 누르면 게임을 시작합니다.
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                return 'quit'
            if event.key == pygame.K_RETURN:
                return 'play'
        if event.type == QUIT:
            return 'quit'

    return 'game_screen'

# 기능 구현을 하기위해서 메인 루프 함수를 만듭니다.
def main_loop():
    # 액션이라는 변수를 만들고
    action = 'game_screen'
    # 액션이 끝나지 않았을때는 게임 스크린을 띄워줍니다.
    while action != 'quit':
        if action == 'game_screen':
            action = game_screen()
    # 액션이 플레이일 경우에는 게임 루프를 돌게합니다.
        elif action == 'play':
            action = game_loop()
    # 이것도 저것도 아니면 pygame을 끝내줍니다.
    pygame.quit()

# 게임을 실행합니다.
main_loop()