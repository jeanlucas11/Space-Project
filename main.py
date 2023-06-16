import pygame
pygame.init()
tamanho = (800,600)
branco = (255,255,255)
tela =  pygame.display.set_mode( tamanho )
running = True
fonte = pygame.font.Font(None, 26)

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    texto1 = fonte.render("Pressione F10 para Salvar os Pontos: ",True, branco )
    texto2 = fonte.render("Pressione F11 para Carregar os Pontos: ",True, branco )
    texto3 = fonte.render("Pressione F12 para Deletar os Pontos: ",True, branco )
    tela.blit(texto1, (10,10))
    tela.blit(texto2, (10,30))
    tela.blit(texto2, (10,50))
    pygame.display.update()
pygame.quit()
