def unique(ids, rem):
    count = 1
    to_remove = 0
    i = 0
    cur = ids[0]
    ids.sort()
    print(ids)
    while i < len(ids):
        if to_remove < rem <= ids[i]:
            ids.remove(ids[i])
            to_remove += 1
            continue
        elif cur < ids[i]:
            cur = ids[i]
            count += 1
        i += 1

    return (count, ids)

# O(n*rem) almost linear time space O(1)
print(unique([1,1,1,1,1,2,3,2],2))