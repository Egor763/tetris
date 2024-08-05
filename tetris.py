import pygame
from screen import Screen
from blocks import Blocks


class Tetris:
    def __init__(self):
        pygame.init()

        self.screen_class = Screen()
        self.screen = self.screen_class.screen_game()
        self.screen_class.handle_state_data()

        self.blocks = Blocks(self.screen)

        self.blocks.block_1()

        pygame.display.update()

    def run_game(self):
        while True:
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # for i in range(4):
            #     self.blocks.red_block()


if __name__ == "__main__":
    ai = Tetris()
    ai.run_game()
