import pygame
import random

pygame.init()

font_family = "Arial"
font_size = 15

W = 600
H = 700
w_cell = 30
h_cell = 30
y_start_area = 10
x_start_area = 50
y_end_area = 610
x_end_area = 350
x_next_block = 450
y_next_block = 400

num_next_block = random.randrange(1, 8)


key_button = ""


coords_blocks = {}


current_block = {
    "num": 7,
    "position": True,
    "coord": [170, 10],
    "cells_block": (0, 0),
    "count_block_screen": 0,
}

figurs = {}
window_size = (W, H)
# num_block = 7

score = 0
level = 0
blocks = 0
high_score = 0
gray = (153, 169, 175)
white = (255, 255, 255)
