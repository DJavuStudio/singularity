# singularity
Singularity, um jogo de aventura e estratégia em um mundo futurista onde a tecnologia e a inteligência artificial têm criado uma realidade complexa e desafiadora.

Se você está pronto para um desafio emocionante e uma aventura futurista, então é hora de entrar em nossa comunidade do Singularity e começar a ajudar a desenvolver esse projeto que tem no fundo um objetivo muito ambicioso: A evolução da humanidade até a singularidade!

Neste jogo, você assume o papel de um personagem que deve navegar por um mundo cheio de perigos e desafios, enquanto tenta descobrir os segredos por trás da criação da inteligência artificial que governa o mundo.

Características:

- Exploração de um mundo futurista com ambientes variados e desafiadores
- Luta contra inimigos poderosos e inteligentes, utilizando uma variedade de armas e habilidades
- Desbloqueio de novas habilidades e melhorias para o personagem, permitindo que você se adapte às mudanças no mundo
- Uma história rica e complexa, com múltiplos finais dependendo das escolhas que você fizer
- Um sistema de inteligência artificial avançado, que permitirá que os inimigos se adaptem às suas táticas e estratégias

Tecnologias Utilizadas:

- Python 3.x
- Pygame
- MoviePy

****************
[personagens.py]
Esse código é uma base para o gerenciamento de personagens no jogo e pode ser expandido e personalizado de acordo com as necessidades do jogo.
Esse código define uma classe Personagem com os seguintes atributos e métodos:

- Atributos:
- nome: o nome do personagem
- vida: a vida do personagem
- mana: a mana do personagem
- nivel: o nível do personagem
- experiencia: a experiência do personagem
- habilidades: as habilidades do personagem
- equipamentos: os equipamentos do personagem
- status: o status do personagem (vivo ou morto)
- Métodos:
- __init__: o construtor da classe
- desenhar: desenha o personagem na tela
- atualizar: atualiza as habilidades e equipamentos do personagem
- adicionar_habilidade: adiciona uma habilidade ao personagem
- adicionar_equipamento: adiciona um equipamento ao personagem
- remover_habilidade: remove uma habilidade do personagem
- remover_equipamento: remove um equipamento do personagem
- ganhar_experiencia: adiciona experiência ao personagem
- perder_vida: reduz a vida do personagem
- curar: aumenta a vida do personagem
- __str__: retorna uma string que descreve o personagem

**********
[mapas.py]
Esse código é uma base para o gerenciamento de mapas no jogo e pode ser expandido e personalizado de acordo com as necessidades do jogo.
Esse código define duas classes: Mapa e Tile.

A classe Mapa representa um mapa no jogo e tem os seguintes atributos e métodos:

- Atributos:
- nome: o nome do mapa
- largura: a largura do mapa
- altura: a altura do mapa
- tiles: uma lista de tiles que compõem o mapa
- objetos: uma lista de objetos que estão no mapa
- inimigos: uma lista de inimigos que estão no mapa
- Métodos:
- __init__: o construtor da classe
- criar_tiles: cria os tiles que compõem o mapa
- desenhar: desenha o mapa na tela
- adicionar_objeto: adiciona um objeto ao mapa
- adicionar_inimigo: adiciona um inimigo ao mapa
- remover_objeto: remove um objeto do mapa
- remover_inimigo: remove um inimigo do mapa

A classe Tile representa um tile no mapa e tem os seguintes atributos e métodos:

- Atributos:
- x: a coordenada x do tile
- y: a coordenada y do tile
- tipo: o tipo do tile (grama, pedra, água)
- Métodos:
- __init__: o construtor da classe
- desenhar: desenha o tile na tela

*************
[texturas.py]
Esse código é uma base para o gerenciamento de texturas no jogo e pode ser expandido e personalizado de acordo com as necessidades do jogo.
Esse código define uma classe Textura que representa uma textura no jogo.
A classe tem os seguintes atributos e métodos:

- Atributos:
- nome: o nome da textura
- largura: a largura da textura
- altura: a altura da textura
- imagem: a imagem da textura
- Métodos:
- __init__: o construtor da classe
- carregar_imagem: carrega uma imagem para a textura
- desenhar: desenha a textura na tela
- criar_textura_solid: cria uma textura sólida com uma cor específica
- criar_textura_gradiente: cria uma textura gradiente com duas cores específicas
- criar_textura_padrão: cria uma textura com um padrão específico (x ou y)

*******
[fx.py]
Esse código é uma base para o gerenciamento de efeitos visuais no jogo e pode ser expandido e personalizado de acordo com as necessidades do jogo.
Esse código define uma classe EfeitoVisual que representa um efeito visual no jogo. A classe tem os seguintes atributos e métodos:

- Atributos:
- nome: o nome do efeito visual
- x: a coordenada x do efeito visual
- y: a coordenada y do efeito visual
- duração: a duração do efeito visual
- tipo: o tipo do efeito visual (explosão, fumaça, partículas)
- Métodos:
- __init__: o construtor da classe
- desenhar: desenha o efeito visual na tela
- atualizar: atualiza o efeito visual
- criar_explosão: cria um efeito visual de explosão
- criar_fumaça: cria um efeito visual de fumaça
- criar_partículas: cria um efeito visual de partículas

***********
[audios.py]
Esse código é uma base para o gerenciamento de áudio no jogo e pode ser expandido e personalizado de acordo com as necessidades do jogo.
Lembre-se de que é necessário instalar a biblioteca pydub para utilizar essa classe. Você pode instalar utilizando o comando pip install pydub.

Esse código define uma classe Audio que representa um áudio no jogo.
A classe tem os seguintes atributos e métodos:

- Atributos:
- nome: o nome do áudio
- arquivo: o arquivo do áudio
- som: o som do áudio
- Métodos:
- __init__: o construtor da classe
- tocar: toca o áudio
- parar: para o áudio
- pausar: pausa o áudio
- despausar: despausa o áudio
- definir_volume: define o volume do áudio
- obter_volume: obtém o volume do áudio
- carregar_musica: carrega uma música
- criar_efeito_sonoro: cria um efeito sonoro
- criar_musica_de_fundo: cria uma música de fundo
- criar_som_de_alerta: cria um som de alerta

***********
[videos.py]
Esse código é uma base para o gerenciamento de vídeos no jogo e pode ser expandido e personalizado de acordo com as necessidades do jogo.
Lembre-se de que é necessário instalar a biblioteca moviepy para utilizar essa classe. Você pode instalar utilizando o comando pip install moviepy.

Esse código define uma classe Video que representa um vídeo no jogo.
A classe tem os seguintes atributos e métodos:

- Atributos:
- nome: o nome do vídeo
- arquivo: o arquivo do vídeo
- video: o vídeo em si
- Métodos:
- __init__: o construtor da classe
- reproduzir: reproduz o vídeo
- pausar: pausa o vídeo
- despausar: despausa o vídeo
- definir_volume: define o volume do vídeo
- obter_volume: obtém o volume do vídeo
- carregar_video: carrega um vídeo
- criar_video_de_introducao: cria um vídeo de introdução
- criar_video_de_fim: cria um vídeo de fim
- criar_video_de_cena: cria um vídeo de cena

************
[missoes.py]
Esse código é uma base para o gerenciamento de missões no jogo e pode ser expandido e personalizado de acordo com as necessidades do jogo.
Esse código define uma classe Missao que representa uma missão no jogo.
A classe tem os seguintes atributos e métodos:

- Atributos:
- nome: o nome da missão
- descricao: a descrição da missão
- objetivo: o objetivo da missão
- recompensa: a recompensa da missão
- status: o status da missão (não iniciada, em andamento, concluída, falhada)
- Métodos:
- __init__: o construtor da classe
- iniciar: inicia a missão
- concluir: conclui a missão
- falhar: falha a missão
- atualizar: atualiza o status da missão
- obter_recompensa: entrega a recompensa ao jogador
- criar_missao_principal: cria uma missão principal
- criar_missao_secundaria: cria uma missão secundária
- criar_missao_boss: cria uma missão boss

*************
[evolucao.py]
Esse código é uma base para o gerenciamento de evolução no jogo e pode ser expandido e personalizado de acordo com as necessidades do jogo.
Esse código define uma classe Evolucao que representa a evolução de um personagem ou monstro no jogo.
A classe tem os seguintes atributos e métodos:

- Atributos:
- nome: o nome do personagem ou monstro
- nivel: o nível do personagem ou monstro
- experiencia: a experiência do personagem ou monstro
- pontos_de_habilidade: os pontos de habilidade do personagem ou monstro
- habilidades: as habilidades do personagem ou monstro
- Métodos:
- __init__: o construtor da classe
- atualizar: atualiza o nível e a experiência do personagem ou monstro
- adicionar_habilidade: adiciona uma habilidade ao personagem ou monstro
- remover_habilidade: remove uma habilidade do personagem ou monstro
- definir_pontos_de_habilidade: define os pontos de habilidade do personagem ou monstro
- obter_pontos_de_habilidade: obtém os pontos de habilidade do personagem ou monstro
- criar_evolucao: cria uma evolução para um personagem ou monstro
- criar_evolucao_personagem: cria uma evolução para um personagem
- criar_evolucao_monstro: cria uma evolução para um monstro

***************
[utilidades.py]
Essas funções podem ser usadas para gerenciar o estado do jogo, criar e apagar arquivos e diretórios, e realizar outras tarefas utilitárias.
Esse código define várias funções utilitárias para o jogo, incluindo:

- salvar_jogo: salva o estado do jogo em um arquivo JSON
- carregar_jogo: carrega o estado do jogo de um arquivo JSON
- criar_diretorio: cria um diretório com o nome especificado
- apagar_diretorio: apaga um diretório com o nome especificado
- criar_arquivo: cria um arquivo com o nome especificado
- apagar_arquivo: apaga um arquivo com o nome especificado
