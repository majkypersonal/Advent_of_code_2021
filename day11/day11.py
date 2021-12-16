file = open('input11', "r+").readlines()
data = [i[:-1] for i in file]


def func1():
    grid = [list(map(int, line)) for line in data]
    shines = 0

    for step in range(1000000):
        grid = [[val + 1 for val in x] for x in grid]
        grid_flashes = {}
        need_check = {}

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] > 9:
                    grid[i][j] = 0
                    if (i, j) not in grid_flashes:
                        shines += 1
                        grid_flashes[(i, j)] = 1

                    if (i, j) in need_check:
                        need_check.pop((i, j))

                    # DOWN
                    if 0 <= i + 1 < len(grid):
                        grid[i + 1][j] += 1
                        if grid[i + 1][j] > 9 and (i + 1, j) not in need_check:
                            need_check[(i + 1, j)] = 1

                        if 0 <= j - 1 < len(grid[i + 1]):
                            grid[i + 1][j - 1] += 1
                            if grid[i + 1][j - 1] > 9 and (i + 1, j - 1) not in need_check:
                                need_check[(i + 1, j - 1)] = 1
                        if 0 <= j + 1 < len(grid[i + 1]):
                            grid[i + 1][j + 1] += 1
                            if grid[i + 1][j + 1] > 9 and (i + 1, j + 1) not in need_check:
                                need_check[(i + 1, j + 1)] = 1

                    # UP
                    if 0 <= i - 1 < len(grid):
                        grid[i - 1][j] += 1
                        if grid[i - 1][j] > 9 and (i - 1, j) not in need_check:
                            need_check[(i - 1, j)] = 1

                        if 0 <= j - 1 < len(grid[i - 1]):
                            grid[i - 1][j - 1] += 1
                            if grid[i - 1][j - 1] > 9 and (i - 1, j - 1) not in need_check:
                                need_check[(i - 1, j - 1)] = 1
                        if 0 <= j + 1 < len(grid[i - 1]):
                            grid[i - 1][j + 1] += 1
                            if grid[i - 1][j + 1] > 9 and (i - 1, j + 1) not in need_check:
                                need_check[(i - 1, j + 1)] = 1

                    # RIGHT
                    if 0 <= j + 1 < len(grid[i]):
                        grid[i][j + 1] += 1
                        if grid[i][j + 1] > 9 and (i, j + 1) not in need_check:
                            need_check[(i, j + 1)] = 1

                    # LEFT
                    if 0 <= j - 1 < len(grid[i]):
                        grid[i][j - 1] += 1
                        if grid[i][j - 1] > 9 and (i, j - 1) not in need_check:
                            need_check[(i, j - 1)] = 1

        grid, shines, grid_flashes = check_surrounding(grid, need_check, grid_flashes, shines)
        for i, j in grid_flashes:
            grid[i][j] = 0

        if sum(sum(grid, [])) == 0:
            print(step)

    print("Shines: {}".format(shines))


def check_surrounding(grid, need_check, grid_flashes, shines):
    while len(need_check) > 0:
        i, j = need_check.popitem()[0]
        grid[i][j] = 0
        if (i, j) not in grid_flashes:
            shines += 1
            grid_flashes[(i, j)] = 1

        # DOWN
        if 0 <= i + 1 < len(grid):
            grid[i + 1][j] += 1
            if grid[i + 1][j] > 9 and (i + 1, j) not in need_check:
                need_check[(i + 1, j)] = 1

            if 0 <= j - 1 < len(grid[i + 1]):
                grid[i + 1][j - 1] += 1
                if grid[i + 1][j - 1] > 9 and (i + 1, j - 1) not in need_check:
                    need_check[(i + 1, j - 1)] = 1
            if 0 <= j + 1 < len(grid[i + 1]):
                grid[i + 1][j + 1] += 1
                if grid[i + 1][j + 1] > 9 and (i + 1, j + 1) not in need_check:
                    need_check[(i + 1, j + 1)] = 1

        # UP
        if 0 <= i - 1 < len(grid):
            grid[i - 1][j] += 1
            if grid[i - 1][j] > 9 and (i - 1, j) not in need_check:
                need_check[(i - 1, j)] = 1

            if 0 <= j - 1 < len(grid[i - 1]):
                grid[i - 1][j - 1] += 1
                if grid[i - 1][j - 1] > 9 and (i - 1, j - 1) not in need_check:
                    need_check[(i - 1, j - 1)] = 1
            if 0 <= j + 1 < len(grid[i - 1]):
                grid[i - 1][j + 1] += 1
                if grid[i - 1][j + 1] > 9 and (i - 1, j + 1) not in need_check:
                    need_check[(i - 1, j + 1)] = 1

        # RIGHT
        if 0 <= j + 1 < len(grid[i]):
            grid[i][j + 1] += 1
            if grid[i][j + 1] > 9 and (i, j + 1) not in need_check:
                need_check[(i, j + 1)] = 1

        # LEFT
        if 0 <= j - 1 < len(grid[i]):
            grid[i][j - 1] += 1
            if grid[i][j - 1] > 9 and (i, j - 1) not in need_check:
                need_check[(i, j - 1)] = 1

    return grid, shines, grid_flashes


if __name__ == "__main__":
    print(func1())
    # func2()
