import pygame

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

        self.border_width = 1

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

    def block_1(self):
        red = (255, 0, 0)
        light_line = (151, 151, 255)
        dark_line = (0, 0, 130)

        count = 1

        x = 450
        y = 500

        while count < 5:
            self._square_item(red, light_line, dark_line, (x, y))

            y += self.h_cell

            count += 1

    def block_2(self):
        blue = (0, 0, 255)
        light_line = (255, 142, 142)
        dark_line = (119, 0, 0)
        count = 1

        x = 450
        y = 500

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
                self._square_item(blue, light_line, dark_line, (x + self.w_cell * 2, y))

            count += 1

    def block_3(self):
        yellow = (255, 255, 0)
        light_line = (255, 237, 157)
        dark_line = (110, 96, 32)
        count = 1

        x = 450
        y = 500

        while count < 5:
            if count != 4:
                self._square_item(yellow, light_line, dark_line, (x, y))

                y += self.h_cell

            else:
                self._square_item(
                    yellow, light_line, dark_line, (x + self.w_cell, y - self.h_cell)
                )

            count += 1

    def block_4(self):
        pink = (175, 0, 175)
        light_line = (255, 0, 255)
        dark_line = (95, 0, 95)

        count = 1

        x = 450
        y = 500

        while count < 5:
            if count != 4:
                self._square_item(pink, light_line, dark_line, (x, y))

                y += self.h_cell

            else:
                self._square_item(
                    pink, light_line, dark_line, (x - self.w_cell, y - self.h_cell)
                )

            count += 1

    # квадрат
    def block_5(self):
        sea_wave = (53, 153, 252)
        light_line = (169, 212, 255)
        dark_line = (59, 86, 113)
        count = 1

        x = 450
        y = 500

        while count < 5:
            if count == 1:
                self._square_item(sea_wave, light_line, dark_line, (x, y))

            if count == 2:
                self._square_item(sea_wave, light_line, dark_line, (x + self.w_cell, y))

            if count == 3:
                self._square_item(sea_wave, light_line, dark_line, (x, y + self.h_cell))

            if count == 4:
                self._square_item(
                    sea_wave, light_line, dark_line, (x + self.w_cell, y + self.h_cell)
                )

            count += 1

    def block_6(self):
        gray = (164, 171, 187)
        light_gray = (255, 255, 255)
        dark_gray = (132, 132, 132)
        count = 1

        x = 80
        y = 10

        while count < 5:
            if count == 1:
                self._square_item(gray, light_gray, dark_gray, (x, y + self.h_cell))

            if count == 2:
                self._square_item(
                    gray, light_gray, dark_gray, (x + self.w_cell, y + self.h_cell)
                )

            if count == 3:
                self._square_item(
                    gray, light_gray, dark_gray, (x + self.w_cell * 2, y + self.h_cell)
                )

            if count == 4:
                self._square_item(gray, light_gray, dark_gray, (x + self.w_cell, y))

            count += 1
