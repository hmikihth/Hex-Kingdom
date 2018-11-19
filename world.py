#!/bin/python3

import random

class Tile():
    def __init__(self, image, name):
        self.image = image
        self.name = name
    def __repr__(self):
        return 'Tile(%s)' % self.image

ANY = 'any'

class Building():
    def __init__(self, image, cost, out, terrain=ANY, delay=5):
        self.upgrades = image
        self.image = self.upgrades[0]
        self.cost = cost
        self.out = out
        self.terrain = terrain
        self.delay = delay
        self.upgrade = -1
    def up(self):
        self.upgrade += 1
        if len(self.upgrades) > self.upgrade:
            self.image = self.upgrades[self.upgrade]
            for item in self.out:
                self.out[item] += 1
            for item in self.cost:
                self.cost[item] += 1
    def __repr__(self):
        return 'Building(%s)' % self.image[0]

GRASS = Tile('grass_19.png', 'grass')
FOREST = Tile('grass_13.png', 'woods')
STONE = Tile('stone_02.png', 'stone')

SHOP = Building(['medieval_blacksmith.png', 'western_general.png', 'modern_shop.png'], \
{'gold':1, 'wood':1}, \
{'gold':1}, \
terrain=ANY, delay=4)

LUMBER = Building(['medieval_lumber.png', 'modern_trailerpark.png', 'stone_18.png'], \
{'gold':2, 'wood':2}, \
{'wood':1}, \
terrain=FOREST, delay=6)

MINE = Building(['medieval_mine.png'], \
{'gold':2, 'wood':2, 'stone':2}, \
{'stone':1, 'gold':1}, \
terrain=STONE, delay=7)

WATERTOWER = Building(['western_watertower.png'], \
{'gold':1, 'wood':2},
{'water':1},
terrain=ANY, delay=2)

FARM = Building(['medieval_farm.png', 'medieval_windmill.png', 'modern_campsite.png'], \
{'water':1, 'gold':1},
{'food':1},
terrain=ANY, delay=10)

MONOLITH = Building(['images/stone_16.png'], \
{'stone':50, 'wood':50, 'gold':50, 'food':50},
{},
terrain=ANY)

FOREST_LAYOUT = [
    [
        [FOREST], [FOREST], [FOREST], [FOREST], [FOREST],
    ],
    [
        [FOREST], [FOREST], [STONE], [FOREST], [FOREST],
    ],
    [
        [FOREST], [STONE], [STONE], [STONE], [FOREST],
    ],
    [
        [FOREST], [FOREST], [STONE], [FOREST], [FOREST],
    ],
    [
        [FOREST], [FOREST], [FOREST], [FOREST], [FOREST],
    ],
]
PLAINS_LAYOUT = [
    [
        [GRASS], [GRASS], [GRASS], [GRASS], [GRASS],
    ],
    [
        [GRASS], [FOREST], [FOREST], [FOREST], [GRASS],
    ],
    [
        [GRASS], [FOREST], [FOREST], [FOREST], [GRASS],
    ],
    [
        [STONE], [STONE], [STONE], [GRASS], [GRASS],
    ],
    [
        [STONE], [STONE], [STONE], [GRASS], [GRASS],
    ],
]
MOUNTAIN_LAYOUT = [
    [
        [STONE], [STONE], [STONE], [STONE], [STONE],
    ],
    [
        [STONE], [STONE], [FOREST], [STONE], [FOREST],
    ],
    [
        [STONE], [FOREST], [STONE], [FOREST], [STONE],
    ],
    [
        [STONE], [STONE], [FOREST], [STONE], [STONE],
    ],
    [
        [STONE], [FOREST], [STONE], [STONE], [STONE],
    ],
]
layouts = [FOREST_LAYOUT, PLAINS_LAYOUT, MOUNTAIN_LAYOUT]
random.shuffle(layouts)
layout = random.choice(layouts)

__import__('pprint').pprint(layout)
