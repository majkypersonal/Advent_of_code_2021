file = open('input05', "r+").readlines()
data = [i[:-1].replace(" -> ", ",") for i in file]


def func1():
    all_data = [''.join(i).split(",") for i in data]
    test = {}

    for x_1, y_1, x_2, y_2 in [[int(y) for y in x] for x in all_data]:
        if x_1 == x_2:
            if y_1 > y_2: y_1, y_2 = y_2, y_1
            for y in range(y_1, y_2 + 1):
                coordinates = (x_1, y)
                if coordinates in test:
                    test[coordinates] += 1
                else:
                    test[coordinates] = 1
        elif y_1 == y_2:
            if x_1 > x_2: x_1, x_2 = x_2, x_1
            for x in range(x_1, x_2 + 1):
                coordinates = (x, y_2)
                if coordinates in test:
                    test[coordinates] += 1
                else:
                    test[coordinates] = 1

    counter = 0
    for value in test.values():
        if value >= 2:
            counter += 1
    print(counter)


def func2():
    all_data = [''.join(i).split(",") for i in data]
    test = {}

    for x_1, y_1, x_2, y_2 in [[int(y) for y in x] for x in all_data]:
        if x_1 == x_2:
            if y_1 > y_2:
                y_1, y_2 = y_2, y_1

            for y in range(y_1, y_2 + 1):
                coordinates = (x_1, y)
                if coordinates in test:
                    test[coordinates] += 1
                else:
                    test[coordinates] = 1
        elif y_1 == y_2:
            if x_1 > x_2:
                x_1, x_2 = x_2, x_1

            for x in range(x_1, x_2 + 1):
                coordinates = (x, y_2)
                if coordinates in test:
                    test[coordinates] += 1
                else:
                    test[coordinates] = 1
        else:
            if x_1 < x_2:
                range_x = list(range(x_1, x_2 + 1))
            else:
                range_x = list(range(x_1, x_2 - 1, -1))

            if y_1 < y_2:
                range_y = list(range(y_1, y_2 + 2))
            else:
                range_y = list(range(y_1, y_2 - 1, -1))

            for i in range(len(range_x)):
                coordinates = (range_x[i], range_y[i])
                if coordinates in test:
                    test[coordinates] += 1
                else:
                    test[coordinates] = 1

    counter = 0
    for value in test.values():
        if value >= 2:
            counter += 1
    print(counter)


if __name__ == "__main__":
    # func1()  # 5145
    func2()  # 18864
