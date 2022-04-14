import heapq
from collections import Counter


def max_consequetive_repeated(A):
    d = Counter(A)
    hp = []

    most_duplicate = 0
    for r in list(d.values()):
        heapq.heappush(hp, -r)
    q = heapq.heappop(hp)
    for k, v in d.items():
        if v == -q:
            most_duplicate = k

    # occurrence = []
    # sequence = []
    # for i in range(0, len(A)-1):
    #     if abs(A[i]-A[i+1]) == 0:
    #         sequence.append(A[i])
    #     occurrence.append(sequence)
    #     sequence = []

    return most_duplicate


# other solution

def max_consequetive_(A):
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
                visited[forward] = True
                length += 1
                forward += 1

            backward = A[i] - 1
            while forward in A_set:
                visited[forward] = True
                length -= 1
                backward -= 1
            max_len = max(max_len, length)

        return max_len

print(max_consequetive_repeated([7, 7, 20, 12, 20, 12, 12, 14, 20, 20, 2]))