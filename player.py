import pygame
from pygame.locals import *  # noqa
from support import import_folder

# Gravity movements
vec = pygame.math.Vector2
acceleration = 0.5
friction = -0.10


class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.import_char_assets()
        self.frame_index = 0
        self.animate_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=position)

        # player moves
        self.direction = vec(0, 0)

        self.position = vec((100, 600))
        self.velocity = vec(0, 0)
        self.acceleration = vec(0, 0)

        self.movement_speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

        # player status
        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

    def import_char_assets(self):
        char_path = './graphics/char/'
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': []}

        for animation in self.animations.keys():
            full_path = char_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]

        # loop over frame index
        self.frame_index += self.animate_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]

        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

        # set the rect
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)

        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright=self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    def get_input(self):
        # 0,5 adds vertical force a.k.a gravity
        self.acceleration = vec(0, 0.5)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        elif pressed_keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        else:
            self.direction.x = 0

        # if pressed_keys[K_LEFT]:
        #     self.acceleration.x = -acceleration
        #     self.facing_right = False
        #     print('Left key pressed')
        # if pressed_keys[K_RIGHT]:
        #     self.acceleration.x = acceleration
        #     self.facing_right = True
        #     print('Right key pressed')

        self.acceleration.x += self.velocity.x * friction
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        if pressed_keys[pygame.K_SPACE] and self.on_ground:
            self.jump()

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()
