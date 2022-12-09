def find_marker(data):
    # 4 unique chars in front
    p1, p2 = 0, 14
    
    while (p2 < len(data)):
        sub = set(data[p1:p2])
        if len(sub) == 14:
            return p2
        p1 += 1
        p2 += 1
    return None

def solve():
    # data = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    file = open('input.txt', 'r')
    data = file.read()
    idx = find_marker(data)
    print('idx is ', idx)
solve()