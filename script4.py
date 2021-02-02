import numpy as np
from functools import partial


transitions = np.array([[1, 2],
                        [2, 1],
                        [-1, 2],
                        [2, -1],
                        [1, -2],
                        [-2, 1],
                        [-1, -2],
                        [-2, -1],
                        ])


def foo(a: tuple, shape: tuple):
    return 0 <= a[0] < shape[0] and 0 <= a[1] < shape[1]


def get_all_next(coords: set, shape: tuple) -> set:
    new_coords = []
    for coord in coords:
        new_coords += list(map(tuple, transitions + coord))

    in_shape = partial(foo, shape=shape)
    new_coords = list(filter(in_shape, new_coords))
    return set(new_coords)


def inp(): return tuple(map(int, input().split()))


def indexes(a): return np.array(list(a)).T.tolist()


shape = inp()
coords = [{inp()}, {inp()}]

# board = np.zeros(shape, dtype=int)
# board[indexes(coords[0])] = 2
# board[indexes(coords[1])] = -1
# print(board)

step = 0
while(len(set.intersection(*coords)) == 0):
    # board[indexes(coords[0])] = 0
    # board[indexes(coords[1])] = 0
    coords[0] = get_all_next(coords[0], shape)
    step += 1
    coords[1] = get_all_next(coords[1], shape)
    # board[indexes(coords[0])] += 2
    # board[indexes(coords[1])] -= 1
    # print(board)
    step += 1

print(step)
