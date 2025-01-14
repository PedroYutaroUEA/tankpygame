import pygame
import random
import math
from time import time
from sfx import hit_sound_effect

pygame.init()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, color):
        super().__init__()
        # body
        self.color = color
        self.image = pygame.Surface((5, 5))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        # actions
        self.direction = direction
        self.bounce_count = 0
        self.hits = 0
        self.move_x = self.direction[0]/2
        self.move_y = self.direction[1]/2
        self.collision_initial_time = time()
        self.collision_final_time = time()

    def update(self, walls):
        self.collision_final_time = time()
        # handle movement
        self.rect.x += self.move_x * 1
        self.collision('horizontal', walls)
        self.rect.y += self.move_y * 1
        self.collision('vertical', walls)
        if self.hits >= 6:
            self.kill()

    def change_dir(self, dir):
        if dir == 'x':
            self.move_x *= -1
        else:
            self.move_y *= -1
        self.collision_initial_time = time()
        self.hits += 1
        hit_sound_effect.play()

    def collision(self, direction, walls):
        for wall in walls:
            if direction == 'horizontal':
                if self.collision_final_time - self.collision_initial_time > 0.1:
                    if self.rect.colliderect(wall):
                        self.change_dir('x')
            if direction == 'vertical':
                if self.collision_final_time - self.collision_initial_time > 0.1:
                    if self.rect.colliderect(wall):
                        self.change_dir('y')

    @staticmethod
    def get_random_direction():
        angles = [0, math.pi / 2, math.pi, 3 * math.pi / 2]
        return random.choice([(math.cos(angle), math.sin(angle)) for angle in angles])
