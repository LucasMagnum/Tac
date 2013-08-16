# coding: utf-8

import pygame


class SpaceCraft(object):
	def __init__(self, size):
		self.size = size
		self.img = pygame.image.load('resources/spacecraft_01.png')
		self.position = (100, 100)

	def draw(self):
		return self.img, self.position
