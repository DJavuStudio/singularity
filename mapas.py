import pygame
import random

class Mapa:
 def __init__(self, nome, largura, altura):
 self.nome = nome
 self.largura = largura
 self.altura = altura
 self.tiles = []
 self.objetos = []
 self.inimigos = []

 def criar_tiles(self):
 for x in range(self.largura):
 for y in range(self.altura):
 self.tiles.append(Tile(x, y))

 def desenhar(self, tela):
 for tile in self.tiles:
 tile.desenhar(tela)

 def adicionar_objeto(self, objeto):
 self.objetos.append(objeto)

 def adicionar_inimigo(self, inimigo):
 self.inimigos.append(inimigo)

 def remover_objeto(self, objeto):
 self.objetos.remove(objeto)

 def remover_inimigo(self, inimigo):
 self.inimigos.remove(inimigo)

 def __str__(self):
 return f"Mapa: {self.nome}, Largura: {self.largura}, Altura: {self.altura}"

class Tile:
 def __init__(self, x, y):
 self.x = x
 self.y = y
 self.tipo = random.choice(["grama", "pedra", "agua"])

 def desenhar(self, tela):
 if self.tipo == "grama":
 pygame.draw.rect(tela, (0, 255, 0), (self.x * 32, self.y * 32, 32, 32))
 elif self.tipo == "pedra":
 pygame.draw.rect(tela, (128, 128, 128), (self.x * 32, self.y * 32, 32, 32))
 elif self.tipo == "agua":
 pygame.draw.rect(tela, (0, 0, 255), (self.x * 32, self.y * 32, 32, 32))