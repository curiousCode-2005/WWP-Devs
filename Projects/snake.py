import random
#from pynput.keyboard import Key, Controller
import pygame

#final variables
BLOCK = 50
FPS = 60
#keyboard = Controller()

#Dimensions
WIDTH, HEIGHT = 800,800
snake = pygame.Rect(WIDTH/2, HEIGHT/2, BLOCK, BLOCK)
tails = []
tails.append(pygame.Rect(WIDTH//(BLOCK*2)*BLOCK, HEIGHT//(BLOCK*2)*BLOCK, BLOCK, BLOCK))

rect1 = pygame.Rect(0,0,WIDTH,BLOCK)
rect2 = pygame.Rect(0,0,BLOCK,HEIGHT)
rect3 = pygame.Rect(WIDTH-BLOCK,0,BLOCK,HEIGHT)
rect4 = pygame.Rect(0,HEIGHT-BLOCK,WIDTH,BLOCK)

#screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


#Color
BLACK = (0,0,0)
WHITE = (255,255,255)
DARK_GREEN = (162,209,73)
LIGHT_GREEN = (170,215,81)
RED = (255,0,0)
BLUE = (79,124,246)
TAIL_BLUE = (67,111,227)
color = DARK_GREEN
#apple
apple = True
apple_rect = pygame.Rect(WIDTH/2+(5*BLOCK),HEIGHT/2,BLOCK,BLOCK)

#movement
left = False #A
right = False #D
up = False #W
down = False #S
count = 0
facing = "w"

#menu
run = True
score = 0


pygame.display.set_caption("Snake")

def switch_color():
    global color
    if color == DARK_GREEN:
        color = LIGHT_GREEN
    else:
        color = DARK_GREEN

def draw_apple(x,y):
    global apple_rect, apple
    apple_rect = pygame.Rect(x*BLOCK,y*BLOCK,BLOCK,BLOCK)
    apple = True

def background():
    for x in range(0,WIDTH,BLOCK):
        switch_color()
        for y in range(0,HEIGHT,BLOCK):
            pygame.draw.rect(WIN, color, pygame.Rect(x,y,BLOCK,BLOCK))
            switch_color()

def draw_screen():
    background()
    pygame.draw.rect(WIN,BLACK,rect1)
    pygame.draw.rect(WIN,BLACK,rect2)
    pygame.draw.rect(WIN,BLACK,rect3)
    pygame.draw.rect(WIN,BLACK,rect4)


    if apple:
        pygame.draw.rect(WIN, RED, apple_rect)
    pygame.draw.rect(WIN, TAIL_BLUE, snake)
    for rect in tails:
        pygame.draw.rect(WIN, BLUE, rect)

def collide():
    global apple, score, run
    if snake.colliderect(apple_rect):
        apple = False
        score += 1
        tails.append(pygame.Rect(tails[len(tails)-1].x, tails[len(tails)-1].y, tails[len(tails)-1].width, tails[len(tails)-1].height))
    for x in range(len(tails)-1):
        if snake.colliderect(tails[x]):
            pygame.time.delay(100)
            run = False
    if snake.colliderect(rect1) or snake.colliderect(rect2) or snake.colliderect(rect3) or snake.colliderect(rect4):
            pygame.time.delay(100)
            run = False




def move_snake(key_pressed):
    global snake, tails, right, left, up, down, count, facing
    count += 1
    if count%10 == 0:
        tails.append(pygame.Rect(snake.x, snake.y, snake.width, snake.height))
        tails.remove(tails[0])
        if (key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]) and not right:
            facing = "a"
            left = True  # A
            right = False  # D
            up = False  # W
            down = False  # S
        elif (key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]) and not left:
            facing = "d"
            left = False  # A
            right = True  # D
            up = False  # W
            down = False  # S
        elif (key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]) and not down:
            facing = "w"
            left = False  # A
            right = False  # D
            up = True  # W
            down = False  # S
        elif (key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]) and not up:
            facing = "s"
            left = False  # A
            right = False  # D
            up = False  # W
            down = True  # S

        if left:
            snake.x -= BLOCK
        elif right:
            snake.x += BLOCK
        elif up:
            snake.y -= BLOCK
        elif down:
            snake.y += BLOCK



def main():
    clock = pygame.time.Clock()
    global run
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            #ALL EVENTS
            if event.type == pygame.QUIT:
                run = False


        #APPLES

        if not apple:
            x = random.randint(BLOCK, WIDTH - BLOCK)
            y = random.randint(BLOCK, HEIGHT - BLOCK)
            draw_apple(x // BLOCK, y // BLOCK)


        #MOVEMENT

        key_pressed = pygame.key.get_pressed()

        #Collisions

        collide()

        move_snake(key_pressed)
        #DRAW

        draw_screen()
        pygame.display.update()

    print("Score: ",score)
    pygame.quit()

if __name__ == "__main__":
    main()