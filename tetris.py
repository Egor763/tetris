import pygame
from screen import Screen
from blocks import Blocks


class Tetris:
    def __init__(self):
        pygame.init()

        self.screen_class = Screen()
        self.screen = self.screen_class.screen_game()
        self.screen_class.handle_state_data()

        self.block_verticle = True

        self.blocks = Blocks(self.screen)

        # self.blocks.block_2(self.block_verticle)

        pygame.display.update()

    def run_game(self):
        while True:
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP5:
                        if self.block_verticle:
                            self.block_verticle = False

                        else:
                            self.block_verticle = True

                        self.blocks.block_1(self.block_verticle)

            # pygame.display.update()


if __name__ == "__main__":
    ai = Tetris()
    ai.run_game()
