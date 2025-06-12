from random import randint
from pygame import *
init()
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,size1,size2):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size1,size2))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y)) 
class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
class Ball(GameSprite):
    def __init__ (self,player_image,player_x,player_y,player_speed,player_speed_y,size1,size2):
        super().__init__(player_image,player_x,player_y,player_speed,size1,size2)
        self.speed_y = player_speed_y
    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed_y
        if self.rect.y < 0 or self.rect.y > 450:
            self.speed_y *= -1
    def collide_rect(self,rect1,rect2):
        return sprite.collide_rect(rect1,rect2)


window = display.set_mode((700,500))
display.set_caption('ping pong')
background = (0,0,100)
window.fill(background)
clock = time.Clock()
FPS = 60
finish = False
game = True
player1 = Player('rocket.png',25,50,10,100,200)
player2 = Player('rocket.png',575,50,10,100,200)
ball = Ball('ball.png',350,50,2,2,50,50)
font1 = font.SysFont('verdana',36)
while game:
    if finish != True:
        window.fill(background)
        player1.reset()
        player1.update1()
        player2.reset()
        player2.update2()
        ball.reset()
        ball.update()

        if ball.collide_rect(player2,ball):
            ball.speed *= -1
            '''ball.speed_y *= -1'''

        if ball.collide_rect(player1,ball):
            ball.speed *= -1
        ''' ball.speed_y *= -1'''
        '''if ball.rect.y > 500 or ball.rect.y < 0:
            speed_x *= -1'''
        if ball.rect.x <= 0 :
            finish = True 
            text_gameover1= font1.render('Второй игрок выиграл',True,(255,255,255))
            window.blit(text_gameover1,(150,200))
            text_gameover2= font1.render('Первый игрок проиграл',True,(255,255,255))
            window.blit(text_gameover2,(150,250))
        if ball.rect.x >= 700 :
            finish = True 
            text_gameover1= font1.render('Первый игрок выиграл',True,(255,255,255))
            window.blit(text_gameover1,(150,200))
            text_gameover2= font1.render('Второй игрок проиграл',True,(255,255,255))
            window.blit(text_gameover2,(150,250))
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)