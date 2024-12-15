#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image

from code.const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_KILLS


class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets/' + name + '.png')  # carregando .png
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.kills = ENTITY_KILLS[self.name]
        self.last_dmg = 'None'

    @abstractmethod
    def move(self, ):
        pass
