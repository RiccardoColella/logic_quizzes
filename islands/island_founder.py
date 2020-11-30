# World's height
H = 1000
# World's width
W = 1000


def set_seen_block(x, y):
    """ Given a block, if not already seen, sets it as seen

    :param x: the x coordinate of the block
    :param y: the y coordinate of the block
    :return: True if the block has been set as seen, False otherwise
    """
    just_set = False
    if world[y][x] == '1':
        just_set = True
        world[y][x] = 'S'
    return just_set


def set_seen_island(x, y):
    """ Given a block, sets all the adjacent blocks as seen

    :param x: the x coordinate of the block
    :param y: the y coordinate of the block
    """
    visited = []
    if x > 0:
        if set_seen_block(x - 1, y):
            visited.append([x - 1, y])
    if x < W - 1:
        if set_seen_block(x + 1, y):
            visited.append([x + 1, y])
    if y > 0:
        if set_seen_block(x, y - 1):
            visited.append([x, y - 1])
    if y < H - 1:
        if set_seen_block(x, y + 1):
            visited.append([x, y + 1])
    for seen_block in visited:
        set_seen_island(seen_block[0], seen_block[1])


def open_file_and_build_world(filename):
    """ Open the txt file containing the world and loads it into a list of lists

    :param filename: the name or path to the file to be opened
    :return: a list of lists of the world
    """
    my_file = open(filename, "r")
    content_list = my_file.readlines()
    world = []
    for x in content_list:
        row = x.split(",")
        row[W - 1] = row[W - 1].replace("\n", "")
        world.append(row)

    return world


if __name__ == '__main__':
    world = open_file_and_build_world("islands.txt")
    islands = 0
    for y in range(H):
        for x in range(W):
            if world[y][x] == '1':
                islands += 1
                set_seen_island(x, y)
    print("The given world contains this number of islands:", islands)


