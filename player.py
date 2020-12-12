import pygame
clock = pygame.time.Clock()
pisada = pygame.mixer.Sound('Data/dirt3.wav')

class player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        #Frente
        self.animation = [pygame.image.load('Data/frontvitoria1.png'), pygame.image.load('Data/frontvitoria1.png'),
                          pygame.image.load('Data/frontvitoria1.png'), pygame.image.load('Data/frontvitoria1.png'),
                          pygame.image.load('Data/frontvitoria2.png'), pygame.image.load('Data/frontvitoria2.png'),
                          pygame.image.load('Data/frontvitoria2.png'), pygame.image.load('Data/frontvitoria2.png'),
                          pygame.image.load('Data/frontvitoria3.png'), pygame.image.load('Data/frontvitoria3.png'),
                          pygame.image.load('Data/frontvitoria3.png'), pygame.image.load('Data/frontvitoria3.png'),
                          pygame.image.load('Data/frontvitoria4.png'), pygame.image.load('Data/frontvitoria4.png'),
                          pygame.image.load('Data/frontvitoria4.png'), pygame.image.load('Data/frontvitoria4.png')]
        self.image = self.animation[0]
        self.cont = 0
        self.image = pygame.transform.scale(self.image, [35, 100])
        self.rect = pygame.Rect(150, 85, 35, 100)
        for index, element in enumerate(self.animation):
            self.animation[index] = pygame.transform.scale(self.animation[index], (35, 100))
        #costa
        self.animation_costa = [pygame.image.load('Data/costa1.png'), pygame.image.load('Data/costa1.png'),
                                pygame.image.load('Data/costa1.png'), pygame.image.load('Data/costa1.png'),
                                pygame.image.load('Data/costa2.png'), pygame.image.load('Data/costa2.png'),
                                pygame.image.load('Data/costa2.png'), pygame.image.load('Data/costa2.png'),
                                pygame.image.load('Data/costa3.png'), pygame.image.load('Data/costa3.png'),
                                pygame.image.load('Data/costa3.png'), pygame.image.load('Data/costa3.png'),
                                pygame.image.load('Data/costa4.png'), pygame.image.load('Data/costa4.png'),
                                pygame.image.load('Data/costa4.png'), pygame.image.load('Data/costa4.png')]
        self.image = self.animation_costa[0]
        self.cont_costa = 0
        self.image = pygame.transform.scale(self.image, [35, 100])
        for index, element in enumerate(self.animation_costa):
            self.animation_costa[index] = pygame.transform.scale(self.animation_costa[index], (35, 100))
        #Direita
        self.animation_right = [pygame.image.load('Data/dir1.png'), pygame.image.load('Data/dir1.png'),
                                pygame.image.load('Data/dir1.png'), pygame.image.load('Data/dir1.png'),
                                pygame.image.load('Data/dir2.png'), pygame.image.load('Data/dir2.png'),
                                pygame.image.load('Data/dir2.png'), pygame.image.load('Data/dir2.png'),
                                pygame.image.load('Data/dir3.png'), pygame.image.load('Data/dir3.png'),
                                pygame.image.load('Data/dir3.png'), pygame.image.load('Data/dir3.png'),
                                pygame.image.load('Data/dir4.png'), pygame.image.load('Data/dir4.png'),
                                pygame.image.load('Data/dir4.png'), pygame.image.load('Data/dir4.png')]
        self.image = self.animation_right[0]
        self.cont_right = 0
        self.image = pygame.transform.scale(self.image, [60, 100])
        for index, element in enumerate(self.animation_right):
            self.animation_right[index] = pygame.transform.scale(self.animation_right[index], (60, 100))
        #Esquerda
        self.animation_left = [pygame.image.load('Data/esq1.png'), pygame.image.load('Data/esq1.png'),
                               pygame.image.load('Data/esq1.png'), pygame.image.load('Data/esq1.png'),
                               pygame.image.load('Data/esq2.png'), pygame.image.load('Data/esq2.png'),
                               pygame.image.load('Data/esq2.png'), pygame.image.load('Data/esq2.png'),
                               pygame.image.load('Data/esq3.png'), pygame.image.load('Data/esq3.png'),
                               pygame.image.load('Data/esq3.png'), pygame.image.load('Data/esq3.png'),
                               pygame.image.load('Data/esq4.png'), pygame.image.load('Data/esq4.png'),
                               pygame.image.load('Data/esq4.png'), pygame.image.load('Data/esq4.png')]
        self.image = self.animation_left[0]
        self.cont_left = 0
        self.image = pygame.transform.scale(self.image, [60, 200])
        for index, element in enumerate(self.animation_left):
            self.animation_left[index] = pygame.transform.scale(self.animation_left[index], (60, 100))
        #Parada
        self.animation_parado = [pygame.image.load('Data/parada1.png'), pygame.image.load('Data/parada1.png'),
                                 pygame.image.load('Data/parada1.png'), pygame.image.load('Data/parada1.png'),
                                 pygame.image.load('Data/parada2.png'), pygame.image.load('Data/parada2.png'),
                                 pygame.image.load('Data/parada2.png'), pygame.image.load('Data/parada2.png'),
                                 pygame.image.load('Data/parada3.png'), pygame.image.load('Data/parada3.png'),
                                 pygame.image.load('Data/parada3.png'), pygame.image.load('Data/parada3.png'),
                                 pygame.image.load('Data/parada4.png'), pygame.image.load('Data/parada4.png'),
                                 pygame.image.load('Data/parada4.png'), pygame.image.load('Data/parada4.png'),]
        self.image = self.animation_parado[0]

        self.cont_parado = 0
        self.image = pygame.transform.scale(self.image, [35, 100])
        for index, element in enumerate(self.animation_parado):
            self.animation_parado[index] = pygame.transform.scale(self.animation_parado[index], (35, 100))





    def update (self, *args):
        clock.tick(30)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:

            self.rect.x -= 4
            self.cont_left += 1
            self.image = self.animation_left[self.cont_left]

            if self.cont_left >= len(self.animation_left) - 1:
                self.cont_left = 0

                if self.cont_left == 0 or 1 or 2 or 3:
                    pisada.play()

        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += 4
            self.cont_right += 1
            self.image = self.animation_right[self.cont_right]

            if self.cont_right >= len(self.animation_right)-1:
                self.cont_right = 0

                if self.cont_right == 0 or 1 or 2 or 3:
                    pisada.play()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= 4
            self.cont_costa += 1
            self.image = self.animation_costa[self.cont_costa]

            if self.cont_costa >= len(self.animation_costa) - 1:
                self.cont_costa = 0
                if self.cont_costa == 0 or 1 or 2 or 3:
                    pisada.play()

        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += 4

            self.cont += 1
            self.image = self.animation[self.cont]

            if self.cont >= len(self.animation)-1:
                self.cont = 0
                if self.cont == 0 or 1 or 2 or 3:
                    pisada.play()

        elif not keys[pygame.K_s] and not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and not keys[pygame.K_UP] and not keys[pygame.K_DOWN] and not keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.cont_parado += 1
            self.image = self.animation_parado[self.cont_parado]
            self.image = pygame.transform.flip(self.image, True, False)

            if self.cont_parado >= len(self.animation_parado) - 1:
                self.cont_parado = 0

        if self.rect.right < 50:
            self.rect.right = 50
        elif self.rect.left > 750:
            self.rect.left = 750
        elif self.rect.top < 50:
            self.rect.top = 50
        elif self.rect.bottom > 620:
            self.rect.bottom = 620