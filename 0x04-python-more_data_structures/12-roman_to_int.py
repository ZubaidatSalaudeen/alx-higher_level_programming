#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_keys = list(roman_nums)
    result, n  = 0, 0
    for i in range(0, len(roman_string)):
        if roman_string[i] not in roman_nums:
            return 0
        if (i != len(roman_string) - 1) and roman_nums[roman_string[i]] < roman_nums[roman_string[i + 1]]:
            result -= roman_nums[roman_string[i]]
        else:
            result += roman_nums[roman_string[i]]
    return result
