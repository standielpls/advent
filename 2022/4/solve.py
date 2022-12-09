f = open('input.txt', 'r')

def extract(line):
    nums = line.split("-")
    start = int(nums[0])
    end = int(nums[1])
    return start, end


def part_one(f):
    count = 0
    for line in f:
        s = line.rstrip().split(",")
        p1 = s[0]
        p2 = s[1]
        
        first_start, first_end = extract(p1)
        second_start, second_end = extract(p2)

        if first_start <= second_start and first_end >= second_end:
            count += 1
        elif second_start <= first_start and second_end >= first_end:
            count += 1

    print("count", count)


def part_two(f):
    count = 0
    for line in f:
        s = line.rstrip().split(",")
        p1 = s[0]
        p2 = s[1]
        
        first_start, first_end = extract(p1)
        second_start, second_end = extract(p2)

        first = set(range(first_start, first_end+1))
        second = set(range(second_start, second_end+1))
        
        print('first', first)
        print('second', second)
        if len(first.intersection(second)) > 0:
            count += 1
    
    print(count)
part_two(f)