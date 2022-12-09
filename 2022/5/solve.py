sample_input = [
    ['N', 'Z'],
    ['D', 'C', 'M'],
    ['P'],
]
input_data = [
    ['F','T','N','Z','M','G','H','J'],
    ['J','W','V'],
    [ 'H','T','B','J','L','V','G'], 
    ['L','V','D','C','N','J','P','B'],
    ['G','R','P','M','S','W','F'],
    ['M','V','N','B','F','C','H','G'],
    ['R','M','G','H','D'],
    ['D','Z','V','M','N','H'],
    ['H','F','N','G'],
]

def modify(data, num, start, end):
    can = list(data[start][-num:])
    data[start] = data[start][:-num]
    print('can', can)
    # can.reverse()

    data[end] = data[end] + can
    return data

def get_last_for_each(data):
    result = ""
    for d in data:
        result += d[-1]
    print("result\n",result)

def pre_run(data):
    for d in data:
        d.reverse()
    return data

def run():
    f = open('input.txt', 'r')
    data = pre_run(input_data)
    for line in f:
        tokens = line.rstrip().split(' ')
        num = int(tokens[1])
        start_idx = int(tokens[3]) - 1
        end_idx = int(tokens[5]) - 1

        data = modify(data, num, start_idx, end_idx)
    get_last_for_each(data)
    
run()
