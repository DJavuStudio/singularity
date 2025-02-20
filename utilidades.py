import pygame
import json
import os

def salvar_jogo(personagem, mapa, missao, evolucao):
 dados = {
 "personagem": {
 "nome": personagem.nome,
 "nivel": personagem.nivel,
 "experiencia": personagem.experiencia,
 "habilidades": personagem.habilidades
 },
 "mapa": {
 "nome": mapa.nome,
 "largura": mapa.largura,
 "altura": mapa.altura
 },
 "missao": {
 "nome": missao.nome,
 "descricao": missao.descricao,
 "objetivo": missao.objetivo,
 "recompensa": missao.recompensa
 },
 "evolucao": {
 "nome": evolucao.nome,
 "nivel": evolucao.nivel,
 "experiencia": evolucao.experiencia,
 "habilidades": evolucao.habilidades
 }
 }
 with open("savegame.json", "w") as arquivo:
 json.dump(dados, arquivo)

def carregar_jogo():
 try:
 with open("savegame.json", "r") as arquivo:
 dados = json.load(arquivo)
 personagem = Personagem(dados["personagem"]["nome"], dados["personagem"]["nivel"], dados["personagem"]["experiencia"])
 mapa = Mapa(dados["mapa"]["nome"], dados["mapa"]["largura"], dados["mapa"]["altura"])
 missao = Missao(dados["missao"]["nome"], dados["missao"]["descricao"], dados["missao"]["objetivo"], dados["missao"]["recompensa"])
 evolucao = Evolucao(dados["evolucao"]["nome"], dados["evolucao"]["nivel"], dados["evolucao"]["experiencia"])
 return personagem, mapa, missao, evolucao
 except FileNotFoundError:
 return None

def criar_diretorio(nome):
 try:
 os.mkdir(nome)
 except FileExistsError:
 pass

def apagar_diretorio(nome):
 try:
 os.rmdir(nome)
 except FileNotFoundError:
 pass

def criar_arquivo(nome):
 try:
 open(nome, "w").close()
 except FileExistsError:
 pass

def apagar_arquivo(nome):
 try:
 os.remove(nome)
 except FileNotFoundError:
 pass