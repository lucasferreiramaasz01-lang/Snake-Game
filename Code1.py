import pygame
import random
from random import randint
from pygame.locals import *
from sys import exit
pygame.init()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
velocidade = 40
FPS = 10
controle_x = 0
controle_y = 0
Game_running = False
relogio = pygame.time.Clock()
lista_cobra = []
cabeca_cobra = []
tamanho = 3
pontos = 0

font = pygame.font.SysFont('Times New Roman', 20, True, True)

morreu = False
x_maca = randint (0, largura-40)
y_maca = randint (0, altura-40)
x_cobra = (largura/2)-40
y_cobra = 280

def GeraCobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [x, y]
        #XeY[0] = x
        #XeY[1] = y
        cobra = pygame.draw.rect(tela, (46, 139, 87), (XeY[0], XeY[1], 40, 40))
def ReiniciarJogo():
    global pontos, controle_x, controle_y, lista_cobra, tamanho, morreu, x_maca, y_maca, x_cobra, y_cobra
    pontos = 0
    controle_x = 0
    controle_y = 0
    lista_cobra = []
    tamanho = 3
    morreu = False
    x_maca = (randint(0, 19)) * 40
    y_maca = (randint(0, 14)) * 40
    x_cobra = (largura/2)-40
    y_cobra = 280
while True:
    relogio.tick(FPS)
    tela.fill((144, 238, 144))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = font.render(mensagem, True, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == (K_a) or (K_s) or (K_w) or (K_d):
                Game_running = True
            if event.key == K_a:
                if controle_x == velocidade:
                    pass
                else:
                    controle_x = -velocidade
                    controle_y = 0
            if event.key == K_d:
                if controle_x == -velocidade:
                    pass
                else:
                    controle_x = velocidade
                    controle_y = 0
            if event.key == K_w:
                if controle_y == velocidade:
                    pass
                else:
                    controle_y = -velocidade
                    controle_x = 0
            if event.key == K_s:
                if controle_y == -velocidade:
                    pass
                else:
                    controle_y = velocidade
                    controle_x = 0
    x_cobra += controle_x
    y_cobra += controle_y
    cabeca_cobra = []
    cabeca_cobra.append(x_cobra)
    cabeca_cobra.append(y_cobra)
    lista_cobra.append(cabeca_cobra)
    cobra = pygame.draw.rect(tela, (46, 139, 87), (x_cobra, y_cobra, 40, 40))
    while (len(lista_cobra) > tamanho):
        del lista_cobra[0]
    GeraCobra(lista_cobra)
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 40, 40))
    if cobra.colliderect(maca):
        tamanho += 1
        pontos += 1
        x_maca = (randint(0, 19)) * 40
        y_maca = (randint(0, 14)) * 40
    if (((lista_cobra.count(cabeca_cobra)>1) or (((cabeca_cobra[1]<0) or (cabeca_cobra[1]>=altura)) or ((cabeca_cobra[0]<0) or (cabeca_cobra[0]>=largura)))) and Game_running==True):
        morreu=True
        fonte2 = pygame.font.SysFont('Times New Roman', 30, True, True )
        mensagem2 = "Você morreu! Pressione R para jogar novamente!"
        texto_formatado2 = fonte2.render(mensagem2, True, (30,144,255))
        ret_texto = texto_formatado2.get_rect()
        while morreu:
            Game_running = False
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        ReiniciarJogo()
            ret_texto.center = (largura // 2, altura // 2)
            tela.blit(texto_formatado2, ret_texto)
            pygame.display.update()
    tela.blit(texto_formatado, (650, 40))
    pygame.display.update()