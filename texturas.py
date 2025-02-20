import pygame

class Textura:
 def __init__(self, nome, largura, altura):
 self.nome = nome
 self.largura = largura
 self.altura = altura
 self.imagem = pygame.Surface((largura, altura))

 def carregar_imagem(self, arquivo):
 self.imagem = pygame.image.load(arquivo)

 def desenhar(self, tela, x, y):
 tela.blit(self.imagem, (x, y))

 def criar_textura_solid(self, cor):
 self.imagem.fill(cor)

 def criar_textura_gradiente(self, cor1, cor2):
 for y in range(self.altura):
 for x in range(self.largura):
 cor = (cor1[0] + (cor2[0] - cor1[0]) * x / self.largura,
 cor1[1] + (cor2[1] - cor1[1]) * x / self.largura,
 cor1[2] + (cor2[2] - cor1[2]) * x / self.largura)
 self.imagem.set_at((x, y), cor)

 def criar_textura_padrão(self, padrão):
 for y in range(self.altura):
 for x in range(self.largura):
 if padrão == "x":
 cor = (255, 0, 0) if x % 2 == 0 else (0, 0, 255)
 elif padrão == "y":
 cor = (255, 0, 0) if y % 2 == 0 else (0, 0, 255)
 self.imagem.set_at((x, y), cor)