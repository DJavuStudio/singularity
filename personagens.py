import pygame

class Personagem:
 def __init__(self, nome, vida, mana):
 self.nome = nome
 self.vida = vida
 self.mana = mana
 self.nivel = 1
 self.experiencia = 0
 self.habilidades = []
 self.equipamentos = []
 self.status = "vivo"

 def desenhar(self, tela):
 # Desenhar o personagem na tela
 pygame.draw.rect(tela, (255, 0, 0), (100, 100, 50, 50))

 def atualizar(self):
 # Atualizar as habilidades e equipamentos do personagem
 pass

 def adicionar_habilidade(self, habilidade):
 self.habilidades.append(habilidade)

 def adicionar_equipamento(self, equipamento):
 self.equipamentos.append(equipamento)

 def remover_habilidade(self, habilidade):
 self.habilidades.remove(habilidade)

 def remover_equipamento(self, equipamento):
 self.equipamentos.remove(equipamento)

 def ganhar_experiencia(self, experiencia):
 self.experiencia += experiencia
 if self.experiencia >= 100:
 self.nivel += 1
 self.experiencia = 0

 def perder_vida(self, vida):
 self.vida -= vida
 if self.vida <= 0:
 self.status = "morto"

 def curar(self, vida):
 self.vida += vida
 if self.vida > 100:
 self.vida = 100

 def __str__(self):
 return f"Personagem: {self.nome}, Vida: {self.vida}, Mana: {self.mana}, Nível: {self.nivel}, Experiência: {self.experiencia}, Status: {self.status}"