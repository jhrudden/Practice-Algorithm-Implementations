
# You are a given a unimodal array of n distinct elements, meaning that its
# entries are in increasing order up until its maximum element, after which its
# elements are in decreasing order. Give an algorithm to compute the maximum
# element that runs in O(log n) time.

# find the largest integer in a unimodal array
def find_largest(input_array):
    # base case
    # if input array is of size 2 return the largest integer of the pair
    # else return the only item in the array
    if len(input_array) <= 2:
        if len(input_array) == 1:
            return input_array[0];
        else:
            if input_array[0] > input_array[1]:
                return input_array[0];
            else:
                return input_array[1];


    pivot = len(input_array) // 2;
    # recursively find the largest value in each half of the array
    largest_half_1 = find_largest(input_array[:pivot]);
    largest_half_2 = find_largest(input_array[pivot:]);


    # return the largest value of the two halves
    if largest_half_1 > largest_half_2:
        return largest_half_1;
    else:
        return largest_half_2;



print(find_largest([1,8,6,5,4]))

print(find_largest([1,2,8,5,4,3]))
