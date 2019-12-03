import pygame
class Bullet1(pyganme.sprite.Sprite);
    def _init_(self,position);
        pygame.sprite.Sprite._init_(self)

        self.image = pygame.image.load("bullet1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 12
        self.active = True
        self.mask = pyganme.mask.from_surface(self.image)

    def move(self);
        self.rect.top -= self.speed

        if self.rect.top<0;
        self.active = False

    def reset(self,position);
        self.rect.left,self.rect.top = position
        self.active = True





