import re

"""
 Problem:
    Count the passports that are valid from the input. Valid fields rules:
        byr (Birth Year) - four digits; at least 1920 and at most 2002.
        iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
        hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        pid (Passport ID) - a nine-digit number, including leading zeroes.
        cid (Country ID) - ignored, missing or not.

    Example:
        Your job is to count the passports where all required fields are both present and valid according to the above 
        rules. Here are some example values:
        
            byr valid:   2002
            byr invalid: 2003
            
            hgt valid:   60in
            hgt valid:   190cm
            hgt invalid: 190in
            hgt invalid: 190
            
            hcl valid:   #123abc
            hcl invalid: #123abz
            hcl invalid: 123abc
            
            ecl valid:   brn
            ecl invalid: wat
            
            pid valid:   000000001
            pid invalid: 0123456789

 Solution:
    Read the input line by line, and for each line check if are the required fields are valid by using field validator
    implementations.

    Complexity:
        Time: O(n*m)
        Space: O(1)
        
        
"""


def in_range(field, min, max):
    return field.isdigit() and int(field) >= min and int(field) <= max


hair_color_regex = re.compile(r'^#[0-9a-f]{6}$')

required_fields = {
    "byr": lambda field: in_range(field, 1920, 2002),
    "iyr": lambda field: in_range(field, 2010, 2020),
    "eyr": lambda field: in_range(field, 2020, 2030),
    "hgt": lambda field: True if (field[-2:] == "cm" and in_range(field[:-2], 150, 193)) or
                                 (field[-2:] == "in" and in_range(field[:-2], 59, 76)) else False,
    "hcl": lambda field: hair_color_regex.match(field),
    "ecl": lambda field: True if field == "amb" or field == "blu" or field == "brn" or field == "gry" or field == "grn"
                                 or field == "hzl" or field == "oth" else False,
    "pid": lambda field: len(field) is 9 and in_range(field, 0, 999999999),
}


def day04part1(passport):
    fields = dict(item.split(":") for item in re.split("\n| ", passport))
    for req_field in required_fields:
        if req_field not in fields or not required_fields[req_field](fields[req_field]):
            return False
    return True


if __name__ == '__main__':
    valid_passports = 0
    with open('input.txt', 'r') as f:
        data = f.read()
    passports = data.split("\n\n")
    for passport in passports:
        if day04part1(passport):
            valid_passports += 1
    print(valid_passports)
