with open('day4_perfect.txt') as f:
    lines = f.readlines()

passports = []
for line in lines:
    passports.append(line.strip())

good_passport_count = 0
needed_cats = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
for passport in passports:
    passport = passport.strip()
    if not passport:
        continue
    entries = passport.split()
    cat_dict = {}
    for entry in entries:
        res = entry.split(":")
        cat_dict[res[0]] = res[1]

    passport_cats = set(cat_dict.keys())
    diff = needed_cats.difference(passport_cats)
    if len(diff) <= 1:
        if len(diff) == 0:
            good_passport_count+=1
        elif len(diff) == 1:
            if 'cid' in diff:
                good_passport_count+=1

print(count)
