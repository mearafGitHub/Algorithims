a = [39, 7, 5]
b = [20, 11, 34]
c = [90, 23, 56]
triples = 0
res = []


def triples_sum(s):
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                if a[i] + b[j] + c[k] == s:
                    global triples
                    triples += 1
                    res.append([a[i], b[j], c[k]])
    return (triples, res)


print(triples_sum(149))


def triples_sumDP(s):
    A
    return (triples, res)


print(triples_sumDP(149))

