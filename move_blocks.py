import settings
import random


class MoveBlocks:
    def __init__(self):
        self.x_start_area = settings.x_start_area
        self.y_start_area = settings.y_start_area
        self.x_end_area = settings.x_end_area
        self.y_end_area = settings.y_end_area
        self.w_cell = settings.w_cell
        self.h_cell = settings.h_cell
        self.current_block = settings.current_block
        self.coords_blocks = settings.coords_blocks
        self.num_next_block = settings.num_next_block
        self.figurs = settings.figurs

    def change_coord(self, initial_coord):
        y = initial_coord + self.h_cell

        return y

    def move_down_block(self, current_block, coords_blocks, num_next_block):
        self.current_block = current_block
        self.coords_blocks = coords_blocks
        self.num_next_block = num_next_block

        if (
            self.current_block["coord"][1]
            + self.h_cell * self.current_block["cells_block"][1]
            < self.y_end_area
        ):

            self.current_block["coord"][1] = self.change_coord(
                self.current_block["coord"][1]
            )

        elif (
            self.current_block["coord"][1]
            + self.h_cell * self.current_block["cells_block"][1]
            == self.y_end_area
        ):

            if len(self.coords_blocks) > 0:
                for key, coord in self.coords_blocks.items():
                    color = key[1:]

                    coord.append(color)

                    self.figurs.append(coord)

            self.current_block["coord"][1] = self.y_start_area

            self.current_block["num"] = self.num_next_block
            self.num_next_block = random.randrange(1, 8)
