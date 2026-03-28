


"""

#1° EXERCICIO

import pygame
    #Inicializando módulos do Python

#Inicializando módulos do Python
pygame.init()

# Criando uma janela com o título "Olá, Turma de Jogos!"
janela =  pygame.display.set_mode((800,400))
pygame.display.set_caption("Olá, Você com certeza é uma pessoa!")

deve_continuar = True

#Loop do jogo
while deve_continuar:
    # Checando eventos
    for event in pygame.event.get():
        # Se for um evento QUIT
        #if event.type == pygame.QUIT or event.type == pygame.KEYDOWN or event.type == pygame.K_ESCAPE:
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                deve_continuar = False
            #abaizo
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("ação ocorreu")
            
            
aparecer_mensagem = pygame.display.set_caption("Olá, Você com certeza não é uma pessoa")


# Encerrando módulos do Pygame
pygame.quit()


"""

""" PRIMEIRA VERSÃO DO TRECO

import pygame
    #Inicializando módulos do Python

#Inicializando módulos do Python
pygame.init()

# Criando uma janela com o título "Olá, Turma de Jogos!"
janela =  pygame.display.set_mode((400,300))
pygame.display.set_caption("Olá, turma de Jogos ELetrônico!")

deve_continuar = True

#Loop do jogo
while deve_continuar:
    # Checando eventos
    for event in pygame.event.get():
        # Se for um evento QUIT
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            deve_continuar = False
            
        
# Encerrando módulos do Pygame
pygame.quit()

"""

"""
#Loop do jogo
while deve continuar:
    #Checando eventos
    for event in pygame.event.get():
    # Se for um evento QUIT
    if event.type == pygame.QUIT:
        deve_continuar - False

# Encerrando módulos do Pygame
pygame.quit()

if event.type == pygame.KEYDOWN:
            event.key == pygame.K_w:
"""
