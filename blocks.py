import pygame

import settings


class Blocks:
    def __init__(self, screen_class):
        pygame.init()

        self.screen_class = screen_class

        self.screen = self.screen_class.screen_game()

        self.green = (0, 255, 0)
        self.sea_wave = (0, 255, 255)
        self.gray = (204, 204, 204)
        self.red = (255, 0, 0)

        self.w_cell = settings.w_cell
        self.h_cell = settings.h_cell
        self.black = (0, 0, 0)

        self.coords_blocks = settings.coords_blocks

        self.x_next_block = settings.x_next_block
        self.y_next_block = settings.y_next_block

        self.figurs = settings.figurs

        self.current_block = settings.current_block

        self.key_button = settings.key_button

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
        self.create_block(
            True, (self.x_next_block, self.y_next_block), num_block, next_figure
        )

    def block_1(self, block_verticle, coord, next_figure):
        count = 1

        x = coord[0]
        y = coord[1]

        if block_verticle:
            self.current_block["cells_block"] = (1, 4, 4)
            while count < 5:
                if not next_figure:
                    self.coords_blocks[f"{count}"] = [x + self.w_cell, y, "red"]
                self.screen_class.square_item("red", (x + self.w_cell, y))
                y += self.h_cell

                count += 1

            pygame.display.update()

        else:
            self.current_block["cells_block"] = (4, 1, 4)

            while count < 5:
                self.coords_blocks[f"{count}"] = [x, y, "red"]
                self.screen_class.square_item("red", (x, y))
                x += self.w_cell

                count += 1

            pygame.display.update()

    def block_2(self, block_verticle, coord, next_figure):
        count = 1

        x = coord[0]
        y = coord[1]

        if block_verticle:
            self.current_block["cells_block"] = (3, 2, 3)

            while count < 5:
                if count == 1:
                    if not next_figure:
                        self.coords_blocks["1"] = [x, y + self.h_cell, "blue"]
                    self.screen_class.square_item(
                        "blue",
                        (x, y + self.h_cell),
                    )
                if count == 2:
                    if not next_figure:
                        self.coords_blocks["2"] = [
                            x + self.w_cell,
                            y + self.h_cell,
                            "blue",
                        ]
                    self.screen_class.square_item(
                        "blue",
                        (x + self.w_cell, y + self.h_cell),
                    )

                if count == 3:
                    if not next_figure:
                        self.coords_blocks["3"] = [x + self.w_cell, y, "blue"]
                    self.screen_class.square_item(
                        "blue",
                        (x + self.w_cell, y),
                    )

                if count == 4:
                    if not next_figure:
                        self.coords_blocks["4"] = [x + self.w_cell * 2, y, "blue"]
                    self.screen_class.square_item(
                        "blue",
                        (x + self.w_cell * 2, y),
                    )

                count += 1

            pygame.display.update()

        else:
            self.current_block["cells_block"] = (2, 3, 3)

            while count < 5:
                if count == 1:
                    self.coords_blocks["1"] = [x, y, "blue"]
                    self.screen_class.square_item("blue", (x, y))
                if count == 2:
                    self.coords_blocks["2"] = [x, y + self.h_cell, "blue"]
                    self.screen_class.square_item("blue", (x, y + self.h_cell))
                if count == 3:
                    self.coords_blocks["3"] = [x + self.w_cell, y + self.h_cell, "blue"]
                    self.screen_class.square_item(
                        "blue",
                        (x + self.w_cell, y + self.h_cell),
                    )
                if count == 4:
                    self.coords_blocks["4"] = [
                        x + self.w_cell,
                        y + self.h_cell * 2,
                        "blue",
                    ]
                    self.screen_class.square_item(
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
            self.current_block["cells_block"] = (2, 3, 3)

            while count < 5:
                if count != 4:
                    if not next_figure:
                        self.coords_blocks[f"{count}"] = [x, y, "yellow"]
                    self.screen_class.square_item("yellow", (x, y))

                    y += self.h_cell
                else:
                    if not next_figure:
                        self.coords_blocks["4"] = [
                            x + self.w_cell,
                            y - self.h_cell,
                            "yellow",
                        ]
                    self.screen_class.square_item(
                        "yellow",
                        (x + self.w_cell, y - self.h_cell),
                    )

                count += 1

            pygame.display.update()

        else:
            self.current_block["cells_block"] = (3, 2, 3)

            while count < 5:
                if count != 4:
                    self.coords_blocks[f"{count}"] = [x, y + self.h_cell, "yellow"]
                    self.screen_class.square_item("yellow", (x, y + self.h_cell))

                    x += self.w_cell

                else:
                    self.coords_blocks["4"] = [x - self.w_cell, y, "yellow"]
                    self.screen_class.square_item(
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
            self.current_block["cells_block"] = (2, 3, 3)

            while count < 5:
                if count != 4:
                    if not next_figure:
                        self.coords_blocks[f"{count}"] = [x + self.w_cell, y, "pink"]
                    self.screen_class.square_item("pink", (x + self.w_cell, y))

                    y += self.h_cell

                else:
                    if not next_figure:
                        self.coords_blocks["4"] = [x, y - self.h_cell, "pink"]
                    self.screen_class.square_item("pink", (x, y - self.h_cell))

                count += 1

            pygame.display.update()
        else:
            self.current_block["cells_block"] = (3, 2, 3)

            while count < 5:
                if count != 4:
                    self.coords_blocks[f"{count}"] = [x, y, "pink"]
                    self.screen_class.square_item("pink", (x, y))
                    x += self.w_cell
                else:
                    self.coords_blocks["4"] = [x - self.w_cell, y + self.h_cell, "pink"]
                    self.screen_class.square_item(
                        "pink", (x - self.w_cell, y + self.h_cell)
                    )

                count += 1

            pygame.display.update()

    # квадрат
    def block_5(self, block_verticle, coord, next_figure):

        count = 1

        self.current_block["cells_block"] = (2, 2, 2)

        x = coord[0]
        y = coord[1]

        while count < 5:
            if count == 1:
                if not next_figure:
                    self.coords_blocks["1"] = [x, y, "sea_wave"]
                self.screen_class.square_item("sea_wave", (x, y))

            if count == 2:
                if not next_figure:
                    self.coords_blocks["2"] = [x + self.w_cell, y, "sea_wave"]
                self.screen_class.square_item("sea_wave", (x + self.w_cell, y))

            if count == 3:
                if not next_figure:
                    self.coords_blocks["3"] = [x, y + self.h_cell, "sea_wave"]
                self.screen_class.square_item("sea_wave", (x, y + self.h_cell))

            if count == 4:
                if not next_figure:
                    self.coords_blocks["4"] = [
                        x + self.w_cell,
                        y + self.h_cell,
                        "sea_wave",
                    ]
                self.screen_class.square_item(
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
            self.current_block["cells_block"] = (3, 2, 3)

            while count < 5:
                if count == 1:
                    if not next_figure:
                        self.coords_blocks["1"] = [x, y + self.h_cell, "gray"]
                    self.screen_class.square_item("gray", (x, y + self.h_cell))

                if count == 2:
                    if not next_figure:
                        self.coords_blocks["2"] = [
                            x + self.w_cell,
                            y + self.h_cell,
                            "gray",
                        ]
                    self.screen_class.square_item(
                        "gray", (x + self.w_cell, y + self.h_cell)
                    )

                if count == 3:
                    if not next_figure:
                        self.coords_blocks["3"] = [
                            x + self.w_cell * 2,
                            y + self.h_cell,
                            "gray",
                        ]
                    self.screen_class.square_item(
                        "gray",
                        (x + self.w_cell * 2, y + self.h_cell),
                    )

                if count == 4:
                    if not next_figure:
                        self.coords_blocks["4"] = [x + self.w_cell, y, "gray"]
                    self.screen_class.square_item("gray", (x + self.w_cell, y))

                count += 1

            pygame.display.update()

        else:
            self.current_block["cells_block"] = (2, 3, 3)

            while count < 5:
                if count == 1:
                    self.coords_blocks["1"] = [x + self.w_cell, y, "gray"]
                    self.screen_class.square_item("gray", (x + self.w_cell, y))
                if count == 2:
                    self.coords_blocks["2"] = [x + self.w_cell, y + self.h_cell, "gray"]
                    self.screen_class.square_item(
                        "gray", (x + self.w_cell, y + self.h_cell)
                    )
                if count == 3:
                    self.coords_blocks["3"] = [
                        x + self.w_cell,
                        y + self.h_cell * 2,
                        "gray",
                    ]
                    self.screen_class.square_item(
                        "gray",
                        (x + self.w_cell, y + self.h_cell * 2),
                    )
                if count == 4:
                    self.coords_blocks["4"] = [x, y + self.h_cell, "gray"]
                    self.screen_class.square_item("gray", (x, y + self.h_cell))

                count += 1

            pygame.display.update()

    def block_7(self, block_verticle, coord, next_figure):
        count = 1
        x = coord[0]
        y = coord[1]

        if block_verticle:
            self.current_block["cells_block"] = (3, 2, 3)

            while count < 5:
                if count == 1:
                    if not next_figure:
                        self.coords_blocks["1"] = [x, y, "green"]
                    self.screen_class.square_item("green", (x, y))
                if count == 2:
                    if not next_figure:
                        self.coords_blocks["2"] = [x + self.w_cell, y, "green"]
                    self.screen_class.square_item("green", (x + self.w_cell, y))
                if count == 3:
                    if not next_figure:
                        self.coords_blocks["3"] = [
                            x + self.w_cell,
                            y + self.h_cell,
                            "green",
                        ]
                    self.screen_class.square_item(
                        "green",
                        (x + self.w_cell, y + self.h_cell),
                    )
                if count == 4:
                    if not next_figure:
                        self.coords_blocks["4"] = [
                            x + self.w_cell * 2,
                            y + self.h_cell,
                            "green",
                        ]
                    self.screen_class.square_item(
                        "green",
                        (x + self.w_cell * 2, y + self.h_cell),
                    )

                count += 1

            pygame.display.update()

        else:
            self.current_block["cells_block"] = (2, 3, 3)

            while count < 5:
                if count == 1:
                    self.coords_blocks["1"] = [x, y, "green"]
                    self.screen_class.square_item("green", (x, y))
                if count == 2:
                    self.coords_blocks["2"] = [x, y + self.h_cell, "green"]
                    self.screen_class.square_item("green", (x, y + self.h_cell))
                if count == 3:
                    self.coords_blocks["3"] = [
                        x + self.w_cell,
                        y + self.h_cell,
                        "green",
                    ]
                    self.screen_class.square_item(
                        "green",
                        (x + self.w_cell, y + self.h_cell),
                    )
                if count == 4:
                    self.coords_blocks["4"] = [
                        x + self.w_cell,
                        y + self.h_cell * 2,
                        "green",
                    ]
                    self.screen_class.square_item(
                        "green",
                        (x + self.w_cell, y + self.h_cell * 2),
                    )

                count += 1

            pygame.display.update()

    def draw_figurs(self, num_next_block):
        # отрисовка сохраненных квадратов
        for key, value in self.figurs.items():
            for i in value:
                self.screen_class.square_item(i[2], (i[0], i[1]))

        # отрисовка следующего блока
        self.next_image(num_next_block, True)

        # отрисовка опускающегося блока

        self.create_block(
            self.current_block["position"],
            self.current_block["coord"],
            self.current_block["num"],
            False,
        )
