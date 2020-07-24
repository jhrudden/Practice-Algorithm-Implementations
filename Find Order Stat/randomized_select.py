import random


# find the ith smallest element in an unsorted array quickSort-esque approach
def quick_select(unsorted_array, order_statistic):
    # base case
    if len(unsorted_array) == 1:
        return unsorted_array[0];

    # uniformly choose a index in input array at random as the pivot, for
    # the paritioning subroutine
    p = find_pivot(unsorted_array);


    # since order statistic starts at one, the index of the pivot after
    # partitioning (j) is 1 less than its respective order stat
    j = partition(unsorted_array, p) + 1

    # when j is equal to the order_statistic, then the search is over
    if j == order_statistic:
        return unsorted_array[j-1];

    # when j is less than the order_statistic, then the searched for value
    # must be in the subarray left of the j-1 index
    elif j > order_statistic:
        return quick_select(unsorted_array[:j-1], order_statistic);

    # the order_statistic must be in the subarray to the right of j-1 index
    # where the order_statistic is the (order_statistic - j)th smallest value
    # of the new sub array
    else:
        return quick_select(unsorted_array[j:], order_statistic-j);


# uniformly choose a index of a array at random to signify a pivot value
def find_pivot(array):
    return random.randrange(len(array));


def partition(unsorted_array, pivot):
    # pre partition step
    # swap the pivot element with first element in partition area
    temp = unsorted_array[pivot]
    unsorted_array[pivot] = unsorted_array[0]
    unsorted_array[0] = temp

    # create an index representing the first element greater than the pivot
    # everything following this in the 1 to j area should be larger than
    # the pivot and everything preceding should be smaller than the pivot
    border_index = 1
    for j in range(1,len(unsorted_array)):
        # as we extend the partition area, if we find an element smaller than
        # the pivot, then swap it with our border current border value
        # then increase the border index as it has been shifted right
        if unsorted_array[j] <= unsorted_array[0]:
            temp = unsorted_array[j]
            unsorted_array[j] = unsorted_array[border_index]
            unsorted_array[border_index] = temp
            border_index+=1;


    # after everything preceding the start index has been partitioned, swap the
    # current pivot value(at the 0th index) with the index inbetween the
    # partition
    temp = unsorted_array[border_index-1]
    unsorted_array[border_index-1] = unsorted_array[0]
    unsorted_array[0] = temp

    return border_index - 1
