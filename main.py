import pygame
from tkinter import simpledialog

pygame.init()

estrelas = []
tamanho = (800,500)
branco = (255,255,255)
tela =  pygame.display.set_mode( tamanho )
running = True
fonte = pygame.font.Font(None, 26)
fundo = pygame.image.load("fundo.jpg")
pygame.mixer.music.load("audio.mp3")
pygame.mixer.music.play(-1)
pygame.display.set_caption("Space do Jean")
icon = pygame.image.load("icone.png")
pygame.display.set_icon(icon)
pos = pygame.mouse.get_pos()
nome_estrela = ""
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela:")
            if item == None:
                item = "desconhecido"+str(pos)
            if item is not None:
                nome_estrela = item
                print(item)

    tela.blit(fundo, (0,0))
    texto1 = fonte.render("Pressione F10 para Salvar os Pontos: ",True, branco )
    texto2 = fonte.render("Pressione F11 para Carregar os Pontos: ",True, branco )
    texto3 = fonte.render("Pressione F12 para Deletar os Pontos: ",True, branco )
    tela.blit(texto1, (10,10))
    tela.blit(texto2, (10,30))
    tela.blit(texto3, (10,50))
    texto_renderizado = fonte.render(nome_estrela, True, branco)
    tela.blit(texto_renderizado, (pos))
    
    


    pygame.display.update()
pygame.quit()
