def func1():
    data = open("input01", "r").readlines()
    value = int(data[0][:-1])
    counter = 0

    for i in data:
        current = int(i[:-1])
        if value < current:
            counter += 1
        value = current
    print(counter)


def func2():
    data = open("input01", "r").readlines()
    data = [int(i[:-1]) for i in data]
    counter = 0

    for i in range(len(data)-3):
        first, second = sum(data[i:i + 3]),sum(data[i + 1:i + 4])
        print(first, second)
        if first < second:
            counter += 1
    print(counter)


if __name__ == "__main__":
    #func1()
    func2()