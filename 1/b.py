from a import larger_than_previous1, larger_than_previous2

import os
from timeit import timeit

def three_sliding_window(m_list: list)-> list:
    return_list = []
    for i, num in enumerate(m_list):
        if i < 2:
            continue
        
        return_list.append(num + m_list[i-1] + m_list[i-2])
    
    return return_list


if __name__ == "__main__":
    FILE1 = "test_input.txt"
    FILE2 = "assignment_input.txt"
    PATH = os.path.join(os.getcwd(), FILE1)

    with open(PATH) as f:
        contents = f.read()
        m_list = contents.split("\n")
        m_list = list(map(int, m_list))
    
    prep_list = three_sliding_window(m_list)

    result1 = larger_than_previous1(prep_list)
    duration1 = timeit(lambda: larger_than_previous1(m_list), number=1000)
    print(f"Result for method 1: {result1} with duration: {duration1}")
