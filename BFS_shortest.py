import sys
a = []
g = {}


def distance(s, n):
    # returns graph with updated distance
    for node in range(1, n+1):
        for v in a:
            # v = [item[i] for item in a]
            if node == s:
                g[node][0] = 0
            # nxt = v[1]
            if node != s:
                # not double edge
                if (v[0] == node and v[1] != g[node][1]) or (v[0] != node and v[1] != g[v[0]][1]):
                    #  avoid self directing node and double edge
                    if v[0] != v[1]:
                        if g[node][0] < 6:
                            if (v[0] == node or v[1] == node):
                                g[node][0] = 6
                                g[node][1] = v[0]

                        elif g[node][0] >= 6:
                            # if there is no smaller => prev is similar
                            if g[node][1] == v[0]:
                                g[node][0] += g[g[node][1]][0]
                            elif g[node][1] != v[0]:
                                g[node][1] = v[0]

    # print(g)
    return g

# new_g = distance({1: [-1, 0], 2: [-1, 0], 3: [-1, 0], 4:[-1, 0]},
#          [[1, 2], [2, 1], [2, 3], [1, 3]],
#          1, 4)


def main():
    q = int(input("\nEnter query number\n").strip())
    if q > 10 or q < 1:
        print("value of q exceeded or under the limit")
        return

    for i in range(q):
        # take n and m
        n, m = [int(value) for value in input("\nEnter n and m\n").split()]
        if n > 1000 or n < 2:
            print("value of n exceeded or under the limit.")
            return
        if m > (n*(n-1))//2 or m < 1:
            print("value of m exceeded or under the limit")
            return

        for j in range(1, n+1):
            u, v = [int(value) for value in input("\nEnter vertices\n").split()]
            a.append([u, v])
            g[j] = [-1, 0]
        s = int(input("\nEnter start\n").strip())
        # find distance for each node
        if s > n or s < 1:
            print("value of q exceeded or under the limit")
            return
        # print(g,"\n", a,"\n", s,"\n", n)
        distance(s, n)
        out = []
        for k, v in g.items():
            out.append(str(v[0]))

        result = " ".join(out[1::])
        sys.stdout.write(result)


if __name__ == "__main__":
    main()


