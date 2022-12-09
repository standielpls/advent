f = open('input.txt', 'r')

def part_one(f):
    max_count = 0
    max_reindeer = 0
    count = 0
    reindeer = 1
    # prev_line = None

    for line in f:
        if not line.isspace():
            count += int(line)
        else:
            if count > max_count:
                max_count = count
                max_reindeer = reindeer
            reindeer += 1
            count = 0

    print(max_count)
    print(max_reindeer)


def part_two(f):
    top = []

    count = 0

    for line in f:
        if not line.isspace():
            count += int(line)
        else:
            if len(top) < 3:
                top.append(count)
                count = 0
                continue
            if count > min(top):
                top.remove(min(top))
                top.append(count)
            
            count = 0
    print(top)
    print(sum(top))
part_two(f)