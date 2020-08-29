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

        :param x_coord: The x-coordinate of the ship
        :param y_coord: The y-coordinate of the ship
        :param x_movement: The x-movement direction/speed of the ship
        :param y_movement: The y-movement direction/speed of the ship
        :param image: The pygame.image.load(image) to load for the ship
        :param fire_rate: The fire rate of the ship, expressed in seconds
        :param health: The health of the ship
        """

