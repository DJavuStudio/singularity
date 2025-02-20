import pygame
import pydub

class Audio:
 def __init__(self, nome, arquivo):
 self.nome = nome
 self.arquivo = arquivo
 self.som = pygame.mixer.Sound(arquivo)

 def tocar(self):
 self.som.play()

 def parar(self):
 self.som.stop()

 def pausar(self):
 self.som.pause()

 def despausar(self):
 self.som.unpause()

 def definir_volume(self, volume):
 self.som.set_volume(volume)

 def obter_volume(self):
 return self.som.get_volume()

 def carregar_musica(self, arquivo):
 self.som = pygame.mixer.Sound(arquivo)

 def criar_efeito_sonoro(self, arquivo):
 self.som = pygame.mixer.Sound(arquivo)

 def criar_musica_de_fundo(self, arquivo):
 self.som = pygame.mixer.Sound(arquivo)

 def criar_som_de_alerta(self, arquivo):
 self.som = pygame.mixer.Sound(arquivo)