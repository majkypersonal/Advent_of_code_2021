from collections import Counter

file = open('input10', "r+").readlines()
data = [i[:-1] for i in file]


def func1():
    score, incomplete_lines = [], []
    counter_bad = 0
    for line in data:
        ok = True
        symbols = [char for char in line]
        wait_to_close = {}
        for idx in range(len(symbols)):
            if symbols[idx] == "(" or symbols[idx] == "[" or symbols[idx] == "{" or symbols[idx] == "<":
                wait_to_close[idx] = symbols[idx]
            else:
                if symbols[idx] == ")":
                    if list(wait_to_close.values())[-1] == chr(ord(symbols[idx]) - 1):
                        wait_to_close.popitem()
                    else:
                        score.append(3)
                        ok = False
                        counter_bad += 1
                        break
                else:
                    symbol_open = list(wait_to_close.values())[-1]
                    if symbol_open == chr(ord(symbols[idx]) - 2):
                        wait_to_close.popitem()
                    else:
                        if symbols[idx] == "]":
                            score.append(57)
                        elif symbols[idx] == "}":
                            score.append(1197)
                        else:
                            score.append(25137)
                        ok = False
                        counter_bad += 1
                        break

        if ok:
            incomplete_lines.append(line)

    print(sum(score))
    return incomplete_lines, counter_bad


def func2(data_lines, bad):
    if len(data_lines) + bad != 106:
        print("Nesedia riadky")
        exit(1)
    score = []
    for line in data_lines:
        line_score = 0
        symbols = [char for char in line]
        wait_to_close = {}
        for idx in range(len(symbols)):
            if symbols[idx] == "(" or symbols[idx] == "[" or symbols[idx] == "{" or symbols[idx] == "<":
                wait_to_close[idx] = symbols[idx]
            else:
                if symbols[idx] == ")":
                    if list(wait_to_close.values())[-1] == chr(ord(symbols[idx]) - 1):
                        wait_to_close.popitem()
                else:
                    symbol_open = list(wait_to_close.values())[-1]
                    if symbol_open == chr(ord(symbols[idx]) - 2):
                        wait_to_close.popitem()

        if len(wait_to_close) > 0:
            arr = list(wait_to_close.values())
            for val in range(len(arr) - 1, -1, -1):
                if arr[val] == "(":
                    line_score = (line_score * 5) + 1
                elif arr[val] == "[":
                    line_score = (line_score * 5) + 2
                elif arr[val] == "{":
                    line_score = (line_score * 5) + 3
                else:
                    line_score = (line_score * 5) + 4

        score.append(line_score)
    score = sorted(score)
    print(score[int(len(score) / 2)])


if __name__ == "__main__":
    incomplete, bad = func1()
    func2(incomplete, bad)
