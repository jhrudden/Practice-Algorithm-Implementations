import math


def find_closest(point_array):
    # setup steps
    ordered_by_x = mergePairSort(point_array);
    return closestPair(ordered_by_x);



def closestPair(sorted_point_array):
    if len(sorted_point_array) <= 1:
        return sorted_point_array;

    pivot = len(sorted_point_array) // 2;
    half_1, half_2 = sorted_point_array[0:pivot], sorted_point_array[pivot:];
    # Q, R represent smallest pair in left and right sides of point_array respectively
    smallest_left, smallest_right = closestPair(half_1), closestPair(half_2)

    smallest_dist = min(d(smallest_left[0],smallest_left[1])
    , d(smallest_right[0],smallest_right[1]));

    S_p = closest_split_pair(sorted_point_array, smallest_dist)

    if d(S_p[0], S_p[1]) < smallest_dist:
        return S_p
    elif smallest_dist == d(smallest_left[0],smallest_left[1]):
        return smallest_left
    else:
        return smallest_right

def closest_split_pair(sorted_point_array, curr_min):
    x_bar = sorted_point_array[len(sorted_point_array) // 2]
    for i in range(0,len(sorted_point_array) - 7):
        for j in range(0, 7):



# calculate euclidean distance
def d(point_1,point_2):
    # d = root_2((x_1-x_2)^2 + (y_1 - y_2)^2)
    return math.sqrt((point_1[0] - point_2[0])**2
    + (point_1[1] - point_2[1])**2);


def mergePairSort(point_array):
    if len(point_array) == 1:
        return point_array;

    #split array and sort

    pivot = (len(point_array) // 2);
    half1, half2 = point_array[0:pivot], point_array[pivot:];

    return merge(mergePairSort(half1), mergePairSort(half2));


def merge(point_array1, point_array2):
    sorted = [];
    pointer1, pointer2 = 0, 0;
    sizeA1, sizeA2 = len(point_array1), len(point_array2)
    while pointer1 < sizeA1 and pointer2 < sizeA2:
        currItem1, currItem2 = point_array1[pointer1], point_array2[pointer2]
        if currItem1[0] < currItem2[0]:
            sorted.append(currItem1);
            pointer1 += 1;
        else:
            sorted.append(currItem2);
            pointer2 += 1;

    if pointer1 < sizeA1:
        sorted.extend(point_array1[pointer1:]);

    elif pointer2 < sizeA2:
        sorted.extend(point_array2[pointer2:]);

    return sorted;
