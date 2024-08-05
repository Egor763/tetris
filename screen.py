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

        self.font_family = settings.font_family
        self.font_size = settings.font_size
        self.screen = pygame.display.set_mode(self.window_size)
        self.font = pygame.font.SysFont(self.font_family, self.font_size)
        self.vert_line_x_left = 48
        self.vert_line_x_right = 352
        self.horiz_line_y = 610
        self.w_cell = 30
        self.h_cell = 30

        pygame.display.set_caption("Тетрис")

    def screen_game(self):
        return self.screen

    def handle_grid(self):
        color = (59, 59, 59)
        self.y = 10
        self.x = 50

        while self.y < 610:
            pygame.draw.line(self.screen, color, (50, self.y), (352, self.y), 1)

            self.y = self.y + 30

        while self.x < 352:
            pygame.draw.line(self.screen, color, (self.x, 10), (self.x, 610))

            self.x = self.x + 30

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

        self.screen.blit(self.score_text, [550, 10])
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
            (self.vert_line_x_left, 10),
            (self.vert_line_x_left, 610),
            2,
        )
        # горизонтальная линия игрового поля
        pygame.draw.line(
            self.screen,
            self.white,
            (50, self.horiz_line_y),
            (350, self.horiz_line_y),
            2,
        )
        # правая линия игрового поля
        pygame.draw.line(
            self.screen,
            self.white,
            (self.vert_line_x_right, 10),
            (self.vert_line_x_right, 610),
            2,
        )
