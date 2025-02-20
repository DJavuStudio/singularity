import pygame
import moviepy.editor as mp

class Video:
 def __init__(self, nome, arquivo):
 self.nome = nome
 self.arquivo = arquivo
 self.video = mp.VideoFileClip(arquivo)

 def reproduzir(self):
 self.video.preview()

 def pausar(self):
 self.video.pause()

 def despausar(self):
 self.video.unpause()

 def definir_volume(self, volume):
 self.video.set_volume(volume)

 def obter_volume(self):
 return self.video.get_volume()

 def carregar_video(self, arquivo):
 self.video = mp.VideoFileClip(arquivo)

 def criar_video_de_introducao(self, arquivo):
 self.video = mp.VideoFileClip(arquivo)

 def criar_video_de_fim(self, arquivo):
 self.video = mp.VideoFileClip(arquivo)

 def criar_video_de_cena(self, arquivo):
 self.video = mp.VideoFileClip(arquivo)