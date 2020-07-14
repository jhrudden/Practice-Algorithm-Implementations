

# sort a arbitrarily ordered array using famous QuickSort Algorithm
def quick_sort(unsorted_array):
    # Base Case
    if len(unsorted_array) <= 1:
        return unsorted_array;

    # in order to be quick sort we need a way to
    pivot = find_pivot(unsorted_array);

    less_than = [];
    greater_than = [];
    for index in range(0, len(unsorted_array)):
        if index == pivot:
            pass    # do nothing
        else:
            # when elements are less than pivot element
            if unsorted_array[index] <= unsorted_array[pivot]:
                less_than.append(unsorted_array[index]);
            # when elements are greater than pivot element
            else:
                greater_than.append(unsorted_array[index]);

                
    less_than = quick_sort(less_than);
    greater_than = quick_sort(greater_than);

    sorted_array = []
    sorted_array.extend(less_than);
    sorted_array.append(unsorted_array[pivot]);
    sorted_array.extend(greater_than);


    return sorted_array;


def find_pivot(array):
    return len(array)//2;


print(quick_sort([8,7,6,5,4,3,2,1]))
