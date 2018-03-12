import math

def is_palindrome(x):
    if x < 0:
        return False
    elif x == 0:
        return True

    digits_num = int(math.log10(x) + 1)
    while x > 0:
        first_digit = x / 10 ** (digits_num - 1)
        last_digit = x % 10

        if first_digit != last_digit:
            return False

        x -= first_digit * (10 ** (digits_num - 1))
        x = x / 10

        digits_num -= 2

    return True

if __name__ == "__main__":
    assert is_palindrome(-1) is False
    assert is_palindrome(0) is True
    assert is_palindrome(121) is True
    assert is_palindrome(123) is False
    assert is_palindrome(1000021) is False
    assert is_palindrome(1002001) is True
