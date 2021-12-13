file = open('input09', "r+").readlines()
data = [i[:-1] for i in file]


def func1():
    values = data
    result = 0
    for i in range(len(values)):
        for j in range(len(values[i])):
            height = values[i][j]
            ok = False
            if 0 <= i + 1 < len(values):
                if height < values[i + 1][j]:
                    ok = True
                else:
                    continue

            if 0 <= j + 1 < len(values[i]):
                if height < values[i][j + 1]:
                    ok = True
                else:
                    continue

            if 0 <= j - 1 < len(values[i]):
                if height < values[i][j - 1]:
                    ok = True
                else:
                    continue

            if 0 <= i - 1 < len(values):
                if height < values[i - 1][j]:
                    ok = True
                else:
                    continue

            if ok:
                result += (int(height) + 1)
    print(result)


def check_surroundings(height, values, i, j, temporary_size, counted_values):
    need_to_look = [[height, i, j]]

    while need_to_look:
        height, i, j = need_to_look.pop()
        if height == 9 or (i, j) in counted_values: continue

        if 0 <= i + 1 < len(values):
            val = int(values[i + 1][j])
            if height < val != 9:
                if not (i + 1, j) in counted_values:
                    need_to_look.append([val, i + 1, j])

        if 0 <= j + 1 < len(values[i]):
            val = int(values[i][j + 1])
            if height < val != 9:
                if not (i, j + 1) in counted_values:
                    need_to_look.append([val, i, j + 1])

        if 0 <= j - 1 < len(values[i]):
            val = int(values[i][j - 1])
            if height < val != 9:
                if not (i, j - 1) in counted_values:
                    need_to_look.append([val, i, j - 1])

        if 0 <= i - 1 < len(values):
            val = int(values[i - 1][j])
            if height < val != 9:
                if not (i - 1, j) in counted_values:
                    need_to_look.append([val, i - 1, j])

        counted_values[(i, j)] = height
        temporary_size += 1
    return temporary_size


def func2():
    values = data
    result = []
    counted_values = {}
    for i in range(len(values)):
        for j in range(len(values[i])):
            height = int(values[i][j])
            if height == 9: continue
            temporary_size = 0

            ok = False
            if 0 <= i + 1 < len(values):
                val = int(values[i + 1][j])
                if height < val:
                    ok = True
                else:
                    continue

            if 0 <= j + 1 < len(values[i]):
                val = int(values[i][j + 1])
                if height < val:
                    ok = True
                else:
                    continue

            if 0 <= j - 1 < len(values[i]):
                val = int(values[i][j - 1])
                if height < val:
                    ok = True
                else:
                    continue

            if 0 <= i - 1 < len(values):
                val = int(values[i - 1][j])
                if height < val:
                    ok = True
                else:
                    continue
            if ok:
                result.append(check_surroundings(height, values, i, j, temporary_size, counted_values))

    res = sorted(result)[len(result) - 3:]
    print(res[0] * res[1] * res[2])


if __name__ == "__main__":
    # func1()
    func2()
