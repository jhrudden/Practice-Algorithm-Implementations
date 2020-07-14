
# Problem

# You are given as input an unsorted array of n distinct numbers, where n is a
# power of 2. Give an algorithm that identifies the second-largest number in the
# array, and that uses at most n+log⁡2n−2n +\log_2 n - 2n+log2​n−2 comparisons.


def find_second_largest(unsorted_array):
    if len(unsorted_array) % 2 != 0:
        return "array is not of size 2^k";


    # look at picture
    largest_pairs = find_largest_pairs(unsorted_array)

    # second element of first pair in array
    curr_second_largest = largest_pairs[0][1]

    for index in range(1,len(largest_pairs)):
        print("smallest")
        curr_int = largest_pairs[index][1]
        if curr_int > curr_second_largest:
            curr_second_largest = curr_int;


    return curr_second_largest



def find_largest_pairs(unsorted_array):
    # base case
    if len(unsorted_array) == 2:
        # return a pair of numbers with the first element being larger than
        # the second
        if unsorted_array[0] > unsorted_array[1]:
            return [(unsorted_array[0] , unsorted_array[1])]
        return [(unsorted_array[1] , unsorted_array[0])]


    pivot = len(unsorted_array) // 2

    # find the 2D arrays on each half, with largest elements in pairs,
    # but closest distance between the numbers
    largest_left_pairs = find_largest_pairs(unsorted_array[0:pivot])
    largest_right_pairs = find_largest_pairs(unsorted_array[pivot:])

    new_pairs = []

    if largest_left_pairs[0][0] > largest_right_pairs[0][0]:
        # if largest first element of every pair is in left list
        # add those pairs to the list to be passed to next level
        # and append a new pair to this list, which features the hearder element
        # of left list followed by the header of the the right list
        # ie. [[6,2],[6,3]],[[5,1],[5,4]] -> [[6,2],[6,3],[6,5]]

        new_pairs.extend(largest_left_pairs)
        newest_pair=[largest_left_pairs[0][0], largest_right_pairs[0][0]]
        new_pairs.append(newest_pair)
    else:
        new_pairs.extend(largest_right_pairs)
        newest_pair=[largest_right_pairs[0][0], largest_left_pairs[0][0]]
        new_pairs.append(newest_pair)

    return new_pairs


a = [7,3,8,1,6,5,2,4]
print(find_second_largest(a))
