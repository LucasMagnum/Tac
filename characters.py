# coding: utf-8

import pygame

from collections import namedtuple


class SpaceCraft(object):
	def __init__(self, size):
		self.width, self.height = size
		self.spacecraft_name = 'spacecraft_01'
		self.img = self.spacecraft_name
		self.position = [100, 100]
		import ipdb; ipdb.set_trace()

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

		if new_position_x > 0 and new_position_x < self.width:
			self.position[0] = new_position_x

		if new_position_y > 0:
			self.position[1] = new_position_y

		if y < 0:
			self.turbe_mode(active=True)
		else:
			self.turbe_mode(active=False)

	def turbe_mode(self, active=False):
		""" Ligar a turbina da nave """
		self.img = '%s_active' % self.spacecraft_name if active else self.spacecraft_name

	def load_img(self):
		""" Carregar imagem da nave """
		self.img_load = pygame.image.load('resources/%s.png' % self.img)

	def draw(self):
		""" Retornar imagem e posição para ser desenhada """
		self.load_img()
		return self.img_load, self.position
