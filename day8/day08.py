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

    g - 186
    f - 193
    e - 197
    d - 182
    c - 179
    b - 184
    a - 174

    """

    # codes = [i.split(" | ")[1].split() for i in data]
    # codes_values = [item for value in codes for item in value]

    all = 0
    for line in data:
        result = ''
        signal, out = line.strip().split(" | ")
        splitted = {length: set(sig) for sig in signal.split() if (length := len(sig)) in (2, 4)}

        for value in out.split():
            length = len(value)
            if length == 2:
                result += '1'
            elif length == 3:
                result += '7'
            elif length == 4:
                result += '4'
            elif length == 7:
                result += '8'
            elif length == 5:
                length = set(value)
                if len(length & splitted[2]) == 2:
                    result += '3'
                elif len(length & splitted[4]) == 2:
                    result += '2'
                else:
                    result += '5'
            else:
                length = set(value)
                if len(length & splitted[2]) == 1:
                    result += '6'
                elif len(length & splitted[4]) == 4:
                    result += '9'
                else:
                    result += '0'

        all += int(result)
    print(all)


if __name__ == "__main__":
    # func1()
    func2()
