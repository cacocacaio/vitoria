import pygame

class cuca(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.animation = [pygame.image.load('Data/cuca1.png'), pygame.image.load('Data/cuca1.png'),
                          pygame.image.load('Data/cuca1.png'), pygame.image.load('Data/cuca1.png'),
                          pygame.image.load('Data/cuca1.png'), pygame.image.load('Data/cuca1.png'),
                          pygame.image.load('Data/cuca1.png'), pygame.image.load('Data/cuca1.png'),
                          pygame.image.load('Data/cuca2.png'), pygame.image.load('Data/cuca2.png'),
                          pygame.image.load('Data/cuca2.png'), pygame.image.load('Data/cuca2.png'),
                          pygame.image.load('Data/cuca2.png'), pygame.image.load('Data/cuca2.png'),
                          pygame.image.load('Data/cuca2.png'), pygame.image.load('Data/cuca2.png')]
        self.image = self.animation[0]
        self.image = pygame.transform.scale(self.image, [100, 115])

        self.rect = pygame.Rect(700, 450, 50, 120)
        self.cont = 0

        for index, element in enumerate(self.animation):
            self.animation[index] = pygame.transform.scale(self.animation[index], (120, 175))

    def update(self, *args):

        for index, element in enumerate(self.animation):
            self.animation[index] = pygame.transform.scale(self.animation[index], (120, 175))
            self.cont += 1
            self.image = self.animation[self.cont]
            self.image = pygame.transform.flip(self.image, True, False)

            if self.cont >= len(self.animation) - 1:
                self.cont = 0
