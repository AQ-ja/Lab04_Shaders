import pygame
from pygame.locals import *
import numpy as np
from gl import Renderer, Model
import shaders


width = 960
height = 540

# Ya que lo vi en internet igual y sirve para el proyecto. 
deltaTime = 0.0
cubeX = 0
cubeY = 0
cubeZ = 0
roll = 0
pitch = 0
yaw = 0
distance = 0

changeY=False
changeX=False




pygame.init()
screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL | pygame.OPENGLBLIT )
clock = pygame.time.Clock()

# Posible fondo 
bgspace = pygame.image.load('white.png')


rend = Renderer(screen)
rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)

face = Model('ufo.obj', 'earth.bmp')
face.position.z = -5

rend.scene.append( face )


isRunning = True
while isRunning:


    keys = pygame.key.get_pressed()

    # Traslacion de camara
    if keys[K_d]:
        rend.camPosition.x += 1 * deltaTime
    if keys[K_a]:
        rend.camPosition.x -= 1 * deltaTime
    if keys[K_w]:
        rend.camPosition.z += 1 * deltaTime
    if keys[K_s]:
        rend.camPosition.z -= 1 * deltaTime
    if keys[K_q]:
        rend.camPosition.y -= 1 * deltaTime
    if keys[K_e]:
        rend.camPosition.y += 1 * deltaTime

    if keys[K_LEFT]:
        if rend.valor > 0:
            rend.valor -= 0.1 * deltaTime

    if keys[K_RIGHT]:
        if rend.valor < 0.2:
            rend.valor += 0.1 * deltaTime

    # Rotacion de camara
    if keys[K_z]:
        rend.camRotation.y += 15 * deltaTime
    if keys[K_x]:
        rend.camRotation.y -= 15 * deltaTime


    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isRunning = False

        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                isRunning = False

            if ev.key == K_1:
                rend.filledMode()
            if ev.key == K_2:
                rend.wireframeMode()
            #Empiezan los shaders
            if ev.key == K_3:
                rend.setShaders(shaders.vertex_shader, shaders.fragment_shader_v2)
            if ev.key == K_4:
                rend.setShaders(shaders.vertex_shader, shaders.fragment_shader_v3)
            if ev.key == K_5:
                rend.setShaders(shaders.vertex_shader, shaders.fragment_shader_v4)
            if ev.key == K_6:
                rend.setShaders(shaders.vertex_toon_shader, shaders.fragment_shader_v5)
            if ev.key == K_7:
                rend.setShaders(shaders.vertex_try_shader, shaders.atlantis)

    rend.tiempo += deltaTime
    deltaTime = clock.tick(60) / 1000

    rend.render()

    pygame.display.flip()

pygame.quit()
