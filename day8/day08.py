from itertools import permutations

file = open('input08', "r+").readlines()
data = [i[:-1] for i in file]


def func1():
    codes = [i.split(" | ")[1].split() for i in data]
    codes_len = [len(item) for value in codes for item in value]
    result = [1 if value in [2, 3, 4, 7] else 0 for value in codes_len]

    print(sum(result))


def func2():
    """
                    cagedb: 0
                    ab: 1
        dddd        gcdfa: 2
       e    a       fbcad: 3
       e    a       eafb: 4
        ffff        cdfbe: 5
       g    b       cdfgeb: 6
       g    b       dab: 7
        cccc        acedgfb: 8
                    cefabd: 9
    """

    codes = [i.split(" | ")[1].split() for i in data]
    codes_values = [item for value in codes for item in value]

    valid_segments, numbers = {}, ['cagedb', 'ab', 'gcdfa', 'fbcad', 'eafb', 'cdfbe', 'cdfgeb', 'dab', 'acedgfb',
                                   'cefabd']

    for i in range(10):
        valid_segments[i] = ["".join(val) for val in permutations(numbers[i])]

    counter = 0
    result = [1 if value in valid_segments else 0 for value in codes_values]

    print(sum(result))  # 941 255


if __name__ == "__main__":
    # func1()
    func2()
