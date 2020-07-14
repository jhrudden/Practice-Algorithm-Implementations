# You are given a sorted (from smallest to largest) array A of n distinct
# integers which can be positive, negative, or zero. You want to decide whether
# or not there is an index i such that A[i] = i. Design the fastest algorithm
# that you can for solving this problem.


# SOME INSIGHT: if A[i] = i, then A[i] - i = 0
# since the array is sorted if A[i] - i < 0, then the only possibility for a
# fixed point is to the right of the entry. Vice versus, if A[i] - i > 0, then
# a fixed point is only possible to the left of entry

# Is there a element in this sorted_array equal to its index?
# binary search-esque implementation, where we only search in areas of possible
# fixed points
def find_fixed(sorted_array):

    # define a parameter of search within the array
    i = 0
    left_boundary = 0;
    right_boundary = len(sorted_array) - 1;

    # while the search area hasn't inverted, keep looking for element
    while left_boundary <= right_boundary:
        # create a point of interest to begin the search in the middle of parameter
        middle = (left_boundary + right_boundary) // 2
        curr_point_difference = sorted_array[middle] - middle;
        if curr_point_difference == 0:
            return True;
        elif curr_point_difference > 0:
            right_boundary = middle - 1;
        else:
            left_boundary = middle + 1;

    return False;


print(find_fixed([-1,0,1,3]))
print(find_fixed([1]))
print(find_fixed([0]))

# Analysis: T(n) = T(n/2) + c = O(logn), as a constant amount of operations <= 5
# occur every round of the algorithm and every round limits the search by half
