"""
 Problem:
    Count the passports that are valid from the input:
    A valid passport requires te following fields:
        byr, iyr, eyr, hgt, hcl, ecl, pid

    Example:
        ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
        byr:1937 iyr:2017 cid:147 hgt:183cm

        iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
        hcl:#cfa07d byr:1929

        hcl:#ae17e1 iyr:2013
        eyr:2024
        ecl:brn pid:760753108 byr:1931
        hgt:179cm

        hcl:#cfa07d eyr:2025 pid:166559648
        iyr:2011 ecl:brn hgt:59in

        According to the above rules, your improved system would report 2 valid passports.

 Solution:
    Read the input line by line, and for each line check if are the required fields are included in the passport.

    Complexity:
        Time: O(n*m)
        Space: O(1)
"""

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def is_passport_valid(passport):
    for field in required_fields:
        if (field + ":") not in passport:
            return False
    return True


if __name__ == '__main__':
    valid_passports = 0
    with open('input.txt', 'r') as f:
        data = f.read()
    passports = data.split("\n\n")
    for passport in passports:
        if is_passport_valid(passport):
            valid_passports += 1
    print(valid_passports)
