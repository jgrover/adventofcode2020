import re

needed_cats = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
validation = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: (x.endswith("in") and 59 <= int(x.strip("in")) <= 76 or x.endswith("cm") and 150 <= int(x.strip("cm")) <= 193),
    'hcl': lambda x: re.match('^#[0-9a-f]{6}$',x),
    'ecl': lambda x: re.match('^(amb|blu||brn|gry|grn|hzl|oth)$',x),
    'pid': lambda x: re.match('^\d{9}$',x)
    }

with open('day4_perfect.txt') as f:
    lines = f.readlines()

passports = []
for line in lines:
    passports.append(line.strip())

part1_good_count = 0
part2_good_count = 0
for passport in passports:
    passport = passport.strip()
    if not passport:
        continue

    # Put each category entry into a dict, skip cid
    entries = passport.split()
    cat_dict = {}
    for entry in entries:
        res = entry.split(":")
        if res[0] == 'cid': 
            continue
        cat_dict[res[0]] = res[1]

    # Filter out the bad passport entries
    passport_cats = set(cat_dict.keys())
    diff = needed_cats.difference(passport_cats)
    diff_len = len(diff)
    if len(diff) == 0:
        good = True
        part1_good_count+=1
        for i, fn in validation.items():
            if not fn(cat_dict[i]):
                good=False
                break
        if good:
            part2_good_count+=1

print("part 1:",part1_good_count)
print("part 2:",part2_good_count)
