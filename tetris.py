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
        self.y_end_area = settings.y_end_area

        self.current_block = settings.current_block

        self.screen_class.handle_state_data()

        pygame.time.set_timer(pygame.USEREVENT, 500)

        self.w_cell = settings.w_cell
        self.h_cell = settings.h_cell

        # self.current_block["coord"][1] = 10

        self.blocks.random_num()

        self.blocks.create_block(
            self.current_block["position"], self.current_block["coord"]
        )

        pygame.display.update()

    def run_game(self):
        while True:
            self.screen_class.screen_game()
            self.screen_class.handle_state_data()

            self.current_time = pygame.time.get_ticks()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # таймер
                if event.type == pygame.USEREVENT:
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

            # pygame.display.update()


if __name__ == "__main__":
    ai = Tetris()
    ai.run_game()
