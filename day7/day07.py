file = open('input07', "r+").readlines()
data = [i[:-1] for i in file]


def func1():
    crabs_positions = list(map(int, data[0].split(",")))
    print(max(crabs_positions), min(crabs_positions), len(crabs_positions))

    result = {}

    for i in range(min(crabs_positions), max(crabs_positions) + 1):
        fuels = [abs(x - i) for x in crabs_positions]
        result[i] = sum(fuels)
    print("Optimized position is: {}".format(min(result.items(), key=lambda x: x[1])))


def func2():
    crabs_positions = list(map(int, data[0].split(",")))
    print(max(crabs_positions), min(crabs_positions), len(crabs_positions))
    result = {}

    for i in range(min(crabs_positions), max(crabs_positions) + 1):
        fuels = [abs(x - i) for x in crabs_positions]

        heavy_fuels = [sum(range(1, k + 1)) for k in fuels]
        result[i] = sum(heavy_fuels)

    print("Optimized position is: {}".format(min(result.items(), key=lambda x: x[1])))
    # 97071960 high


if __name__ == "__main__":
    # func1()
    func2()
