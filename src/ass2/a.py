from typing import Tuple
import os
import sys

sys.path.append(os.getcwd())

from src.modules.aoc_module import get_data

def convert_navigation_list(nav_list:list)->list:
    def interpret_navigation(action:str)->Tuple[str, int]:
        result = action.split(" ")
        return result[0], int(result[1])

    result_list = []

    for item in nav_list:
        result_list.append(interpret_navigation(item))
    
    return result_list

def navigate(nav_list: list, start_depth:int, start_horizontal: int)->Tuple[int, int]:

    depth_position = start_depth
    horizontal_position = start_horizontal

    for item in nav_list:

        if item[0] == 'forward':
            horizontal_position += item[1]
        elif item[0] == 'down':
            depth_position += item[1]
        else:
            depth_position -= item[1]

    return depth_position, horizontal_position

if __name__ == "__main__":
    data_list = get_data('2', 'FILE2')

    START_DEPTH = 0
    START_HORIZONTAL = 0

    conv_nav_list = convert_navigation_list(data_list)

    depth, horizontal = navigate(conv_nav_list, START_DEPTH, START_HORIZONTAL)
    print(f'DEPTH: {depth}, HORIZONTAL: {horizontal} -> PRODUCT: {depth*horizontal}')