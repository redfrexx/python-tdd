from functools import reduce

def sum(*addends):
    # return reduce(lambda a, b: a + b, addends, 0)
    sum = 0
    for addend in addends:
        if (addend < 0):
            raise ValueError("Addends must not be negative")
        sum += addend
    return sum

if __name__ == '__main__':
    print('3 + 5 =', sum(3, 5))
