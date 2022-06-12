import sys, pygame
from configuracoes import *
from Tiles import Tile


# Inicialização do jogo
pygame.init()
tela = pygame.display.set_mode((larguraTela, alturaTela))
clock = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill('black')

    pygame.display.update()
    clock.tick(60)