#Jogo de encostar do quadrado#

import pygame
import random
import sys

pygame.init()

LARGURA = 550
ALTURA = 500
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Toque no Quadrado!")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (200, 0, 0)
AZUL = (0, 0, 200)
ROSA = (225, 0, 127)

player_tam = 50
player_vel = 10

enemy_tam = 50
enemy_vel = 10


fonte = pygame.font.SysFont("Arial", 30)
clock = pygame.time.Clock()

def desenhar_tela(player_x, player_y, enemy_x, enemy_y, pontos):
    tela.fill(PRETO)
    pygame.draw.rect(tela, AZUL, (player_x, player_y, player_tam, player_tam))
    pygame.draw.rect(tela, VERMELHO, (enemy_x, enemy_y, enemy_tam, enemy_tam))
    texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto, (10, 10))
    pygame.display.update()

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
        if teclas[pygame.K_UP] and player_y > 0:
            player_y -= player_vel
        if teclas[pygame.K_DOWN] and player_y < ALTURA - player_tam:
            player_y += player_vel

        if teclas[pygame.K_ESCAPE]:
            pygame.quit()

        enemy_y += enemy_vel
        if enemy_y > ALTURA:
            enemy_y = -enemy_tam
            enemy_x = random.randint(0, LARGURA - enemy_tam)

        # Colisão com o inimigo => ganhar pontos e reposicionar o inimigo
        if (player_x < enemy_x + enemy_tam and
            player_x + player_tam > enemy_x and
            player_y < enemy_y + enemy_tam and
            player_y + player_tam > enemy_y):
            pontos += 1
            enemy_x = random.randint(0, LARGURA - enemy_tam)
            enemy_y = -enemy_tam

        desenhar_tela(player_x, player_y, enemy_x, enemy_y, pontos)
        clock.tick(60)
        


while True:
    jogo()
