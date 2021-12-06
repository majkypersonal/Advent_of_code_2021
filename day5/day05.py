file = open('input05', "r+").readlines()
data = [i[:-1] for i in file]


def func1():
    val = data
    print("X")


def func2():
    print("Func2")


if __name__ == "__main__":
    func1()
    # func2()
