import numpy as np

file = open('input04', "r+").readlines()
data = [i[:-1] for i in file]


def get_grid(values):
    grid = [[]]
    tmp = []
    sum_of_one_grid = []
    for value in values:
        if value == '':
            grid.append(tmp)
            sum_of_one_grid.append(sum(sum(tmp, [])))
            tmp = []
        else:
            tmp.append(list(map(int, value.split())))

    sum_of_one_grid.append(sum(sum(tmp, [])))
    grid.append(tmp)

    return grid[1:], sum_of_one_grid


def is_win(choices_grid):
    sum_column = [sum(x) for x in zip(*choices_grid)]

    for i in range(len(choices_grid)):
        if sum(choices_grid[i]) == 5:
            return True

        if 5 in sum_column:
            return True

    return False


def func1():
    choices = data.pop(0)
    choices = list(map(int, choices.split(",")))
    values = data[1:]

    grids, sum_of_grids = get_grid(values)
    choices_grid = [[[0 for col in range(5)] for row in range(5)] for val in range(100)]
    for choice in choices:
        for i in range(len(grids)):
            for j in range(len(grids[i])):
                for k in range(len(grids[i][j])):
                    if grids[i][j][k] == choice:
                        sum_of_grids[i] -= choice
                        choices_grid[i][j][k] = 1
                        if is_win(choices_grid[i]):
                            return sum_of_grids[i], choice


def func2():
    choices = data.pop(0)
    choices = list(map(int, choices.split(",")))
    values = data[1:]
    win_grids = [0 for i in range(100)]
    grids, sum_of_grids = get_grid(values)
    choices_grid = [[[0 for col in range(5)] for row in range(5)] for val in range(100)]

    for choice in choices:
        for i in range(len(grids)):
            for j in range(len(grids[i])):
                for k in range(len(grids[i][j])):
                    if grids[i][j][k] == choice:
                        sum_of_grids[i] -= choice
                        choices_grid[i][j][k] = 1
                        if is_win(choices_grid[i]):
                            win_grids[i] = 1
                            if sum(win_grids) == 100:
                                return sum_of_grids[i], choice


if __name__ == "__main__":
    # print(func1()) # 35711
    print(func2())  # 5586
