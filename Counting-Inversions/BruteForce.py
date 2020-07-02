
def brute_force(input_array, current_index, comp_index):
    '''
     - Array Integer Integer -> Integer
     - count the amount of indices with large values proceding, in an Array

    '''
    if current_index >= len(input_array):
        return 0;
    elif comp_index >= len(input_array):
        return brute_force(input_array, current_index+1, current_index+2);
    elif input_array[current_index] > input_array[comp_index]:
        return 1 + brute_force(input_array, current_index, comp_index+1);
    else:
        return brute_force(input_array, current_index, comp_index+1);


print(brute_force([1,3,5,2,4,6], 0, 1))
