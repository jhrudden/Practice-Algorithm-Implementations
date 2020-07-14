import numpy as np
# You are given an n by n grid of distinct numbers. A number is a local minimum
# if it is smaller than all of its neighbors. (A neighbor of a number is one
# immediately above, below, to the left, or the right. Most numbers have four
# neighbors; numbers on the side have three; the four corners have two.) Use the
# divide-and-conquer algorithm design paradigm to compute a local minimum with
# only O(n) comparisons between pairs of numbers. (Note: since there are
# n2n^2n2 numbers in the input, you cannot afford to look at all of them.
# Hint: Think about what types of recurrences would give you the desired upper
# bound.)

# Finds a local minimum within this 2D array
def find_local_minimum(grid):
    # base case: found minimum
    if len(grid) == 1 and len(grid[0]) == 1:
        return grid[0][0];

    middle_x = (len(grid[0])-1);
    middle_y = (len(grid)-1);
    print(middle_y,middle_x)
    # find the smallest element in the center column
    # initialize it to the first item in the center column
    smallest_column = grid[0][middle_x];
    smallest_column_yx = [0,middle_x];
    for y in range(1,len(grid)):
        curr_item = grid[y][middle_x];
        if curr_item < smallest_column:
            smallest_column = curr_item;
            smallest_column_yx = [y,middle_x]


    # find the smallest element in the center row
    # initialize it to the first item in the center row
    smallest_row = grid[middle_y][0];
    smallest_row_yx = [middle_y, 0];
    for x in range(1,len(grid)):
        curr_item = grid[middle_y][x];
        if curr_item < smallest_row:
            smallest_row = curr_item;
            smallest_row_yx = [middle_y,x]

    # when the smallest item in the center row is the smallest item in the
    # center column, this item must be in the center of the cross made by
    # the intersection, thus is a local minimum
    if smallest_column_yx == smallest_row_yx:
        return smallest_column;
    else:
        # if the smallest item in the cross is in the middle column, check
        # side neighbors values to either extend the search or confirm that the
        # item is a local minimum
        if smallest_column < smallest_row:
            if smallest_column_yx[1] > 0:
                left_neighbor = grid[smallest_column_yx[0]][middle_x-1]
                if left_neighbor < smallest_column:
                    # since left neighbor is bigger search for a new minimum in
                    # left neighbors quadrant
                    if smallest_column_yx[0] < middle_y:
                        local_minimum = find_local_minimum(grid[:middle_y,:middle_x])
                    else:
                        local_minimum = find_local_minimum(grid[middle_y+1:,:middle_x])
                    return local_minimum
            if smallest_column_yx[1] < len(grid[0]) - 1:
                #check right element
                right_neighbor = grid[smallest_column_yx[0]][middle_x+1]
                if right_neighbor < smallest_column:
                    # since right neighbor is bigger search for a new minimum in
                    # right neighbors quadrant
                    if smallest_column_yx[0] < middle_y:
                        local_minimum = find_local_minimum(grid[:middle_y,middle_x+1:])
                    else:
                        local_minimum = find_local_minimum(grid[middle_y+1:,middle_x+1:])
                    return local_minimum

            return smallest_column

        # if the smallest item in the cross is in the middle row, check
        # up and down neighbors values to either extend the search or confirm
        # that the item is a local minimum
        else:
            if smallest_row_yx[0] > 0:
                #check up element
                up_neighbor = grid[middle_y+1][smallest_row_yx[1]]

                if up_neighbor < smallest_row:
                # since up neighbor is bigger search for a new minimum in
                # up neighbors quadrant
                    if smallest_row_yx[1] < middle_x:
                        local_minimum = find_local_minimum(grid[:middle_y,:middle_x])
                    else:
                        local_minimum = find_local_minimum(grid[:middle_y,middle_x+1:])
                    return local_minimum

            if smallest_column_yx[1] < len(grid) - 1:
                #check down element
                down_neighbor = grid[middle_y-1][smallest_row_yx[1]]
                if smallest_row_yx[1] < middle_x:
                    local_minimum = find_local_minimum(grid[middle_y+1:,:middle_x])
                else:
                    local_minimum = find_local_minimum(grid[middle_y+1:,middle_x+1:])
                return local_minimum

            return smallest_row




a = np.array([[40,41,45,44,42],
     [52,39,30,7,15],
     [56,47,29,8,23],
     [60,49,31,10,22],
     [40,38,36,35,24]])

b = [[4,3],[1,2]]
print(find_local_minimum(a))
