from collections import deque


def phone_num_string(ping):
    map_num_string = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl'
    }
    res = deque([''])

    for i in range(len(ping)):
        while len(res) >= i:
            tmp = res.pop()
            num_string = map_num_string[ping[i]]
            for c in num_string:
                res.append(tmp + c)
    return res


print(phone_num_string('23'))
