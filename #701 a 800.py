'''
import PyPDF2
from PyPDF2.errors import PdfReadError

def Ler_Pdf(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'rb') as arquivo_pdf:
            pdf = PyPDF2.PdfReader(arquivo_pdf)
            texto_primeira_pagina = pdf.pages[0].extract_text()
            return texto_primeira_pagina

    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None
    except PdfReadError:
        print("Erro ao ler o arquivo PDF.")
        return None

caminho = input("Digite o caminho do arquivo PDF: ").strip('""')
conteudo = Ler_Pdf(caminho)

if conteudo:
    print("Conteudo da primeira página: ")
    print(conteudo)


import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True


pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(3)


pyautogui.click(x = 679, y = 418)


pyautogui.click(x = 298, y = 59)
pyautogui.write('https//youtube.com')
pyautogui.press('enter')
time.sleep(3)
'''

import pygame
import random
import sys

pygame.init ()

LARGURA = 500
ALTURA = 500
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Desvie do Quadrado!")

BRANCO = (255,255,255)
PRETO = (0,0,0)
VERMELHO = (200,0,0)
AZUL = (0,0,200)

player_tam = 50
player_vel = 10

enemy_tam = 50
enemy_vel = 15

fonte = pygame.font.SysFont("Arial", 30)
fonte_gameover = pygame.font.SysFont("Arial", 50, bold=True)

clock = pygame.time.Clock()

def desenhar_tela(player_x, player_y, enemy_x, enemy_y, pontos):
    tela.fill(BRANCO)
    pygame.draw.rect(tela, AZUL, (player_x, player_y, player_tam, player_tam))
    pygame.draw.rect(tela, VERMELHO, (enemy_x, enemy_y, enemy_tam, enemy_tam))
    texto = fonte.render(f"Pontos: {pontos}", True, PRETO)
    tela.blit(texto, (10,10))
    pygame.display.update()

def game_over_screen(pontos):
    tela.fill(BRANCO)
    texto1 = fonte_gameover.render("GAME OVER", True, VERMELHO)
    texto2 = fonte.render(f"Sua pontuação: {pontos}", True, PRETO)
    texto3 = fonte.render("pressione R para reiniciar ou ESC para sair", True, PRETO)
    tela.blit(texto1, (LARGURA//2 - texto1.get_width()//2, 150))
    tela.blit(texto2, (LARGURA//2 - texto2.get_width()//2, 250))
    tela.blit(texto3, (LARGURA//2 - texto3.get_width()//2, 300))
    pygame.display.update()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if evento.key == pygame.K_r:
                    esperando = False

def jogo():

    player_x = LARGURA // 2 - player_tam // 2
    player_y = ALTURA - player_tam - 10

    enemy_x = random.randint(0, LARGURA - enemy_tam)
    enemy_y = -enemy_tam
    
    pontos = 0

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and player_x > 0:
            player_x -= player_vel
        if teclas[pygame.K_RIGHT] and player_x < LARGURA - player_tam:
            player_x += player_vel
        

        enemy_y += enemy_vel
        if enemy_y > ALTURA:
            enemy_y = -enemy_tam
            enemy_x = random.randint(0, LARGURA - enemy_tam)
            pontos += 1

        if (player_x < enemy_x + enemy_tam and
            player_x + player_tam > enemy_x and
            player_y < enemy_y + enemy_tam and
            player_y + player_tam > enemy_y):
            game_over_screen(pontos)
            return
        
        desenhar_tela(player_x, player_y , enemy_x , enemy_y, pontos)
        clock.tick(30)

while True:
    jogo()