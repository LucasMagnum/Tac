# coding: utf-8

import pygame

from collections import namedtuple


class SpaceCraft(object):
    def __init__(self, size):
        self.width, self.height = size
        self.spacecraft_name = 'spacecraft_01'
        self.img = self.spacecraft_name
        self.position = self.set_initial_position()
        self.turbe_active = False

    def set_position(self, x=0, y=0):
        """ 
            Definir a nova posição da nave 
            Para mover para direita, aumente no X
            Para mover para esquerda, diminua no X
            Para mover para cima, aumente o Y
            Para mover para baixo, diminua o Y
        """
        # verifica o turbo mode
        self.turbe_mode()

        new_position_x = self.position[0] + x
        new_position_y = self.position[1] + y

        # tamanhos do display, desconsiderando o tamanho da nave
        display_width = self.width - self.img_rect.width
        display_height = self.height - self.img_rect.height

        if new_position_x > 0 and new_position_x < display_width:
            self.position[0] = new_position_x
            # desliga o modo turbo
            self.turbe_active = False

        if new_position_y > 0 and new_position_y < display_height:
            self.position[1] = new_position_y


    def set_initial_position(self):
        """ Retornar as posições iniciais da nave
            Exatamente no meio da tela
        """
        self.load_img()
        # para centralizar, dividir a tela em 2 metades
        # e subtrair da metade da nave, assim fica exatamente no meio.
        position_x = (self.width/2) - (self.img_rect.width/2)
        position_y = self.height - self.img_rect.height
        return [position_x, position_y]


    def turbe_mode(self):
        """ Ligar a turbina da nave """
        self.img = '%s_active' % self.spacecraft_name if self.turbe_active else self.spacecraft_name

    def load_img(self):
        """ Carregar imagem da nave """
        self.img_load = pygame.image.load('resources/%s.png' % self.img)
        self.img_rect = self.img_load.get_rect()

    def draw(self):
        """ Retornar imagem e posição para ser desenhada """
        self.load_img()
        return self.img_load, self.position
