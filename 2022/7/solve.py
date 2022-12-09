class Node():
    def __init__(self, name, is_dir, parent, children, size):
        self.name = name
        self.is_dir = is_dir
        self.parent = parent
        self.children = children
        self.size = size # optional

class DirectoryManager():
    def __init__(self):
        self.directory = {'/': Node('/', is_dir=True, parent=None, children=[], size=None)}
    
    def move_out_from(self, from_node):
        return from_node.parent
    
    def move_in_to(self, to_node):
        pass

    def lookup(self, name):
        return self.directory.get(name, None)

    def add_directory(self, parent_name, child_name):
        parent = self.lookup(parent_name)
        if parent is not None:
            child_node = Node(child_name, True, parent, [], 0)
            parent.children.append(child_node.name)
            self.directory[child_name] = child_node
            self.directory[parent_name] = parent
    
    def add_file(self, parent_name, child_name, size):
        parent = self.lookup(parent_name)
        if parent is not None:
            child_node = Node(name=child_name, is_dir=False, parent=parent_name, children=[], size=size)
            parent.children.append(child_node.name)
            self.directory[child_name] = child_node
            self.directory[parent_name] = parent

def calculate_dir_sizes(dm, root, dirs):
    root_node = dm.lookup(root)
    
    count = 0
    for ch in root_node.children:
        ch_node = dm.lookup(ch)
        if ch_node.is_dir is True:
            count += calculate_dir_sizes(dm, ch_node.name, dirs)
        else:
            count += ch_node.size
    dirs[root] = count
    return count


def parse_terminal_output(f):
    output = [line for line in f]
    
    idx = 0
    current_dir = ""

    dm = DirectoryManager()
    while (idx < len(output)):

        line = output[idx]
        s = line.rstrip().split(" ")
        
        if s[0] == "$":
            if s[1] == "cd":
                if s[2] == "..":
                    n = dm.lookup(current_dir)
                    current_dir = n.parent.name

                else:
                    name = s[2]
                    if name != "/":
                        if current_dir == "/":
                            name = current_dir + name
                        else:
                            name = current_dir+"/"+name
                    current_dir = name
            if s[1] == "ls":
                idx += 1
                continue
        else:
            if s[0] == "dir":
                name = s[1]
                full_name = f'{current_dir}{"" if current_dir == "/" else "/"}{name}'
                dm.add_directory(current_dir, full_name)
            else:
                size = int(s[0])
                name = s[1]
                full_name = f'{current_dir}{"" if current_dir == "/" else "/"}{name}'
                dm.add_file(current_dir, full_name, size)
        idx += 1
    m = {}
    total = calculate_dir_sizes(dm, "/", m)
    print("m", m)
    some_count = 0

    root_count = m["/"]
    free_space = 70000000 - root_count
    enough_for_30m = 30000000 - free_space

    min_ish = 100000000
    some_other_count = 0
    for x, y in m.items():
        if y < 100000:
            some_count += y
        if y >= enough_for_30m:
            some_other_count = y
            if some_other_count < min_ish:
                min_ish = some_other_count
    print('total', some_count)
    print('enough space', min_ish)

parse_terminal_output(open("input.txt", 'r'))
