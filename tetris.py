import pygame
from screen import Screen
from blocks import Blocks
from move_blocks import MoveBlocks


class Tetris:
    def __init__(self):
        pygame.init()

        self.screen_class = Screen()
        self.screen = self.screen_class.screen_game()
        self.blocks = Blocks(self.screen)
        self.move_blocks = MoveBlocks()

        self.screen_class.handle_state_data()

        pygame.time.set_timer(pygame.USEREVENT, 1000)

        self.block_verticle = True

        self.y_block = 10

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
                    self.y_block = self.move_blocks.change_coord(self.y_block)
                    self.blocks.block_2(self.block_verticle, self.y_block)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP5:
                        if self.block_verticle:
                            self.block_verticle = False

                        else:
                            self.block_verticle = True

                        self.blocks.block_2(self.block_verticle)

            # pygame.display.update()


if __name__ == "__main__":
    ai = Tetris()
    ai.run_game()
