import math
# for arrays >= size 2
# find the closest pair of points in given array
def find_closest(point_array):
    # setup steps
    ordered_by_x = mergePairSort(point_array, 0);
    ordered_by_y = mergePairSort(point_array, 1);
    return closestPair(ordered_by_x, ordered_by_y);

# two sorted versions of an array find the closest pair of points
# (f_x sorted by x values)
# (f_y sorted by y values)
def closestPair(f_x, f_y):
    if len(f_x) <= 3:
        return brute_force(f_x)

    pivot = len(f_x) // 2;

    # split each array into two halves
    lf_x, rf_x = f_x[0:pivot], f_x[pivot:];
    lf_y, rf_y = f_y[0:pivot], f_y[pivot:];


    # find smallest pair of points on left side of array
    (p1,q1) = closestPair(lf_x,lf_y);
    # find smallest pair of points on right side of array
    (p2,q2) = closestPair(rf_x, rf_y);

    # find the closest non split pair of points
    curr_smallest_dist = min(d(p1,q1), d(p2,q2))

    # find the closest split pair of points ie. one point on either half of arr
    (p3,q3) = closest_split_pair(f_x, f_y, curr_smallest_dist);

    if d(p3,q3) < curr_smallest_dist:
        return p3,q3;
    elif d(p2,q2) == curr_smallest_dist:
        return p2,q2;
    else:
        return p1,q1;

# compare each cartesian point in a sorted array to each preceding
# to find the pair with the smallest euclidean distance
def brute_force(point_array):
    p,q = point_array[0],point_array[1]
    smallest_d =  d(p,q);
    for i in range(0,len(point_array)):
        j = 1;
        while i+j < len(point_array):
            curr_d = d(point_array[i],point_array[i+j])
            if curr_d < smallest_d:
                p,q = point_array[i],point_array[i+j]
                smallest_d = curr_d
            j+=1;
    return p,q;

def closest_split_pair(f_x, f_y, curr_smallest_dist):
    # biggest x coord in left of array
    x_bar = f_x[(len(f_x)//2)-1][0]
    # all points in the array that have xcoord in range -
    # [x_bar - curr_smallest_dist, x_bar + curr_smallest_dist]
    # sorted in ascending y coord
    s_y = []
    for index in range(0, len(f_y)):
        (curr_x, curr_y) = f_y[index];
        if curr_x >= x_bar - curr_smallest_dist and curr_x <= x_bar + curr_smallest_dist:
            s_y.append((curr_x,curr_y));

    best = curr_smallest_dist;
    # init closest pair to arbitraury values in s_y array
    best_pair = (s_y[0],s_y[1]);

    for i in range(0,len(s_y) - 1):
        for j in range(1, min(len(s_y) - i, 7)):
            p,q = s_y[i],s_y[i+j]
            if d(p,q) < best:
                best = d(p,q);
                best_pair = (p,q);

    return best_pair[0],best_pair[1];



# calculate euclidean distance
def d(point_1,point_2):
    # d = root_2((x_1-x_2)^2 + (y_1 - y_2)^2)
    return math.sqrt((point_1[0] - point_2[0])**2
    + (point_1[1] - point_2[1])**2);




# sort pairs of cartesian points based on
# sort based on x coords -> index=0
# sort based on y coords -> index=1
def mergePairSort(point_array, index):
    if len(point_array) == 1:
        return point_array;

    #split array and sort

    pivot = (len(point_array) // 2);
    half1, half2 = point_array[0:pivot], point_array[pivot:];

    return merge(mergePairSort(half1, index), mergePairSort(half2, index), index);


def merge(point_array1, point_array2, index):
    sorted = [];
    pointer1, pointer2 = 0, 0;
    sizeA1, sizeA2 = len(point_array1), len(point_array2)
    while pointer1 < sizeA1 and pointer2 < sizeA2:
        currItem1, currItem2 = point_array1[pointer1], point_array2[pointer2]
        if currItem1[index] < currItem2[index]:
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



# a = [(1,1),(6,7),(6,5)]
a = [[1,4],[2,4],[3,4],[1,5],[2,5],[3,5]]

# p,q = brute_force(a)
p,q = find_closest(a)
print(p,q)
