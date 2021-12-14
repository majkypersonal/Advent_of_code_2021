from collections import Counter

file = open('test10.txt', "r+").readlines()
data = [i[:-1] for i in file]


def func1():
    score = 0
    for line in data:
        symbols = [char for char in line]
        for symbol in symbols:
            pass
        counters = Counter(symbols)
        diff = [counters["("] - counters[")"],
                counters["["] - counters["]"],
                counters["{"] - counters["}"],
                counters["<"] - counters[">"]]

        if diff[0] != 0:
            score += (diff[0] * 3)
        if diff[1] != 0:
            score += (diff[1] * 57)
        if diff[2] != 0:
            score += (diff[2] * 1197)
        if diff[3] != 0:
            score += (diff[3] * 25137)

    print(score)


def func2():
    print("Func2")


if __name__ == "__main__":
    func1()
    # func2()
