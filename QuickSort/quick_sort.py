import random
# sort a arbitrarily ordered array using famous QuickSort Algorithm
def quick_sort(unsorted_array, start, end):
    # Base Case
    # if the area of seach is of unit size or less, then there is nothing to
    # partition
    if end - start <= 1:
        return;

    pivot = find_pivot(unsorted_array,start,end);
    pivot = partition(unsorted_array, start, end, pivot)
    quick_sort(unsorted_array, start, pivot)
    quick_sort(unsorted_array, pivot+1, end)

# randomly pick a pivot which is start<=pivot<=end
def find_pivot(array,start,end):
    return random.randrange(start, end);

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

# test if QS can sort a list of 10000 arbitrarily sorted integers
text_file = open("unsorted_integers.txt")
text_file = text_file.read().split()
a = []
for str in text_file:
    a.append(int(str))

print(a)
quick_sort(a,0,len(a))
print(a)
