import numpy
import random
import pygame
from scipy.spatial import Voronoi

class Map():
    def __init__(self, screen):
        self.screen = screen
        self.voronoi = self.__generate_voronoi()
        self.color = (0, 0, 128)

    def __generate_voronoi(self):
        points = numpy.zeros([48, 2], numpy.uint16)
        for i in range(0, 8):
            for j in range(0, 6):
                points[i * 6 + j][0] = numpy.uint16(random.randint(i * 100 + 16, (i + 1) * 100 - 32))
                points[i * 6 + j][1] = numpy.uint16(random.randint(j * 100 + 16, (j + 1) * 100 - 32))
        self.coord = tuple(random.choice(points))
        self.honey_coord = tuple(random.choice([p for p in points if tuple(p) != self.coord]))
        enemy_points = [p for p in points if tuple(p) not in [self.coord, self.honey_coord]]
        self.enemy_coords = [tuple(i) for i in random.sample(enemy_points, 7)]
        return Voronoi(points)

    def draw_map(self):
        for i in self.voronoi.ridge_vertices:
            if -1 not in i:
                start_pos = self.voronoi.vertices[i[0]]
                end_pos = self.voronoi.vertices[i[1]]
                pygame.draw.line(self.screen, self.color, start_pos, end_pos)

