# coding: utf-8

import time
import pygame

BULLET_PIXEL_MOVE = 3 # Pixels por loop que a bala irá se mover
GUN_RELOAD_TIME = 0.4 # Tempo para carregar a arma em segundos


class Bullet(object):
    """ 
        Bullet é responsável por criar uma imagem para a bala
        e move-la na tela.
    """
    def __init__(self, bullet_name, position):
        self.img = pygame.image.load('resources/%s.png' % bullet_name)
        self.rect = self.img.get_rect()
        self.position = self.set_position(position) 

    def set_position(self, position):
        """ 
            Definir posição da bala, desconsiderando metade do seu tamanho 
            para que ela seja centralizada no meio da nave
        """
        position_x, position_y = position
        position_x -= self.rect.width/2

        return [position_x, position_y]

    def move(self):
        """ 
            Função para mover a bala, originalmente diminuindo o valor do Y a
            bala sobe. 
            Deve permitir a escolha a direção da bala, para que possa ser usada
            tanto para spacecrafts quanto para seus inimigos.
        """
        self.position[1] -= BULLET_PIXEL_MOVE

    @property
    def displayed(self):
        """ 
            Define se a bala está em area que possibilita a visualização.
        """
        return self.position[1] > 0


class Gun(object):
    """
        Gun é responsável por realizar os disparos e
        verificar se acertou algum objeto e mostrar os 
        disparos na tela
    """
    def __init__(self, spacecraft, bullet_name='bullet_01'):
        """
            Para inicializar uma arma, é necessário informar
            em qual spacecraft ela está acoplada, assim
            como qual será seu tipo de disparo padrão.
        """
        self.spacecraft = spacecraft
        self.bullet_name = bullet_name        
        self._bullets = []
        self._last_shot = time.time()

    @property
    def ready(self):
        """ 
            Verifica se o tempo do ultimo disparo é
            maior que o tempo de carregamento da arma
        """
        last_shot = time.time() - self._last_shot
        return last_shot > GUN_RELOAD_TIME:

    def bullets(self, bullet=None):
        """ Função para registrar um disparo """
        if bullet is not None:
            self._bullets.append(bullet)
            self._last_shot = time.time()
        else:
            return self._bullets

    def shot(self):
        """ 
            Para disparar um tiro é necessário verificar se arma está em condições
        """
        bullet = Bullet(self.bullet_name, self.spacecraft.middle_position)
        if self.ready:
            self.bullets(bullet)

    def clear_gun(self):
        """ 
            Deixar somente os disparos que estão sendo mostrados
        """
        self._bullets = filter(lambda bullet: bullet.displayed, self._bullets)

    def draw(self, display):
        """ 
            Desenhar os disparos realizados e limpar os que já ultrapassaram
            os limites de visualização
        """
        for bullet in self.bullets():
            bullet.move()
            display.blit(bullet.img, bullet.position)

        self.clear_gun()
