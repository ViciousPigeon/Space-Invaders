import pygame

class Ship(pygame.sprite.Sprite):

    def __init__(self,
                 x_coord: int,
                 y_coord: int,
                 x_movement: int,
                 y_movement:int,
                 image: str,
                 fire_rate: int,
                 health: int
                 ):
        """
        Base class used for ship generation, both player and enemy.
        :param x_coord:
        :param y_coord:
        :param x_movement:
        :param y_movement:
        :param image:
        :param fire_rate:
        :param health:
        """

