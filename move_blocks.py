import settings
import random
import pygame


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

    def add_figure(self):
        if len(self.coords_blocks) > 0:
            for coord in self.coords_blocks.values():
                for key, value in self.figurs.items():
                    if key == str(coord[0]):
                        value.append(coord)

                # self.figurs.append(coord)
                print("coord: ", coord[0])

        self.current_block["coord"][1] = self.y_start_area

        self.current_block["num"] = self.num_next_block
        self.num_next_block = random.randrange(1, 8)

    def move_down_block(self, current_block, coords_blocks, num_next_block):
        self.current_block = current_block
        self.coords_blocks = coords_blocks
        self.num_next_block = num_next_block

        for val in self.coords_blocks.values():
            for key, value in self.figurs.items():
                if str(val[0]) == key:
                    if len(value) > 0:
                        for item in value:
                            if val[1] == item[1]:
                                print("g")
                                # self.add_figure()

        if (
            self.current_block["coord"][1]
            + self.h_cell * self.current_block["cells_block"][1]
            < self.y_end_area
        ):
            # print(self.coords_blocks)
            # print(self.figurs)
            # for value in self.coords_blocks.values():
            #     print(value)

            self.current_block["coord"][1] = self.change_coord(
                self.current_block["coord"][1]
            )

        elif (
            self.current_block["coord"][1]
            + self.h_cell * self.current_block["cells_block"][1]
            == self.y_end_area
        ):
            self.add_figure()

            # if len(self.coords_blocks) > 0:
            #     for coord in self.coords_blocks.values():
            #         for key, value in self.figurs.items():
            #             if key == str(coord[0]):
            #                 value.append(coord)

            #         # self.figurs.append(coord)
            #         print("coord: ", coord[0])

            # self.current_block["coord"][1] = self.y_start_area

            # self.current_block["num"] = self.num_next_block
            # self.num_next_block = random.randrange(1, 8)
