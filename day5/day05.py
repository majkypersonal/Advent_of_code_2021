file = open('input05', "r+").readlines()
data = [i[:-1].replace(" -> ", ",") for i in file]


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
        # idea - https://www.kite.com/python/answers/how-to-create-a-list-of-numbers-between-two-values-in-python
        x_values = x1[i] - x2[i]
        y_values = y1[i] - y2[i]

        direct_X = True if x_values >= 0 else False
        direct_Y = True if y_values >= 0 else False

    print(max(x1), max(y1), max(x2), max(y2))


def func2():
    print("Func2")


if __name__ == "__main__":
    func1()
    # func2()
