def mergeSort(numArray):
    if len(numArray) == 1:
        return numArray;

    #split array and sort

    pivot = (len(numArray) // 2);
    half1, half2 = numArray[0:pivot], numArray[pivot:];

    return merge(mergeSort(half1), mergeSort(half2));


def merge(numArray1, numArray2):
    sorted = [];
    pointer1, pointer2 = 0, 0;
    sizeA1, sizeA2 = len(numArray1), len(numArray2)
    while pointer1 < sizeA1 and pointer2 < sizeA2:
        currItem1, currItem2 = numArray1[pointer1], numArray2[pointer2]
        if currItem1 < currItem2:
            sorted.append(currItem1);
            pointer1 += 1;
        else:
            sorted.append(currItem2);
            pointer2 += 1;

    if pointer1 < sizeA1:
        sorted.extend(numArray1[pointer1:]);

    elif pointer2 < sizeA2:
        sorted.extend(numArray2[pointer2:]);

    return sorted;


array1 = [7,6,5,4,3,2,1]
print(mergeSort(array1))
