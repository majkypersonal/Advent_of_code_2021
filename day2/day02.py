file = open('input02', "r+").readlines()
data = [i[:-1] for i in file]


def func1():
    depth, horizontal = 0, 0
    for i in data:
        value = int(i[-1])

        if 'u' in i[0]:
            depth -= value
        elif 'd' in i[0]:
            depth += value
        else:
            horizontal += value

    print(depth * horizontal)


def func2():
    depth, horizontal, aim = 0, 0, 0

    for i in data:
        value = int(i[-1])

        if 'u' in i[0]:
            aim -= value
        elif 'd' in i[0]:
            aim += value
        else:
            horizontal += value
            depth += (aim * value)
    print(depth * horizontal)


if __name__ == "__main__":
    # func1()
    func2()
