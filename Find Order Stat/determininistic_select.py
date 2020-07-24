import numpy


# find a given order statistic in an unsorted array deterministically in O(n)
# time
def d_select(A, order_stat):
    # base case
    if len(A) == 1:
        return A[0]

    # cut array A into subarrays of size 5, and sort those arrays
    C = []
    j = -1
    for i in range(len(A)):
        if (i) % 5 == 0:
            j += 1
            C.append([]);
        C[j].append(A[i])

    # find the minimum of each of the n/5 subsets of A
    for i in range(len(C)):
        C[i] = numpy.sort(C[i])
        C[i] = C[i][len(C[i]) // 2 + (len(C[i]) % 2)]

    # find the medians of medians from the updated C matrix
    p = d_select(C, (len(C) // 2 + (len(C) % 2)))

    # find the order statistic of the above pivot after partition
    j = partition(A, p) + 1

    # if that order stat is equal to the stat of search, our search
    # is over
    if j == order_stat:
        return A[j-1];

    # if the j order stat is larger than the one of search, then recur down the
    # left subsection of the parition
    elif j > order_stat:
        return d_select(A[:j-1], order_stat);

    # else recur down the right of partition
    else:
        return d_select(A[j:], order_stat-j);


# partition an arbitraurily sorted array based on a given value
def partition(A, p_val):
    # insert tha value at the beginning of the array
    A.insert(0,p_val)
    # i represents first value larger than pivot
    i = 1

    # go down the array, if a point that is found is less than pivot, place
    # it at the boundary and adjust the border, other wise continue down the
    # array
    j = 1
    while j < len(A):
        # if the value is seen, then delete it
        if A[j] == p_val:
            A.pop(j)
            j-=1
        elif A[j] < p_val:
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
            i+=1
        j +=1

    # swap the p_value with the value before the pivot, and the partition
    # is complete
    temp = A[0]
    A[0] = A[i-1]
    A[i-1] = temp

    # return the index of the p_value
    return i-1




print(d_select([13,1,8,3,7,12,10,11,9,5,4,6,2], 2))
