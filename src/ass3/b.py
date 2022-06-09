# https://adventofcode.com/2021/day/3

import os
import sys

sys.path.append(os.getcwd())

from src.modules.aoc_module import get_data
from src.ass3.a import zip_list_items, convert_bin_to_int


def get_ox_rating(data_list: list)->str:
    
    def get_ox_rating_helper(data_list: list, cycle: int):
        if len(data_list) == 1:
            return data_list[0]
        transposed_row = zip_list_items(data_list)[cycle]
        most_occ = '1' if transposed_row.count('1')>=(len(transposed_row)/2) else '0'
        result_list = []
        for i, j in enumerate(transposed_row):
            if j == most_occ:
                result_list.append(data_list[i])

        return get_ox_rating_helper(result_list, cycle + 1)

    return get_ox_rating_helper(data_list, 0)

#lazy copy
def get_scrub_rating(data_list: list)->str:
    
    def get_ox_rating_helper(data_list: list, cycle: int):
        if len(data_list) == 1:
            return data_list[0]
        transposed_row = zip_list_items(data_list)[cycle]
        least_occ = '0' if transposed_row.count('0')<=(len(transposed_row)/2) else '1'
        result_list = []
        for i, j in enumerate(transposed_row):
            if j == least_occ:
                result_list.append(data_list[i])

        return get_ox_rating_helper(result_list, cycle + 1)

    return get_ox_rating_helper(data_list, 0)








if __name__ == "__main__":
    data_list = get_data('3', 'FILE2')
    ox_rating = get_ox_rating(data_list)
    scrub_rating = get_scrub_rating(data_list)
    print(f'OX_RATING: {ox_rating}, SCRUB_RATING: {scrub_rating} with PRODUCT {convert_bin_to_int(ox_rating)*convert_bin_to_int(scrub_rating)}')

