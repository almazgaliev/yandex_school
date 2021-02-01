import re

p0 = r'(([1-6](TAX|TBX))|(7(TAX|TBX|TEX))) \d{4}'
p1 = r'.*0{4}$'
count = 0
with open('taxi.in') as file:
    for s in file.readlines():
        s = s.strip()
        is_valid = re.fullmatch(p0, s) is not None \
            and re.fullmatch(p1, s) is None
        count += is_valid
        if is_valid:
            print(s)

print(count)
