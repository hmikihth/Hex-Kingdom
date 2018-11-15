#!/bin/python3

import world
import render
import pygame
import time

TITLE = 'Hex Kingdom'
screen = pygame.display.set_mode((render.SCREEN_SIZE[0] + 140, render.SCREEN_SIZE[1]), 0, 32)
pygame.display.set_caption(TITLE)

resources = {'gold':5, 'wood':5, 'stone':5}
buildings = []
turn = 0
building = None
build_x = 0
build_y = 0
started = False
won = False
times = []
cam_x = 0
cam_y = 0
scroll_y = 0

while True:
    screen.fill(render.BG)
    if started and not won:
        if world.MONOLITH in buildings:
            pygame.time.wait(2000)
            won = True
        now = time.time()
        print(int(now - start))
        render.draw_world(world.layout, screen, cam_x, cam_y)
        if building:
            building_copy = pygame.image.load(building.image).convert()
            building_copy.set_colorkey((0, 0, 0))
            building_copy.set_alpha(128)
            if build_y % 2 == 0:
                screen.blit(pygame.transform.scale(building_copy, render.TILE_SIZE), \
                (build_x * render.TILE_SIZE[0], build_y * render.TILE_SIZE[1] - (build_y * 20)))
            else:
                screen.blit(pygame.transform.scale(building_copy, render.TILE_SIZE), \
                (build_x * render.TILE_SIZE[0] + (render.TILE_SIZE[0] / 2), build_y * render.TILE_SIZE[1] - (build_y * 20)))
        resource_y = -1
        for resource in resources:
            resource_y += 1
            resource_text = render.FONT.render(resource + ': ' + str(resources[resource]), False, (0, 0, 0))
            screen.blit(resource_text, (render.SCREEN_SIZE[0] / 2 - 60, render.SCREEN_SIZE[1] - (resource_y * 20) - 40))
        for build in buildings:
            if int(now - start) % build.delay == 0:
                if int(now - start) not in times:
                    times.append(int(now - start))
                    for out in build.out:
                        if out in resources:
                            resources[out] += build.out[out]
                        else:
                            resources[out] = build.out[out]
        pygame.draw.rect(screen, (0, 0, 0), (render.SCREEN_SIZE[0], 0, 140, render.SCREEN_SIZE[1]))
        if building:
            screen.blit(pygame.transform.scale(pygame.image.load(building.image), render.BIG_TILE_SIZE), (render.SCREEN_SIZE[0], 0))
            cost_text = 'Cost:\n'
            out_text = 'Output:\n'
            for item in building.cost:
                cost_text += item + ': ' + str(building.cost[item]) + '\n'
            for item in building.out:
                out_text += item + ': ' + str(building.out[item]) + '\n'
            cost_y = 8
            for line in cost_text.split('\n'):
                cost_y += 1
                line = render.FONT.render(line, False, (255, 255, 255))
                screen.blit(line, (render.SCREEN_SIZE[0], (cost_y * 20)))
            out_y = cost_y
            for line in out_text.split('\n'):
                out_y += 1
                line = render.FONT.render(line, False, (255, 255, 255))
                screen.blit(line, (render.SCREEN_SIZE[0], (out_y * 20)))
            try:
                terrain_text = 'Must be\nbuilt on\n' + building.terrain.name.lower()
            except:
                terrain_text = 'Can be\nbuilt on\nanything'
            terrain_y = out_y
            for line in terrain_text.split('\n'):
                terrain_y += 1
                line = render.FONT.render(line, False, (255, 255, 255))
                screen.blit(line, (render.SCREEN_SIZE[0], (terrain_y * 20)))
            upgrade_text = 'Level ' + str(building.upgrade + 2)
            upgrade_y = terrain_y + 2
            line = render.FONT.render(upgrade_text, False, (255, 255, 255))
            screen.blit(line, (render.SCREEN_SIZE[0], (upgrade_y * 20)))
    elif not started and not won:
        text = '''
        Hex Kingdom
        Press space to start
        '''
        text_y = -1
        for line in text.split('\n'):
            text_y += 1
            line = render.FONT.render(line, False, (0, 0, 0))
            screen.blit(line, (render.SCREEN_SIZE[0] / 2 - 280, render.SCREEN_SIZE[1] / 2 + (text_y * 20) - 40))
    elif started and won:
        text = '''






















        Victory!
        You have built
        the monolith
        and your people
        have evolved
        into super
        beings!
        Press space to keep
        building your
        empire.



























        Hex Kingdom by sugarfi
        Graphics from kenney.nl
        Font from urbanfonts.com
        Created with Pygame
        '''
        text_y = -1
        for line in text.split('\n'):
            text_y += 1
            line = render.FONT.render(line, False, (0, 0, 0))
            screen.blit(line, (render.SCREEN_SIZE[0] / 2 - 280, (text_y * 20) - scroll_y))
        scroll_y += 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                building = world.LUMBER
            elif event.key == pygame.K_2:
                building = world.MINE
            elif event.key == pygame.K_3:
                building = world.FARM
            elif event.key == pygame.K_4:
                building = world.WATERTOWER
            elif event.key == pygame.K_5:
                building = world.SHOP
            elif event.key == pygame.K_9:
                building = world.MONOLITH
            elif event.key == pygame.K_LEFT:
                if building:
                    if build_x > 0:
                        build_x -= 1
                else:
                    if cam_x > 0:
                        cam_x -= 1
            elif event.key == pygame.K_RIGHT:
                if building:
                    if build_x < len(world.layout[build_y]) - 1:
                        build_x += 1
                else:
                    if cam_x < len(world.layout[cam_y]) - 1:
                        cam_x += 1
            elif event.key == pygame.K_UP:
                if building:
                    if build_y > 0:
                        build_y -= 1
                else:
                    if cam_y > 0:
                        cam_y -= 1
            elif event.key == pygame.K_DOWN:
                if building:
                    if build_y < len(world.layout) - 1:
                        build_y += 1
                else:
                    if cam_y < len(world.layout) - 1:
                        cam_y += 1
            elif event.key == pygame.K_SPACE:
                if started and not won:
                    if building:
                        done = 0
                        if building.terrain in world.layout[build_y][build_x] or building.terrain == world.ANY:
                            if len(world.layout[build_y][build_x]) == 1:
                                if building:
                                    for item in building.cost:
                                        if item in resources:
                                            if resources[item] >= building.cost[item]:
                                                resources[item] -= building.cost[item]
                                                done += 1
                                            else:
                                                break
                                        else:
                                            break
                            else:
                                for build in world.layout[build_y][build_x]:
                                    if build == building:
                                        build.up()
                            if done == len(building.cost):
                                world.layout[build_y][build_x].append(building)
                                buildings.append(building)
                                print(buildings)
                    building = None
                    build_x = cam_x
                    build_y = cam_y
                elif not started and not won:
                    started = True
                    start = time.time()
                elif started and won:
                    won = False
    pygame.display.flip()
