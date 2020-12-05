import re


def checkYear(val, mini, maxi):
    if len(val) == 4 and val.isdigit():
        num = int(val)
        if num >= mini and num <= maxi:
            return True
    return False


def checkHeight(height):
    num = height[:-2]
    unit = height[-2:]
    if num.isdigit():
        num = int(num)
        if unit == 'cm' and num >= 150 and num <= 193:
            return True
        elif unit == 'in' and num >= 59 and num <= 76:
            return True
    return False


def checkHair(hair):
    return re.match("^#[a-f0-9]{6}$", hair)


def checkEye(eye):
    return eye in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def checkPID(pid):
    return re.match("^\d{9}$", pid)


def checkFields(passport):
    if 'byr' not in passport or 'iyr' not in passport or 'eyr' not in passport or 'hgt' not in passport or 'hcl' not in passport or 'ecl' not in passport or 'pid' not in passport:
        return False
    if not checkYear(passport['byr'], 1920, 2002):
        return False
    if not checkYear(passport['iyr'], 2010, 2020):
        return False
    if not checkYear(passport['eyr'], 2020, 2030):
        return False
    if not checkHeight(passport['hgt']):
        return False
    if not checkHair(passport['hcl']):
        return False
    if not checkEye(passport['ecl']):
        return False
    if not checkPID(passport['pid']):
        return False
    return True


fs = open('2020/day4/input.txt', 'r')

valid = 0

line = fs.readline().strip('\n')
while line:
    passport = {}
    while line:
        fields = line.split(' ')
        for f in fields:
            key, value = f.split(':')
            passport[key] = value

        line = fs.readline().strip('\n')

    keys = list(passport.keys())
    if len(keys) == 8 or len(keys) == 7:
        if checkFields(passport):
            valid += 1

    line = fs.readline().strip('\n')

print(valid)

fs.close()
