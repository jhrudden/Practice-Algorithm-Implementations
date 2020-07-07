

def sort_and_count(array_A):
    '''
     - Array Integer Integer -> Integer
     - count the amount of indices with large values proceding, in an Array
     - while also merge sorting that array

    '''
    if len(array_A) <= 1:
        return 0, array_A;

    pivot = len(array_A) // 2;
    # check the amount of inversions on the front and back half of the array
    left_inversions, sorted_1st = sort_and_count(array_A[:pivot])
    right_inversions, sorted_2nd = sort_and_count(array_A[pivot:])

    # check the inversions where for i,j, i<n/2<=j A[i] > A[j] / split inversions
    split_inversions, complete_sorted = count_split_invr(sorted_1st, sorted_2nd)

    return left_inversions + right_inversions + split_inversions, complete_sorted;


def count_split_invr(half_1, half_2):
    '''
     - Array Array -> Integer, Array
     - Sort the amount

    '''
    index_1 = 0;
    index_2 = 0;
    sorted = [];
    split_inversions = 0;
    while index_1 < len(half_1) and index_2 < len(half_2):
        if half_1[index_1] > half_2[index_2]:
            # since both arrays are sorted, if an element in the right array
            # is smaller than the left, then the right item must also be smaller
            # than every element after the given item in the left array
            split_inversions += len(half_1) - (index_1);
            sorted.append(half_2[index_2]);
            index_2 += 1
        else:
            sorted.append(half_1[index_1]);
            index_1 +=1
    sorted.extend(half_1[index_1:]);
    sorted.extend(half_2[index_2:]);

    return split_inversions, sorted



pars_matrix = open("matrix.txt")
matrix = []
for str in pars_matrix.read().split():
    matrix.append(int(str))


splits, sorts = sort_and_count(matrix)
print(splits)
