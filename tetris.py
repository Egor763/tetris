import pygame
import random
from screen import Screen
from blocks import Blocks
from move_blocks import MoveBlocks
import settings


class Tetris:
    def __init__(self):
        pygame.init()

        self.screen_class = Screen()
        self.screen = self.screen_class.screen_game()
        self.blocks = Blocks(self.screen_class)
        self.move_blocks = MoveBlocks()
        self.x_start_area = settings.x_start_area
        self.x_end_area = settings.x_end_area
        self.y_start_area = settings.y_start_area
        self.y_end_area = settings.y_end_area

        self.num_next_block = settings.num_next_block

        self.coords_blocks = settings.coords_blocks

        self.current_block = settings.current_block

        # self.figurs = settings.figurs

        self.screen_class.handle_state_data()

        self.USEREVENT = pygame.USEREVENT
        pygame.time.set_timer(self.USEREVENT, 500)

        self.w_cell = settings.w_cell
        self.h_cell = settings.h_cell

        self.key_button = settings.key_button

        self.clock = pygame.time.Clock()

        # self.current_block["num"] = random.randrange(1, 8)
        self.num_next_block = random.randrange(1, 8)

        self.current_block["num"] = 1

        # отрисовка квадратов
        self.blocks.draw_figurs(self.num_next_block)

        pygame.display.update()

    def run_game(self):
        while True:
            self.screen_class.screen_game()

            self.current_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # таймер
                if event.type == self.USEREVENT and not bool(self.key_button):
                    # TODO первый блок смещается на клетку вправо
                    # отрисовка квадратов
                    self.blocks.draw_figurs(self.num_next_block)

                    self.move_blocks.move_down_block(
                        self.current_block, self.coords_blocks, self.num_next_block
                    )

                if event.type == pygame.KEYDOWN:
                    # ! закрытие окна на escape
                    if event.key == pygame.K_ESCAPE:
                        exit()

                    if event.key == pygame.K_KP5:
                        if self.current_block["position"]:
                            self.current_block["position"] = False

                        else:
                            self.current_block["position"] = True

                        self.blocks.create_block(
                            self.current_block["position"],
                            self.current_block["coord"],
                            self.current_block["num"],
                            False,
                        )

                    if event.key == pygame.K_LEFT:
                        self.key_button = "left"
                        pygame.time.set_timer(self.USEREVENT, 0)
                        if (
                            self.x_start_area < self.current_block["coord"][0]
                            and self.current_block["num"] != 1
                        ):
                            self.current_block["coord"][0] -= self.w_cell
                            print("n: ", self.current_block["num"])
                            # отрисовка квадратов
                            self.blocks.draw_figurs(self.num_next_block)

                        elif (
                            self.x_start_area - self.w_cell
                            < self.current_block["coord"][0]
                            and self.current_block["num"] == 1
                            and self.current_block["position"]
                        ):
                            print("l")
                            self.current_block["coord"][0] -= self.w_cell

                            # отрисовка квадратов
                            self.blocks.draw_figurs(self.num_next_block)

                    if (
                        event.key == pygame.K_RIGHT
                        and self.x_end_area
                        > self.current_block["coord"][0]
                        + self.w_cell * self.current_block["cells_block"][0]
                    ):
                        self.key_button = "right"
                        pygame.time.set_timer(self.USEREVENT, 0)
                        self.current_block["coord"][0] += self.w_cell

                        # отрисовка квадратов
                        self.blocks.draw_figurs(self.num_next_block)

                    if event.key == pygame.K_DOWN:
                        self.current_block["coord"][1] = (
                            self.y_end_area
                            - self.h_cell * self.current_block["cells_block"][1]
                        )

                        self.num_next_block = random.randrange(1, 8)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        pygame.time.set_timer(self.USEREVENT, 500)

                        self.key_button = ""

                    if event.key == pygame.K_RIGHT:
                        pygame.time.set_timer(self.USEREVENT, 500)

                        self.key_button = ""

            self.clock.tick(200)


if __name__ == "__main__":
    ai = Tetris()
    ai.run_game()
