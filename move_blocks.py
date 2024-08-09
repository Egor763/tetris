import settings


class MoveBlocks:
    def __init__(self):
        self.x_start_area = settings.x_start_area
        self.y_start_area = settings.y_start_area
        self.x_end_area = settings.x_end_area
        self.y_end_area = settings.y_end_area
        self.w_cell = settings.w_cell
        self.h_cell = settings.h_cell

    def change_coord(self, initial_coord):
        y = initial_coord + self.h_cell

        return y

    # def change_coord_x_left(self, coord):
    #     print("m")
    #     x = coord - self.w_cell

    #     return x

    # def change_coord_x_right(self, coord):
    #     print("l")
    #     x = coord + self.w_cell

    #     return x
