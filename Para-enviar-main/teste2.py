import pygame 

pygame.init()


janela = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Figura e texto")

# Definindo as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0 ,0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)



janela.fill(BRANCO)

fonte = pygame.font.Font(None, 48)
texto = fonte.render("Olá, Turma de Jogos!", True, VERMELHO, AZUL)
janela.blit(texto, [40, 150])

pygame.draw.line(janela, VERDE, (60, 260), (420, 260), 4)
pygame.draw.polygon(janela, PRETO, ((191, 206), (236, 277), (156, 277)), 0)
pygame.draw.circle(janela, AZUL, (300, 50), 20, 0)
pygame.draw.ellipse(janela, VERMELHO, (400, 250, 40, 80), 1)
pygame.draw.rect(janela, VERDE, (20, 20, 60, 40), 0)

pygame.display.update()

deve_continuar = True
while deve_continuar:
    # Checando eventos
    for event in pygame.event.get():
        # Se for um evento QUIT
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            deve_continuar = False

deve_continuar = True


            
        
# Encerrando módulos do Pygame
pygame.quit()
