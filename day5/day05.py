import numpy as np

file = open('input05', "r+").readlines()
data = [i[:-1].replace(" -> ", ",") for i in file]


def point_grid(position, idx, start, stop, grid):
    if start > stop:
        start, stop = stop, start
    for i in range(start, stop + 1):
        if position:
            grid[idx][i] += 1
        else:
            grid[i][idx] += 1

    return grid


def func1():
    all_data = [''.join(i).split(",") for i in data]
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    test = {}

    all = 0
    for x_1, y_1, x_2, y_2 in [[int(y) for y in x] for x in all_data]:
        if x_1 == x_2:
            if y_1 > y_2: y_1, y_2 = y_2, y_1
            for y in range(y_1, y_2 + 1):
                coordinates = (x_1, y)
                if coordinates in test:
                    test[coordinates] += 1
                else:
                    test[coordinates] = 1

            # point_grid(True, x_1, y_1, y_2, grid)
        elif y_1 == y_2:
            if x_1 > x_2: x_1, x_2 = x_2, x_1
            for x in range(x_1, x_2 + 1):
                coordinates = (x, y_2)
                if coordinates in test:
                    test[coordinates] += 1
                else:
                    test[coordinates] = 1
            # point_grid(False, y_1, x_1, x_2, grid)
        else:
            all += 1

    counter = 0
    for value in test.values():
        if value >= 2:
            counter += 1
    print(counter, all)

    np_array = np.array(grid)
    print(np.count_nonzero(np_array >= 2))

    val = 0
    for x in grid:
        for k in x:
            if k >= 2:
                val += 1

    print(val)


def func2():
    print("Func2")


if __name__ == "__main__":
    func1()  # 4822, 6283
    # func2() # 18864
