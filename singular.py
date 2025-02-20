import pygame
import random
import sys

# Definições de constantes
TAMANHO_TELA = (800, 600)
COR_FUNDO = (255, 255, 255)
COR_TEXTO = (0, 0, 0)

# Definições de variáveis
personagem = {
 "nome": "Jogador",
 "atributos": {
 "força": 10,
 "destreza": 10,
 "inteligência": 10,
 "sabedoria": 10,
 "carisma": 10
 },
 "habilidades": {
 "combate corpo a corpo": 0,
 "tiro com arco": 0,
 "magia": 0,
 "roubo": 0,
 "persuasão": 0
 },
 "perks": [],
 "níveis": 1,
 "pontos": 0,
 "recursos": 100
}

armas = [
 {"nome": "Espada", "dano": 10, "precisão": 0.5, "velocidade de ataque": 1},
 {"nome": "Arco e flecha", "dano": 5, "precisão": 0.8, "velocidade de ataque": 2},
 {"nome": "Magia", "dano": 15, "precisão": 0.3, "velocidade de ataque": 1}
]

poções = [
 {"nome": "Poção de cura", "efeito": "cura"},
 {"nome": "Poção de força", "efeito": "força"},
 {"nome": "Poção de velocidade", "efeito": "velocidade"}
]

magia = [
 {"nome": "Fogo", "dano": 10, "precisão": 0.5, "velocidade de ataque": 1},
 {"nome": "Gelo", "dano": 5, "precisão": 0.8, "velocidade de ataque": 2},
 {"nome": "Raio", "dano": 15, "precisão": 0.3, "velocidade de ataque": 1}
]

# Inicialização do Pygame
pygame.init()
tela = pygame.display.set_mode(TAMANHO_TELA)
pygame.display.set_caption("Singularidade")

# Definição de fontes
fonte = pygame.font.SysFont("Arial", 24)

# Função para desenhar a tela
def desenhar_tela():
 tela.fill(COR_FUNDO)
 texto = fonte.render(f"Pontos: {personagem['pontos']}", True, COR_TEXTO)
 tela.blit(texto, (10, 10))
 texto = fonte.render(f"Nível: {personagem['níveis']}", True, COR_TEXTO)
 tela.blit(texto, (10, 40))
 texto = fonte.render(f"Recursos: {personagem['recursos']}", True, COR_TEXTO)
 tela.blit(texto, (10, 70))

# Função para atualizar o jogo
def atualizar_jogo():
 global personagem
 personagem['pontos'] += 1
 personagem['recursos'] -= 1
 if personagem['recursos'] <= 0:
 personagem['níveis'] += 1
 personagem['recursos'] = 100

# Função para lidar com a saída do jogo
def lidar_com_saida():
 pygame.quit()
 sys.exit()

# Loop principal do jogo
while True:
 desenhar_tela()
 atualizar_jogo()
 for evento in pygame.event.get():
 if evento.type == pygame.QUIT:
 lidar_com_saida()
 pygame.display.update()
 pygame.time.Clock().tick(60)