def count_neighbors(cord=(0, 0)):
    """
    count_neighbors function - This function should accept the entire
world, and a position in the world (i.e. a row and column). Then, the function should
count and return the number of living neighbors for the location specified by the
row/cell parameters. Where should this function be called? Who needs this info?
    """
    count = 0
    isleft = cord[0] == 0
    isright = cord[0] == world_size[0] - 1
    istop = cord[1] == 0
    isbottom = cord[1] == world_size[1] - 1

    if not (isleft or isright or istop or isbottom):
        count += count_adjacent_row(cord[0] - 1, cord[1])
        count += count_adjacent_row(cord[0] + 1, cord[1])
        count_same_row(cord[0], cord[1])
    else:
        if isleft and istop:
        elif isleft and isbottom:
        elif isright and istop:
        elif isright anf isbottom:
        else:
            if isleft:

            if isright:

            if istop:

            if isbottom:


def count_same_row(row, center):
    return world

def count_adjacent_row(row, center):


def handle_top_left():
    def handle_bottom_left():

        def handle_top_right():

        def handle_bottom_right():

        def handle_left():

        def handle_right():

        def handle_top();