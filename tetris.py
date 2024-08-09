import pygame
from screen import Screen
from blocks import Blocks
from move_blocks import MoveBlocks
import settings


class Tetris:
    def __init__(self):
        pygame.init()

        self.screen_class = Screen()
        self.screen = self.screen_class.screen_game()
        self.blocks = Blocks(self.screen)
        self.move_blocks = MoveBlocks()
        self.x_start_area = settings.x_start_area
        self.x_end_area = settings.x_end_area
        self.y_start_area = settings.y_start_area
        self.y_end_area = settings.y_end_area

        self.num_next_block = settings.num_next_block

        self.current_block = settings.current_block

        self.screen_class.handle_state_data()

        self.USEREVENT = pygame.USEREVENT
        pygame.time.set_timer(self.USEREVENT, 500)

        self.w_cell = settings.w_cell
        self.h_cell = settings.h_cell

        self.key_button = settings.key_button

        # self.current_block["coord"][1] = 10

        self.blocks.random_num(False)
        self.blocks.random_num(True)

        self.blocks.create_block(
            self.current_block["position"], self.current_block["coord"]
        )

        pygame.display.update()

    def run_game(self):
        while True:
            self.screen_class.screen_game()
            # self.screen_class.handle_state_data()

            self.current_time = pygame.time.get_ticks()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # таймер
                if event.type == self.USEREVENT and not bool(self.key_button):
                    # print(self.current_block["cells_block"])
                    # self.blocks.random_block(self.current_block["position"], self.current_block["coord"][1])
                    self.blocks.create_block(
                        self.current_block["position"], self.current_block["coord"]
                    )
                    # TODO доделать (четыре количества клеток фигуры по вертикали)
                    if (
                        self.current_block["coord"][1] + self.h_cell * 4
                        < self.y_end_area
                    ):

                        self.current_block["coord"][1] = self.move_blocks.change_coord(
                            self.current_block["coord"][1]
                        )

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP5:
                        if self.current_block["position"]:
                            self.current_block["position"] = False

                        else:
                            self.current_block["position"] = True

                        self.blocks.create_block(
                            self.current_block["position"],
                            self.current_block["coord"],
                        )

                    if (
                        event.key == pygame.K_LEFT
                        and self.x_start_area < self.current_block["coord"][0]
                    ):
                        pygame.time.set_timer(self.USEREVENT, 0)

                        self.key_button = "left"
                        self.current_block["coord"][0] -= self.w_cell
                        self.blocks.create_block(
                            self.current_block["position"],
                            self.current_block["coord"],
                        )

                    if (
                        event.key == pygame.K_RIGHT
                        and self.x_end_area
                        > self.current_block["coord"][0]
                        + self.w_cell * self.current_block["cells_block"][0]
                    ):
                        pygame.time.set_timer(self.USEREVENT, 0)
                        self.key_button = "right"
                        self.current_block["coord"][0] += self.w_cell
                        self.blocks.create_block(
                            self.current_block["position"],
                            self.current_block["coord"],
                        )

                    if event.key == pygame.K_DOWN:
                        self.current_block["coord"][1] = (
                            self.y_end_area
                            - self.h_cell * self.current_block["cells_block"][1]
                        )

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        pygame.time.set_timer(self.USEREVENT, 500)

                        self.key_button = ""

                    if event.key == pygame.K_RIGHT:
                        pygame.time.set_timer(self.USEREVENT, 500)

                        self.key_button = ""

            # pygame.display.update()


if __name__ == "__main__":
    ai = Tetris()
    ai.run_game()
