# coding: utf-8

import random

import pygame
from pygame.locals import *

from collections import namedtuple
from itertools import count

# quantidade de pixels que os desenhos deverao movimentar
PIXEL_PER_LOOP = 3


class SpaceCraft(object):
    def __init__(self, size, name='spacecraft_02'):
        self.width, self.height = size
        self.spacecraft_name = name
        self.img = self.spacecraft_name
        self.position = self.set_initial_position()
        self.turbe_active = False

    def on_keys(self, keys):
        if keys[K_RIGHT]:
            self.set_position(x=PIXEL_PER_LOOP)
        if keys[K_LEFT]:
            self.set_position(x=-PIXEL_PER_LOOP)
        if keys[K_DOWN]:
            self.set_position(y=PIXEL_PER_LOOP)
        if keys[K_UP]:
            # Ligar as turbinas da nave
            self.turbe_active = True
            self.set_position(y=-PIXEL_PER_LOOP)
        self.turbe_mode()

    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                pass # shot here

    def set_position(self, x=0, y=0):
        """ 
            Definir a nova posição da nave 
            Para mover para direita, aumente no X
            Para mover para esquerda, diminua no X
            Para mover para cima, aumente o Y
            Para mover para baixo, diminua o Y
        """
        new_position_x = self.position[0] + x
        new_position_y = self.position[1] + y

        # tamanhos do display, desconsiderando o tamanho da nave
        display_width = self.width - self.img_rect.width
        display_height = self.height - self.img_rect.height

        if new_position_x > 0 and new_position_x < display_width:
            self.position[0] = new_position_x

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
        self.turbe_active = False

    def load_img(self):
        """ Carregar imagem da nave """
        self.img_load = pygame.image.load('resources/%s.png' % self.img)
        self.img_rect = self.img_load.get_rect()

    def draw(self, display):
        """ Desenha a nave no display na sua posição """
        self.load_img()
        display.blit(self.img_load, self.position)

