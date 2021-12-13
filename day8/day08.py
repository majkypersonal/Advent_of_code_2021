from itertools import permutations

file = open('input08', "r+").readlines()
data = [i[:-1] for i in file]


def func1():
    codes = [i.split(" | ")[1].split() for i in data]
    codes_len = [len(item) for value in codes for item in value]
    result = [1 if value in [2, 3, 4, 7] else 0 for value in codes_len]

    print(sum(result))


def func2():
    all_values = 0

    for line in data:
        result = ''
        signal, out = line.strip().split(" | ")
        exact_numbers = {length: set(sig) for sig in signal.split() if (length := len(sig)) in (2, 4)}

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
                if len(length & exact_numbers[2]) == 2:
                    result += '3'
                elif len(length & exact_numbers[4]) == 2:
                    result += '2'
                else:
                    result += '5'
            else:
                length = set(value)
                if len(length & exact_numbers[2]) == 1:
                    result += '6'
                elif len(length & exact_numbers[4]) == 4:
                    result += '9'
                else:
                    result += '0'

        all_values += int(result)
    print(all_values)


if __name__ == "__main__":
    # func1()
    func2()
