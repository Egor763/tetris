import pygame
import random

import settings


class Blocks:
    def __init__(self, screen):
        pygame.init()

        self.screen = screen

        self.green = (0, 255, 0)
        self.sea_wave = (0, 255, 255)
        self.gray = (204, 204, 204)
        self.red = (255, 0, 0)

        self.w_cell = settings.w_cell
        self.h_cell = settings.h_cell
        self.black = (0, 0, 0)

        self.num_next_block = settings.num_next_block

        self.coords_blocks = settings.coords_blocks

        self.x_next_block = settings.x_next_block
        self.y_next_block = settings.y_next_block

        self.current_block = settings.current_block

        self.key_button = settings.key_button

        self.border_width = 1

    def random_num(self):
        # if next_num:
        #     self.num_next_block = random.randrange(1, 8)

        # else:
        #     self.current_block["num"] = random.randrange(1, 8)

        return random.randrange(1, 8)

    def create_block(self, block_verticle, coord, num_block, next_figure):

        if num_block == 1:
            self.block_1(block_verticle, coord, next_figure)

        if num_block == 2:
            self.block_2(block_verticle, coord, next_figure)

        if num_block == 3:
            self.block_3(block_verticle, coord, next_figure)

        if num_block == 4:
            self.block_4(block_verticle, coord, next_figure)

        if num_block == 5:
            self.block_5(block_verticle, coord, next_figure)

        if num_block == 6:
            self.block_6(block_verticle, coord, next_figure)

        if num_block == 7:
            self.block_7(block_verticle, coord, next_figure)

    def next_image(self, num_block, next_figure):
        # next_block = random.randrange(1, 8)

        # if self.key_button:
        self.create_block(
            True, (self.x_next_block, self.y_next_block), num_block, next_figure
        )

    # print(next_block)

    # self.screen.blit(next_block, (self.x_next_block, self.y_next_block))

    def _square_item(self, square_color, coord):

        if square_color == "red":
            color = (255, 0, 0)
            color_light = (151, 151, 255)
            color_dark = (0, 0, 130)

        elif square_color == "blue":
            color = (0, 0, 255)
            color_light = (255, 142, 142)
            color_dark = (119, 0, 0)

        elif square_color == "yellow":
            color = (255, 255, 0)
            color_light = (255, 237, 157)
            color_dark = (110, 96, 32)

        elif square_color == "pink":
            color = (175, 0, 175)
            color_light = (255, 0, 255)
            color_dark = (95, 0, 95)

        elif square_color == "sea_wave":
            color = (53, 153, 252)
            color_light = (169, 212, 255)
            color_dark = (59, 86, 113)

        elif square_color == "gray":
            color = (164, 171, 187)
            color_light = (255, 255, 255)
            color_dark = (132, 132, 132)

        elif square_color == "green":
            color = (0, 175, 0)
            color_light = (125, 255, 125)
            color_dark = (0, 92, 0)

        size_rect = 29
        x = coord[0]
        y = coord[1]

        pygame.draw.rect(
            self.screen,
            color,
            (x + 1, y + 1, self.w_cell - 2, self.h_cell - 2),
        )

        # низ
        pygame.draw.line(
            self.screen,
            color_dark,
            (x, y + size_rect),
            (x + size_rect, y + size_rect),
            self.border_width,
        )
        # левая
        pygame.draw.line(
            self.screen,
            color_light,
            (x, y),
            (x, y + size_rect),
            self.border_width,
        )
        # правая
        pygame.draw.line(
            self.screen,
            color_dark,
            (x + size_rect, y),
            (x + size_rect, y + size_rect),
            self.border_width,
        )
        # верх
        pygame.draw.line(
            self.screen,
            color_light,
            (x, y),
            (x + size_rect, y),
            self.border_width,
        )

    def block_1(self, block_verticle, coord, next_figure):
        count = 1

        x = coord[0]
        y = coord[1]

        if block_verticle:
            self.current_block["cells_block"] = (1, 4)
            while count < 5:
                if not next_figure:
                    self.coords_blocks[f"{count}red"] = [x + self.w_cell, y]
                # self.coords_blocks["block_1"][str(count)][1] = y
                self._square_item("red", (x + self.w_cell, y))
                y += self.h_cell

                count += 1

            pygame.display.update()

        else:
            self.current_block["cells_block"] = (4, 1)

            while count < 5:
                # self.coords_blocks["block_1"][str(count)][0] = x
                # self.coords_blocks["block_1"][str(count)][1] = y
                self.coords_blocks[f"{count}red"] = [x, y]
                self._square_item("red", (x, y))
                x += self.w_cell

                count += 1

            pygame.display.update()

    def block_2(self, block_verticle, coord, next_figure):

        count = 1

        x = coord[0]
        y = coord[1]

        if block_verticle:
            self.current_block["cells_block"] = (3, 2)

            while count < 5:
                if count == 1:
                    # self.coords_blocks["block_2"]["1"][0] = x
                    # self.coords_blocks["block_2"]["1"][1] = y + self.h_cell
                    if not next_figure:
                        self.coords_blocks["1blue"] = [x, y + self.h_cell]
                    self._square_item(
                        "blue",
                        (x, y + self.h_cell),
                    )
                    # self._square_item(blue, color_light, color_dark, (x, y + self.h_cell))
                if count == 2:
                    # self.coords_blocks["block_2"]["2"][0] = x + self.w_cell
                    # self.coords_blocks["block_2"]["2"][1] = y + self.h_cell
                    if not next_figure:
                        self.coords_blocks["2blue"] = [
                            x + self.w_cell,
                            y + self.h_cell,
                        ]
                    self._square_item(
                        "blue",
                        (x + self.w_cell, y + self.h_cell),
                    )
                    # self._square_item(
                    #     blue, color_light, color_dark, (x + self.w_cell, y + self.h_cell)
                    # )
                if count == 3:
                    # self.coords_blocks["block_2"]["3"][0] = x + self.w_cell
                    # self.coords_blocks["block_2"]["3"][1] = y
                    if not next_figure:
                        self.coords_blocks["3blue"] = [x + self.w_cell, y]
                    self._square_item(
                        "blue",
                        (x + self.w_cell, y),
                    )
                    # self._square_item(blue, color_light, color_dark, (x + self.w_cell, y))

                if count == 4:
                    if not next_figure:
                        self.coords_blocks["4blue"] = [
                            x + self.w_cell * 2,
                            y,
                        ]
                    # self.coords_blocks["block_2"]["4"][0] = x + self.w_cell * 2
                    # self.coords_blocks["block_2"]["4"][1] = y
                    self._square_item(
                        "blue",
                        (x + self.w_cell * 2, y),
                    )
                    # self._square_item(
                    #     blue, color_light, color_dark, (x + self.w_cell * 2, y)
                    # )

                count += 1

            pygame.display.update()

        else:
            self.current_block["cells_block"] = (2, 3)

            while count < 5:
                if count == 1:
                    # self.coords_blocks["block_2"]["1"][0] = x
                    # self.coords_blocks["block_2"]["1"][1] = y
                    self.coords_blocks["1blue"] = [x, y]
                    self._square_item("blue", (x, y))
                    # self._square_item(blue, color_light, color_dark, (x, y))
                if count == 2:
                    # self.coords_blocks["block_2"]["1"][0] = x
                    # self.coords_blocks["block_2"]["1"][1] = y + self.h_cell
                    self.coords_blocks["2blue"] = [x, y + self.h_cell]
                    self._square_item("blue", (x, y + self.h_cell))
                    # self._square_item(blue, color_light, color_dark, (x, y + self.h_cell))
                if count == 3:
                    # self.coords_blocks["block_2"]["1"][0] = x + self.w_cell
                    # self.coords_blocks["block_2"]["1"][1] = y + self.h_cell
                    self.coords_blocks["3blue"] = [
                        x + self.w_cell,
                        y + self.h_cell,
                    ]
                    self._square_item(
                        "blue",
                        (x + self.w_cell, y + self.h_cell),
                    )
                if count == 4:
                    # self.coords_blocks["block_2"]["1"][0] = x + self.w_cell
                    # self.coords_blocks["block_2"]["1"][1] = y + self.h_cell * 2
                    self.coords_blocks["4blue"] = [
                        x + self.w_cell,
                        y + self.h_cell * 2,
                    ]
                    self._square_item(
                        "blue",
                        (x + self.w_cell, y + self.h_cell * 2),
                    )
                count += 1

            pygame.display.update()

    def block_3(self, block_verticle, coord, next_figure):

        count = 1

        x = coord[0]
        y = coord[1]

        if block_verticle:
            self.current_block["cells_block"] = (2, 3)

            while count < 5:
                if count != 4:
                    # self.coords_blocks["block_3"][str(count)][0] = x
                    # self.coords_blocks["block_3"][str(count)][1] = y
                    if not next_figure:
                        self.coords_blocks[f"{count}yellow"] = [x, y]
                    self._square_item("yellow", (x, y))

                    y += self.h_cell

                else:
                    # self.coords_blocks["block_3"]["4"][0] = x + self.w_cell
                    # self.coords_blocks["block_3"]["4"][1] = y - self.h_cell
                    if not next_figure:
                        self.coords_blocks["4yellow"] = [
                            x + self.w_cell,
                            y - self.h_cell,
                        ]
                    self._square_item(
                        "yellow",
                        (x + self.w_cell, y - self.h_cell),
                    )

                count += 1

            pygame.display.update()

        else:
            self.current_block["cells_block"] = (3, 2)

            while count < 5:
                if count != 4:
                    self.coords_blocks[f"{count}yellow"] = [x, y + self.h_cell]
                    # self.coords_blocks["block_3"][str(count)][0] = x
                    # self.coords_blocks["block_3"][str(count)][1] = y + self.h_cell
                    self._square_item("yellow", (x, y + self.h_cell))

                    x += self.w_cell

                else:
                    # self.coords_blocks["block_3"]["4"][0] = x - self.w_cell
                    # self.coords_blocks["block_3"]["4"][1] = y
                    self.coords_blocks["4yellow"] = [x - self.w_cell, y]
                    self._square_item(
                        "yellow",
                        (x - self.w_cell, y),
                    )
                count += 1

            pygame.display.update()

    def block_4(self, block_verticle, coord, next_figure):

        count = 1

        x = coord[0]
        y = coord[1]

        if block_verticle:
            self.current_block["cells_block"] = (2, 3)

            while count < 5:
                if count != 4:
                    if not next_figure:
                        self.coords_blocks[f"{count}pink"] = [x + self.w_cell, y]
                    # self.coords_blocks["block_4"][str(count)][0] = x + self.w_cell
                    # self.coords_blocks["block_4"][str(count)][1] = y
                    self._square_item("pink", (x + self.w_cell, y))

                    y += self.h_cell

                else:
                    if not next_figure:
                        self.coords_blocks["4pink"] = [x, y - self.h_cell]
                    # self.coords_blocks["block_4"]["4"][0] = x
                    # self.coords_blocks["block_4"]["4"][1] = y - self.h_cell
                    self._square_item("pink", (x, y - self.h_cell))

                count += 1

            pygame.display.update()

        else:
            self.current_block["cells_block"] = (3, 2)

            while count < 5:
                if count != 4:
                    self.coords_blocks[f"{count}pink"] = [x, y]
                    # self.coords_blocks["block_4"][str(count)][0] = x
                    # self.coords_blocks["block_4"][str(count)][1] = y
                    self._square_item("pink", (x, y))
                    x += self.w_cell
                else:
                    self.coords_blocks["4pink"] = [
                        x - self.w_cell,
                        y + self.h_cell,
                    ]
                    # self.coords_blocks["block_4"]["4"][0] = x - self.w_cell
                    # self.coords_blocks["block_4"]["4"][1] = y + self.h_cell
                    self._square_item("pink", (x - self.w_cell, y + self.h_cell))

                count += 1

            pygame.display.update()

    # квадрат
    def block_5(self, block_verticle, coord, next_figure):

        count = 1

        self.current_block["cells_block"] = (2, 2)

        x = coord[0]
        y = coord[1]

        # if block_verticle:

        while count < 5:
            if count == 1:
                if not next_figure:
                    self.coords_blocks["1sea_wave"] = [x, y]
                # self.coords_blocks["block_5"]["1"][0] = x
                # self.coords_blocks["block_5"]["1"][1] = y
                self._square_item("sea_wave", (x, y))

            if count == 2:
                if not next_figure:
                    self.coords_blocks["2sea_wave"] = [x + self.w_cell, y]
                # self.coords_blocks["block_5"]["2"][0] = x + self.w_cell
                # self.coords_blocks["block_5"]["2"][1] = y
                self._square_item("sea_wave", (x + self.w_cell, y))

            if count == 3:
                if not next_figure:
                    self.coords_blocks["3sea_wave"] = [x, y + self.h_cell]
                # self.coords_blocks["block_5"]["3"][0] = x
                # self.coords_blocks["block_5"]["3"][1] = y + self.h_cell
                self._square_item("sea_wave", (x, y + self.h_cell))

            if count == 4:
                if not next_figure:
                    self.coords_blocks["4sea_wave"] = [
                        x + self.w_cell,
                        y + self.h_cell,
                    ]
                # self.coords_blocks["block_5"]["4"][0] = x + self.w_cell
                # self.coords_blocks["block_5"]["4"][1] = y + self.h_cell
                self._square_item(
                    "sea_wave",
                    (x + self.w_cell, y + self.h_cell),
                )

            count += 1

        pygame.display.update()

    def block_6(self, block_verticle, coord, next_figure):

        count = 1

        x = coord[0]
        y = coord[1]

        if block_verticle:
            self.current_block["cells_block"] = (3, 2)

            while count < 5:
                if count == 1:
                    # self.coords_blocks["block_6"]["1"][0] = x
                    # self.coords_blocks["block_6"]["1"][1] = y + self.h_cell
                    if not next_figure:
                        self.coords_blocks["1gray"] = [x, y + self.h_cell]
                    self._square_item("gray", (x, y + self.h_cell))

                if count == 2:
                    if not next_figure:
                        self.coords_blocks["2gray"] = [
                            x + self.w_cell,
                            y + self.h_cell,
                        ]
                    # self.coords_blocks["block_6"]["2"][0] = x + self.w_cell
                    # self.coords_blocks["block_6"]["2"][1] = y + self.h_cell
                    self._square_item("gray", (x + self.w_cell, y + self.h_cell))

                if count == 3:
                    if not next_figure:
                        self.coords_blocks["3gray"] = [
                            x + self.w_cell * 2,
                            y + self.h_cell,
                        ]
                    # self.coords_blocks["block_6"]["3"][0] = x + self.w_cell * 2
                    # self.coords_blocks["block_6"]["3"][1] = y + self.h_cell
                    self._square_item(
                        "gray",
                        (x + self.w_cell * 2, y + self.h_cell),
                    )

                if count == 4:
                    # self.coords_blocks["block_6"]["4"][0] = x + self.w_cell
                    # self.coords_blocks["block_6"]["4"][1] = y
                    if not next_figure:
                        self.coords_blocks["4gray"] = [x + self.w_cell, y]
                    self._square_item("gray", (x + self.w_cell, y))

                count += 1

            pygame.display.update()

        else:
            self.current_block["cells_block"] = (2, 3)

            while count < 5:
                if count == 1:
                    self.coords_blocks["1gray"] = [x + self.w_cell, y]
                    # self.coords_blocks["block_6"]["1"][0] = x + self.w_cell
                    # self.coords_blocks["block_6"]["1"][1] = y
                    self._square_item("gray", (x + self.w_cell, y))
                if count == 2:
                    self.coords_blocks["2gray"] = [
                        x + self.w_cell,
                        y + self.h_cell,
                    ]
                    # self.coords_blocks["block_6"]["2"][0] = x + self.w_cell
                    # self.coords_blocks["block_6"]["2"][1] = y + self.h_cell
                    self._square_item("gray", (x + self.w_cell, y + self.h_cell))
                if count == 3:
                    self.coords_blocks["3gray"] = [
                        x + self.w_cell,
                        y + self.h_cell * 2,
                    ]
                    # self.coords_blocks["block_6"]["3"][0] = x + self.w_cell
                    # self.coords_blocks["block_6"]["3"][1] = y + self.h_cell * 2
                    self._square_item(
                        "gray",
                        (x + self.w_cell, y + self.h_cell * 2),
                    )
                if count == 4:
                    self.coords_blocks["4gray"] = [x, y + self.h_cell]
                    # self.coords_blocks["block_6"]["4"][0] = x
                    # self.coords_blocks["block_6"]["4"][1] = y + self.h_cell
                    self._square_item("gray", (x, y + self.h_cell))

                count += 1

            pygame.display.update()

    def block_7(self, block_verticle, coord, next_figure):

        count = 1
        x = coord[0]
        y = coord[1]

        if block_verticle:
            self.current_block["cells_block"] = (3, 2)

            while count < 5:
                if count == 1:
                    if not next_figure:
                        self.coords_blocks["1green"] = [x, y]
                    # self.coords_blocks["block_7"]["1"][0] = x
                    # self.coords_blocks["block_7"]["1"][1] = y
                    self._square_item("green", (x, y))
                if count == 2:
                    if not next_figure:
                        self.coords_blocks["2green"] = [x + self.w_cell, y]
                    # self.coords_blocks["block_7"]["2"][0] = x + self.w_cell
                    # self.coords_blocks["block_7"]["2"][1] = y
                    self._square_item("green", (x + self.w_cell, y))
                if count == 3:
                    if not next_figure:
                        self.coords_blocks["3green"] = [
                            x + self.w_cell,
                            y + self.h_cell,
                        ]
                    # self.coords_blocks["block_7"]["3"][0] = x + self.w_cell
                    # self.coords_blocks["block_7"]["3"][1] = y + self.h_cell
                    self._square_item(
                        "green",
                        (x + self.w_cell, y + self.h_cell),
                    )
                if count == 4:
                    if not next_figure:
                        self.coords_blocks["4green"] = [
                            x + self.w_cell * 2,
                            y + self.h_cell,
                        ]
                    # self.coords_blocks["block_7"]["4"][0] = x + self.w_cell * 2
                    # self.coords_blocks["block_7"]["4"][1] = y + self.h_cell
                    self._square_item(
                        "green",
                        (x + self.w_cell * 2, y + self.h_cell),
                    )

                count += 1

            pygame.display.update()

        else:
            self.current_block["cells_block"] = (2, 3)

            while count < 5:
                if count == 1:
                    self.coords_blocks["1green"] = [x, y]
                    # self.coords_blocks["block_7"]["1"][0] = x
                    # self.coords_blocks["block_7"]["1"][1] = y
                    self._square_item("green", (x, y))
                if count == 2:
                    self.coords_blocks["2green"] = [x, y + self.h_cell]
                    # self.coords_blocks["block_7"]["2"][0] = x
                    # self.coords_blocks["block_7"]["2"][1] = y + self.h_cell
                    self._square_item("green", (x, y + self.h_cell))
                if count == 3:
                    self.coords_blocks["3green"] = [
                        x + self.w_cell,
                        y + self.h_cell,
                    ]
                    # self.coords_blocks["block_7"]["3"][0] = x + self.w_cell
                    # self.coords_blocks["block_7"]["3"][1] = y + self.h_cell
                    self._square_item(
                        "green",
                        (x + self.w_cell, y + self.h_cell),
                    )
                if count == 4:
                    self.coords_blocks["4green"] = [
                        x + self.w_cell,
                        y + self.h_cell * 2,
                    ]
                    # self.coords_blocks["block_7"]["4"][0] = x + self.w_cell
                    # self.coords_blocks["block_7"]["4"][1] = y + self.h_cell * 2
                    self._square_item(
                        "green",
                        (x + self.w_cell, y + self.h_cell * 2),
                    )

                count += 1

            pygame.display.update()
