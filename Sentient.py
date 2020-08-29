import pygame


class Sentient(pygame.sprite.Sprite):

    def __init__(self,
                 name: str,
                 x_coord: int,
                 y_coord: int,
                 fire_rate: float,
                 health: int,
                 image: str,
                 movement_area_x: tuple,
                 movement_area_y: tuple,
                 x_movement_velocity: float = 0,
                 y_movement_velocity: float = 0
                 ):

        """
        Define a "sentient" object, player or enemy.
        :param name: "player", "enemy" (or in future, enemy type)
        :param x_coord: the coordinates to first place the sentient at
        :param y_coord: " "
        :param fire_rate the rate at which the sentient can fire projectiles
        :param health: health of the sentient
        :param image: image to load for the sentient
        :param movement_area_x: The bounding x area for movement
        :param movement_area_y: The bounding y area for movement
        :param x_movement_velocity: movement speed in the x direction
        :param y_movement_velocity: movement speed in the y direction
        """

        super().__init__()
        self.name = name
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.fire_rate = fire_rate
        self.health = health
        self.image = pygame.image.load(image).convert()
        self.x_movement_velocity = x_movement_velocity
        self.y_movement_velocity = y_movement_velocity
        self.movement_area_x = movement_area_x
        self.movement_area_y = movement_area_y

        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()

        self.rect = self.image.get_rect(x=self.x_coord, y=self.y_coord)

    def change_velocity(self, x_change=0, y_change=0):

        self.x_movement_velocity *= x_change
        self.y_movement_velocity *= y_change

    def modify_health(self, modifier=0):

        self.health += modifier

    def modify_fire_rate(self, modifier=0):

        self.fire_rate *= modifier

    def update(self, screen: pygame.display):

        # This will be deprecated pending new methods for movement
        # self.rect.x += self.x_movement
        # self.rect.y += self.y_movement

        screen.blit(self.image, self.rect)

    def move(self):

        self.rect.x += self.x_movement_velocity
        self.rect.y += self.y_movement_velocity

        if self.rect.x < self.movement_area_x[0] or self.rect.x > self.movement_area_x[1] - self.image_width:
            self.x_movement_velocity *= -1
            self.y_coord += 10
        # Commenting this out; adding in a change in to the x if statement: if the x hits the boundary, all
        # enemies need to drop by a certain amount
        # if self.rect.y < self.movement_area_y[0] or self.rect.y > self.movement_area_y[1] - self.image_height:
        #     self.y_movement_velocity *= -1

    def move_left(self):
        """
        Move the object left. Bound the object within the screen dimensions. If
        the object is named player, it is simply not allowed to leave the screen.
        If the object is an enemy, hitting the edge of the screen causes its
        velocity vector to reverse.
        """
        self.rect.x -= self.x_movement_velocity


        if self.name == "player":
            if self.rect.x < self.movement_area_x[0]:
                self.rect.x = self.movement_area_x[0]
            if self.rect.x > self.movement_area_x[1]:
                self.rect.x = self.movement_area_x[1]

        if self.name == "enemy":
            if self.rect.x < self.movement_area_x[0] or self.rect.x > self.movement_area_x[1]:
                self.x_movement_velocity *= -1


    def move_right(self):
        """
        Move the object right. Bound the object within the screen dimensions. If
        the object is named player, it is simply not allowed to leave the screen.
        If the object is an enemy, hitting the edge of the screen causes its
        velocity vector to reverse.
        """
        self.rect.x += self.x_movement_velocity

        if self.name == "player":
            if self.rect.x < self.movement_area_x[0]:
                self.rect.x = self.movement_area_x[0]
            if self.rect.x > (self.movement_area_x[1] - self.image_width):
                self.rect.x = (self.movement_area_x[1] - self.image_width)

        if self.name == "enemy":
            if self.rect.x < self.movement_area_x[0] or self.rect.x > (self.movement_area_x[1] - self.image_width):
                self.x_movement_velocity *= -1


    def move_up(self):
        """
        Move the object up. Bound the object within the screen dimensions. If
        the object is named player, it is simply not allowed to leave the screen.
        If the object is an enemy, hitting the edge of the screen causes its
        velocity vector to reverse.
        """
        self.rect.y -= self.y_movement_velocity

        if self.name == "player":
            if self.rect.y < self.movement_area_y[0]:
                self.rect.y = self.movement_area_y[0]
            if self.rect.y > self.movement_area_y[1]:
                self.rect.y = self.movement_area_y[1]

        if self.name == "enemy":
            if self.rect.y < self.movement_area_y[0] or self.rect.y > self.movement_area_y[1]:
                self.y_movement_velocity *= -1

    def move_down(self):
        """
        Move the object up. Bound the object within the screen dimensions. If
        the object is named player, it is simply not allowed to leave the screen.
        If the object is an enemy, hitting the edge of the screen causes its
        velocity vector to reverse.
        """
        self.rect.y += self.y_movement_velocity

        if self.name == "player":
            if self.rect.y < self.movement_area_y[0]:
                self.rect.y = self.movement_area_y[0]
            if self.rect.y > (self.movement_area_y[1] - self.image_height):
                self.rect.y = (self.movement_area_y[1] - self.image_height)

        if self.name == "enemy":
            if self.rect.y < self.movement_area_y[0] or self.rect.y > (self.movement_area_y[1] - self.image_height):
                self.y_movement_velocity *= -1



    def fire(self, current_fire_time, last_fired_time) -> bool:
        """
        Try to fire. The outcome will be based on fire rate and last time fired. Return true if allowed to fire
        :return: bool
        """
        return True if (current_fire_time - last_fired_time) > (self.fire_rate * 1000) else False







