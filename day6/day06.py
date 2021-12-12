import decimal
import collections

file = open('input06', "r+").readlines()
data = [i[:-1] for i in file]


def func1_2():
    old_fish = list(map(int, data[0].split(",")))

    fish = collections.Counter(old_fish)

    for day in range(1, 257):
        tmp = {8: fish[0] if fish[0] else 0, 7: fish[8] if fish[8] else 0, 6: fish[7] if fish[7] else 0,
               5: fish[6] if fish[6] else 0, 4: fish[5] if fish[5] else 0, 3: fish[4] if fish[4] else 0,
               2: fish[3] if fish[3] else 0, 1: fish[2] if fish[2] else 0, 0: fish[1] if fish[1] else 0}

        tmp[6] += fish[0] if fish[0] else 0

        fish = tmp.copy()
        if day == 80:
            print("Number of fishes day 80: {}".format(sum(fish.values())))

    print("Number of fishes day 256: {}".format(sum(fish.values())))


if __name__ == "__main__":
    func1_2()
