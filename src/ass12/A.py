import pprint

FILE_PATH = r'D:\Nextcloud\Hobbies\Coding\Advent of Code\2021\12\input.txt'
OUTPUT_PATH = r'D:\Nextcloud\Hobbies\Coding\Advent of Code\2021\12\output.txt'

class Cave():
    def __init__(self, name, size):
        self._name = name
        self._size = size
        self._connections = []
    
    def __eq__(self, other):
        if (isinstance(other, str)):
            return self._name == other
        return False
    
    def __repr__(self):
        return self._name

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return self._size
    
    @property
    def connections(self):
        return self._connections.copy()

    def add_to_connections(self, new_value):
        self._connections.append(new_value)

def read_caves_from_file(file_path) -> list:
    caves_list = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            cave1 = line.split('-')[0].strip()
            cave2 = line.split('-')[1].strip()

            # Setup new cave
            if cave1 not in caves_list:

                size = 's' if cave1.islower() else 'l'
                cave = Cave(name=cave1, size=size)
                cave.add_to_connections(cave2)
                caves_list.append(cave)
            else:
                cave = [cave for cave in caves_list if cave1 == cave][0]
                if cave2 not in cave.connections:
                    cave.add_to_connections(cave2)
            
            # Setup connection to other side
            if cave2 not in caves_list:
                size = 's' if cave2.islower() else 'l'
                cave = Cave(name=cave2, size=size)
                cave.add_to_connections(cave1)
                caves_list.append(cave)
            else:
                cave = [cave for cave in caves_list if cave2 == cave][0]
                if cave1 not in cave.connections:
                    cave.add_to_connections(cave1)

    return caves_list

def generate_paths(start_cave: Cave, caves_list: list) -> list:
    cave_connections = [[start_cave]]

    while True:
        paths = []
        for cave_connection in cave_connections:
            if cave_connection[-1] == 'end':
                result = cave_connection.copy()
                paths.append(result)
                continue

            if len(cave_connection) > 50:
                continue

            for connection in cave_connection[-1].connections:

                connection_cave = [cave for cave in caves_list if cave.name == connection][0]

                if connection_cave.size == 's' and connection_cave in cave_connection:
                    continue

                result = cave_connection.copy()
                result.append(connection_cave)
                paths.append(result)
        
        if len(paths) == len(cave_connections):
            break

        cave_connections = paths
    
    return cave_connections

if __name__ == '__main__':
    caves = read_caves_from_file(FILE_PATH)
    start_cave = [cave for cave in caves if cave.name == 'start'][0]
    end_cave = [cave for cave in caves if cave.name == 'end'][0]

    for cave in caves:
        cave: Cave
        print(f'Cave {cave.name} found with connections to {cave.connections}')

    paths = generate_paths(start_cave, caves)
    print('-------------------------------------------------')
    print(f'Number of different unique routes are: {len(paths)}')
    #pprint.pprint(paths)
    with open(OUTPUT_PATH, 'w') as f:
        for item in paths:
            caves = [cave.name for cave in item]
            f.write('-'.join(caves))
            f.write('\n')
