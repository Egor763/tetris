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

        self.x_next_block = settings.x_next_block
        self.y_next_block = settings.y_next_block

        self.current_block = settings.current_block

        self.key_button = settings.key_button

        self.border_width = 1

    def random_num(self, next_num):
        if next_num:
            self.num_next_block = random.randrange(1, 8)

        else:
            self.current_block["num"] = random.randrange(1, 8)

        self.next_image()

    def create_block(self, block_verticle, coord):

        if self.current_block["num"] == 1:
            self.block_1(block_verticle, coord)

        if self.current_block["num"] == 2:
            self.block_2(block_verticle, coord)

        if self.current_block["num"] == 3:
            self.block_3(block_verticle, coord)

        if self.current_block["num"] == 4:
            self.block_4(block_verticle, coord)

        if self.current_block["num"] == 5:
            self.block_5(block_verticle, coord)

        if self.current_block["num"] == 6:
            self.block_6(block_verticle, coord)

        if self.current_block["num"] == 7:
            self.block_7(block_verticle, coord)

    def next_image(self):
        next_block = random.randrange(1, 8)

        if self.key_button:
            block = self.create_block(True, (self.x_next_block, self.y_next_block))

        print(next_block)

        # self.screen.blit(next_block, (self.x_next_block, self.y_next_block))

    def _square_item(self, color, color_light, color_dark, coord):
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

    def block_1(self, block_verticle, coord):
        red = (255, 0, 0)
        light_line = (151, 151, 255)
        dark_line = (0, 0, 130)

        count = 1

        x = coord[0]
        y = coord[1]

        if block_verticle:
            self.current_block["cells_block"] = (1, 4)
            while count < 5:
                self._square_item(red, light_line, dark_line, (x + self.w_cell, y))
                y += self.h_cell

                pygame.display.update()

                count += 1

        else:
            self.current_block["cells_block"] = (4, 1)

            while count < 5:

                self._square_item(red, light_line, dark_line, (x, y))
                x += self.w_cell

                pygame.display.update()

                count += 1

    def block_2(self, block_verticle, coord):
        blue = (0, 0, 255)
        light_line = (255, 142, 142)
        dark_line = (119, 0, 0)
        count = 1

        x = coord[0]
        y = coord[1]

        if block_verticle:
            self.current_block["cells_block"] = (3, 2)

            while count < 5:
                if count == 1:

                    self._square_item(blue, light_line, dark_line, (x, y + self.h_cell))
                if count == 2:
                    self._square_item(
                        blue, light_line, dark_line, (x + self.w_cell, y + self.h_cell)
                    )
                if count == 3:
                    self._square_item(blue, light_line, dark_line, (x + self.w_cell, y))

                if count == 4:
                    self._square_item(
                        blue, light_line, dark_line, (x + self.w_cell * 2, y)
                    )
                pygame.display.update()
                count += 1

        else:
            self.current_block["cells_block"] = (2, 3)

            while count < 5:
                if count == 1:
                    self._square_item(blue, light_line, dark_line, (x, y))
                if count == 2:
                    self._square_item(blue, light_line, dark_line, (x, y + self.h_cell))
                if count == 3:
                    self._square_item(
                        blue,
                        light_line,
                        dark_line,
                        (x + self.w_cell, y + self.h_cell),
                    )
                if count == 4:
                    self._square_item(
                        blue,
                        light_line,
                        dark_line,
                        (x + self.w_cell, y + self.h_cell * 2),
                    )
                pygame.display.update()

                count += 1

    def block_3(self, block_verticle, coord):
        yellow = (255, 255, 0)
        light_line = (255, 237, 157)
        dark_line = (110, 96, 32)
        count = 1

        x = coord[0]
        y = coord[1]

        if block_verticle:
            self.current_block["cells_block"] = (2, 3)

            while count < 5:
                if count != 4:
                    self._square_item(yellow, light_line, dark_line, (x, y))

                    y += self.h_cell

                else:
                    self._square_item(
                        yellow,
                        light_line,
                        dark_line,
                        (x + self.w_cell, y - self.h_cell),
                    )
                pygame.display.update()

                count += 1

        else:
            self.current_block["cells_block"] = (3, 2)

            while count < 5:
                if count != 4:
                    self._square_item(
                        yellow, light_line, dark_line, (x, y + self.h_cell)
                    )

                    x += self.w_cell

                else:
                    self._square_item(
                        yellow,
                        light_line,
                        dark_line,
                        (x - self.w_cell, y),
                    )
                pygame.display.update()

                count += 1

    def block_4(self, block_verticle, coord):
        pink = (175, 0, 175)
        light_line = (255, 0, 255)
        dark_line = (95, 0, 95)

        count = 1

        x = coord[0]
        y = coord[1]

        if block_verticle:
            self.current_block["cells_block"] = (2, 3)

            while count < 5:
                if count != 4:
                    self._square_item(pink, light_line, dark_line, (x + self.w_cell, y))

                    y += self.h_cell

                else:
                    self._square_item(pink, light_line, dark_line, (x, y - self.h_cell))

                pygame.display.update()

                count += 1

        else:
            self.current_block["cells_block"] = (3, 2)

            while count < 5:
                if count != 4:
                    self._square_item(pink, light_line, dark_line, (x, y))
                    x += self.w_cell
                else:
                    self._square_item(
                        pink, light_line, dark_line, (x - self.w_cell, y + self.h_cell)
                    )

                pygame.display.update()

                count += 1

    # квадрат
    def block_5(self, block_verticle, coord):
        sea_wave = (53, 153, 252)
        light_line = (169, 212, 255)
        dark_line = (59, 86, 113)
        count = 1

        self.current_block["cells_block"] = (2, 2)

        x = coord[0]
        y = coord[1]

        # if block_verticle:

        while count < 5:
            if count == 1:
                self._square_item(sea_wave, light_line, dark_line, (x, y))

            if count == 2:
                self._square_item(sea_wave, light_line, dark_line, (x + self.w_cell, y))

            if count == 3:
                self._square_item(sea_wave, light_line, dark_line, (x, y + self.h_cell))

            if count == 4:
                self._square_item(
                    sea_wave,
                    light_line,
                    dark_line,
                    (x + self.w_cell, y + self.h_cell),
                )

            pygame.display.update()

            count += 1

        # else:
        #     while count < 5:

        #         if count == 1:
        #             self._square_item(sea_wave, light_line, dark_line, (x, y))

        #         if count == 2:
        #             self._square_item(
        #                 sea_wave, light_line, dark_line, (x, y + self.h_cell)
        #             )

        #         if count == 3:
        #             self._square_item(
        #                 sea_wave, light_line, dark_line, (x + self.w_cell, y)
        #             )

        #         if count == 4:
        #             self._square_item(
        #                 sea_wave,
        #                 light_line,
        #                 dark_line,
        #                 (x + self.w_cell, y + self.h_cell),
        #             )

        #         pygame.display.update()

        #         count += 1

    def block_6(self, block_verticle, coord):
        gray = (164, 171, 187)
        light_gray = (255, 255, 255)
        dark_gray = (132, 132, 132)
        count = 1

        x = coord[0]
        y = coord[1]

        if block_verticle:
            self.current_block["cells_block"] = (3, 2)

            while count < 5:
                if count == 1:
                    self._square_item(gray, light_gray, dark_gray, (x, y + self.h_cell))

                if count == 2:
                    self._square_item(
                        gray, light_gray, dark_gray, (x + self.w_cell, y + self.h_cell)
                    )

                if count == 3:
                    self._square_item(
                        gray,
                        light_gray,
                        dark_gray,
                        (x + self.w_cell * 2, y + self.h_cell),
                    )

                if count == 4:
                    self._square_item(gray, light_gray, dark_gray, (x + self.w_cell, y))

                pygame.display.update()
                count += 1

        else:
            self.current_block["cells_block"] = (2, 3)

            while count < 5:
                if count == 1:
                    self._square_item(gray, light_gray, dark_gray, (x + self.w_cell, y))
                if count == 2:
                    self._square_item(
                        gray, light_gray, dark_gray, (x + self.w_cell, y + self.h_cell)
                    )
                if count == 3:
                    self._square_item(
                        gray,
                        light_gray,
                        dark_gray,
                        (x + self.w_cell, y + self.h_cell * 2),
                    )
                if count == 4:
                    self._square_item(gray, light_gray, dark_gray, (x, y + self.h_cell))

                pygame.display.update()

                count += 1

    def block_7(self, block_verticle, coord):
        green = (0, 175, 0)
        light_line = (125, 255, 125)
        dark_line = (0, 92, 0)
        count = 1
        x = coord[0]
        y = coord[1]

        if block_verticle:
            self.current_block["cells_block"] = (3, 2)

            while count < 5:
                if count == 1:
                    self._square_item(green, light_line, dark_line, (x, y))
                if count == 2:
                    self._square_item(
                        green, light_line, dark_line, (x + self.w_cell, y)
                    )
                if count == 3:
                    self._square_item(
                        green, light_line, dark_line, (x + self.w_cell, y + self.h_cell)
                    )
                if count == 4:
                    self._square_item(
                        green,
                        light_line,
                        dark_line,
                        (x + self.w_cell * 2, y + self.h_cell),
                    )

                pygame.display.update()

                count += 1

        else:
            self.current_block["cells_block"] = (2, 3)

            while count < 5:
                if count == 1:
                    self._square_item(green, light_line, dark_line, (x, y))
                if count == 2:
                    self._square_item(
                        green, light_line, dark_line, (x, y + self.h_cell)
                    )
                if count == 3:
                    self._square_item(
                        green, light_line, dark_line, (x + self.w_cell, y + self.h_cell)
                    )
                if count == 4:
                    self._square_item(
                        green,
                        light_line,
                        dark_line,
                        (x + self.w_cell, y + self.h_cell * 2),
                    )

                pygame.display.update()

                count += 1
