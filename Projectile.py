import pygame

class Projectile(pygame.sprite.Sprite):

    def __init__(self,
                 owner: str,
                 x_coord: int,
                 y_coord: int,
                 image: str,
                 sound: str,
                 damage_modifier: int,
                 movement_area_x: tuple,
                 movement_area_y: tuple,
                 x_movement_velocity: int = 0,
                 y_movement_velocity: int = 0
                 ):

        """

        :param owner:
        :param x_coord:
        :param y_coord:
        :param image:
        :param sound:
        :param damage_modifier:
        :param movement_area_x:
        :param movement_area_y:
        :param x_movement_velocity:
        :param y_movement_velocity:
        """

        super().__init__()

        self.owner = owner
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.image = pygame.image.load(image).convert()
        self.sound = pygame.mixer.Sound(sound)
        self.damage_modifier = damage_modifier
        self.movement_area_x = movement_area_x
        self.movement_area_y = movement_area_y
        self.x_movement_velocity = x_movement_velocity
        self.y_movement_velocity = y_movement_velocity

        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()

        self.rect = self.image.get_rect(x=self.x_coord, y=self.y_coord)


    def update(self, screen: pygame.display):


        self.rect.x += self.x_movement_velocity
        if self.rect.x < self.movement_area_x[0]:
            self.kill()

        if self.rect.x > self.movement_area_x[1] - self.image_width:
            self.kill()

        self.rect.y += self.y_movement_velocity

        if self.rect.y < self.movement_area_y[0]:
            self.kill()

        if self.rect.y > self.movement_area_y[1] - self.image_height:
            self.kill()

        screen.blit(self.image, self.rect)


    def play_sound(self):
        self.sound.play()
