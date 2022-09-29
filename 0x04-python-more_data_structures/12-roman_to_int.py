#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return 0
    roman_nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}
    result = 0
    for i in range(0, len(roman_string)):
        if roman_string[i] not in roman_nums or (i != len(roman_string) - 1
                and roman_string[i + 1] not in roman_nums):
            return 0
        if ((i != len(roman_string) - 1) and
                roman_nums[roman_string[i]] < roman_nums[roman_string[i + 1]]):
            result -= roman_nums[roman_string[i]]
        else:
            result += roman_nums[roman_string[i]]
    return result
