from typing import Tuple
import os
import sys

sys.path.append(os.getcwd())

from src.modules.aoc_module import get_data
from src.ass2.a import convert_navigation_list

def navigate(nav_list: list, start_depth:int, start_horizontal: int, start_aim: int)->Tuple[int, int, int]:
    depth_position = start_depth
    horizontal_position = start_horizontal
    aim = start_aim

    def down(units, depth_position, horizontal_position, aim):
        aim += units

        return depth_position, horizontal_position, aim

    def up(units, depth_position, horizontal_position, aim):
        aim -= units

        return depth_position, horizontal_position, aim

    def forward(units, depth_position, horizontal_position, aim):
        horizontal_position += units
        depth_position += (aim*units)

        return depth_position, horizontal_position, aim

    for item in nav_list:
        depth_position, horizontal_position, aim = locals()[item[0]](item[1], depth_position, horizontal_position, aim)
            
    return depth_position, horizontal_position, aim

if __name__ == "__main__":
    data_list = get_data('2', 'FILE2')

    START_DEPTH = 0
    START_HORIZONTAL = 0
    START_AIM = 0

    conv_nav_list = convert_navigation_list(data_list)

    depth, horizontal, aim = navigate(conv_nav_list, START_DEPTH, START_HORIZONTAL, START_AIM)
    print(f'DEPTH: {depth}, HORIZONTAL: {horizontal}, AIM: {aim} -> PRODUCT: {depth*horizontal}')