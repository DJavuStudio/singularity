import pygame

class Evolucao:
 def __init__(self, nome, nivel, experiencia):
 self.nome = nome
 self.nivel = nivel
 self.experiencia = experiencia
 self.pontos_de_habilidade = 0
 self.habilidades = []

 def atualizar(self):
 # Atualizar o nível e a experiência do personagem
 if self.experiencia >= 100:
 self.nivel += 1
 self.experiencia = 0

 def adicionar_habilidade(self, habilidade):
 self.habilidades.append(habilidade)
 self.pontos_de_habilidade += 1

 def remover_habilidade(self, habilidade):
 self.habilidades.remove(habilidade)
 self.pontos_de_habilidade -= 1

 def definir_pontos_de_habilidade(self, pontos):
 self.pontos_de_habilidade = pontos

 def obter_pontos_de_habilidade(self):
 return self.pontos_de_habilidade

 def criar_evolucao(self, nome, nivel, experiencia):
 return Evolucao(nome, nivel, experiencia)

 def criar_evolucao_personagem(self, personagem):
 return Evolucao(personagem.nome, personagem.nivel, personagem.experiencia)

 def criar_evolucao_monstro(self, monstro):
 return Evolucao(monstro.nome, monstro.nivel, monstro.experiencia)