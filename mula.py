import pygame

class mula(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.animation = [pygame.image.load('Data/mula1.png'), pygame.image.load('Data/mula1.png'),
                          pygame.image.load('Data/mula1.png'), pygame.image.load('Data/mula1.png'),
                          pygame.image.load('Data/mula2.png'), pygame.image.load('Data/mula2.png'),
                          pygame.image.load('Data/mula2.png'), pygame.image.load('Data/mula2.png'),
                          pygame.image.load('Data/mula3.png'), pygame.image.load('Data/mula3.png'),
                          pygame.image.load('Data/mula3.png'), pygame.image.load('Data/mula3.png'),
                          pygame.image.load('Data/mula4.png'), pygame.image.load('Data/mula4.png'),
                          pygame.image.load('Data/mula4.png'), pygame.image.load('Data/mula4.png')]
        self.image = self.animation[0]
        self.image = pygame.transform.scale(self.image, [100, 115])

        self.rect = pygame.Rect(550, 150, 50, 120)
        self.cont = 0

        for index, element in enumerate(self.animation):
            self.animation[index] = pygame.transform.scale(self.animation[index], (150, 175))

    def update(self, *args):

        for index, element in enumerate(self.animation):
            self.animation[index] = pygame.transform.scale(self.animation[index], (150, 175))
            self.cont += 1
            self.image = self.animation[self.cont]

            if self.cont >= len(self.animation) - 1:
                self.cont = 0
