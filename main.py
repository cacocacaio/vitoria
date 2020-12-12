import os
import sys
import pygame
import random
import threading
from threading import Thread
import socket
from pygame.locals import *

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

def ghostPosition(element):

    arr = element.split(", ")

    if len(arr) == 1:
        return "repeat", int(arr[0])
    else:
        return int(arr[0]), int(arr[1])

#inicializando
pygame.init()
buttomsong = pygame.mixer.Sound('Data/desert.wav')

def jogo():
    gameLoop_3 = True
    global end
    global menu
    global buttomsong
    global game
    global gameLoop
    from player import player
    from saci import saci
    from homemdosaco import homemdosaco
    from cuca import cuca
    from mula import mula

    ghost = getGhost()
    gframe = 0
    gcount = 0

    altura = 640
    largura = 840
    display = pygame.display.set_mode([largura, altura])
    pygame.display.set_caption('Vitória: Uma Odisseia no folclore Brasileiro ')

    objectGroup = pygame.sprite.Group()
    objectGroup1 = pygame.sprite.Group()
    objectGroup2 = pygame.sprite.Group()
    objectGroup3 = pygame.sprite.Group()
    objectGroup4 = pygame.sprite.Group()

    bg = pygame.sprite.Sprite(objectGroup)
    bg.image = pygame.image.load('Data/grass.jpg')
    bg.image = pygame.transform.scale(bg.image, [largura, altura])
    bg.rect = bg.image.get_rect()

    # VEGETAÇÂO
    mato = pygame.sprite.Sprite(objectGroup)
    mato.image = pygame.image.load('Data/Mato.png')
    mato.image = pygame.transform.scale(mato.image, [80, 100])
    mato.rect = pygame.Rect(50, 50, 52, 50)
    mato = pygame.sprite.Sprite(objectGroup)
    mato.image = pygame.image.load('Data/Mato.png')
    mato.image = pygame.transform.scale(mato.image, [80, 100])
    mato.rect = pygame.Rect(-10, 50, 52, 50)
    mato = pygame.sprite.Sprite(objectGroup)
    mato.image = pygame.image.load('Data/Mato.png')
    mato.image = pygame.transform.scale(mato.image, [80, 100])
    mato.rect = pygame.Rect(100, 50, 52, 50)
    mato = pygame.sprite.Sprite(objectGroup)
    mato.image = pygame.image.load('Data/Mato.png')
    mato.image = pygame.transform.scale(mato.image, [80, 100])
    mato.rect = pygame.Rect(150, 50, 52, 50)
    mato = pygame.sprite.Sprite(objectGroup)
    mato.image = pygame.image.load('Data/Mato.png')
    mato.image = pygame.transform.scale(mato.image, [80, 100])
    mato.rect = pygame.Rect(200, 50, 52, 50)
    mato = pygame.sprite.Sprite(objectGroup)
    mato.image = pygame.image.load('Data/Mato.png')
    mato.image = pygame.transform.scale(mato.image, [80, 100])
    mato.rect = pygame.Rect(250, 50, 52, 50)
    mato = pygame.sprite.Sprite(objectGroup)
    mato.image = pygame.image.load('Data/Mato.png')
    mato.image = pygame.transform.scale(mato.image, [80, 100])
    mato.rect = pygame.Rect(300, 50, 52, 50)
    mato = pygame.sprite.Sprite(objectGroup)
    mato.image = pygame.image.load('Data/Mato.png')
    mato.image = pygame.transform.scale(mato.image, [80, 100])
    mato.rect = pygame.Rect(350, 50, 52, 50)
    mato = pygame.sprite.Sprite(objectGroup)
    mato.image = pygame.image.load('Data/Mato.png')
    mato.image = pygame.transform.scale(mato.image, [80, 100])
    mato.rect = pygame.Rect(400, 50, 52, 50)
    mato = pygame.sprite.Sprite(objectGroup)
    mato.image = pygame.image.load('Data/Mato.png')
    mato.image = pygame.transform.scale(mato.image, [80, 100])
    mato.rect = pygame.Rect(450, 50, 52, 50)
    mato = pygame.sprite.Sprite(objectGroup)
    mato.image = pygame.image.load('Data/Mato.png')
    mato.image = pygame.transform.scale(mato.image, [80, 100])
    mato.rect = pygame.Rect(500, 50, 52, 50)
    mato = pygame.sprite.Sprite(objectGroup)
    mato.image = pygame.image.load('Data/Mato.png')
    mato.image = pygame.transform.scale(mato.image, [80, 100])
    mato.rect = pygame.Rect(550, 50, 52, 50)
    mato = pygame.sprite.Sprite(objectGroup)
    mato.image = pygame.image.load('Data/Mato.png')
    mato.image = pygame.transform.scale(mato.image, [80, 100])
    mato.rect = pygame.Rect(600, 50, 52, 50)
    mato = pygame.sprite.Sprite(objectGroup)
    mato.image = pygame.image.load('Data/Mato.png')
    mato.image = pygame.transform.scale(mato.image, [80, 100])
    mato.rect = pygame.Rect(650, 50, 52, 50)
    mato = pygame.sprite.Sprite(objectGroup)
    mato.image = pygame.image.load('Data/Mato.png')
    mato.image = pygame.transform.scale(mato.image, [80, 100])
    mato.rect = pygame.Rect(700, 50, 52, 50)
    mato = pygame.sprite.Sprite(objectGroup)
    mato.image = pygame.image.load('Data/Mato.png')
    mato.image = pygame.transform.scale(mato.image, [80, 100])
    mato.rect = pygame.Rect(750, 50, 52, 50)
    # divisão
    arvore = pygame.sprite.Sprite(objectGroup)
    arvore.image = pygame.image.load('Data/arvore.png')
    arvore.image = pygame.transform.scale(arvore.image, [200, 400])
    arvore.rect = pygame.Rect(0, -250, 20, 200)
    arvore = pygame.sprite.Sprite(objectGroup)
    arvore.image = pygame.image.load('Data/arvore.png')
    arvore.image = pygame.transform.scale(arvore.image, [200, 400])
    arvore.rect = pygame.Rect(150, -250, 20, 200)
    mato = pygame.sprite.Sprite(objectGroup)
    mato.image = pygame.image.load('Data/Mato.png')
    mato.image = pygame.transform.scale(mato.image, [80, 100])
    mato.rect = pygame.Rect(200, 50, 52, 50)
    arvore = pygame.sprite.Sprite(objectGroup)
    arvore.image = pygame.image.load('Data/arvore.png')
    arvore.image = pygame.transform.scale(arvore.image, [200, 400])
    arvore.rect = pygame.Rect(300, -250, 20, 200)
    arvore = pygame.sprite.Sprite(objectGroup3)
    arvore.image = pygame.image.load('Data/arvore.png')
    arvore.image = pygame.transform.scale(arvore.image, [200, 400])
    arvore.rect = pygame.Rect(-140, -75, 20, 200)
    arvore = pygame.sprite.Sprite(objectGroup)
    arvore.image = pygame.image.load('Data/arvore.png')
    arvore.image = pygame.transform.scale(arvore.image, [200, 400])
    arvore.rect = pygame.Rect(675, -250, 20, 200)
    arvore = pygame.sprite.Sprite(objectGroup3)
    arvore.image = pygame.image.load('Data/arvore.png')
    arvore.image = pygame.transform.scale(arvore.image, [200, 400])
    arvore.rect = pygame.Rect(750, -75, 20, 200)
    arvore = pygame.sprite.Sprite(objectGroup3)
    arvore.image = pygame.image.load('Data/arvore.png')
    arvore.image = pygame.transform.scale(arvore.image, [200, 400])
    arvore.rect = pygame.Rect(750, 200, 20, 200)
    arvore = pygame.sprite.Sprite(objectGroup3)
    arvore.image = pygame.image.load('Data/arvore.png')
    arvore.image = pygame.transform.scale(arvore.image, [200, 400])
    arvore.rect = pygame.Rect(-150, 200, 20, 200)
    arvore = pygame.sprite.Sprite(objectGroup3)
    arvore.image = pygame.image.load('Data/arvore.png')
    arvore.image = pygame.transform.scale(arvore.image, [200, 400])
    arvore.rect = pygame.Rect(-150, 300, 20, 200)

    moita2 = pygame.sprite.Sprite(objectGroup)
    moita2.image = pygame.image.load('Data/Moita2.png')
    moita2.image = pygame.transform.scale(moita2.image, [80, 100])
    moita2.rect = pygame.Rect(300, 50, 20, 200)
    moita2 = pygame.sprite.Sprite(objectGroup)
    moita2.image = pygame.image.load('Data/Moita2.png')
    moita2.image = pygame.transform.scale(moita2.image, [80, 100])
    moita2.rect = pygame.Rect(100, 50, 20, 200)
    moita2 = pygame.sprite.Sprite(objectGroup)
    moita2.image = pygame.image.load('Data/Moita2.png')
    moita2.image = pygame.transform.scale(moita2.image, [80, 100])
    moita2.rect = pygame.Rect(650, 50, 20, 200)

    moita2 = pygame.sprite.Sprite(objectGroup3)
    moita2.image = pygame.image.load('Data/Moita2.png')
    moita2.image = pygame.transform.scale(moita2.image, [80, 100])
    moita2.rect = pygame.Rect(800, 545, 40, 200)
    moita2p1 = pygame.sprite.Sprite(objectGroup3)
    moita2p1.image = pygame.image.load('Data/Moita2.png')
    moita2p1.image = pygame.transform.scale(moita2.image, [80, 100])
    moita2p1.rect = pygame.Rect(300, 200, 40, 200)
    moita2p2 = pygame.sprite.Sprite(objectGroup3)
    moita2p2.image = pygame.image.load('Data/Moita2.png')
    moita2p2.image = pygame.transform.scale(moita2.image, [80, 100])
    moita2p2.rect = pygame.Rect(115, 300, 40, 200)
    moita2p3 = pygame.sprite.Sprite(objectGroup3)
    moita2p3.image = pygame.image.load('Data/Moita2.png')
    moita2p3.image = pygame.transform.scale(moita2.image, [80, 100])
    moita2p3.rect = pygame.Rect(400, 500, 40, 200)
    moita2p4 = pygame.sprite.Sprite(objectGroup3)
    moita2p4.image = pygame.image.load('Data/Moita2.png')
    moita2p4.image = pygame.transform.scale(moita2.image, [80, 100])
    moita2p4.rect = pygame.Rect(600, 125, 40, 200)
    moita2p5 = pygame.sprite.Sprite(objectGroup3)
    moita2p5.image = pygame.image.load('Data/Moita2.png')
    moita2p5.image = pygame.transform.scale(moita2.image, [80, 100])
    moita2p5.rect = pygame.Rect(150, 500, 40, 200)
    moita2p6 = pygame.sprite.Sprite(objectGroup3)
    moita2p6.image = pygame.image.load('Data/Moita2.png')
    moita2p6.image = pygame.transform.scale(moita2.image, [80, 100])
    moita2p6.rect = pygame.Rect(600, 400, 40, 200)
    moita2p7 = pygame.sprite.Sprite(objectGroup3)
    moita2p7.image = pygame.image.load('Data/Moita2.png')
    moita2p7.image = pygame.transform.scale(moita2.image, [80, 100])
    moita2p7.rect = pygame.Rect(350, 360, 40, 200)
    moita2p8 = pygame.sprite.Sprite(objectGroup3)
    moita2p8.image = pygame.image.load('Data/Moita2.png')
    moita2p8.image = pygame.transform.scale(moita2.image, [80, 100])
    moita2p8.rect = pygame.Rect(510, 300, 40, 200)

    arvore = pygame.sprite.Sprite(objectGroup)
    arvore.image = pygame.image.load('Data/arvore.png')
    arvore.image = pygame.transform.scale(arvore.image, [200, 400])
    arvore.rect = pygame.Rect(500, -250, 20, 200)


    saci = saci(objectGroup)
    player = player(objectGroup1)
    homemdosaco = homemdosaco(objectGroup4)
    cuca = cuca(objectGroup4)
    mula = mula(objectGroup4)

    # Sons
    pygame.mixer.music.load('Data/bensound-adventure.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)

    win = 0

    movements = []

    while gameLoop_3:

        movements.append([player.rect.x, player.rect.y])

        if gframe<len(ghost) and not gcount:
            ghostx, ghosty = ghostPosition(ghost[gframe])
            gframe += 1
            if ghostx == "repeat":
                gcount = ghosty
                ghostx, ghosty = ghostPosition(ghost[gframe])
        else:
            gcount -= 1

        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
                gameLoop_3 = False

        if player.rect.y > moita2p1.rect.y:
            objectGroup3.remove(moita2p1)
            objectGroup.add(moita2p1)
        if player.rect.y < moita2p1.rect.y:
            objectGroup.remove(moita2p1)
            objectGroup3.add(moita2p1)
        if player.rect.y > moita2p2.rect.y:
            objectGroup3.remove(moita2p2)
            objectGroup.add(moita2p2)
        if player.rect.y < moita2p2.rect.y:
            objectGroup.remove(moita2p2)
            objectGroup3.add(moita2p2)
        if player.rect.y > moita2p3.rect.y:
            objectGroup3.remove(moita2p3)
            objectGroup.add(moita2p3)
        if player.rect.y < moita2p3.rect.y:
            objectGroup.remove(moita2p3)
            objectGroup3.add(moita2p3)
        if player.rect.y > moita2p4.rect.y:
            objectGroup3.remove(moita2p4)
            objectGroup.add(moita2p4)
        if player.rect.y < moita2p4.rect.y:
            objectGroup.remove(moita2p4)
            objectGroup3.add(moita2p4)
        if player.rect.y > moita2p5.rect.y:
            objectGroup3.remove(moita2p5)
            objectGroup.add(moita2p5)
        if player.rect.y < moita2p5.rect.y:
            objectGroup.remove(moita2p5)
            objectGroup3.add(moita2p5)
        if player.rect.y > moita2p6.rect.y:
            objectGroup3.remove(moita2p6)
            objectGroup.add(moita2p6)
        if player.rect.y < moita2p6.rect.y:
            objectGroup.remove(moita2p6)
            objectGroup3.add(moita2p6)
        if player.rect.y > moita2p7.rect.y:
            objectGroup3.remove(moita2p7)
            objectGroup.add(moita2p7)
        if player.rect.y < moita2p7.rect.y:
            objectGroup.remove(moita2p7)
            objectGroup3.add(moita2p7)
        if player.rect.y > moita2p8.rect.y:
            objectGroup3.remove(moita2p8)
            objectGroup.add(moita2p8)
        if player.rect.y < moita2p8.rect.y:
            objectGroup.remove(moita2p8)
            objectGroup3.add(moita2p8)


        objectGroup.update()
        objectGroup1.update()
        objectGroup2.update()
        objectGroup3.update()
        objectGroup4.update()
        # desenho:
        objectGroup.draw(display)
        objectGroup1.draw(display)
        objectGroup2.draw(display)
        objectGroup3.draw(display)
        objectGroup4.draw(display)
        pygame.display.update()

        colissions = pygame.sprite.groupcollide(objectGroup4, objectGroup1, True, False, pygame.sprite.collide_mask)

        if colissions:
            win += 1

        if win == 3:
            gameLoop_3 = False
            game = False
            end = True

    movdictionary(movements)



class Background:

    def __init__(self):
        image = pygame.image.load("Data/Title.png")
        image = image.convert()
        background = image
        self.surface = pygame.Surface(background.get_size())
        self.surface.convert()
        self.surface.blit(background, (0, 0))
        self.pos = background.get_rect()

class fimdejogo:

    def __init__(self):
        image = pygame.image.load('Data/win.jpeg')
        image = image.convert()
        background = image
        self.surface = pygame.Surface(background.get_size())
        self.surface.convert()
        self.surface.blit(background, (0, 0))
        self.pos = background.get_rect()

class quadros:

    def __init__(self):
        image = pygame.image.load("Data/quadrinho1.png")
        image = image.convert()
        quadros = image
        self.surface = pygame.Surface(quadros.get_size())
        self.surface.convert()
        self.surface.blit(quadros, (0, 0))
        self.pos = quadros.get_rect()

class quadros2:

    def __init__(self):
        image = pygame.image.load("Data/quadrinho2.png")
        image = image.convert()
        quadros2 = image
        self.surface = pygame.Surface(quadros2.get_size())
        self.surface.convert()
        self.surface.blit(quadros2, (0, 0))
        self.pos = quadros2.get_rect()

class quadros3:

    def __init__(self):
        image = pygame.image.load("Data/quadrinho3.png")
        image = image.convert()
        quadros3 = image
        self.surface = pygame.Surface(quadros3.get_size())
        self.surface.convert()
        self.surface.blit(quadros3, (0, 0))
        self.pos = quadros3.get_rect()

class quadros4:

    def __init__(self):
        image = pygame.image.load("Data/quadrinho4.png")
        image = image.convert()
        quadros4 = image
        self.surface = pygame.Surface(quadros4.get_size())
        self.surface.convert()
        self.surface.blit(quadros4, (0, 0))
        self.pos = quadros4.get_rect()

class Button:

    def __init__(self, str, x, y):
        font = pygame.font.Font(None, 60)
        text = font.render(str, 0, (0, 0, 0))
        textpos = text.get_rect()

        self.surface = pygame.Surface((max(300, textpos.width), textpos.height + 10))
        self.surface.fill((0, 255, 0))
        self.surface.set_colorkey((0, 255, 0))
        self.surfacepos = self.surface.get_rect()
        textpos.centerx = self.surfacepos.centerx
        textpos.centery = self.surfacepos.centery
        self.surface.blit(text, textpos)
        self.surfacepos.centerx = x
        self.surfacepos.top = y

    def move(self, x, y):

        self.surfacepos.centerx = x
        self.surfacepos.top = y

def uploadGhost():

    HOST = ''
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Conectado com ', addr)
            with open("Data/dic.txt") as data:
                conn.sendall(data.read().encode())

    return


def updateGhost(HOST):

    PORT = 65432
    dic = ""

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            dic = s.recv(32768).decode()
    except:
        return "Invalido"

    file = open("Data/dic.txt", "a")
    file.write(str(dic) + "\n")
    file.close()
    return "Concluido"

def getGhost():

    file = open("Data/dic.txt", "r")
    array = file.read().split("\n")
    if len(array) == 1: return
    array = array[random.randrange(len(array)-1)]
    array = array[2:-2]
    array = array.split("], [")
    return array

def main():
    gameLoop_2 = True
    global gameLoop_3
    global gameLoop
    global menu
    global game
    global cenas
    global buttomsong
    pygame.init()
    screen = pygame.display.set_mode((840, 640))
    pygame.display.set_caption("Vitoria: uma odisseia no folclore brasileiro")

    t = threading.Thread(target=uploadGhost, daemon=True)
    t.start()

    blank_screen = pygame.Surface(screen.get_size())
    blank_screen = blank_screen.convert()
    blank_screen.fill((255, 255, 255))

    new_screen = blank_screen

    b = Background()
    b.pos.centerx = new_screen.get_rect().centerx
    b.pos.bottom = new_screen.get_rect().bottom
    new_screen.blit(b.surface, b.pos)

    play = Button("JOGAR", new_screen.get_rect().centerx, new_screen.get_rect().centery)
    new_screen.blit(play.surface, play.surfacepos)
    help = Button("INSTRUÇÕES", new_screen.get_rect().centerx, new_screen.get_rect().centery+80)
    new_screen.blit(help.surface, help.surfacepos)
    credito = Button("CRÉDITOS", new_screen.get_rect().centerx, new_screen.get_rect().centery+160)
    new_screen.blit(credito.surface, credito.surfacepos)
    conect = Button("CONECTAR FANTASMA", new_screen.get_rect().centerx, new_screen.get_rect().centery+240)
    new_screen.blit(conect.surface, conect.surfacepos)
    back = Button("VOLTAR", -300, -300)

    font = pygame.font.Font(None, 30)
    font_title = pygame.font.Font(None, 60)

    vitoria = font_title.render("VITÓRIA", 0, (200, 10, 30))
    vitoriapos = vitoria.get_rect()
    odisseia = font.render("uma odisseia no folclore brasileiro", 0, (255, 255, 255))
    odisseiapos = odisseia.get_rect()
    titulo = pygame.Surface((odisseiapos.width, screen.get_height()))
    titulo.fill((0, 255, 0))
    titulo.set_colorkey((0, 255, 0))
    titulopos = titulo.get_rect()
    vitoriapos.centerx = titulopos.centerx
    vitoriapos.top = titulopos.centery
    odisseiapos.centerx = titulopos.centerx
    odisseiapos.top = vitoriapos.bottom + 20
    titulo.blits(((vitoria, vitoriapos), (odisseia, odisseiapos)))
    titulopos.centery = new_screen.get_rect().top + 100
    titulopos.centerx = new_screen.get_rect().centerx
    new_screen.blit(titulo, titulopos)

    inputclick = False
    IP = ''
    inp = font_title.render(IP, 0, (255, 255, 255))
    inppos = inp.get_rect()
    inpbox = pygame.Surface((350, 50))
    inpboxpos = inpbox.get_rect()
    inpbox.fill((0, 0, 0))
    inppos.centerx = inpboxpos.centerx
    inppos.centery = inpboxpos.centery
    inpbox.blit(inp, inppos)
    pygame.draw.rect(inpbox, (255, 255, 255), inpboxpos, 5)
    inpboxpos.centerx = -300
    inpboxpos.centery = -300

    mover = font.render("Pressione as SETAS para se mover.", 0, (255, 255, 255))
    moverpos = mover.get_rect()
    instrucoes = pygame.Surface((int(screen.get_width()/2), (mover.get_height())*2))
    instrucoes.fill((0, 255, 0))
    instrucoes.set_colorkey((0, 255, 0))
    instrucoespos = instrucoes.get_rect()
    moverpos.centerx = instrucoespos.centerx
    moverpos.top = instrucoespos.top + 10
    instrucoes.blit(mover, moverpos)
    instrucoespos.left = int(screen.get_width()/4)
    instrucoespos.top = new_screen.get_rect().centery - 100

    c_caio = font.render("Caio César Nogueira : Programador, Artista Conceitual;", 0, (255, 255, 255))
    c_caiopos = c_caio.get_rect()
    c_jere = font.render("Jeremias : Artista;", 0, (255, 255, 255))
    c_jerepos = c_jere.get_rect()
    c_vini = font.render("Vinicius : Programador.", 0, (255, 255, 255))
    c_vinipos = c_vini.get_rect()
    creditos = pygame.Surface(((int(screen.get_width()*2/3)), (c_caio.get_height() + c_jere.get_height() + c_vini.get_height())*2))
    creditos.fill((0, 255, 0))
    creditos.set_colorkey((0, 255, 0))
    creditospos = creditos.get_rect()
    c_caiopos.centerx = creditospos.centerx
    c_vinipos.centerx = creditospos.centerx
    c_jerepos.centerx = creditospos.centerx
    c_caiopos.top = creditospos.top
    c_jerepos.top = c_caiopos.bottom + 20
    c_vinipos.top = c_jerepos.bottom + 20
    creditos.blits(((c_caio, c_caiopos), (c_jere, c_jerepos), (c_vini, c_vinipos)))
    creditospos.left = int(screen.get_width()/6)
    creditospos.top = new_screen.get_rect().centery - 50

    screen.blit(new_screen, (0, 0))
    pygame.display.flip()

    pygame.mixer.music.load('Data/bensound-adventure.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.8)

    global disconnect

    while gameLoop_2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                gameLoop_2 = False
                gameLoop = False
                disconnect = False

            if inputclick:

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        IP = updateGhost(IP)
                    elif event.key == pygame.K_BACKSPACE:
                        IP = IP[:-1]
                    else:
                        IP += event.unicode


            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if inpboxpos.collidepoint(pos):inputclick = True
                else: inputclick = False

                if play.surfacepos.collidepoint(pos):
                    buttomsong.play()
                    cenas = True
                    menu = False
                    gameLoop_2 = False
                    disconnect = False

                if help.surfacepos.collidepoint(pos):

                    buttomsong.play()
                    new_screen = blank_screen
                    play.move(-300, -300)
                    help.move(-300, -300)
                    credito.move(-300, -300)
                    conect.move(-300, -300)
                    back.move(new_screen.get_rect().centerx, new_screen.get_rect().centery+200)
                    b.pos.right = new_screen.get_rect().right
                    b.pos.bottom = new_screen.get_rect().bottom
                    new_screen.blit(b.surface, b.pos)
                    new_screen.blit(back.surface, back.surfacepos)
                    new_screen.blit(instrucoes, instrucoespos)

                if credito.surfacepos.collidepoint(pos):

                    buttomsong.play()
                    new_screen = blank_screen
                    play.move(-300, -300)
                    help.move(-300, -300)
                    credito.move(-300, -300)
                    conect.move(-300, -300)
                    back.move(new_screen.get_rect().centerx, new_screen.get_rect().centery+200)
                    b.pos.centerx = new_screen.get_rect().centerx
                    b.pos.top = new_screen.get_rect().top
                    new_screen.blit(b.surface, b.pos)
                    new_screen.blit(creditos, creditospos)
                    new_screen.blit(back.surface, back.surfacepos)

                if conect.surfacepos.collidepoint(pos):

                    buttomsong.play()
                    new_screen = blank_screen
                    back.move(new_screen.get_rect().centerx, new_screen.get_rect().centery+200)
                    play.move(-300, -300)
                    help.move(-300, -300)
                    credito.move(-300, -300)
                    conect.move(-300, -300)
                    new_screen.blit(b.surface, b.pos)
                    inpboxpos.centerx = new_screen.get_rect().centerx
                    inpboxpos.centery = new_screen.get_rect().centery - 100
                    new_screen.blit(back.surface, back.surfacepos)

                if back.surfacepos.collidepoint(pos):

                    buttomsong.play()
                    new_screen = blank_screen
                    play.move(new_screen.get_rect().centerx, new_screen.get_rect().centery)
                    help.move(new_screen.get_rect().centerx, new_screen.get_rect().centery+80)
                    credito.move(new_screen.get_rect().centerx, new_screen.get_rect().centery+160)
                    conect.move(new_screen.get_rect().centerx, new_screen.get_rect().centery+240)
                    inpboxpos.centerx = -300
                    inpboxpos.centery = -300
                    back.move(-300, -300)
                    b.pos.centerx = new_screen.get_rect().centerx
                    b.pos.bottom = new_screen.get_rect().bottom
                    new_screen.blit(b.surface, b.pos)
                    new_screen.blit(play.surface, play.surfacepos)
                    new_screen.blit(help.surface, help.surfacepos)
                    new_screen.blit(credito.surface, credito.surfacepos)
                    new_screen.blit(conect.surface, conect.surfacepos)
                    new_screen.blit(titulo, titulopos)

        inp = font_title.render(IP, 0, (255, 255, 255))
        inppos = inp.get_rect()
        inpbox.fill((0, 0, 0))
        pygame.draw.rect(inpbox, (255, 255, 255), inpboxpos, 5)
        inpbox.blit(inp, inppos)
        new_screen.blit(inpbox, inpboxpos)
        screen.blit(new_screen, (0, 0))
        pygame.display.flip()

def cutscene():
    global buttomsong
    global cenas
    global game
    global gameLoop

    quadropas1 = True
    quadropas2 = False
    quadropas3 = False
    quadropas4 = False


    pygame.init()
    screen = pygame.display.set_mode((840, 640))
    pygame.display.set_caption("Vitoria: uma odisseia no folclore brasileiro")


    blank_screen = pygame.Surface(screen.get_size())
    blank_screen = blank_screen.convert()
    blank_screen.fill((255, 255, 255))
    new_screen = blank_screen

    quadro = quadros()
    quadro.pos.centerx = new_screen.get_rect().centerx - 50
    quadro.pos.bottom = new_screen.get_rect().bottom + 100
    new_screen.blit(quadro.surface, quadro.pos)


    gameLoop_4 = True

    while gameLoop_4:
        for event in pygame.event.get():
            if quadropas1:
                continuar1 = Button("Continuar", new_screen.get_rect().centerx + -315,
                                    new_screen.get_rect().centery + 270)
                new_screen.blit(continuar1.surface, continuar1.surfacepos)
                screen.blit(new_screen, (0, 0))
                if event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if continuar1.surfacepos.collidepoint(pos):
                        buttomsong.play()
                        quadropas1 = False
                        quadropas2 = True
            if quadropas2:
                quadro2 = quadros2()
                quadro2.pos.centerx = new_screen.get_rect().centerx - 50
                quadro2.pos.bottom = new_screen.get_rect().bottom + 100
                new_screen.blit(quadro2.surface, quadro2.pos)
                continuar2 = Button("Continuar", new_screen.get_rect().centerx -90,
                                    new_screen.get_rect().centery + 270)
                new_screen.blit(continuar2.surface, continuar2.surfacepos)
                screen.blit(new_screen, (0, 0))
                if event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if continuar2.surfacepos.collidepoint(pos):
                        buttomsong.play()
                        quadropas2= False
                        quadropas3 = True
            if quadropas3:
                quadro3 = quadros3()
                quadro3.pos.centerx = new_screen.get_rect().centerx - 50
                quadro3.pos.bottom = new_screen.get_rect().bottom + 100
                new_screen.blit(quadro3.surface, quadro3.pos)
                continuar3 = Button("Continuar", new_screen.get_rect().centerx +130,
                                    new_screen.get_rect().centery + 270)
                new_screen.blit(continuar3.surface, continuar3.surfacepos)
                screen.blit(new_screen, (0, 0))
                if event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if continuar3.surfacepos.collidepoint(pos):
                        buttomsong.play()
                        quadropas3 = False
                        quadropas4 = True
            if quadropas4:
                quadro4 = quadros4()
                quadro4.pos.centerx = new_screen.get_rect().centerx - 50
                quadro4.pos.bottom = new_screen.get_rect().bottom + 100
                new_screen.blit(quadro4.surface, quadro4.pos)
                continuar4 = Button("Continuar", new_screen.get_rect().centerx + 320,
                                    new_screen.get_rect().centery + 270)
                new_screen.blit(continuar4.surface, continuar4.surfacepos)
                screen.blit(new_screen, (0, 0))
                if event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if continuar4.surfacepos.collidepoint(pos):
                        buttomsong.play()
                        game = True
                        gameLoop_4 = False
                        cenas = False

            if event.type == pygame.QUIT:
                gameLoop_4 = False
                gameLoop = False

        screen.blit(new_screen, (0, 0))
        pygame.display.flip()

def gameover():
    global gameLoop
    global menu
    global end
    gameLoop_5 = True
    pygame.init()
    screen = pygame.display.set_mode((840, 640))
    pygame.display.set_caption("Vitoria: uma odisseia no folclore brasileiro")

    blank_screen = pygame.Surface(screen.get_size())
    blank_screen = blank_screen.convert()
    blank_screen.fill((255, 255, 255))
    new_screen = blank_screen

    final = fimdejogo()
    final.pos.centerx = new_screen.get_rect().centerx - 50
    final.pos.bottom = new_screen.get_rect().bottom + 420
    new_screen.blit(final.surface, final.pos)

    voltar_menu = Button("Voltar ao menu", new_screen.get_rect().centerx,
                        new_screen.get_rect().centery)
    new_screen.blit(voltar_menu.surface, voltar_menu.surfacepos)

    agradecimento = Button("VITÓRIA", new_screen.get_rect().centerx - 120,
                        new_screen.get_rect().centery - 100)
    new_screen.blit(agradecimento.surface, agradecimento.surfacepos)

    agradecimento = Button("CONSEGUIU!", new_screen.get_rect().centerx +120,
                        new_screen.get_rect().centery - 95)
    new_screen.blit(agradecimento.surface, agradecimento.surfacepos)

    while gameLoop_5:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if voltar_menu.surfacepos.collidepoint(pos):
                    buttomsong.play()
                    gameLoop_5 = False
                    end = False
                    menu = True
            if event.type == pygame.QUIT:
                gameLoop_5 = False
                gameLoop = False



        screen.blit(new_screen, (0, 0))
        pygame.display.flip()

def movdictionary(movs):

    idle = 0
    out = []

    for p, e in enumerate(movs[:-1]):

        if e != movs[p+1]:

            if idle:
                out.append([idle])
                idle = 0
            out.append(e)
        else:

            idle += 1

    out.append(movs[-1])

    file = open("Data/dic.txt", "a")
    file.write(str(out) + "\n")
    file.close

gameLoop = True
menu = True
game = False
cenas = False
end = False

clock = pygame.time.Clock()
while gameLoop:
    clock.tick(30)
    if cenas:
        cutscene()
    if menu:
        main()
    if game:
        jogo()
    if end:
        gameover()



        pygame.display.update()
