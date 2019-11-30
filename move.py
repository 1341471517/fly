#检测用户的键盘操作
key_pressed = pygame.get pressed()
#移动我方飞机
if key_pressed[K_w] or key_pressed[K_UP]:
    me.moveUp()
if key_pressed[K_s] or key_pressed[K_DOWN]:
    me.moveDOWN()
if key_pressed[K_a] or key_pressed[K_LEFT]:
    me.moveLEFT()
if key_pressed[K_d] or key_pressed[K_RIGHT]:
    me.moveRIGHT()
sreen.blit(background,(0,0))
#绘制我方飞机
screen.blit(me.image,me.rect)
