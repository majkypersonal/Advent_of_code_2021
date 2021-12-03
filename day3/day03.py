import numpy as np

file = open('input03', "r+").readlines()
data = [i[:-1] for i in file]
gamma, epsilon = '', ''


def get_max_bits():
    result_number = []
    result_values = data

    for bit in range(len(data[0])):
        counter0, counter1 = 0, 0

        for number in result_values:
            if number[bit] == '0':
                counter0 += 1
            else:
                counter1 += 1

        if counter0 > counter1:
            result_values = get_values_on_bit(bit, 0, result_values)
            result_number.append(0)
        else:
            result_values = get_values_on_bit(bit, 1, result_values)
            result_number.append(1)

    return result_values, result_number


def get_min_bits():
    result_number = []
    result_values = data

    for bit in range(len(data[0])):
        counter0, counter1 = 0, 0
        for number in result_values:
            if number[bit] == '0':
                counter0 += 1
            else:
                counter1 += 1

        if counter0 > counter1:
            result_values = get_values_on_bit(bit, 1, result_values)
            result_number.append(1)
        else:
            result_values = get_values_on_bit(bit, 0, result_values)
            result_number.append(0)

        if len(result_values) == 1: break

    return result_values, result_number


def get_values_on_bit(bit_position, bit, result_value):
    result = []
    for value in result_value:
        if value[bit_position] == str(bit):
            result.append(value)

    return result


def func1():
    result_number = get_max_bits()
    gamma_number = np.array(result_number)
    epsilon_number = np.where((gamma_number == 0) | (gamma_number == 1), gamma_number ^ 1, gamma_number)

    gamma_number = np.array2string(gamma_number, separator=',').replace(",", "").replace("[", "").replace("]", "")
    epsilon_number = np.array2string(epsilon_number, separator=',').replace(",", "").replace("[", "").replace("]", "")

    print("Result: ", int(gamma_number, 2) * int(epsilon_number, 2))


def func2():
    result_values_oxygen, result_number_oxygen = get_max_bits()
    result_values_co2, result_number_co2 = get_min_bits()

    print(result_values_oxygen, result_values_co2)

    print(int(''.join(result_values_oxygen), 2) * int(''.join(result_values_co2), 2))


if __name__ == "__main__":
    # func1()
    func2()
