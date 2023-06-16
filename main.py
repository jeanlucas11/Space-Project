import pygame

pygame.init()

tamanho = (800,500)
branco = (255,255,255)
tela =  pygame.display.set_mode( tamanho )
running = True
fonte = pygame.font.Font(None, 26)
fundo = pygame.image.load("fundo.jpg")
pygame.mixer.music.load("audio.mp3")
pygame.mixer.music.play(-1)
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
    tela.blit(fundo, (0,0))
    texto1 = fonte.render("Pressione F10 para Salvar os Pontos: ",True, branco )
    texto2 = fonte.render("Pressione F11 para Carregar os Pontos: ",True, branco )
    texto3 = fonte.render("Pressione F12 para Deletar os Pontos: ",True, branco )
    tela.blit(texto1, (10,10))
    tela.blit(texto2, (10,30))
    tela.blit(texto2, (10,50))

    pygame.display.update()
pygame.quit()
