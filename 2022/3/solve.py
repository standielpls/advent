import math
f = open('sample.txt', 'r')

# A = 65 -> 27 (38)
# a = 97 -> 1 (96)
def part_one(f):
    total_count = 0 

    for line in f:
        count = 0 
        mid = math.floor(len(line) / 2)
        first = line[0:mid]
        second = line[mid:len(line)]
        m = set()
        for ch in first:
            m.add(ch)
        for ch in second:
            if ch in m:
                ascii_val = ord(ch)
                if ch.isupper():
                    count += ascii_val - 38
                else:
                    count += ascii_val - 96
                break
        total_count += count
    print(total_count)

def calc(group):
    common = group[0].intersection(group[1], group[2])
    item = list(common)[0]
    ascii_val = ord(item)
    if item.isupper():
        return ascii_val - 38
    return ascii_val - 96

def part_two(f):
    total_count = 0
    group = []
    all_groups = []
    for x, line in enumerate(f):
        part = set(line.rstrip())
        group.append(part)
        idx = x + 1
        if idx % 3 == 0:
            all_groups.append(group)
            group = []
    for g in all_groups:
        total_count += calc(g)
    print(total_count)


# part_one(f)
part_two(f)