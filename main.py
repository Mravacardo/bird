import pygame
pygame.innit()

screen=pygame.diplay.set_caption(['Bird'])

screen_width=700
screen_height=500
screen = pygame.display.set_mode([screen_width,screen_height])




class Player(pygame.sprite.Sprite):
    def __init__(self)
        self.image = pygame.image.load("character.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,100))
        self.rect = self.image.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)



        if self.rect
