import sys

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
    moves = []
    if start in range(16, 64):
        if start not in range(0, 64, 8):
            up_left = start - (8*2) - 1
            moves.append(up_left)
        if start not in range(7, 64, 8):
            up_right = start - (8*2) + 1
            moves.append(up_right)

    if start not in range(6, 64, 8) + range(7, 64, 8):
        if start not in range(0, 8):
            right_up = start + 2 - 8
            moves.append(right_up)
        if start not in range(56, 64):
            right_down = start + 2 + 8
            moves.append(right_down)

    if start in range(0, 48):
        if start not in range(7, 64, 8):
            down_right = start + (8*2) + 1
            moves.append(down_right)
        if start not in range(0, 64, 8):
            down_left = start + (8*2) - 1
            moves.append(down_left)

    if start not in range(0, 64, 8) + range(1, 64, 8):
        if start not in range(56, 64):
            left_down = start - 2 + 8
            moves.append(left_down)
        if start not in range(0, 8):
            left_up = start - 2 - 8
            moves.append(left_up)

    return moves
