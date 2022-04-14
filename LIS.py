# this solves the longest increasing sub-sequence in a given integer array


def longest_inc_subseq(N):
    lis = {}
    for i in range(len(N)):
        lis[i] = 1
    lrg = 0
    for i in range(len(N)-1, -1, -1):
        for j in range(i+1, len(N)):
            if N[i] < N[j]:
                lis[i] = max(lis[i], 1 + lis[j])
    lrg = max(lis[i], lrg)
    return lrg

print(longest_inc_subseq([1,2,4,3,5,7,9,12]))
