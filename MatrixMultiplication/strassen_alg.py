import numpy as np

# implemented for even nxn matrices
def strassen(matrix_a, matrix_b):
    n = len(matrix_a)
    if n == 0:
        return matrix_a;
    if n == 1:
        return [[matrix_a[0][0]*matrix_b[0][0]]];
    pivot = n // 2
    # Four quadrants of A
    A = matrix_a[0:pivot,0:pivot];
    B = matrix_a[0:pivot,pivot:];
    C = matrix_a[pivot:,0:pivot];
    D = matrix_a[pivot:,pivot:];

    # Four quadrants of B
    E = matrix_b[0:pivot,0:pivot];
    F = matrix_b[0:pivot,pivot:];
    G = matrix_b[pivot:,0:pivot];
    H = matrix_b[pivot:,pivot:];

    # print(A,matrix_sub(F,H))
    p1 = strassen(A,matrix_sub(F,H))
    p2 = strassen(matrix_add(A,B),H)
    p3 = strassen(matrix_add(C,D),E)
    p4 = strassen(D,matrix_sub(G,E))
    p5 = strassen(matrix_add(A,D),matrix_add(E,H))
    p6 = strassen(matrix_sub(B,D), matrix_add(G,H))
    p7 = strassen(matrix_sub(A,C), matrix_add(E,F))

    # calculate the new quadrant values which are equivalent to respective
    # quadrant after matrix multiplication
    l_upper_quadr = matrix_add(matrix_add(p5,matrix_sub(p4,p2)),p6)
    r_upper_quadr = matrix_add(p1,p2)
    l_lower_quadr = matrix_add(p3,p4)
    r_lower_quadr = matrix_sub(matrix_sub(matrix_add(p1,p5), p3),p7)
    c = []

    # re construct resulant matrix from the newly calculate quadrants
    for row_index in range(0, len(matrix_a)):
        c.append([])
        for col_index in range(0, len(matrix_a[0])):
            if pivot > row_index:
                # left upper quad
                if pivot > col_index:
                    c[row_index].append(l_upper_quadr[row_index][col_index])
                # right upper quadrant
                else :
                    c[row_index].append(r_upper_quadr[row_index][col_index-pivot])

            else:
                # left lower quadrant
                if pivot > col_index:
                    c[row_index].append(l_lower_quadr[row_index-pivot][col_index])
                # right lower quadrant
                else :
                    c[row_index].append(r_lower_quadr[row_index-pivot][col_index-pivot])
    # return the matrix product
    return c;

# subtract one square matrix from the other
def matrix_sub(a,b):
    c= np.zeros((len(a),len(a[0])), dtype=int)

    for i in range(0, len(a)):
        for j in range(0,len(a[0])):
            c[i][j] = a[i][j] - b[i][j]

    return c

# add one square matrix to the other
def matrix_add(a,b):
    c= np.zeros((len(a),len(a[0])),dtype=int)

    for i in range(0, len(a)):
        for j in range(0,len(a[0])):
            c[i][j] = a[i][j] + b[i][j]

    return c


a = np.array([[5,6],[2,3]])
b = np.array([[77,7],[67,23]])

print(strassen(a,b))
