def nthMin(arr):
    min = arr[0]
    min2 = arr[1]
    for i in arr:
        if i < min:
            min2 = min
            min = i
        elif i > min:
            min2 = i
    return [min, min2]

# we dont really care for the leftside of the array
A = [11, 100, 4, 6, 35, 8, 2, 40, 9, 20, 15, 150, 7, 1000, 12, 200]
def itemSwap(A):
    for i in range(0, len(A)-1):
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
            # itemSwap(A)

def Nth(A, m):
    for i in range(0,( m + (len(A)//2) -1) ):
        itemSwap(A)
    return [A[m], A, m]

x = Nth(A, 15)
print(x)
# itemSwap(A)
# print(A)
# time = O(nlog(n))
# space = O(n)