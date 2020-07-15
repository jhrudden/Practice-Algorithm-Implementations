

# sort a arbitrarily ordered array using famous QuickSort Algorithm
def quick_sort(unsorted_array, start, end):
    # Base Case
    # if the area of seach is of unit size or less, then there is nothing to
    # partition
    if end - start <= 1:
        return;

    # in order to be quick sort we need a way to
    pivot = find_pivot(unsorted_array,start,end);
    pivot = partition(unsorted_array, start, end, pivot)
    quick_sort(unsorted_array, start, pivot)
    quick_sort(unsorted_array, pivot+1, end)

def find_pivot(array,start,end):
    return (end+start)//2;

def partition(unsorted_array, start, end, pivot):
    # pre partition step
    # swap the pivot element with first element in partition area
    temp = unsorted_array[pivot]
    unsorted_array[pivot] = unsorted_array[start]
    unsorted_array[start] = temp

    # create an index representing the first element greater than the pivot
    # everything following this in the start+1 to j area should be larger than
    # the pivot and everything preceding should be smaller than the pivot
    border_index = start+1
    for j in range(start+1,end):
        # as we extend the partition area, if we find an element smaller than
        # the pivot, then swap it with our border current border value
        # then increase the border index as it has been shifted right
        if unsorted_array[j] <= unsorted_array[start]:
            temp = unsorted_array[j]
            unsorted_array[j] = unsorted_array[border_index]
            unsorted_array[border_index] = temp
            border_index+=1;


    # after everything preceding the start index has been partitioned, swap the
    # current pivot value(at the start index) with the index inbetween the
    # partition
    temp = unsorted_array[border_index-1]
    unsorted_array[border_index-1] = unsorted_array[start]
    unsorted_array[start] = temp

    return border_index - 1

a=[8,7,6,5,4,3,2,1]
print(a)
quick_sort(a,0,8)
print(a)
