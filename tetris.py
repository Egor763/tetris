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

        self.coords_blocks = settings.coords_blocks

        self.current_block = settings.current_block

        self.figurs = settings.figurs

        self.screen_class.handle_state_data()

        self.USEREVENT = pygame.USEREVENT
        pygame.time.set_timer(self.USEREVENT, 500)

        self.w_cell = settings.w_cell
        self.h_cell = settings.h_cell

        self.key_button = settings.key_button

        self.clock = pygame.time.Clock()

        # self.current_block["coord"][1] = 10

        # print(self.blocks.)

        # self.current_block["num"] = self.blocks.random_num()
        self.current_block["num"] = 7
        # self.current_block["is_current"] = True
        self.num_next_block = self.blocks.random_num()

        self.blocks.create_block(
            self.current_block["position"],
            self.current_block["coord"],
            self.current_block["num"],
        )

        self.blocks.next_image(self.num_next_block)

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

                    print(self.coords_blocks["block_7"])

                    self.blocks.next_image(self.num_next_block)

                    self.blocks.create_block(
                        self.current_block["position"],
                        self.current_block["coord"],
                        self.current_block["num"],
                    )

                    if (
                        self.current_block["coord"][1]
                        + self.h_cell * self.current_block["cells_block"][1]
                        < self.y_end_area
                        # and self.current_block["is_current"]
                    ):

                        self.current_block["coord"][1] = self.move_blocks.change_coord(
                            self.current_block["coord"][1]
                        )

                    elif (
                        self.current_block["coord"][1]
                        + self.h_cell * self.current_block["cells_block"][1]
                        == self.y_end_area
                        # and self.current_block["is_current"]
                        # and self.current_block["is_current"]
                    ):
                        # pygame.time.set_timer(self.USEREVENT, 0)

                        # self.current_block["is_current"] = False

                        self.current_block["coord"][1] = self.y_start_area

                        # pygame.time.set_timer(self.USEREVENT, 500)

                        self.current_block["num"] = self.num_next_block
                        self.num_next_block = self.blocks.random_num()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP5:
                        if self.current_block["position"]:
                            self.current_block["position"] = False

                        else:
                            self.current_block["position"] = True

                        self.blocks.create_block(
                            self.current_block["position"],
                            self.current_block["coord"],
                            self.current_block["num"],
                        )

                    if (
                        event.key == pygame.K_LEFT
                        and self.x_start_area < self.current_block["coord"][0]
                    ):
                        self.blocks.next_image(self.num_next_block)

                        pygame.time.set_timer(self.USEREVENT, 0)

                        self.key_button = "left"
                        self.current_block["coord"][0] -= self.w_cell
                        self.blocks.create_block(
                            self.current_block["position"],
                            self.current_block["coord"],
                            self.current_block["num"],
                        )

                    if (
                        event.key == pygame.K_RIGHT
                        and self.x_end_area
                        > self.current_block["coord"][0]
                        + self.w_cell * self.current_block["cells_block"][0]
                    ):
                        self.blocks.next_image(self.num_next_block)

                        pygame.time.set_timer(self.USEREVENT, 0)
                        self.key_button = "right"
                        self.current_block["coord"][0] += self.w_cell
                        self.blocks.create_block(
                            self.current_block["position"],
                            self.current_block["coord"],
                            self.current_block["num"],
                        )

                    if event.key == pygame.K_DOWN:
                        self.current_block["coord"][1] = (
                            self.y_end_area
                            - self.h_cell * self.current_block["cells_block"][1]
                        )

                        self.num_next_block = self.blocks.random_num()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        pygame.time.set_timer(self.USEREVENT, 500)

                        self.key_button = ""

                    if event.key == pygame.K_RIGHT:
                        pygame.time.set_timer(self.USEREVENT, 500)

                        self.key_button = ""

            # if (
            #     self.current_block["coord"][1]
            #     + self.h_cell * self.current_block["cells_block"][1]
            #     - self.h_cell
            #     == self.y_end_area
            #     # and self.current_block["is_current"]
            # ):
            #     # pygame.time.set_timer(self.USEREVENT, 0)

            #     # self.current_block["is_current"] = False

            #     self.current_block["coord"][1] = self.y_start_area

            #     # pygame.time.set_timer(self.USEREVENT, 500)

            #     self.current_block["num"] = self.num_next_block
            #     self.num_next_block = self.blocks.random_num()

            self.clock.tick(200)

            # pygame.display.update()


if __name__ == "__main__":
    ai = Tetris()
    ai.run_game()
