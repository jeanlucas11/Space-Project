import pygame
from tkinter import simpledialog
import json

pygame.init()


pontos = {}
textos = []
tamanho = (800,500)
branco = (255,255,255)
tela =  pygame.display.set_mode( tamanho )
running = True
fonte = pygame.font.Font(None, 26)
fonteEstrela = pygame.font.Font(None, 24)
fundo = pygame.image.load("./assets/fundo.png")
pygame.mixer.music.load("./assets/audio.mp3")
pygame.mixer.music.play(-1)
pygame.display.set_caption("Space do Jean")
icon = pygame.image.load("./assets/icone.png")
pygame.display.set_icon(icon)
pos = pygame.mouse.get_pos()
posicao = (0,0)
nome_estrela = None
contador = 0
contadorNomeEstrela = 0

def excluiPontos():
    pontos.clear()    

def salvarPontos():
    with open("pontos.json", "w") as file:
        json.dump(pontos, file)

def carregarPontos():
    global pontos
    try:
        with open("pontos.json", "r") as file:
            pontos = json.load(file)
    except:
        with open("pontos.json", "r") as file:
            json.dump(pontos, file)
    
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            salvarPontos()
            running = False
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            salvarPontos()
            running = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            nome_estrela = simpledialog.askstring("Space", "Nome da Estrela:")
            if nome_estrela == None:
                nome_estrela = "desconhecido"+str()
            if nome_estrela == "":
                nome_estrela = "desconhecido"
                if "desconhecido" in pontos:
                    contador = contador + 1
                    item = "desconhecido" + str(contador)
            elif nome_estrela in pontos:
                contadorNomeEstrela = contadorNomeEstrela + 1
                nome_estrela = nome_estrela + str(contadorNomeEstrela)
            pontos[nome_estrela] = pos
            print(contadorNomeEstrela)
            print(pontos)
            # if nome_estrela is not None:
            #     nome_estrela = nome_estrela
            #     teste = {
            #         'nome': item,
            #         'pos': pos
            #     }            
            #     textos.append(teste)    deixei comentado pois tem outro jeito, não sei se está totalmente certo, porque até uma parte deu certo!
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F10:
            salvarPontos()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F11: 
            carregarPontos()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F12:
            excluiPontos()
       
    tela.blit(fundo, (0,0))
    for chave in pontos:
        posicao = pontos[chave]
        pygame.draw.circle(tela,branco,(posicao),5)
        nomeEstrelaPrint = fonteEstrela.render(chave + str(posicao),True,branco)
        tela.blit(nomeEstrelaPrint,(posicao))

    chaves = list(pontos.keys())
    for i in range(len(chaves)-1):
         chaveAtual = chaves[i]
         proximaChave = chaves[i + 1]
         pontoAtual = pontos[chaveAtual]
         proximoPonto = pontos[proximaChave]
         pygame.draw.line(tela,branco,pontoAtual,proximoPonto)
         
    f10 = fonte.render("Pressione F10 para Salvar os Pontos: ",True, branco )
    f11 = fonte.render("Pressione F11 para Carregar os Pontos: ",True, branco )
    f12 = fonte.render("Pressione F12 para Deletar os Pontos: ",True, branco )
    tela.blit(f10, (10,10))
    tela.blit(f11, (10,30))
    tela.blit(f12, (10,50))
    # for t in textos:
    #     texto_renderizado = fonte.render(t['nome'], True, branco)
    #     tela.blit(texto_renderizado, (t['pos']))
    #     pygame.draw.circle(tela, branco, t['pos'], (5))
    #     pygame.draw.line(tela, branco, t["pos"], pos, 1 ) deixei comentado pois tem outro jeito, não sei se está totalmente certo, porque até uma parte deu certo!

    pygame.display.update()
pygame.quit()
