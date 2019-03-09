#!/usr/bin/env python3
#coding=utf-8

import random

SCENES = ["town", "forest"]

SKY = ["🌕", "🌙", "☁️", "☁️", "🚁"]
TOWN_TILES = ["🏢", "🏫", "🌳", "🏥", "🏪", "⛪"]
FOREST_TILES = ["🌲", "🌲", "🌲", "🦌", "🌳", "🌳", "🌳"]
ROAD_TILES = ["🚙", "🚗", "🚓", "🚕", "🚲"]

def make_tiny_road():
    sky = make_sky()
    sidewalk = make_sidewalk()
    road = make_road()

    set_the_scene = (
        sky + "\n" + \
        sidewalk[0] + "\n" + \
        road[0] + "\n" + \
        road[1]
    )

    return set_the_scene

def make_sidewalk():
    sidewalk = []
    scene = random.choice(SCENES)
    row = ""

    if scene == "town":
        tileset = TOWN_TILES
    elif scene == "forest":
        tileset = FOREST_TILES

    for spot in range(20):
        row += random.choice(tileset)

    sidewalk.append(row)

    return sidewalk

def make_road():
    road = []
    tileset = ROAD_TILES

    for row in range(2):
        row = ""
        for spot in range(20):
            tile = random.randint(0,100)
            if tile%5 == 0:
                row += random.choice(tileset)
            else:
                row += " "

        road.append(row)
    return road

def make_sky():
    sky = ""
    orb = random.choice(SKY)
    
    for _ in range(20):
        sky += " "
    orb_placement = random.randint(0,len(sky)-1)

    sky = sky[:orb_placement] + orb + sky[orb_placement:]
    return sky

if __name__ == "__main__":
    make_tiny_road()
    