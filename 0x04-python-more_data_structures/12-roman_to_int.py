#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    sum = 0
    nums = {'I': 1, 'V': 5,
            'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000}
    lnums = list(nums.keys())

    for c in range(len(roman_string)):
        if roman_string[c] == 'I':
            if ('V' in roman_string[c+1:] or
                    'X' in roman_string[c+1:] or
                    'L' in roman_string[c+1:] or
                    'C' in roman_string[c+1:] or
                    'D' in roman_string[c+1:] or
                    'M' in roman_string[c+1:]):
                sum -= 1
            else:
                    sum += 1
        if roman_string[c] == 'V':
            if ('X' in roman_string[c+1:] or
                    'L' in roman_string[c+1:] or
                    'C' in roman_string[c+1:] or
                    'D' in roman_string[c+1:] or
                    'M' in roman_string[c+1:]):
                sum -= 5
            else:
                sum += 5
        if roman_string[c] == 'X':
            if ('L' in roman_string[c+1:] or
                    'C' in roman_string[c+1:] or
                    'D' in roman_string[c+1:] or
                    'M' in roman_string[c+1:]):
                sum -= 10
            else:
                sum += 10
        if roman_string[c] == 'L':
            if ('C' in roman_string[c+1:] or
                    'D' in roman_string[c+1:] or
                    'M' in roman_string[c+1:]):
                sum -= 50
            else:
                sum += 50
        if roman_string[c] == 'C':
            if ('D' in roman_string[c+1:] or
                    'M' in roman_string[c+1:]):
                sum -= 100
            else:
                sum += 100
        if roman_string[c] == 'D':
            if ('M' in roman_string[c+1:]):
                sum -= 500
            else:
                sum += 500
        if roman_string[c] == 'M':
                sum += 1000
    return sum
