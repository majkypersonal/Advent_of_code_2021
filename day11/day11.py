file = open('input11', "r+").readlines()
data = [i[:-1] for i in file]


def func1():
    grid = [list(map(int, line)) for line in data]
    shines = 0

    for _ in range(100):
        grid = [[val + 1 for val in x] for x in grid]

        need_check = 0

        if need_check > 0:
            for i in range(len(grid)):
                for j in grid[i]:
                    if grid[i][j] > 9:
                        shines += 1
                        grid[i][j] = 0
                        
                        # DOWN
                        if 0 <= i + 1 < len(grid):
                            grid[i + 1][j] += 1
                            if grid[i + 1][j] > 9:
                                need_check += 1

                            if 0 <= j - 1 < len(grid[i + 1]):
                                grid[i + 1][j - 1] += 1
                                if grid[i + 1][j - 1] > 9:
                                    need_check += 1
                            elif 0 <= j + 1 < len(grid[i + 1]):
                                grid[i + 1][j] += 1
                                if grid[i + 1][j] > 9: need_check += 1
                        # UP
                        if 0 <= i - 1 < len(grid):
                            grid[i - 1][j] += 1
                            if grid[i + 1][j] > 9: need_check += 1
                        if 0 <= j + 1 < len(grid[i]):
                            grid[i + 1][j] += 1
                            if grid[i + 1][j] > 9: need_check += 1
                        if 0 <= j - 1 < len(grid[i]):
                            grid[i + 1][j] += 1
                            if grid[i + 1][j] > 9: need_check += 1


def func2():
    print("Func2")


if __name__ == "__main__":
    func1()
    # func2()
