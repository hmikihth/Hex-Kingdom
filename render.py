#!/bin/python3

import pygame
import world

pygame.font.init()

TILE_SIZE = (60, 70)
SMALL_TILE_SIZE = (TILE_SIZE[0] // 2, TILE_SIZE[1] // 2)
BIG_TILE_SIZE = (TILE_SIZE[0] * 2, TILE_SIZE[1] * 2)
SCREEN_SIZE = (TILE_SIZE[0] * 7, TILE_SIZE[1] * 7)
FONT = pygame.font.Font('ubuntu_title/Ubuntu-Title.ttf', 36)
BG = (255, 255, 255)

def draw_world(layout, display, cam_x=0, cam_y=0):
    global TILE_SIZE
    global SMALL_TILE_SIZE
    print(layout)
    y = -1
    x = -1
    for row in layout[cam_y:]:
        y += 1
        x = -1
        for tile in row[cam_x:]:
            x += 1
            for item in tile:
                image = pygame.image.load(item.image)
                if type(item) == world.Building:
                    image = pygame.transform.scale(image, TILE_SIZE)
                elif type(item) == world.Tile:
                    image = pygame.transform.scale(image, TILE_SIZE)
                if y % 2 == 0:
                    display.blit(image, \
                    (x * TILE_SIZE[0], y * TILE_SIZE[1] - (y * 20)))
                else:
                    display.blit(image, \
                    (x * TILE_SIZE[0] + (TILE_SIZE[0] / 2), y * TILE_SIZE[1] - (y * 20)))
