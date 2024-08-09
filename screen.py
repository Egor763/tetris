import pygame
import settings


class Screen:
    def __init__(self):
        self.W = settings.W
        self.H = settings.H
        self.window_size = settings.window_size
        self.score = settings.score
        self.level = settings.level
        self.blocks = settings.blocks
        self.high_score = settings.high_score
        self.gray = settings.gray

        self.white = settings.white

        self.black = (0, 0, 0)

        self.font_family = settings.font_family
        self.font_size = settings.font_size
        self.screen = pygame.display.set_mode(self.window_size)
        self.font = pygame.font.SysFont(self.font_family, self.font_size)
        self.vert_line_x_left = settings.x_start_area - 2
        self.vert_line_x_right = settings.x_end_area + 2
        self.x_start_area = settings.x_start_area
        self.y_start_area = settings.y_start_area
        self.x_end_area = settings.x_end_area
        self.y_end_area = settings.y_end_area
        self.w_cell = settings.w_cell
        self.h_cell = settings.h_cell

        pygame.display.set_caption("Тетрис")

    def screen_game(self):
        self.screen.fill(self.black)
        self.handle_state_data()
        return self.screen

    def handle_grid(self):
        color = (59, 59, 59)
        self.y = self.y_start_area
        self.x = self.x_start_area

        while self.y < self.y_end_area:
            pygame.draw.line(
                self.screen,
                color,
                (self.x_start_area, self.y),
                (self.x_end_area + 2, self.y),
                1,
            )

            self.y = self.y + self.h_cell

        while self.x < self.x_end_area + 2:
            pygame.draw.line(
                self.screen,
                color,
                (self.x, self.y_start_area),
                (self.x, self.y_end_area),
            )

            self.x = self.x + self.w_cell

    def handle_state_data(self):
        self.handle_grid()

        self.score_text = self.font.render("Счёт", True, self.gray)
        self.score_number = self.font.render(str(self.score), True, self.white)
        self.level_text = self.font.render("Уровень", True, self.gray)
        self.level_number = self.font.render(str(self.level), True, self.white)
        self.blocks_text = self.font.render("Блоков", True, self.gray)
        self.blocks_number = self.font.render(str(self.blocks), True, self.white)
        self.high_score_text = self.font.render("Лучший счёт", True, self.gray)
        self.high_score_number = self.font.render(
            str(self.high_score), True, self.white
        )
        self.next = self.font.render("Следующий", True, self.gray)

        self.screen.blit(self.score_text, [550, self.y_start_area])
        self.screen.blit(self.score_number, [575, 35])
        self.screen.blit(self.level_text, [530, 70])
        self.screen.blit(self.level_number, [575, 95])
        self.screen.blit(self.blocks_text, [535, 120])
        self.screen.blit(self.blocks_number, [575, 155])
        self.screen.blit(self.high_score_text, [495, 180])
        self.screen.blit(self.high_score_number, [575, 205])
        self.screen.blit(self.next, [495, 350])

        # левая линия игрового поля
        pygame.draw.line(
            self.screen,
            self.white,
            (self.vert_line_x_left, self.y_start_area),
            (self.vert_line_x_left, self.y_end_area),
            2,
        )
        # горизонтальная линия игрового поля
        pygame.draw.line(
            self.screen,
            self.white,
            (self.x_start_area, self.y_end_area),
            (self.x_end_area, self.y_end_area),
            2,
        )
        # правая линия игрового поля
        pygame.draw.line(
            self.screen,
            self.white,
            (self.vert_line_x_right, self.y_start_area),
            (self.vert_line_x_right, self.y_end_area),
            2,
        )
