# https://adventofcode.com/2021/day/1

import os
import sys
from timeit import timeit


def larger_than_previous1(list_to_check: list)-> int:
    prev_num = 0
    counter = 0

    for i, j in enumerate(list_to_check):
        if i > 0 and j > prev_num:
            counter += 1
        
        prev_num = j
    
    return counter

def larger_than_previous2(list_to_check: list)-> int:

    def larger_than_previous2_helper(list_to_check, counter, prev_num, enumerator):
        if list_to_check == []:
            return counter
        else:
            current = list_to_check[0]
            if enumerator > 0 and current > prev_num:
                counter += 1
            
            larger_than_previous2_helper(list_to_check[1:], counter, current, enumerator + 1)


        for i, j in enumerate(list_to_check):
            if i > 0 and j > prev_num:
                counter += 1
            
            prev_num = j
        
        return counter

    return larger_than_previous2_helper(list_to_check, 0, 0, 0)



if __name__ == "__main__":
    sys.setrecursionlimit(1000)
    FILE1 = "test_input.txt"
    FILE2 = "assignment_input.txt"
    PATH = os.path.join(os.getcwd(), FILE2)

    with open(PATH) as f:
        contents = f.read()
        m_list = contents.split("\n")
        m_list = list(map(int, m_list))
    
    result1 = larger_than_previous1(m_list)
    duration1 = timeit(lambda: larger_than_previous1(m_list), number=1000)
    print(f"Result for method 1: {result1} with duration: {duration1}")

    try:
        result2 = larger_than_previous2(m_list)
        duration2 = timeit(lambda: larger_than_previous2(m_list), number=1000)
        print(f"Result for method 2: {result2} with duration: {duration2}")
    except RecursionError as re:
        print("Recursion error for result 2")