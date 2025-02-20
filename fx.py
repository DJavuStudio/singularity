import pygame
import random

class EfeitoVisual:
 def __init__(self, nome, x, y):
 self.nome = nome
 self.x = x
 self.y = y
 self.duração = 0
 self.tipo = None

 def desenhar(self, tela):
 if self.tipo == "explosão":
 self.desenhar_explosão(tela)
 elif self.tipo == "fumaça":
 self.desenhar_fumaça(tela)
 elif self.tipo == "partículas":
 self.desenhar_partículas(tela)

 def desenhar_explosão(self, tela):
 pygame.draw.circle(tela, (255, 0, 0), (self.x, self.y), 20)

 def desenhar_fumaça(self, tela):
 pygame.draw.rect(tela, (128, 128, 128), (self.x, self.y, 10, 10))

 def desenhar_partículas(self, tela):
 for i in range(10):
 pygame.draw.rect(tela, (255, 255, 255), (self.x + random.randint(-5, 5), self.y + random.randint(-5, 5), 2, 2))

 def atualizar(self):
 self.duração -= 1
 if self.duração <= 0:
 self.tipo = None

 def criar_explosão(self, x, y):
 self.tipo = "explosão"
 self.x = x
 self.y = y
 self.duração = 10

 def criar_fumaça(self, x, y):
 self.tipo = "fumaça"
 self.x = x
 self.y = y
 self.duração = 20

 def criar_partículas(self, x, y):
 self.tipo = "partículas"
 self.x = x
 self.y = y
 self.duração = 30