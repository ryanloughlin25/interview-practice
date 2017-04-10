import sys

move_transforms = [
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
    (1, 2),
    (-1, 2),
    (1, -2),
    (-1, -2),
]

def find_path_length(src, dest):
    explored, visible, unexplored = initialize_graph(src)
    while dest not in explored:
        start = min(visible, key=visible.get)
        start_value = visible[start]
        visible.pop(start)
        moves = find_moves(start)
        for move in moves:
            if move in visible:
                visible[move] = min(visible[move], start_value + 1)
            elif move in unexplored:
                unexplored.pop(move)
                visible[move] = start_value + 1
        explored[start]=start_value
    return explored[dest]

def initialize_graph(src):
    explored = {
        src: 0,
    }

    visible_nodes = find_moves(src)
    visible = {}
    for node in visible_nodes:
        visible[node] = 1

    unexplored = {}
    for val in range(0, 64):
        if val not in explored and val not in visible:
            unexplored[val] = sys.maxint

    return explored, visible, unexplored

def find_moves(start):
    coords_list = []
    coords = square_to_coords(start)
    for transform in move_transforms:
        new_coords = [sum(nums) for nums in zip(coords, transform)]
        coords_list.append(new_coords)
    moves = [coords_to_square(loc) for loc in coords_list if is_valid(loc)]
    return moves

def is_valid(coords):
    return all(map(in_bounds, coords))

def in_bounds(num):
    return num < 8 and num >= 0

def square_to_coords(position):
    column = position % 8
    row = position / 8
    coords = (column, row)
    return coords

def coords_to_square(coords):
    square = (coords[1] - 1) * 8 + coords[0]
    return square
