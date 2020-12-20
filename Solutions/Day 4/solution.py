# -*- coding: utf-8 -*-
"""
Day 4: Passport Processing
https://adventofcode.com/2020/day/4
"""
import re  # Allow regex usage for cleaner data validation code

# This problem lends itself nicely to a dictionary structure. However,
# the inconsistent formatting of the puzzle input requires a few
# reformatting iterations.  It is possible to have performed the full
# reformatting more compactly, but readability is more important.
#
# Unfortunately the nature of the reformatting requires a newline after
# each passport entry, so the initial input_list has this manually
# added on, since splitline() removes ending newlines.
#
# Note also that for numeric fields in the puzzle input only integers
# are used, which allows for simplified data validation.  Of course,
# the validation can be modified to account for non-integers, but this
# was not required.

with open('input.txt') as input:
    input_list = input.read().splitlines() + [""]

passport_list = []
holder_list = []
for item in input_list:
    if item != "":
        holder_list.append(item)
    else:
        passport_list.append(holder_list)
        holder_list = []

passport_list_formatted = []
for passport in passport_list:
    holder_list = []
    for item in passport:
        holder_list.extend(item.split())
    passport_list_formatted.append(holder_list)

passport_dictionaries = []
for passport in passport_list_formatted:
    holder_dictionary = {}
    for field in passport:
        holder_dictionary[field[:field.find(":")]] = field[field.find(":")+1:]
    passport_dictionaries.append(holder_dictionary)

# This section solves Part One.
def valid_passport(passport):
    if (len(passport) == 8 or
        (len(passport) == 7 and passport.get("cid") == None)):
        return True
    return False

def valid_passport_count(passport_list):
    count = 0
    for passport in passport_list:
        if valid_passport(passport):
            count += 1
    return count

print(valid_passport_count(passport_dictionaries))

# This section solves Part Two.
def valid_byr(field):
    if field.isnumeric():
        if 1920 <= int(field) <= 2002:
            return True
    return False

def valid_iyr(field):
    if field.isnumeric():
        if 2010 <= int(field) <= 2020:
            return True
    return False

def valid_eyr(field):
    if field.isnumeric():
        if 2020 <= int(field) <= 2030:
            return True
    return False

def valid_hgt(field):
    if ((field[-2:] == "cm" and 150 <= int(field[:-2]) <= 193)
        or field[-2:] == "in" and 59 <= int(field[:-2]) <= 76):
        return True
    return False

def valid_hcl(field):
    if re.match("^#[a-f0-9]{6}$", field):
        return True
    return False

def valid_ecl(field):
    if (field == "amb" or field == "blu" or field == "brn"
        or field == "gry" or field == "grn" or field == "hzl"
        or field == "oth"):
        return True
    return False
        
def valid_pid(field):
    if re.match("^\d{9}$", field):
        return True
    return False

def strict_valid_passport(passport):
    if (len(passport) == 8 or
        (len(passport) == 7 and passport.get("cid") == None)):
        if (valid_byr(passport.get("byr"))
            and valid_iyr(passport.get("iyr"))
            and valid_eyr(passport.get("eyr"))
            and valid_hgt(passport.get("hgt"))
            and valid_hcl(passport.get("hcl"))
            and valid_ecl(passport.get("ecl"))
            and valid_pid(passport.get("pid"))):
                return True
    return False

def strict_valid_passport_count(passport_list):
    count = 0
    for passport in passport_list:
        if strict_valid_passport(passport):
            count += 1
    return count

print(strict_valid_passport_count(passport_dictionaries))
