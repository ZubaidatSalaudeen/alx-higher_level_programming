#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "XXI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CXXIV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XCIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "LXXXIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "IIp"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = 567
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = ""
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
