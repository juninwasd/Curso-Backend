#Jogo de desviar do quadrado#
import pygame
import random
import sys

pygame.init ()

LARGURA = 550
ALTURA = 500
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Desvie do Quadrado!")

BRANCO = (255,255,255)
PRETO = (0,0,0)
VERMELHO = (200,0,0)
AZUL = (0,0,200)
ROSA = (225,0,127)

player_tam = 50
player_vel = 10

enemy_tam = 50
enemy_vel = 10

fonte = pygame.font.SysFont("Arial", 30)
fonte_gameover = pygame.font.SysFont("Arial", 50, bold=True)

clock = pygame.time.Clock()

def desenhar_tela(player_x, player_y, enemy_x, enemy_y, pontos):
    tela.fill(PRETO)
    pygame.draw.rect(tela, AZUL, (player_x, player_y, player_tam, player_tam))
    pygame.draw.rect(tela, ROSA, (enemy_x, enemy_y, enemy_tam, enemy_tam))
    texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto, (10,10))
    pygame.display.update()

def game_over_screen(pontos):
    tela.fill(PRETO)
    texto1 = fonte_gameover.render("GAME OVER", True, VERMELHO)
    texto2 = fonte.render(f"Sua pontuação: {pontos}", True, BRANCO)
    texto3 = fonte.render("pressione R para reiniciar ou ESC para sair", True, BRANCO)
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
        if teclas[pygame.K_UP] and player_y < ALTURA + player_tam:
            player_y -= player_vel
        if teclas[pygame.K_DOWN] and player_y < ALTURA - player_tam:
            player_y += player_vel
       
        if teclas[pygame.K_ESCAPE]:
            pygame.quit()

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
        clock.tick(60)

while True:
    jogo()