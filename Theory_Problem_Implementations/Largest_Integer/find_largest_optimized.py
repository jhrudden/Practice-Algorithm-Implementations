# more optimized versions of find largest integer algorithm



# You are a given a unimodal array of n distinct elements, meaning that its
# entries are in increasing order up until its maximum element, after which its
# elements are in decreasing order. Give an algorithm to compute the maximum
# element that runs in O(log n) time.

# find the largest element in array of integers using a binary
# search-esque approach
def find_largest_integer(input_array):
    # base case
    if len(input_array) == 1:
        return input_array[0];

    pivot = len(input_array) // 2
    # find largest is in the right or left side of array then recursively look
    # for the largest element in that side
    if input_array[pivot - 1] > input_array[pivot]:
        return find_largest_integer(input_array[:pivot]);
    else:
        return find_largest_integer(input_array[pivot:]);


print(find_largest_integer([1,8,6,5,4]))
print(find_largest_integer([1,2,8,5,4,3]))
print(find_largest_integer([1]))
print(find_largest_integer([1,2]))
print(find_largest_integer([1,3,2]))
