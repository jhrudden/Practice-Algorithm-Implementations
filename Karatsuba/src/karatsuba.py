
# take two integers and multiply them using karatsuba algorithm
def karatsuba(intX, intY):
    # BASE CASE: if either of the integers are of magnitude 10^1, return product
    if len(str(intX)) == 1 and len(str(intY)) == 1:
        return intX*intY;


    # find the largest magnitude of the two integers
    maxMagnitude = max(len(str(intX)), len(str(intY)));

    # find pivot to split digits of both integers based on the larger of two's
    # magnitude.
    # if max magnitude is odd ceil(maxMag/ 2)
    pivot = maxMagnitude // 2 + maxMagnitude % 2;

    # split intX,intY into a,b,c,d based on pivot
    a = intX // 10**pivot;
    b = intX % 10**pivot;
    c = intY // 10**pivot;
    d = intY % 10**pivot;

    # recursively find the product of a*c
    ac = karatsuba(a,c);

    # recursively find the product of b*d
    bd = karatsuba(b,d);
    # instead of additionally having to find products of ad,bc
    # compute (a+b)(c+d) - ac - bd = ac+ad+bc+bd-ac-bd = ad+bc
    # skipping half of the computation of finding ad,bc seperately
    adPlusbc = karatsuba(a+b,c+d) - ac - bd;

    XYproduct = ac*10**(2*pivot) + adPlusbc*10**pivot +bd;

    return XYproduct;

int1 = 3141592653589793238462643383279502884197169399375105820974944592
int2 = 2718281828459045235360287471352662497757247093699959574966967627

print(karatsuba(int1,int2))
