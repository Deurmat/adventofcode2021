import os

def get_data(assignment:str, FILE:str)-> list:
    if FILE == 'FILE1':
        FILENAME = "test_input.txt"
    elif FILE == 'FILE2':
        FILENAME = "assignment_input.txt"
    PATH = os.path.join(os.getcwd(), 'src', f'ass{assignment}', FILENAME)

    with open(PATH) as f:
        contents = f.read()
        data_list = contents.split("\n")
    
    return data_list
