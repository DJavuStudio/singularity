import pygame

class Missao:
 def __init__(self, nome, descricao, objetivo, recompensa):
 self.nome = nome
 self.descricao = descricao
 self.objetivo = objetivo
 self.recompensa = recompensa
 self.status = "não iniciada"

 def iniciar(self):
 self.status = "em andamento"

 def concluir(self):
 self.status = "concluída"

 def falhar(self):
 self.status = "falhada"

 def atualizar(self):
 # Atualizar o status da missão com base nas ações do jogador
 pass

 def obter_recompensa(self):
 # Entregar a recompensa ao jogador quando a missão for concluída
 pass

 def criar_missao_principal(self, nome, descricao, objetivo, recompensa):
 return Missao(nome, descricao, objetivo, recompensa)

 def criar_missao_secundaria(self, nome, descricao, objetivo, recompensa):
 return Missao(nome, descricao, objetivo, recompensa)

 def criar_missao_boss(self, nome, descricao, objetivo, recompensa):
 return Missao(nome, descricao, objetivo, recompensa)