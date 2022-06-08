import os
import sys
from timeit import timeit

sys.path.append(os.getcwd())

from src.modules.aoc_module import get_data
from src.ass1.a import larger_than_previous1


def three_sliding_window(m_list: list)-> list:
    return_list = []
    for i, num in enumerate(m_list):
        if i < 2:
            continue
        
        return_list.append(num + m_list[i-1] + m_list[i-2])
    
    return return_list


if __name__ == "__main__":
    m_list = get_data('1', 'FILE2')
    m_list = list(map(int, m_list))
    
    prep_list = three_sliding_window(m_list)

    result1 = larger_than_previous1(prep_list)
    duration1 = timeit(lambda: larger_than_previous1(m_list), number=1000)
    print(f"Result for method 1: {result1} with duration: {duration1}")
