import numpy as np

file = open('input05', "r+").readlines()
data = [i[:-1].replace(" -> ", ",") for i in file]


def point_grid(position, idx, start, stop, grid):
    if start > stop:
        start, stop = stop, start

    for i in range(start, stop + 1):
        if position:
            grid[i][idx] += 1
        else:
            grid[idx][i] += 1

    return grid


def func1():
    tmp = [''.join(i).split(",") for i in data]

    x1, x2 = [], []
    y1, y2 = [], []

    for value in tmp:
        for i in range(len(value)):
            position = i % 4
            if position == 0:
                x1.append(int(value[i]))
            elif position == 1:
                y1.append(int(value[i]))
            elif position == 2:
                x2.append(int(value[i]))
            else:
                y2.append(int(value[i]))

    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for i in range(len(x1)):
        x_1, x_2 = int(x1[i]), int(x2[i])
        y_1, y_2 = int(y1[i]), int(y2[i])

        if x_1 == x_2:
            grid = point_grid(True, x_1, y_1, y_2, grid)
        elif y_1 == y_2:
            grid = point_grid(False, y_1, x_1, x_2, grid)
        else:
            continue

    np_array = np.array(grid)
    print(np.count_nonzero(np_array == 2))  # 4822, 6283


def func2():
    print("Func2")


if __name__ == "__main__":
    func1()
    # func2() # 18864
