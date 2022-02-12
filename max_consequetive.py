occurance = []
max = {}
pointer = 0

def max_consequetive(A):
    sequence = []
    for i in range(0, len(A)-1):
        if abs(A[i]-A[i+1]) == 1:
            sequence.append(A[i])
    max[i] = sequence
    occurance.append(sequence)
    return max
    # print(pointer

print(max_consequetive([7,7,5,10,11,12,13,14,20,30,40,1,2,3]))


#  someone else's code

def max_consequetive(A):
    visited = [False] * len(A)
    length = 0
    max_len = 0
    A_set = set(A)
    for i in range(0, len(A_set)):
        if not visited[i]:
            visited[i] = True
            length += 1
            # then go forward
            forward = A[i] + 1
            while forward in A_set:
                visited[foraward] = True
                lenght += 1
                forward += 1

            backward = A[i] - 1
            while forward in A_set:
                visited[foraward] = True
                lenght -= 1
                backward -= 1

            max_len = max(max_len, length)
            lenght = 0
        return max_len