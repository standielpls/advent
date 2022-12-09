def is_visible(mat, x, y) -> bool:
    can = mat[x][y]

    # top 
    top_visible = True
    start = x - 1
    end = 0
    top_count = 0
    while start >= end:
        top_count += 1
        if can <= mat[start][y]:
            top_visible = False
            break
        start -= 1

    # bottom
    start = x+1
    end = len(mat) - 1
    bottom_visible = True
    bottom_count = 0
    while start <= end:
        bottom_count += 1
        if can <= mat[start][y]:
            bottom_visible = False
            break
        start += 1

    # left
    start = y - 1
    end = 0
    left_visible = True
    left_count = 0
    while start >= end:
        left_count += 1
        if can <= mat[x][start]:
            left_visible = False
            break
        start -= 1

    # right
    start = y+1
    end = len(mat[0]) - 1
    right_visible = True
    right_count = 0
    while start <= end:
        right_count += 1
        if can <= mat[x][start]:
            right_visible = False
            break
        start += 1

    score = left_count*right_count*top_count*bottom_count
    print(score)
    return (top_visible or bottom_visible or left_visible or right_visible), score

def solve(f):
    mat = []
    for line in f:
        s = list(line.rstrip())
        mat.append(s)

    x, y = 1, 1
    highest_score = 0

    count = 0 
    while x < len(mat) - 1:
        y = 1
        while y < len(mat[0]) - 1:
            lala = mat[x][y]
            vis, score = is_visible(mat, x, y) 
            if vis is True:
                count += 1
            if score > highest_score:
                highest_score = score
            y += 1
        x += 1
    
    size = (len(mat) * 2) + ((len(mat[0]) - 2) * 2)
    visible = size + count
    print(visible, count)
    print('scenic score', highest_score)

    pass
solve(open('input.txt', 'r'))
