import math
import numpy as np

RANGE = np.iinfo("int32")
MIN_VALUE, MAX_VALUE = RANGE.min, RANGE.max

def is_integer32_overflow(x):
    if x > MAX_VALUE or x < MIN_VALUE:
        return True
    else:
        return False

def reverse(x):
    is_positive = True
    if x == 0 or is_integer32_overflow(x):
        return 0
    elif x < 0:
        is_positive = False
        x *= -1

    num_digits = int(math.log10(x) + 1)
    result, weights = 0, 0
    for i in range(num_digits)[::-1]:
        result += (x / (10 ** i)) * (10 ** weights)
        x = x % (10 ** i)
        weights += 1

    if is_positive is False:
        result *= -1

    return 0 if is_integer32_overflow(result) else result

if __name__ == "__main__":
    assert reverse(123) == 321
    assert reverse(-123) == -321
    assert reverse(120) == 21
