import numpy as np

file = open('test.txt', "r+").readlines()
data = [i[:-1] for i in file]


def func1():
    old_fish = list(map(int, data[0].split(",")))
    number_of_zeroes = 0

    for day in range(1, 81):
        old_fish.extend([8] * number_of_zeroes)

        old_fish = [i - 1 for i in old_fish]
        number_of_zeroes = np.count_nonzero(np.array(old_fish) == 0)
        old_fish = np.where(old_fish == 0, 6, old_fish)

    print(len(old_fish))


def func2():
    print("Func2")


if __name__ == "__main__":
    func1()
    # func2()
