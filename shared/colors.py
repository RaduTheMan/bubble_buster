"""
    This module provides some predefined colors.
"""

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
BROWN = (165, 42, 42)
GRAY = (220, 220, 220)
GREEN = (0, 255, 0)
ORANGE = (255, 215, 0)
PINK = (255, 192, 203)
PURPLE = (230, 230, 250)
RED = (255, 0, 0)
YELLOW = (250, 255, 0)
WHITE = (255, 255, 255)
DEFAULT = WHITE

table = {
    'BLK': BLACK,
    'BL': BLUE,
    'BR': BROWN,
    'GRY': GRAY,
    'GR': GREEN,
    'O': ORANGE,
    'PN': PINK,
    'PR': PURPLE,
    'R': RED,
    'Y': YELLOW,
    'W': WHITE
}


def get_color_code(color):
    """

    :param color: an rgb color (tuple[int, int, int])
    :return: (string): the corresponding code of the color from the table
    """
    color_codes = list(table.keys())
    colors = list(table.values())
    color_index = colors.index(color)
    return color_codes[color_index]
