# coding: utf-8

import pygame
from pygame.locals import *

from characters import SpaceCraft


class SpaceInvaders(object):
    def __init__(self):
        self._running = True
        self._display = None
        self.size = self.width, self.height = 1000, 600

    def load_itens(self):
        """ Carregar imagens, personagens e outros itens da tela """
        self.background = pygame.image.load('resources/space_background.jpg')
        self.spacecraft = SpaceCraft(size=self.size)

    def on_init(self):
        """ Inicializar os modulos do pygame como outros detalhes do game """
        # inicializar modulos
        pygame.init()

        self.load_itens()

        # definir o titulo
        pygame.display.set_caption('Space Invaders - Lucas Magnum')
        # setar o tamanho inicial da tela
        self._display = pygame.display.set_mode(self.size)

    def on_keys(self):
        """ Ações para as Keys pressionadas """
        keys = pygame.key.get_pressed()
        # chama as ações do spacecraft
        self.spacecraft.on_keys(keys)

    def on_event(self, event):
        """ Ações para o eventos realizados no jogo """
        # se o evento for um quit, fechar
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        """  Ações que devem ser disparadas a cada loop """
        # atualizar a pagina
        pygame.display.update()
        
    def on_render(self):
        """ Itens que devem ser renderizados """
        # desenhar background na tela
        self._display.blit(self.background, (0, 0))

        # desenhar spacecraft
        self.spacecraft.draw(self._display)

    def on_cleanup(self):
        # sair do programa
        pygame.quit()

    def on_execute(self):
        """ Responsável pela execução do Jogo """
        self.on_init()

        while(self._running):
            self.on_render()

            for event in pygame.event.get():
                self.on_event(event)
                self.spacecraft.on_event(event)

            self.on_keys()
            self.on_loop()

        self.on_cleanup()


if __name__ == '__main__':
    game = SpaceInvaders()
    game.on_execute()

