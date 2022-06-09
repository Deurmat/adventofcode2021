# https://adventofcode.com/2021/day/3

import os
import sys

sys.path.append(os.getcwd())

from src.modules.aoc_module import get_data

def zip_list_items(ziplist: list)->list:
    return [''.join([item[i] for item in ziplist]) for i in range(0, len(ziplist[0]))]

def generate_bin_from_occurence(occ_list: list)-> str:
    return ''.join(['1' if item.count('1')>(len(item)/2) else '0' for item in occ_list])

def flip_binary(bin_str:str)->str:
    return ''.join(['1' if i == '0' else '0' for i in bin_str])

def convert_bin_to_int(binary:str)->int:
    return int(binary, 2)



if __name__ == "__main__":
    data_list = get_data('3', 'FILE1')
    zipped_list = zip_list_items(data_list)
    gamma_bin = generate_bin_from_occurence(zipped_list)
    gamma = convert_bin_to_int(gamma_bin)
    epsilon_bin = flip_binary(gamma_bin)
    epsilon = convert_bin_to_int(epsilon_bin)

    print(f'GAMMA: {gamma}, EPSILON: {epsilon}, PRODUCT: {gamma*epsilon}')
