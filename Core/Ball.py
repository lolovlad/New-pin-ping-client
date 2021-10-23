from pygame.math import Vector2
from Model.Enemy import GameObject
from pygame import Rect


class Ball(GameObject):
    def __init__(self, start_position, size, color, speed, min_speed, max_speed, direction):
        super().__init__(start_position, size, color, speed, min_speed, max_speed, direction)
        self.__normalize_direction = self.direction.normalize()

    def reflect(self, new_dir):
        self.__normalize_direction = self.__normalize_direction.reflect(Vector2(new_dir)).normalize()

    def move(self):
        self.position += self.__normalize_direction * self.speed
        self.rect.center = round(self.position.x), round(self.position.y)

    def add_speed(self, speed):
        if self.speed + speed >= self.max_speed:
            self.speed = self.max_speed
        elif self.speed + speed <= self.min_speed:
            self.speed = self.min_speed
        else:
            self.speed += speed
